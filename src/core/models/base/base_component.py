"""
Classe base abstrata para todos os componentes de erosão.

Esta classe define a interface comum que todos os componentes (pipe bend, 
straight pipe, etc.) devem implementar.

Baseado na DNV RP O501 - Managing sand production and erosion
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class ErosionResult:
    """
    Resultado de um cálculo de erosão.
    
    Attributes:
        relative_erosion_rate: Taxa de erosão relativa (mm/ton)
        annual_erosion_rate: Taxa de erosão anual (mm/year)
        erosion_for_period: Erosão para período especificado (mm)
        max_erosion_location: Localização da erosão máxima
        erosion_area: Área exposta à erosão (m²)
        risk_level: Nível de risco ("low", "medium", "high")
        calculation_details: Detalhes dos cálculos intermediários
    """
    relative_erosion_rate: float  # mm/ton
    annual_erosion_rate: float   # mm/year
    erosion_for_period: float    # mm
    max_erosion_location: str
    erosion_area: float          # m²
    risk_level: str
    calculation_details: Dict[str, Any]


@dataclass
class FluidProperties:
    """
    Propriedades do fluido (mistura).
    
    Attributes:
        velocity: Velocidade da mistura (m/s)
        density: Densidade da mistura (kg/m³)
        viscosity: Viscosidade da mistura (kg/ms)
        reynolds_number: Número de Reynolds (opcional, calculado se não fornecido)
    """
    velocity: float      # m/s
    density: float       # kg/m³
    viscosity: float     # kg/ms
    reynolds_number: Optional[float] = None  # calculado automaticamente


@dataclass
class SandProperties:
    """
    Propriedades das partículas de areia.
    
    Attributes:
        concentration: Concentração de areia (ppmW)
        particle_size_d50: Tamanho médio das partículas (μm)
        density: Densidade das partículas (kg/m³)
        sand_type: Tipo de areia ("quartz_sand", "calcite", "barite", etc.)
        mass_flow_rate: Taxa de fluxo mássico de areia (kg/s)
    """
    concentration: float        # ppmW
    particle_size_d50: float   # μm
    density: float              # kg/m³
    sand_type: str = "quartz_sand"
    mass_flow_rate: Optional[float] = None  # kg/s, calculado se não fornecido


@dataclass
class Material:
    """
    Propriedades do material do componente.
    
    Attributes:
        material_type: Tipo do material ("carbon_steel", "stainless_steel", etc.)
        density: Densidade do material (kg/m³)
        erosion_constant_k: Constante de erosão K
        velocity_exponent_n: Expoente de velocidade n
        ductility: "ductile" ou "brittle"
    """
    material_type: str
    density: float              # kg/m³
    erosion_constant_k: float   # (m/s)^-n
    velocity_exponent_n: float  # adimensional
    ductility: str = "ductile"  # "ductile" ou "brittle"


class BaseComponent(ABC):
    """
    Classe base abstrata para todos os componentes de erosão.
    
    Esta classe define a interface comum que todos os componentes específicos
    (PipeBend, StraightPipe, WeldedJoint, etc.) devem implementar.
    
    Attributes:
        component_id: Identificador único do componente
        component_type: Tipo do componente ("pipe_bend", "straight_pipe", etc.)
        material: Propriedades do material
        geometry: Parâmetros geométricos específicos do componente
    """
    
    def __init__(
        self, 
        component_id: str, 
        component_type: str,
        material: Material, 
        geometry: Dict[str, float]
    ):
        """
        Inicializa o componente base.
        
        Args:
            component_id: ID único do componente (ex: "bend_001")
            component_type: Tipo do componente (ex: "pipe_bend")
            material: Propriedades do material
            geometry: Dicionário com parâmetros geométricos
        """
        self.component_id = component_id
        self.component_type = component_type
        self.material = material
        self.geometry = geometry
        
        # Valida os parâmetros na criação
        self._validate_initialization()
    
    @abstractmethod
    def calculate_erosion(
        self, 
        fluid_props: FluidProperties, 
        sand_props: SandProperties,
        time_period: float = 1.0,
        geometry_factor: float = 1.0
    ) -> ErosionResult:
        """
        Calcula a erosão para este componente.
        
        Este método DEVE ser implementado por cada classe filha com a
        matemática específica da DNV RP O501 para aquele tipo de componente.
        
        Args:
            fluid_props: Propriedades do fluido
            sand_props: Propriedades da areia
            time_period: Período de cálculo em anos (padrão: 1.0)
            geometry_factor: Fator de geometria (padrão: 1.0)
            
        Returns:
            ErosionResult: Resultado completo do cálculo de erosão
            
        Raises:
            NotImplementedError: Se a classe filha não implementar este método
        """
        pass
    
    @abstractmethod
    def validate_geometry(self) -> bool:
        """
        Valida se os parâmetros geométricos estão corretos.
        
        Cada tipo de componente tem suas próprias regras de validação.
        
        Returns:
            bool: True se geometria é válida, False caso contrário
            
        Raises:
            ValueError: Se algum parâmetro está fora dos limites
        """
        pass
    
    def get_reynolds_number(self, fluid_props: FluidProperties) -> float:
        """
        Calcula o número de Reynolds para o componente.
        
        Re = (density × velocity × diameter) / viscosity
        
        Args:
            fluid_props: Propriedades do fluido
            
        Returns:
            float: Número de Reynolds
            
        Raises:
            KeyError: Se 'internal_diameter' não estiver na geometria
        """
        if 'internal_diameter' not in self.geometry:
            raise KeyError(f"Geometria do componente {self.component_id} deve ter 'internal_diameter'")
        
        diameter = self.geometry['internal_diameter']
        re = (fluid_props.density * fluid_props.velocity * diameter) / fluid_props.viscosity
        return re
    
    def calculate_sand_mass_flow(
        self, 
        fluid_props: FluidProperties, 
        sand_props: SandProperties
    ) -> float:
        """
        Calcula o fluxo mássico de areia baseado na concentração.
        
        mass_flow_sand = concentration × total_mass_flow / 1e6
        
        Args:
            fluid_props: Propriedades do fluido
            sand_props: Propriedades da areia
            
        Returns:
            float: Fluxo mássico de areia (kg/s)
        """
        if sand_props.mass_flow_rate is not None:
            return sand_props.mass_flow_rate
        
        # Calcula área da seção transversal
        if 'internal_diameter' not in self.geometry:
            raise KeyError("Geometria deve ter 'internal_diameter' para calcular fluxo")
        
        diameter = self.geometry['internal_diameter']
        area = 3.14159 * (diameter / 2) ** 2  # πr²
        
        # Fluxo mássico total do fluido
        total_mass_flow = fluid_props.density * fluid_props.velocity * area
        
        # Fluxo mássico de areia (ppmW = partes por milhão em peso)
        sand_mass_flow = sand_props.concentration * total_mass_flow / 1e6
        
        return sand_mass_flow
    
    def _validate_initialization(self) -> None:
        """
        Valida os parâmetros de inicialização.
        
        Raises:
            ValueError: Se algum parâmetro é inválido
            TypeError: Se algum tipo está incorreto
        """
        # Valida component_id
        if not isinstance(self.component_id, str) or not self.component_id.strip():
            raise ValueError("component_id deve ser uma string não vazia")
        
        # Valida component_type
        if not isinstance(self.component_type, str) or not self.component_type.strip():
            raise ValueError("component_type deve ser uma string não vazia")
        
        # Valida material
        if not isinstance(self.material, Material):
            raise TypeError("material deve ser uma instância de Material")
        
        # Valida geometry
        if not isinstance(self.geometry, dict):
            raise TypeError("geometry deve ser um dicionário")
        
        if not self.geometry:
            raise ValueError("geometry não pode estar vazio")
    
    def get_info(self) -> Dict[str, Any]:
        """
        Retorna informações básicas do componente.
        
        Returns:
            Dict[str, Any]: Dicionário com informações do componente
        """
        return {
            "component_id": self.component_id,
            "component_type": self.component_type,
            "material_type": self.material.material_type,
            "geometry": self.geometry.copy()
        }
    
    def __str__(self) -> str:
        """Representação string do componente."""
        return f"{self.component_type}(id='{self.component_id}', material='{self.material.material_type}')"
    
    def __repr__(self) -> str:
        """Representação detalhada do componente."""
        return (f"{self.__class__.__name__}("
                f"component_id='{self.component_id}', "
                f"component_type='{self.component_type}', "
                f"material={self.material.material_type})")





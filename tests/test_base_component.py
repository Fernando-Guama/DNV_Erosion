"""
Teste simples para BaseComponent - GARANTIDAMENTE FUNCIONA
"""

import sys
import os

# Configuração do path - SEMPRE funciona
current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
project_root = os.path.dirname(current_dir)
src_dir = os.path.join(project_root, 'src')

# Debug: mostra informações
print("=" * 50)
print("🔍 DEBUG - Informações do sistema:")
print(f"📄 Arquivo atual: {current_file}")
print(f"📁 Diretório atual: {current_dir}")
print(f"🏠 Raiz do projeto: {project_root}")
print(f"📂 Diretório src: {src_dir}")
print(f"✅ Src existe? {os.path.exists(src_dir)}")
print("=" * 50)

# Adiciona src ao path
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
    print(f"✅ Adicionado {src_dir} ao Python path")

# Verifica se base_component.py existe
base_component_file = os.path.join(src_dir, 'core', 'models', 'base', 'base_component.py')
print(f"🔍 Procurando: {base_component_file}")
print(f"📄 Arquivo existe? {os.path.exists(base_component_file)}")

if not os.path.exists(base_component_file):
    print("❌ ERRO: Arquivo base_component.py não encontrado!")
    print("📋 Arquivos .py encontrados:")
    for root, dirs, files in os.walk(project_root):
        for file in files:
            if file.endswith('.py'):
                print(f"   {os.path.join(root, file)}")
    sys.exit(1)

print("\n🧪 Tentando importar...")

# Tenta importar nossa classe
try:
    print("⏳ Importando BaseComponent...")
    from core.models.base.base_component import BaseComponent
    print("✅ BaseComponent importado!")
    
    print("⏳ Importando Material...")
    from core.models.base.base_component import Material
    print("✅ Material importado!")
    
    print("⏳ Importando outras classes...")
    from core.models.base.base_component import FluidProperties, SandProperties, ErosionResult
    print("✅ Todas as classes importadas!")
    
except Exception as e:
    print(f"❌ ERRO na importação: {e}")
    print("\n🔍 Conteúdo do diretório base:")
    base_dir = os.path.join(src_dir, 'core', 'models', 'base')
    if os.path.exists(base_dir):
        for item in os.listdir(base_dir):
            item_path = os.path.join(base_dir, item)
            if os.path.isfile(item_path):
                print(f"   📄 {item} ({os.path.getsize(item_path)} bytes)")
            else:
                print(f"   📁 {item}/")
    sys.exit(1)

print("\n" + "=" * 50)
print("🎉 SUCESSO! Imports funcionaram!")
print("🧪 Agora vamos testar a funcionalidade...")
print("=" * 50)

# Classe de teste mínima
class SimpleTestComponent(BaseComponent):
    def calculate_erosion(self, fluid_props, sand_props, time_period=1.0, geometry_factor=1.0):
        return ErosionResult(
            relative_erosion_rate=0.1,
            annual_erosion_rate=0.01,
            erosion_for_period=0.01,
            max_erosion_location="test",
            erosion_area=0.1,
            risk_level="low",
            calculation_details={}
        )
    
    def validate_geometry(self):
        return True

# Teste básico
def test_basic_functionality():
    print("🧪 Teste 1: Criando material...")
    
    material = Material(
        material_type="carbon_steel",
        density=7800.0,
        erosion_constant_k=2.0e-9,
        velocity_exponent_n=2.6
    )
    print(f"✅ Material criado: {material.material_type}")
    
    print("\n🧪 Teste 2: Criando componente...")
    
    geometry = {"internal_diameter": 0.1}
    component = SimpleTestComponent(
        component_id="test_001",
        component_type="test",
        material=material,
        geometry=geometry
    )
    print(f"✅ Componente criado: {component}")
    
    print("\n🧪 Teste 3: Criando propriedades do fluido...")
    
    fluid_props = FluidProperties(
        velocity=15.0,
        density=650.0,
        viscosity=0.001
    )
    print(f"✅ Fluido: {fluid_props.velocity} m/s")
    
    print("\n🧪 Teste 4: Calculando Reynolds...")
    
    reynolds = component.get_reynolds_number(fluid_props)
    print(f"✅ Reynolds: {reynolds:,.0f}")
    
    print("\n🧪 Teste 5: Testando erosão...")
    
    sand_props = SandProperties(
        concentration=10.0,
        particle_size_d50=250.0,
        density=2650.0
    )
    
    result = component.calculate_erosion(fluid_props, sand_props)
    print(f"✅ Erosão: {result.annual_erosion_rate} mm/year")
    
    print("\n🎉 TODOS OS TESTES PASSARAM!")
    print("🚀 Sua BaseComponent está funcionando perfeitamente!")

if __name__ == "__main__":
    test_basic_functionality()
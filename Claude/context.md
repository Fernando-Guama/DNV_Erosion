# DNV Erosion Calculator API

## Objetivo
Desenvolver uma API profissional de classe industrial, para calcular taxas de erosão em tubulações de acordo com os modelos da DNV RP O501 (Recommended Practice para Erosional Velocity & Corrosion Rate Calculation), para democratizar acesso a cálculos de Flow Assurance, criando reconhecimento técnico na comunidade de engenharia de óleo e gás e desenvolvendo soluções que possam me gerar uma renda extra.

## Especificações Técnicas
- **Linguagem:** Python 3.9+
- **Framework:** FastAPI
- **Bibliotecas:** 
  - Pydantic (validação)
  - NumPy (cálculos)
  - Pandas (manipulação de dados)
  - SQLAlchemy (banco de dados)
  - Pytest (testes)

## BASE TÉCNICA - DNV-RP-O501
- **Versão:** Edição 2015, Emendada 2021 ("Managing sand production and erosion")
- **Seções a implementar:** 3 (Fundamentals), 4 (Empirical models), 5 (Model parameters)
- **Componentes:** Curvas, tubos retos, tês cegos, reduções, juntas soldadas, válvulas choke, tubos flexíveis
- **Validação:** Casos do Apêndice E (Model validation)

## Input
** dados de entrada de um JSON estruturado:**
- Dados de fluido: densidade, viscosidade, velocidade
- Geometria da tubulação: diâmetro, rugosidade
- Propriedades do material: dureza, composição
- Condições operacionais: temperatura, pressão
- Concentração de sólidos

## Output
** dados de saída de um JSON estruturado:**
- Taxa de erosão (mm/ano)
- Vida útil estimada da tubulação
- Classificação de risco
- Recomendações de manutenção

## Modularização
1. **auth/** - Autenticação e autorização
2. **models/** - Modelos DNV RP O501
3. **API/** - Endpoints REST
4. **io/** - Input and Output
5. **validators/** - Validação de entrada
6. **tests/** - Testes unitários
7. **utils/** - Arquivos utilitários
 
## GitHub
https://github.com/Fernando-Guama/DNV_Erosion

## Status Atual
[ ] Configuração inicial
[ ] Estrutura base do projeto
[ ] Implementação dos modelos DNV

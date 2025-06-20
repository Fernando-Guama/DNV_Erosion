# DNV Erosion Calculator API

## Objetivo
Desenvolver uma API profissional de classe industrial, para calcular taxas de eros�o em tubula��es de acordo com os modelos da DNV RP O501 (Recommended Practice para Erosional Velocity & Corrosion Rate Calculation), para democratizar acesso a c�lculos de Flow Assurance, criando reconhecimento t�cnico na comunidade de engenharia de �leo e g�s e desenvolvendo solu��es que possam me gerar uma renda extra.

## Especifica��es T�cnicas
- **Linguagem:** Python 3.9+
- **Framework:** FastAPI
- **Bibliotecas:** 
  - Pydantic (valida��o)
  - NumPy (c�lculos)
  - Pandas (manipula��o de dados)
  - SQLAlchemy (banco de dados)
  - Pytest (testes)

## BASE T�CNICA - DNV-RP-O501
- **Vers�o:** Edi��o 2015, Emendada 2021 ("Managing sand production and erosion")
- **Se��es a implementar:** 3 (Fundamentals), 4 (Empirical models), 5 (Model parameters)
- **Componentes:** Curvas, tubos retos, t�s cegos, redu��es, juntas soldadas, v�lvulas choke, tubos flex�veis
- **Valida��o:** Casos do Ap�ndice E (Model validation)

## Input
** dados de entrada de um JSON estruturado:**
- Dados de fluido: densidade, viscosidade, velocidade
- Geometria da tubula��o: di�metro, rugosidade
- Propriedades do material: dureza, composi��o
- Condi��es operacionais: temperatura, press�o
- Concentra��o de s�lidos

## Output
** dados de sa�da de um JSON estruturado:**
- Taxa de eros�o (mm/ano)
- Vida �til estimada da tubula��o
- Classifica��o de risco
- Recomenda��es de manuten��o

## Modulariza��o
1. **auth/** - Autentica��o e autoriza��o
2. **models/** - Modelos DNV RP O501
3. **API/** - Endpoints REST
4. **io/** - Input and Output
5. **validators/** - Valida��o de entrada
6. **tests/** - Testes unit�rios
7. **utils/** - Arquivos utilit�rios
 
## GitHub
https://github.com/Fernando-Guama/DNV_Erosion

## Status Atual
[ ] Configura��o inicial
[ ] Estrutura base do projeto
[ ] Implementa��o dos modelos DNV

# Decis�es Arquiteturais - DNV Erosion API

## 1. Framework Web: FastAPI
**Decis�o:** Usar FastAPI ao inv�s de Flask/Django
**Raz�o:** 
- Documenta��o autom�tica (Swagger)
- Valida��o autom�tica com Pydantic
- Performance superior
- Suporte nativo para async/await

## 2. Banco de Dados: PostgreSQL
**Decis�o:** PostgreSQL como banco principal
**Raz�o:**
- Suporte robusto para dados num�ricos
- Extens�es para c�lculos cient�ficos
- Escalabilidade
- JSON nativo para logs de c�lculos

## 3. Estrutura de C�lculos
**Decis�o:** Separar cada modelo DNV em classes independentes
**Raz�o:**
- Facilita testes unit�rios
- Permite extens�o futura
- C�digo mais limpo e manuten�vel

## 4. Valida��o de Dados
**Decis�o:** Usar Pydantic para toda valida��o
**Raz�o:**
- Integra��o nativa com FastAPI
- Valida��o robusta de tipos
- Mensagens de erro claras

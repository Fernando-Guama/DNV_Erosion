# Decisões Arquiteturais - DNV Erosion API

## 1. Framework Web: FastAPI
**Decisão:** Usar FastAPI ao invés de Flask/Django
**Razão:** 
- Documentação automática (Swagger)
- Validação automática com Pydantic
- Performance superior
- Suporte nativo para async/await

## 2. Banco de Dados: PostgreSQL
**Decisão:** PostgreSQL como banco principal
**Razão:**
- Suporte robusto para dados numéricos
- Extensões para cálculos científicos
- Escalabilidade
- JSON nativo para logs de cálculos

## 3. Estrutura de Cálculos
**Decisão:** Separar cada modelo DNV em classes independentes
**Razão:**
- Facilita testes unitários
- Permite extensão futura
- Código mais limpo e manutenível

## 4. Validação de Dados
**Decisão:** Usar Pydantic para toda validação
**Razão:**
- Integração nativa com FastAPI
- Validação robusta de tipos
- Mensagens de erro claras

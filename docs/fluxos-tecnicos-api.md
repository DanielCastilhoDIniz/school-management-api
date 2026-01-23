# Fluxos Técnicos da API

Do Request ao Response – Sistema de Gestão Educacional

Este documento descreve o comportamento técnico interno da API REST, detalhando o caminho completo de uma requisição HTTP desde a chegada até a resposta final.

O objetivo é demonstrar entendimento profundo da arquitetura backend, separação de responsabilidades e fluxo de execução.

---

## Visão Geral do Fluxo Técnico

Toda requisição segue a seguinte cadeia lógica:

1. Request HTTP
2. Middleware de autenticação
3. Resolução de permissões (RBAC)
4. Validação de dados
5. Execução de regras de negócio (domínio)
6. Persistência ou leitura de dados
7. Serialização da resposta
8. Retorno HTTP padronizado

---

## 1. Entrada da Requisição (Request)

* Cliente envia requisição HTTP
* Método HTTP define intenção (GET, POST, PUT, DELETE)
* Headers incluem token JWT (quando necessário)
* Payload enviado em JSON

---

## 2. Autenticação

* Token JWT é extraído do header
* Validação de assinatura e expiração
* Identificação do usuário
* Rejeição imediata se token inválido ou ausente

Resultado possível:

* 401 Unauthorized

---

## 3. Autorização (RBAC)

* Sistema identifica o papel do usuário
* Permissões são verificadas por endpoint
* Acesso permitido ou negado

Resultado possível:

* 403 Forbidden

---

## 4. Validação de Dados

* Validação estrutural do payload
* Validação semântica (regras básicas)
* Normalização de dados

Resultado possível:

* 400 Bad Request
* 422 Unprocessable Entity

---

## 5. Camada de Domínio

* Aplicação das regras de negócio
* Verificações de estado
* Consistência entre entidades

Exemplos:

* Verificar se aluno já está matriculado
* Verificar período letivo ativo

Resultado possível:

* 409 Conflict
* Erro de regra de negócio

---

## 6. Persistência de Dados

* Interação com camada ORM
* Criação, leitura, atualização ou exclusão
* Uso de transações quando necessário

---

## 7. Serialização da Resposta

* Conversão dos dados internos para JSON
* Aplicação de filtros de campos
* Respeito a permissões de visibilidade

---

## 8. Resposta HTTP

* Estrutura padronizada de resposta
* Código HTTP adequado
* Mensagem clara

---

## Exemplo: Fluxo de Matrícula

1. POST /api/v1/matriculas/
2. Autenticação do usuário (secretaria)
3. Verificação de permissão
4. Validação de aluno e turma
5. Regra de negócio: vaga disponível
6. Criação da matrícula
7. Retorno 201 Created

---

## Exemplo: Consulta de Boletim

1. GET /api/v1/boletins/
2. Autenticação
3. RBAC: aluno ou responsável
4. Agregação de notas
5. Serialização
6. Retorno 200 OK

---

## Tratamento Global de Erros

* Erros capturados centralmente
* Conversão para padrão de resposta
* Logs internos para análise
* Mensagens seguras para o cliente

---

## Benefícios da Abordagem

* Clareza arquitetural
* Facilidade de manutenção
* Previsibilidade de comportamento
* Base sólida para testes

---

## Consideração Final

Este fluxo técnico serve como referência para toda implementação e manutenção da API, garantindo consistência e qualidade ao longo do tempo.

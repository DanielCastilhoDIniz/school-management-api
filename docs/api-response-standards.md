# Padrão de Respostas e Erros da API REST

Sistema de Gestão Educacional

## 1. Objetivo

Este documento define o **padrão oficial de respostas HTTP da API REST**, abrangendo:

* estrutura de respostas de sucesso
* estrutura de respostas de erro
* padronização de mensagens
* uso correto de códigos HTTP
* previsibilidade para clientes (frontend, mobile, integrações)

O objetivo é garantir **consistência, clareza e facilidade de integração**.

---

## 2. Princípios Adotados

* API orientada a recursos
* Uso semântico de códigos HTTP
* Corpo de resposta sempre em JSON
* Estrutura previsível em todas as respostas
* Mensagens pensadas para desenvolvedores
* Segurança: não expor detalhes internos

---

## 3. Estrutura Geral de Resposta

Todas as respostas seguem um formato base:

### 3.1 Resposta de Sucesso

```json
{
  "success": true,
  "message": "Descrição clara da operação realizada",
  "data": {}
}
```

### Campos

* **success**: indica sucesso lógico da operação
* **message**: mensagem resumida e legível
* **data**: payload da resposta (objeto, lista ou null)

---

### 3.2 Resposta de Erro

```json
{
  "success": false,
  "error": {
    "code": "IDENTIFICADOR_DO_ERRO",
    "message": "Mensagem clara do erro",
    "details": {}
  }
}
```

### Campos

* **code**: identificador estável para tratamento programático
* **message**: descrição resumida do problema
* **details**: informações adicionais (opcional)

---

## 4. Códigos HTTP Utilizados

### 4.1 Sucesso

| Código         | Uso                  |
| -------------- | -------------------- |
| 200 OK         | leitura, atualização |
| 201 Created    | criação de recurso   |
| 204 No Content | exclusão sem retorno |

---

### 4.2 Erros do Cliente

| Código                   | Uso                 |
| ------------------------ | ------------------- |
| 400 Bad Request          | dados inválidos     |
| 401 Unauthorized         | não autenticado     |
| 403 Forbidden            | sem permissão       |
| 404 Not Found            | recurso inexistente |
| 409 Conflict             | conflito de estado  |
| 422 Unprocessable Entity | validação semântica |

---

### 4.3 Erros do Servidor

| Código                    | Uso                          |
| ------------------------- | ---------------------------- |
| 500 Internal Server Error | erro inesperado              |
| 503 Service Unavailable   | indisponibilidade temporária |

---

## 5. Exemplos de Respostas

### 5.1 Listagem

```json
{
  "success": true,
  "message": "Lista de alunos recuperada com sucesso",
  "data": [
    {
      "id": 1,
      "nome": "João Silva"
    }
  ]
}
```

---

### 5.2 Detalhe de Recurso

```json
{
  "success": true,
  "message": "Aluno encontrado",
  "data": {
    "id": 1,
    "nome": "João Silva"
  }
}
```

---

### 5.3 Criação

```json
{
  "success": true,
  "message": "Aluno criado com sucesso",
  "data": {
    "id": 5
  }
}
```

HTTP 201 Created

---

### 5.4 Erro de Validação

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos",
    "details": {
      "email": ["Este campo é obrigatório"]
    }
  }
}
```

HTTP 422 Unprocessable Entity

---

### 5.5 Não Autenticado

```json
{
  "success": false,
  "error": {
    "code": "AUTH_REQUIRED",
    "message": "Autenticação necessária"
  }
}
```

HTTP 401 Unauthorized

---

### 5.6 Acesso Negado

```json
{
  "success": false,
  "error": {
    "code": "PERMISSION_DENIED",
    "message": "Você não tem permissão para acessar este recurso"
  }
}
```

HTTP 403 Forbidden

---

### 5.7 Recurso Não Encontrado

```json
{
  "success": false,
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Recurso não encontrado"
  }
}
```

HTTP 404 Not Found

---

## 6. Erros Comuns Padronizados

| Código                  | Situação                |
| ----------------------- | ----------------------- |
| AUTH_REQUIRED           | usuário não autenticado |
| PERMISSION_DENIED       | RBAC negou acesso       |
| VALIDATION_ERROR        | erro de validação       |
| RESOURCE_NOT_FOUND      | recurso inexistente     |
| BUSINESS_RULE_VIOLATION | regra de negócio        |
| CONFLICT_STATE          | conflito de estado      |
| INTERNAL_ERROR          | erro inesperado         |

---

## 7. Regras Importantes

* Nunca retornar stack trace
* Nunca expor nomes de tabelas ou campos internos
* Mensagens devem ser estáveis
* `details` é opcional e contextual
* Frontend não depende de texto para lógica

---

## 8. Benefícios do Padrão

✅ API previsível
✅ Fácil integração
✅ Menos bugs no frontend
✅ Melhor DX (Developer Experience)
✅ Facilita testes automatizados

---

## 9. Conexão com RBAC

* Erros de permissão sempre retornam 403
* RBAC nunca revela existência do recurso
* Segurança por obscuridade é evitada

---


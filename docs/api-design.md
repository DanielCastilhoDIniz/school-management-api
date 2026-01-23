# Design da API REST

Mapeamento de Models → Endpoints
Sistema de Gestão Educacional

## 1. Objetivo

Este documento define o **design conceitual da API REST**, mapeando os **models do Django ORM** para **endpoints HTTP**, seguindo boas práticas REST, clareza semântica e foco em escalabilidade.

O objetivo é:

* expor o domínio de forma consistente
* facilitar consumo por frontends e integrações
* garantir segurança e previsibilidade
* servir como base para implementação com Django REST Framework

---

## 2. Princípios de Design Adotados

* Arquitetura RESTful
* URLs orientadas a recursos (substantivos)
* Uso correto de métodos HTTP
* Versionamento de API
* Separação entre leitura e escrita
* Controle de acesso via RBAC
* Respostas previsíveis e padronizadas

Prefixo global da API:

```
/api/v1/
```

---

## 3. Convenções Gerais

### Métodos HTTP

* `GET` → leitura
* `POST` → criação
* `PUT` / `PATCH` → atualização
* `DELETE` → remoção lógica ou física

### Padrões

* JSON como formato de troca
* Paginação em listas
* Filtros via query params
* Ordenação explícita
* Erros padronizados

---

## 4. Endpoints por Contexto de Domínio

---

## 4.1 Autenticação e Autorização (`accounts`)

### Autenticação

* `POST /api/v1/auth/login/`
* `POST /api/v1/auth/refresh/`
* `POST /api/v1/auth/logout/`

Responsabilidades:

* emissão de access token
* renovação via refresh token
* invalidação de sessão quando aplicável

---

### Usuários

* `GET /api/v1/users/`
* `POST /api/v1/users/`
* `GET /api/v1/users/{id}/`
* `PATCH /api/v1/users/{id}/`
* `DELETE /api/v1/users/{id}/`

Controle de acesso:

* administradores e gestores

---

### Papéis (RBAC)

* `GET /api/v1/roles/`
* `POST /api/v1/roles/`
* `GET /api/v1/roles/{id}/`
* `PATCH /api/v1/roles/{id}/`

---

## 4.2 Instituições e Estrutura (`institutions`)

### Instituições

* `GET /api/v1/institutions/`
* `POST /api/v1/institutions/`
* `GET /api/v1/institutions/{id}/`
* `PATCH /api/v1/institutions/{id}/`

---

### Períodos Letivos

* `GET /api/v1/academic-periods/`
* `POST /api/v1/academic-periods/`
* `GET /api/v1/academic-periods/{id}/`
* `PATCH /api/v1/academic-periods/{id}/`

Filtros comuns:

* por instituição
* por tipo de período

---

## 4.3 Domínio Acadêmico (`academics`)

---

### Alunos

* `GET /api/v1/students/`
* `POST /api/v1/students/`
* `GET /api/v1/students/{id}/`
* `PATCH /api/v1/students/{id}/`

---

### Professores

* `GET /api/v1/teachers/`
* `POST /api/v1/teachers/`
* `GET /api/v1/teachers/{id}/`
* `PATCH /api/v1/teachers/{id}/`

---

### Turmas

* `GET /api/v1/classes/`
* `POST /api/v1/classes/`
* `GET /api/v1/classes/{id}/`
* `PATCH /api/v1/classes/{id}/`

---

### Disciplinas

* `GET /api/v1/subjects/`
* `POST /api/v1/subjects/`
* `GET /api/v1/subjects/{id}/`
* `PATCH /api/v1/subjects/{id}/`

---

### Matrículas

* `GET /api/v1/enrollments/`
* `POST /api/v1/enrollments/`
* `PATCH /api/v1/enrollments/{id}/`

Regra:

* não se remove matrícula, apenas altera status

---

## 4.4 Aulas e Avaliações (`academics` / `evaluations`)

---

### Aulas

* `GET /api/v1/lessons/`
* `POST /api/v1/lessons/`
* `GET /api/v1/lessons/{id}/`

Filtro:

* por turma
* por data

---

### Avaliações

* `GET /api/v1/assessments/`
* `POST /api/v1/assessments/`
* `GET /api/v1/assessments/{id}/`

---

### Notas

* `GET /api/v1/grades/`
* `POST /api/v1/grades/`
* `PATCH /api/v1/grades/{id}/`

Restrições:

* aluno deve estar matriculado
* professor responsável pela turma

---

## 5. Endpoints Aninhados (quando necessário)

Uso **controlado** de nested routes:

Exemplos:

* `/api/v1/classes/{id}/students/`
* `/api/v1/classes/{id}/assessments/`
* `/api/v1/students/{id}/grades/`

Justificativa:

* melhora legibilidade
* evita excesso de joins no cliente

---

## 6. Controle de Acesso por Endpoint

Exemplos:

* alunos → apenas leitura dos próprios dados
* professores → escrita em aulas e notas
* gestores → controle acadêmico
* administradores → acesso global

Controle feito:

* via RBAC
* aplicado no backend
* nunca apenas no frontend

---

## 7. Versionamento da API

* Versão no path (`/v1/`)
* Mudanças breaking → nova versão
* Compatibilidade mantida por versão

---
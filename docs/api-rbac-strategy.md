# Estratégia de Permissões por Endpoint

RBAC Aplicado à API REST
Sistema de Gestão Educacional

## 1. Objetivo

Este documento define a **estratégia de controle de acesso baseada em papéis (RBAC)** aplicada aos **endpoints da API REST** do sistema de gestão educacional.

O objetivo é:

* garantir segurança e isolamento de dados
* alinhar permissões às responsabilidades institucionais
* evitar acesso indevido
* orientar a implementação no backend (DRF)

Este controle é aplicado **exclusivamente no backend**.

---

## 2. Princípios de Segurança

* Acesso negado por padrão
* Permissões concedidas explicitamente
* RBAC como camada primária de controle
* Validações adicionais por contexto (instituição, turma, matrícula)
* Nenhuma decisão de segurança no frontend

---

## 3. Papéis do Sistema

Papéis considerados neste documento:

* **Administrador**
* **Gestor**
* **Professor**
* **Aluno**
* **Responsável** (opcional)

Papéis são **atributos do usuário**, não do recurso.

---

## 4. Níveis de Permissão

Definição conceitual de ações:

* **READ** – visualizar dados
* **WRITE** – criar e atualizar
* **DELETE** – remover ou desativar
* **ADMIN** – controle total

---

## 5. Estratégia Geral de Aplicação

Cada endpoint possui:

1. verificação de autenticação
2. verificação de papel
3. verificação de escopo institucional
4. verificação contextual (quando aplicável)

Exemplo:

> Professor autenticado + papel válido + turma sob sua responsabilidade

---

## 6. Matriz de Permissões por Recurso

### 6.1 Autenticação

| Endpoint | Admin | Gestor | Professor | Aluno |
| -------- | ----- | ------ | --------- | ----- |
| login    | ✔     | ✔      | ✔         | ✔     |
| refresh  | ✔     | ✔      | ✔         | ✔     |
| logout   | ✔     | ✔      | ✔         | ✔     |

---

### 6.2 Usuários

| Ação            | Admin | Gestor | Professor | Aluno |
| --------------- | ----- | ------ | --------- | ----- |
| listar usuários | ✔     | ✔      | ✖         | ✖     |
| criar usuário   | ✔     | ✔      | ✖         | ✖     |
| editar usuário  | ✔     | ✔      | ⚠️        | ⚠️    |
| excluir usuário | ✔     | ✖      | ✖         | ✖     |

⚠️ edição restrita ao próprio usuário

---

### 6.3 Instituições

| Ação       | Admin | Gestor | Professor | Aluno |
| ---------- | ----- | ------ | --------- | ----- |
| visualizar | ✔     | ✔      | ✖         | ✖     |
| editar     | ✔     | ✖      | ✖         | ✖     |

---

### 6.4 Alunos

| Ação       | Admin | Gestor | Professor | Aluno |
| ---------- | ----- | ------ | --------- | ----- |
| listar     | ✔     | ✔      | ✔         | ✖     |
| criar      | ✔     | ✔      | ✖         | ✖     |
| visualizar | ✔     | ✔      | ✔         | ✔     |
| editar     | ✔     | ✔      | ✖         | ⚠️    |

⚠️ aluno pode editar apenas dados pessoais permitidos

---

### 6.5 Professores

| Ação   | Admin | Gestor | Professor | Aluno |
| ------ | ----- | ------ | --------- | ----- |
| listar | ✔     | ✔      | ✖         | ✖     |
| criar  | ✔     | ✔      | ✖         | ✖     |
| editar | ✔     | ✔      | ⚠️        | ✖     |

⚠️ professor edita apenas próprio perfil

---

### 6.6 Turmas

| Ação   | Admin | Gestor | Professor | Aluno |
| ------ | ----- | ------ | --------- | ----- |
| listar | ✔     | ✔      | ✔         | ✔     |
| criar  | ✔     | ✔      | ✖         | ✖     |
| editar | ✔     | ✔      | ⚠️        | ✖     |

⚠️ professor apenas em turmas atribuídas

---

### 6.7 Matrículas

| Ação          | Admin | Gestor | Professor | Aluno |
| ------------- | ----- | ------ | --------- | ----- |
| criar         | ✔     | ✔      | ✖         | ✖     |
| editar status | ✔     | ✔      | ✖         | ✖     |
| visualizar    | ✔     | ✔      | ✔         | ⚠️    |

⚠️ aluno apenas suas próprias matrículas

---

### 6.8 Aulas

| Ação       | Admin | Gestor | Professor | Aluno |
| ---------- | ----- | ------ | --------- | ----- |
| criar      | ✔     | ✔      | ✔         | ✖     |
| editar     | ✔     | ✔      | ✔         | ✖     |
| visualizar | ✔     | ✔      | ✔         | ✔     |

---

### 6.9 Avaliações

| Ação       | Admin | Gestor | Professor | Aluno |
| ---------- | ----- | ------ | --------- | ----- |
| criar      | ✔     | ✔      | ✔         | ✖     |
| editar     | ✔     | ✔      | ⚠️        | ✖     |
| visualizar | ✔     | ✔      | ✔         | ✔     |

⚠️ professor apenas antes da publicação

---

### 6.10 Notas

| Ação       | Admin | Gestor | Professor | Aluno |
| ---------- | ----- | ------ | --------- | ----- |
| lançar     | ✔     | ✔      | ✔         | ✖     |
| editar     | ✔     | ✔      | ⚠️        | ✖     |
| visualizar | ✔     | ✔      | ✔         | ✔     |

⚠️ professor apenas em turmas atribuídas

---

## 7. Permissões Contextuais

Além do papel, validam-se:

* vínculo com a instituição
* vínculo com a turma
* matrícula ativa
* período letivo vigente

RBAC ≠ autorização completa → contexto é obrigatório.

---

## 8. Auditoria e Segurança

* ações sensíveis devem ser auditáveis
* alterações de notas e avaliações geram histórico
* tentativas de acesso indevido são registradas

---

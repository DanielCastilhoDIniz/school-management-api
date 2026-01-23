# Mapeamento ERD Lógico → Django Models

Sistema de Gestão Educacional

## 1. Objetivo

Este documento descreve o **mapeamento conceitual entre o ERD Lógico e os modelos do Django ORM** utilizados no sistema de gestão educacional.

O foco é:

* traduzir o domínio em estruturas persistentes
* manter separação clara de responsabilidades
* preparar o sistema para APIs REST escaláveis
* evitar decisões prematuras de implementação

Este documento **não contém código**, apenas decisões arquiteturais.

---

## 2. Diretrizes Gerais de Modelagem

As seguintes diretrizes orientam a criação dos modelos:

* Separação entre identidade (usuário) e domínio acadêmico
* Normalização até 3ª Forma Normal
* Relacionamentos explícitos quando há regras de negócio
* Compatibilidade direta com Django ORM e DRF
* Clareza para manutenção e evolução futura

---

## 3. Organização dos Apps Django

A modelagem segue **divisão por contexto de domínio**, evitando monólitos acoplados.

### Estrutura lógica de apps

* `accounts`
  Autenticação, usuários e RBAC

* `institutions`
  Estrutura institucional e períodos letivos

* `academics`
  Alunos, professores, turmas, disciplinas e matrículas

* `evaluations`
  Avaliações e notas

* `core`
  Modelos base e comportamentos reutilizáveis

---

## 4. Mapeamento de Entidades para Models

---

## 4.1 App `institutions`

### Institution

Representa a instituição educacional.

**Responsabilidades:**

* escopo organizacional do sistema
* vínculo com usuários e dados acadêmicos

**Relacionamentos:**

* um-para-muitos com usuários
* um-para-muitos com períodos letivos
* um-para-muitos com turmas

---

### AcademicPeriod

Representa períodos letivos configuráveis.

**Responsabilidades:**

* organização temporal do calendário acadêmico
* suporte a bimestre, trimestre, semestre etc.

**Relacionamentos:**

* pertence a uma instituição
* associado a turmas
* associado a avaliações

---

## 4.2 App `accounts`

### User

Representa a identidade autenticável.

**Decisão arquitetural:**
Usuário **não é** aluno nem professor — apenas identidade.

**Responsabilidades:**

* autenticação
* estado da conta
* vínculo institucional

**Relacionamentos:**

* pertence a uma instituição
* muitos-para-muitos com papéis
* um-para-um opcional com aluno
* um-para-um opcional com professor

---

### Role

Define papéis do sistema (RBAC).

**Responsabilidades:**

* agrupar permissões
* facilitar controle de acesso

**Relacionamentos:**

* muitos-para-muitos com usuários

---

## 4.3 App `academics`

### Student

Representa o aluno no domínio acadêmico.

**Responsabilidades:**

* dados acadêmicos
* vínculo com matrículas e notas

**Relacionamentos:**

* um-para-um com usuário
* um-para-muitos com matrículas
* um-para-muitos com notas

---

### Teacher

Representa o professor.

**Responsabilidades:**

* atuação acadêmica
* vínculo com disciplinas

**Relacionamentos:**

* um-para-um com usuário
* muitos-para-muitos com disciplinas

---

### Class (Turma)

Agrupa alunos em um contexto acadêmico.

**Responsabilidades:**

* organização acadêmica
* contexto para aulas e avaliações

**Relacionamentos:**

* pertence a uma instituição
* pertence a um período letivo
* um-para-muitos com matrículas
* muitos-para-muitos com disciplinas
* um-para-muitos com aulas
* um-para-muitos com avaliações

---

### Subject

Representa disciplinas curriculares.

**Responsabilidades:**

* definição de componentes curriculares reutilizáveis

**Relacionamentos:**

* muitos-para-muitos com turmas
* muitos-para-muitos com professores

---

### Enrollment

Representa a matrícula.

**Responsabilidades:**

* materializar aluno ↔ turma
* armazenar estado da matrícula

**Relacionamentos:**

* pertence a um aluno
* pertence a uma turma

**Restrições:**

* aluno + turma deve ser único

---

### Lesson

Representa aulas ministradas.

**Responsabilidades:**

* registro de encontros acadêmicos

**Relacionamentos:**

* pertence a uma turma

---

## 4.4 App `evaluations`

### Assessment

Representa avaliações acadêmicas.

**Responsabilidades:**

* definição de instrumentos avaliativos

**Relacionamentos:**

* pertence a uma turma
* pertence a um período letivo
* um-para-muitos com notas

---

### Grade

Representa notas individuais.

**Responsabilidades:**

* armazenar desempenho do aluno

**Relacionamentos:**

* pertence a uma avaliação
* pertence a um aluno

**Regra de negócio crítica:**

* aluno deve estar matriculado na turma da avaliação

---

## 5. Modelos Base (`core`)

### TimeStampedModel (abstrato)

Modelo reutilizável para auditoria temporal.

**Responsabilidades:**

* data de criação
* data de atualização

Aplicável à maioria dos modelos do sistema.

---

## 6. Benefícios do Mapeamento

Este documento garante:

* coerência entre domínio e persistência
* facilidade de implementação futura
* clareza para revisões técnicas
* alinhamento com práticas profissionais
* leitura clara para recrutadores e arquitetos

---
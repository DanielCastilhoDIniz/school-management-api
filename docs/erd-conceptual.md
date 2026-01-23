
# ERD Conceitual – Sistema de Gestão Educacional

## 1. Objetivo

Este documento descreve o **Modelo Entidade–Relacionamento (ERD) em nível conceitual** do sistema de gestão educacional.
O objetivo é representar, de forma abstrata e independente de tecnologia, as **principais entidades do domínio**, seus **relacionamentos** e **regras conceituais**, servindo como base para as fases posteriores de modelagem lógica e implementação.

Este modelo não considera detalhes técnicos como banco de dados, ORM ou framework.

---

## 2. Visão Geral do Domínio

O sistema de gestão educacional é responsável por administrar:

* Estrutura institucional
* Usuários e seus papéis
* Organização acadêmica
* Matrículas e turmas
* Registro de aulas
* Avaliações e notas
* Períodos letivos configuráveis

O domínio foi modelado para suportar diferentes formatos educacionais, respeitando variações como bimestres, trimestres, quadrimestres ou semestres.

---

## 3. Entidades Conceituais

### 3.1 Instituição

Representa a organização educacional (escola, faculdade, centro educacional).

**Responsabilidade conceitual:**

* Centralizar o contexto organizacional do sistema
* Agrupar usuários, turmas e períodos letivos

---

### 3.2 Usuário

Representa qualquer pessoa que acessa o sistema.

**Responsabilidade conceitual:**

* Autenticação e autorização
* Base para diferentes papéis (aluno, professor, gestor, etc.)

---

### 3.3 Papel

Define o conjunto de responsabilidades e permissões atribuídas a um usuário.

**Responsabilidade conceitual:**

* Determinar o nível de acesso e atuação no sistema

---

### 3.4 Aluno

Representa o indivíduo matriculado em uma instituição para fins acadêmicos.

**Responsabilidade conceitual:**

* Participar de turmas
* Receber avaliações e notas

---

### 3.5 Professor

Representa o profissional responsável por ministrar disciplinas e registrar atividades acadêmicas.

**Responsabilidade conceitual:**

* Ministrar disciplinas
* Registrar aulas e avaliações

---

### 3.6 Turma

Representa um agrupamento de alunos em um determinado período letivo.

**Responsabilidade conceitual:**

* Organizar alunos e disciplinas
* Servir de contexto para aulas e avaliações

---

### 3.7 Disciplina

Representa um componente curricular oferecido pela instituição.

**Responsabilidade conceitual:**

* Estruturar o conteúdo acadêmico ministrado em turmas

---

### 3.8 Matrícula

Entidade associativa que formaliza o vínculo entre aluno, turma e período letivo.

**Responsabilidade conceitual:**

* Registrar a participação do aluno em uma turma específica

---

### 3.9 Aula

Representa um encontro acadêmico realizado dentro de uma turma.

**Responsabilidade conceitual:**

* Registrar conteúdos ministrados e presença

---

### 3.10 Avaliação

Representa um instrumento de avaliação aplicado a uma turma.

**Responsabilidade conceitual:**

* Medir o desempenho dos alunos em uma disciplina ou período

---

### 3.11 Nota

Representa o resultado de uma avaliação para um aluno específico.

**Responsabilidade conceitual:**

* Registrar o desempenho individual do aluno

---

### 3.12 Período Letivo

Define a divisão temporal do calendário acadêmico.

**Responsabilidade conceitual:**

* Organizar o ano letivo em bimestres, trimestres, semestres ou outros formatos

---

## 4. Relacionamentos Conceituais

### Instituição ↔ Usuário

* Uma instituição possui vários usuários
* Um usuário pertence a uma instituição
  **Cardinalidade:** 1 — N

---

### Usuário ↔ Papel

* Um usuário pode possuir um ou mais papéis
* Um papel pode ser atribuído a vários usuários
  **Cardinalidade:** N — N

---

### Aluno ↔ Turma (via Matrícula)

* Um aluno pode estar matriculado em várias turmas ao longo do tempo
* Uma turma possui vários alunos
  **Cardinalidade:** N — N
  **Entidade associativa:** Matrícula

---

### Professor ↔ Disciplina

* Um professor pode ministrar várias disciplinas
* Uma disciplina pode ser ministrada por vários professores
  **Cardinalidade:** N — N

---

### Turma ↔ Disciplina

* Uma turma possui uma ou mais disciplinas
* Uma disciplina pode ser ofertada em várias turmas
  **Cardinalidade:** N — N

---

### Turma ↔ Aula

* Uma turma possui várias aulas
* Uma aula pertence a uma única turma
  **Cardinalidade:** 1 — N

---

### Turma ↔ Avaliação

* Uma turma pode possuir várias avaliações
* Uma avaliação pertence a uma única turma
  **Cardinalidade:** 1 — N

---

### Avaliação ↔ Nota

* Uma avaliação gera várias notas
* Uma nota pertence a uma única avaliação e a um aluno
  **Cardinalidade:** 1 — N

---

### Instituição ↔ Período Letivo

* Uma instituição define vários períodos letivos
* Um período letivo pertence a uma instituição
  **Cardinalidade:** 1 — N

---

## 5. Regras Conceituais Importantes

* Uma **nota não existe sem uma avaliação associada**
* Um **aluno só pode receber nota se estiver matriculado na turma**
* Avaliações são sempre vinculadas a um período letivo
* O formato do período letivo é configurável pela instituição
* Usuários podem acumular múltiplos papéis no sistema

---

## 6. Escopo e Limitações

Este ERD:

* É **independente de tecnologia**
* Não define tipos de dados
* Não define chaves técnicas
* Não considera otimizações de banco de dados

Esses aspectos serão tratados na **modelagem lógica** e na **implementação**.

---
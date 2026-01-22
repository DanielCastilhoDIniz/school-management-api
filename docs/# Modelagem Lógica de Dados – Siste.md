# Modelagem Lógica de Dados – Sistema de Gestão Educacional

## 1. Objetivo da Modelagem

Esta modelagem lógica transforma o domínio educacional previamente definido em uma estrutura consistente de dados, independente de banco ou framework, servindo como base para a implementação com Django + DRF.

O foco está em integridade, clareza de relacionamentos e aderência às regras de negócio.

---

## 2. Entidades e Identificadores

Todas as entidades possuem um identificador único e imutável.

* Instituição
* Aluno
* Professor
* Classe
* Turma
* Matrícula
* Disciplina
* Registro de Aula
* Avaliação
* Nota

---

## 3. Entidades Principais (Visão Lógica)

### Instituição

* Identificador
* Nome
* Modelo de período avaliativo
* Calendário letivo
* Status

Relacionamentos:

* Uma instituição possui muitos alunos, professores e classes

---

### Aluno

* Identificador
* Dados pessoais
* Situação acadêmica

Relacionamentos:

* Um aluno possui várias matrículas

Restrição:

* Um aluno não pode possuir mais de uma matrícula ativa na mesma turma

---

### Professor

* Identificador
* Dados funcionais
* Área de atuação

Relacionamentos:

* Um professor pode estar associado a várias turmas e disciplinas

---

### Classe (Série / Ano / Semestre)

* Identificador
* Nome ou código
* Ordem acadêmica

Relacionamentos:

* Uma classe possui várias turmas
* Uma classe possui várias disciplinas

---

### Turma

* Identificador
* Ano letivo
* Período
* Status

Relacionamentos:

* Uma turma pertence a uma classe
* Uma turma possui várias matrículas
* Uma turma possui várias disciplinas

Restrição:

* Apenas turmas ativas aceitam novas matrículas

---

### Matrícula

* Identificador
* Data de ingresso
* Status

Relacionamentos:

* Uma matrícula pertence a um aluno
* Uma matrícula pertence a uma turma

Restrição:

* Deve existir apenas uma matrícula ativa por aluno e turma

---

### Disciplina

* Identificador
* Nome
* Carga horária

Relacionamentos:

* Uma disciplina pertence a uma classe
* Uma disciplina pode ser ministrada em várias turmas

---

### Registro de Aula

* Identificador
* Data da aula
* Conteúdo ministrado

Relacionamentos:

* Um registro de aula pertence a uma turma
* Um registro de aula pertence a uma disciplina
* Um registro de aula pertence a um professor

Restrição:

* Não pode existir registro de aula para turma encerrada

---

### Avaliação

* Identificador
* Tipo
* Peso
* Período avaliativo
* Status

Relacionamentos:

* Uma avaliação pertence a uma disciplina
* Uma avaliação pertence a uma turma

Restrição:

* Avaliações só podem ser criadas em períodos letivos ativos

---

### Nota

* Identificador
* Valor

Relacionamentos:

* Uma nota pertence a um aluno
* Uma nota pertence a uma avaliação

Restrição:

* Notas só podem ser lançadas para alunos com matrícula ativa

---

## 4. Cardinalidades Principais

* Instituição 1:N Aluno
* Instituição 1:N Professor
* Classe 1:N Turma
* Turma 1:N Matrícula
* Aluno 1:N Matrícula
* Disciplina 1:N Avaliação
* Avaliação 1:N Nota

---

## 5. Estados e Controle de Fluxo

### Turma

* Planejada
* Ativa
* Encerrada

### Matrícula

* Ativa
* Trancada
* Cancelada
* Concluída

### Avaliação

* Criada
* Aplicada
* Encerrada

Estados controlam permissões e ações possíveis no sistema.

---

## 6. Integridade e Consistência

A modelagem prioriza:

* Normalização lógica
* Evitar redundância
* Garantir histórico acadêmico
* Clareza nos vínculos entre entidades

---

## 7. Uso no Projeto

Este documento orienta:

* Criação dos models no Django
* Definição de constraints
* Estruturação de serializers
* Definição de endpoints REST
* Escrita de testes de integridade

---

## 8. Valor para Portfólio

Esta modelagem demonstra:

* Capacidade de traduzir domínio em estrutura de dados
* Preocupação com regras reais de negócio
* Pensamento arquitetural aplicado a backend

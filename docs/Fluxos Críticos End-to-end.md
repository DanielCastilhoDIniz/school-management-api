# Fluxos Críticos End-to-End

Este documento descreve os principais fluxos de negócio do sistema de gestão educacional, do ponto de vista funcional e arquitetural, sem entrar em detalhes de implementação.

## Objetivo

Garantir entendimento claro dos processos centrais do sistema, alinhando regras de negócio, modelos de domínio, permissões (RBAC) e endpoints REST.

---

## Fluxo 1 – Matrícula de Aluno

### Atores Envolvidos

* Secretaria
* Sistema

### Pré-condições

* Aluno cadastrado
* Turma existente
* Período letivo ativo

### Passos

1. Secretaria autentica-se no sistema
2. Seleciona aluno
3. Seleciona turma e período letivo
4. Sistema valida disponibilidade de vagas
5. Sistema cria registro de matrícula
6. Sistema retorna confirmação

### Pós-condições

* Aluno associado à turma
* Matrícula ativa

---

## Fluxo 2 – Registro de Aula

### Atores Envolvidos

* Professor

### Pré-condições

* Professor vinculado à turma
* Disciplina associada

### Passos

1. Professor autentica-se
2. Seleciona turma e disciplina
3. Registra conteúdo e data
4. Sistema valida vínculo
5. Sistema salva registro de aula

### Pós-condições

* Aula registrada
* Disponível para consulta

---

## Fluxo 3 – Lançamento de Avaliações

### Atores Envolvidos

* Professor

### Pré-condições

* Avaliação criada
* Alunos matriculados

### Passos

1. Professor autentica-se
2. Seleciona avaliação
3. Informa notas dos alunos
4. Sistema valida regras (período, peso)
5. Sistema salva notas

### Pós-condições

* Notas registradas

---

## Fluxo 4 – Consulta de Boletim

### Atores Envolvidos

* Aluno
* Responsável

### Pré-condições

* Notas lançadas

### Passos

1. Usuário autentica-se
2. Solicita boletim
3. Sistema verifica permissão
4. Sistema agrega dados
5. Retorna boletim consolidado

### Pós-condições

* Visualização do desempenho

---

## Observações Arquiteturais

* Todos os fluxos passam por autenticação JWT
* RBAC aplicado por endpoint
* Regras de negócio centralizadas no domínio

---

## Próximos Fluxos Possíveis

* Transferência de aluno
* Encerramento de período letivo
* Emissão de históricos

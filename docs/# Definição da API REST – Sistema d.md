# Definição da API REST – Sistema de Gestão Educacional

## 1. Objetivo da API

Esta API REST expõe funcionalidades do domínio educacional de forma segura, previsível e desacoplada, permitindo o consumo por aplicações web e mobile.

A API é orientada a recursos e casos de uso, não sendo um espelhamento direto das entidades do banco de dados.

---

## 2. Princípios de Design

* Versionamento explícito da API (v1)
* Uso consistente de verbos HTTP
* Recursos nomeados no plural
* Estados do domínio controlam ações permitidas
* Regras de negócio aplicadas antes de persistência

---

## 3. Recursos Principais

### Instituições

Recurso responsável pela configuração acadêmica global.

Ações expostas:

* Criar instituição
* Consultar dados institucionais
* Atualizar configurações acadêmicas

---

### Alunos

Recurso responsável pelo cadastro e consulta de discentes.

Ações expostas:

* Criar aluno
* Listar alunos
* Consultar aluno específico
* Atualizar dados cadastrais

---

### Professores

Recurso responsável pelo cadastro e gestão de docentes.

Ações expostas:

* Criar professor
* Listar professores
* Consultar professor específico
* Atualizar dados funcionais

---

### Classes

Recurso responsável pela organização dos níveis educacionais.

Ações expostas:

* Criar classe
* Listar classes
* Consultar classe específica

---

### Turmas

Recurso responsável pela gestão de turmas em períodos letivos.

Ações expostas:

* Criar turma
* Ativar turma
* Encerrar turma
* Listar turmas
* Consultar turma específica

Observação:

* Ações de ativação e encerramento dependem do estado atual da turma

---

### Matrículas

Recurso responsável pelo vínculo aluno–turma.

Ações expostas:

* Criar matrícula
* Consultar matrículas por aluno ou turma
* Trancar matrícula
* Cancelar matrícula
* Concluir matrícula

Observação:

* Mudanças de estado seguem regras do domínio

---

### Disciplinas

Recurso responsável pelo cadastro curricular.

Ações expostas:

* Criar disciplina
* Associar disciplina a classes e turmas
* Listar disciplinas

---

### Registros de Aula

Recurso responsável pelo registro de aulas ministradas.

Ações expostas:

* Registrar aula
* Consultar registros por turma ou disciplina

Observação:

* Apenas professores vinculados podem registrar aulas

---

### Avaliações

Recurso responsável pela criação e gestão de instrumentos avaliativos.

Ações expostas:

* Criar avaliação
* Aplicar avaliação
* Encerrar avaliação
* Consultar avaliações por turma ou disciplina

---

### Notas

Recurso responsável pelo lançamento e consulta de notas.

Ações expostas:

* Lançar nota
* Consultar notas por aluno, avaliação ou turma

Observação:

* Notas só podem ser lançadas para matrículas ativas

---

## 4. Ações de Domínio (não-CRUD)

Algumas ações representam transições de estado e são tratadas explicitamente:

* Ativar turma
* Encerrar turma
* Trancar matrícula
* Cancelar matrícula
* Concluir matrícula
* Aplicar avaliação
* Encerrar avaliação

Essas ações não representam simples atualizações de campos, mas regras de negócio.

---

## 5. Controle de Acesso (visão geral)

* Administradores: acesso total aos recursos
* Professores: acesso a turmas, disciplinas, registros de aula e avaliações associadas
* Alunos: acesso restrito a dados próprios, matrículas e notas

---

## 6. Padrões de Resposta

* Respostas padronizadas em JSON
* Uso consistente de códigos HTTP
* Mensagens de erro claras e sem vazamento de informações sensíveis

---

## 7. Uso no Projeto

Este documento orienta:

* Definição de ViewSets e rotas no Django REST Framework
* Aplicação de permissões e autenticação
* Escrita de serializers orientados a casos de uso
* Documentação OpenAPI

---

## 8. Valor para Portfólio

Esta definição de API demonstra:

* Capacidade de transformar domínio em contratos REST
* Separação entre dados e comportamento
* Design de APIs orientado a regras de negócio

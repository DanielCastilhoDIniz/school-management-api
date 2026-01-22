# Perfis de Acesso e Permissões – Sistema de Gestão Educacional

## 1. Objetivo

Este documento define os perfis de acesso do sistema e as permissões associadas a cada recurso da API REST, garantindo segurança, segregação de responsabilidades e aderência às regras de negócio do domínio educacional.

As permissões são orientadas a **papéis (RBAC)** e **estados do domínio**, não apenas a operações CRUD.

---

## 2. Perfis de Usuário

### Administrador Institucional

Representa usuários responsáveis pela gestão global da instituição.

Responsabilidades gerais:

* Configuração acadêmica
* Gestão de cadastros
* Supervisão de operações

---

### Professor

Representa o docente responsável por ministrar aulas e avaliar alunos.

Responsabilidades gerais:

* Registro de aulas
* Criação e aplicação de avaliações
* Lançamento de notas

---

### Aluno

Representa o discente vinculado à instituição.

Responsabilidades gerais:

* Consulta de dados acadêmicos próprios
* Acompanhamento de matrículas, avaliações e notas

---

## 3. Permissões por Recurso

### Instituições

* Administrador: criar, consultar e atualizar
* Professor: consulta
* Aluno: consulta

---

### Alunos

* Administrador: criar, listar, consultar e atualizar
* Professor: consulta
* Aluno: consulta e atualização restrita aos próprios dados

---

### Professores

* Administrador: criar, listar, consultar e atualizar
* Professor: consulta e atualização restrita aos próprios dados
* Aluno: consulta

---

### Classes

* Administrador: criar, listar e consultar
* Professor: consulta
* Aluno: consulta

---

### Turmas

* Administrador: criar, ativar, encerrar, listar e consultar
* Professor: consulta das turmas vinculadas
* Aluno: consulta das turmas vinculadas

Restrição:

* Apenas administradores podem alterar o estado da turma

---

### Matrículas

* Administrador: criar, trancar, cancelar, concluir e consultar
* Professor: consulta
* Aluno: consulta das próprias matrículas

Restrição:

* Alunos não podem alterar o estado de matrículas

---

### Disciplinas

* Administrador: criar, associar a classes e turmas, listar
* Professor: consulta das disciplinas vinculadas
* Aluno: consulta

---

### Registros de Aula

* Administrador: consulta
* Professor: criar e consultar registros das turmas vinculadas
* Aluno: consulta

Restrição:

* Apenas professores vinculados à turma podem registrar aulas

---

### Avaliações

* Administrador: consulta
* Professor: criar, aplicar, encerrar e consultar avaliações das turmas vinculadas
* Aluno: consulta

Restrição:

* Apenas professores podem alterar o estado de avaliações

---

### Notas

* Administrador: consulta
* Professor: lançar e consultar notas das turmas vinculadas
* Aluno: consulta das próprias notas

Restrição:

* Notas só podem ser lançadas para alunos com matrícula ativa

---

## 4. Permissões Baseadas em Estado

Algumas ações dependem do estado atual da entidade:

* Turmas encerradas não aceitam novas matrículas ou registros de aula
* Matrículas trancadas ou canceladas não recebem novas notas
* Avaliações encerradas não podem ser alteradas

---

## 5. Considerações de Segurança

* O sistema aplica autenticação antes de autorização
* Permissões são avaliadas por recurso e ação
* Regras de domínio prevalecem sobre permissões genéricas

---

## 6. Uso no Projeto

Este documento orienta:

* Implementação de classes de permissão no DRF
* Definição de políticas de acesso
* Escrita de testes de autorização
* Documentação de segurança da API

---

## 7. Valor para Portfólio

Esta definição demonstra:

* Aplicação prática de RBAC
* Integração entre domínio e segurança
* Preocupação com controle de acesso em sistemas reais

# Checklist de Implementação Backend

API REST – Sistema de Gestão Educacional (Django + DRF)

Este documento descreve a ordem lógica e profissional de implementação do backend, do zero até um sistema pronto para produção, sem entrar em código.

---

## Fase 0 – Preparação do Projeto

* Definir escopo funcional mínimo (MVP)
* Definir domínio principal (educacional)
* Definir arquitetura (API REST desacoplada)
* Criar repositório Git
* Definir convenções de commit e branches

---

## Fase 1 – Ambiente e Base Técnica

* Criar ambiente virtual
* Definir versão estável do Python
* Instalar Django
* Criar projeto Django
* Criar app core
* Ajustar settings iniciais
* Configurar variáveis de ambiente

---

## Fase 2 – Frameworks e Infraestrutura

* Instalar Django REST Framework
* Definir padrão de respostas da API
* Configurar autenticação JWT
* Documentar autenticação (authentication.md)
* Configurar Swagger / OpenAPI
* Criar documentação da API (openapi.md)

---

## Fase 3 – Usuários, Papéis e Permissões

* Definir modelo de usuário customizado
* Definir papéis (admin, secretaria, professor, aluno, responsável)
* Definir permissões por papel
* Documentar RBAC (rbac.md)

---

## Fase 4 – Modelagem do Domínio Acadêmico

* Definir entidades principais (Aluno, Professor, Turma, Disciplina)
* Definir relações entre entidades
* Criar documentação de domínio (domain-academic.md)
* Criar ERD conceitual
* Criar ERD lógico (pensando em ORM)
* Mapear ERD → Models Django

---

## Fase 5 – Design da API

* Definir recursos REST
* Definir endpoints por entidade
* Definir métodos HTTP
* Definir filtros, paginação e ordenação
* Mapear Models → Endpoints
* Definir permissões por endpoint

---

## Fase 6 – Regras de Negócio

* Implementar validações de domínio
* Definir regras de matrícula
* Definir regras de avaliação
* Definir regras de acesso a notas
* Documentar regras críticas

---

## Fase 7 – Fluxos End-to-End

* Implementar fluxo de matrícula
* Implementar fluxo de registro de aula
* Implementar fluxo de lançamento de notas
* Implementar fluxo de consulta de boletim

---

## Fase 8 – Qualidade e Segurança

* Implementar tratamento global de erros
* Garantir uso correto de códigos HTTP
* Aplicar RBAC em todos os endpoints
* Revisar exposição de dados sensíveis

---

## Fase 9 – Testes

* Criar testes de modelos
* Criar testes de endpoints
* Criar testes de permissões
* Criar testes de fluxos críticos

---

## Fase 10 – Finalização

* Revisar documentação
* Ajustar README
* Versionar API (v1)
* Preparar projeto para deploy

---

## Observação Final

A implementação segue o princípio de evoluir de uma base simples (nível júnior/pleno) para refinamentos progressivos (nível sênior), garantindo clareza, organização e manutenibilidade.

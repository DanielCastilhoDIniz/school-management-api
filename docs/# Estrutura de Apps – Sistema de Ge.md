# Estrutura de Apps – Sistema de Gestão Educacional

## 1. Objetivo

Definir uma estrutura de aplicações (apps) no Django alinhada ao domínio educacional, promovendo:

* Separação clara de responsabilidades
* Escalabilidade
* Manutenção facilitada
* Aderência a boas práticas de projetos profissionais

A divisão em apps segue **fronteiras de domínio**, não critérios técnicos arbitrários.

---

## 2. Princípios Adotados

* Cada app representa um **subdomínio coeso**
* Apps não conhecem detalhes internos uns dos outros
* Comunicação ocorre via modelos bem definidos e regras de negócio
* Evita-se um "app monolítico" genérico

---

## 3. Apps Principais do Projeto

### 3.1 accounts

Responsável por autenticação e identidade dos usuários.

Responsabilidades:

* Usuário base do sistema
* Perfis (Administrador, Professor, Aluno)
* Autenticação e autorização

Observação:

* Não contém regras acadêmicas
* Serve como base para controle de acesso

---

### 3.2 institutions

Representa a entidade institucional.

Responsabilidades:

* Cadastro de instituições
* Configurações acadêmicas globais
* Parâmetros como modelo de avaliação (bimestre, trimestre etc.)

---

### 3.3 academic

Núcleo do domínio educacional.

Responsabilidades:

* Classes (séries, níveis)
* Disciplinas
* Estrutura curricular

Observação:

* Define o "o que é ensinado"

---

### 3.4 classes

Responsável pela organização acadêmica anual ou semestral.

Responsabilidades:

* Turmas
* Associação entre classes, disciplinas e professores
* Estados da turma (ativa, encerrada)

---

### 3.5 enrollment

Gerencia o vínculo entre alunos e turmas.

Responsabilidades:

* Matrículas
* Estados da matrícula (ativa, trancada, cancelada, concluída)

Observação:

* Central para regras de elegibilidade

---

### 3.6 attendance

Registra a execução das aulas.

Responsabilidades:

* Registro de aulas
* Datas, conteúdos ministrados
* Frequência (opcional)

---

### 3.7 evaluation

Responsável pelo processo avaliativo.

Responsabilidades:

* Avaliações
* Critérios avaliativos
* Períodos (bimestre, trimestre, semestre)

---

### 3.8 grades

Gerencia resultados acadêmicos.

Responsabilidades:

* Lançamento de notas
* Consolidação de resultados
* Consulta de desempenho

Restrição:

* Depende de enrollment e evaluation

---

## 4. Apps de Suporte

### core

Responsável por funcionalidades compartilhadas.

Exemplos:

* Modelos base
* Campos reutilizáveis
* Exceções de domínio

---

### audit (opcional)

Responsável por rastreabilidade.

Responsabilidades:

* Registro de ações críticas
* Histórico de alterações

---

## 5. Benefícios Dessa Estrutura

* Facilita testes isolados por domínio
* Permite crescimento gradual do sistema
* Aproxima o projeto de arquiteturas reais de mercado
* Evita acoplamento excessivo

---

## 6. Uso no Portfólio

Esta estrutura demonstra:

* Capacidade de decompor sistemas complexos
* Compreensão de arquitetura backend
* Adoção de boas práticas com Django e DRF

---

## 7. Próximo Passo

Com os apps definidos, o projeto está pronto para:

* Planejar o passo a passo de implementação
* Definir a ordem correta de criação dos componentes

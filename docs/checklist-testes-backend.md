# Checklist de Testes Backend

API REST – Sistema de Gestão Educacional

Este documento define a estratégia e o checklist de testes do backend, com foco em confiabilidade, segurança e previsibilidade do comportamento da API.

O objetivo não é apenas garantir funcionamento, mas **assegurar regras de negócio, permissões e contratos da API**.

---

## 1. Princípios de Testes

* Testes automatizados como parte do desenvolvimento
* Prioridade para regras de negócio críticas
* Testes independentes e previsíveis
* Separação clara entre tipos de testes

---

## 2. Tipos de Testes Adotados

### 2.1 Testes de Modelo (Domínio)

Validam regras de negócio diretamente no nível de dados.

Checklist:

* Criação válida de entidades
* Restrições de unicidade
* Relacionamentos obrigatórios
* Estados inválidos
* Regras de consistência (ex: matrícula duplicada)

---

### 2.2 Testes de Serialização

Garantem integridade dos dados de entrada e saída.

Checklist:

* Campos obrigatórios
* Tipos de dados
* Validações semânticas
* Campos somente leitura
* Exclusão de dados sensíveis

---

### 2.3 Testes de Autenticação

Validam controle de acesso baseado em JWT.

Checklist:

* Acesso sem token
* Token inválido
* Token expirado
* Token válido
* Renovação de token

---

### 2.4 Testes de Permissões (RBAC)

Garantem que cada papel só acessa o que é permitido.

Checklist:

* Admin com acesso total
* Secretaria criando matrículas
* Professor registrando aulas
* Aluno acessando apenas seus dados
* Responsável acessando dados permitidos

---

### 2.5 Testes de Endpoints

Validam comportamento REST dos recursos.

Checklist:

* Métodos HTTP corretos
* Códigos HTTP esperados
* Estrutura padrão de resposta
* Paginação e filtros
* Ordenação

---

### 2.6 Testes de Fluxos Críticos

Validam processos completos ponta a ponta.

Fluxos prioritários:

* Matrícula de aluno
* Registro de aula
* Lançamento de notas
* Consulta de boletim

Checklist:

* Sequência correta
* Validações intermediárias
* Respostas finais

---

## 3. Testes de Erro e Exceções

Checklist:

* Validações inválidas
* Recurso inexistente
* Permissão negada
* Conflito de estado
* Erros inesperados

---

## 4. Testes de Segurança

Checklist:

* Tentativas de acesso indevido
* Escalonamento de privilégios
* Exposição de dados sensíveis
* Injeções e payloads maliciosos

---

## 5. Testes de Performance (Básico)

Checklist:

* Endpoints de listagem
* Paginação sob carga
* Consultas agregadas (boletins)

---

## 6. Organização dos Testes

* Testes separados por domínio
* Nomes claros e objetivos
* Dados de teste controlados
* Reprodutibilidade garantida

---

## 7. Benefícios da Estratégia

* Redução de bugs em produção
* Segurança reforçada
* Confiança para refatorar
* Documentação viva do sistema

---

## Consideração Final

O checklist de testes orienta a implementação e manutenção do backend, garantindo qualidade técnica e alinhamento com as regras de negócio.

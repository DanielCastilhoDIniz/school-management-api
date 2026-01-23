# Regras de Negócio e Validações Críticas

Sistema de Gestão Educacional

## 1. Objetivo

Este documento descreve as **regras de negócio essenciais** e as **validações críticas** do sistema de gestão educacional.

O objetivo é:

* garantir integridade dos dados
* evitar estados inválidos no domínio
* orientar a implementação no backend
* servir como referência arquitetural e funcional

As regras aqui definidas **independem de framework** e devem ser aplicadas **no backend**, preferencialmente no nível de domínio/serviço.

---

## 2. Princípios Gerais

* Toda regra crítica deve ser validada no backend
* Frontend **não é fonte de verdade**
* Estados inválidos devem ser impossíveis de persistir
* Falhas devem gerar erros claros e previsíveis
* Regras refletem o funcionamento real de instituições educacionais

---

## 3. Regras Relacionadas à Instituição

### 3.1 Escopo Institucional

* Todo dado acadêmico pertence a **uma única instituição**
* Usuários só podem acessar dados da própria instituição

**Validações:**

* impedir associação cruzada entre instituições
* validar escopo institucional em todas as operações sensíveis

---

## 4. Regras de Usuários e Papéis (RBAC)

### 4.1 Usuário Ativo

* Apenas usuários ativos podem autenticar
* Usuários inativos não podem consumir endpoints protegidos

---

### 4.2 Papéis Obrigatórios

* Todo usuário deve possuir **ao menos um papel**
* Papéis determinam permissões, nunca o contrário

---

### 4.3 Separação de Identidade e Domínio

* Usuário pode existir sem ser aluno ou professor
* Aluno e professor **não existem sem usuário associado**

---

## 5. Regras Acadêmicas – Alunos e Matrículas

### 5.1 Matrícula Única

* Um aluno não pode estar matriculado duas vezes na mesma turma

**Validação:**

* unicidade aluno + turma

---

### 5.2 Matrícula Ativa

* Apenas alunos com matrícula ativa:

  * aparecem em listas de chamada
  * recebem notas
  * participam de avaliações

---

### 5.3 Histórico de Matrículas

* Matrículas não devem ser apagadas
* Alterações ocorrem via status (ativa, trancada, cancelada)

---

## 6. Regras de Turmas e Disciplinas

### 6.1 Associação Obrigatória

* Turma deve estar vinculada:

  * a uma instituição
  * a um período letivo

---

### 6.2 Disciplinas em Turmas

* Uma turma deve possuir ao menos uma disciplina
* Disciplinas podem ser reutilizadas em múltiplas turmas

---

## 7. Regras de Aulas

### 7.1 Aula Vinculada

* Aula sempre pertence a uma turma
* Aula não existe fora de um contexto acadêmico

---

### 7.2 Registro Temporal

* Não é permitido registrar aula fora do período letivo da turma

---

## 8. Regras de Avaliações

### 8.1 Avaliação Contextual

* Avaliação pertence a:

  * uma turma
  * um período letivo

---

### 8.2 Avaliação Única por Contexto

* A instituição pode definir limites:

  * número máximo de avaliações por período
  * tipos de avaliação permitidos

---

### 8.3 Avaliação Imutável Após Publicação

* Após publicação:

  * tipo e peso não podem ser alterados
  * apenas notas podem ser ajustadas (com auditoria)

---

## 9. Regras de Notas

### 9.1 Matrícula Obrigatória

* Nota só pode ser lançada se:

  * aluno estiver matriculado
  * matrícula estiver ativa

---

### 9.2 Nota Única

* Um aluno só pode ter **uma nota por avaliação**

---

### 9.3 Intervalo de Valores

* Notas devem respeitar limites definidos pela instituição

  * exemplo: 0 a 10
  * exemplo: 0 a 100

---

## 10. Regras de Permissões por Ação

### 10.1 Professores

* Podem:

  * registrar aulas
  * criar avaliações
  * lançar notas
* Apenas em turmas sob sua responsabilidade

---

### 10.2 Alunos

* Apenas leitura:

  * próprias notas
  * próprias avaliações
* Nunca escrita

---

### 10.3 Gestores

* Controle acadêmico completo
* Sem acesso a dados sensíveis de autenticação

---

## 11. Validações Transversais

Aplicáveis a múltiplos domínios:

* datas coerentes (início < fim)
* referências existentes
* estados válidos
* escopo institucional respeitado
* permissões verificadas antes da ação

---

## 12. Tratamento de Erros

* Erros devem ser:

  * claros
  * padronizados
  * semanticamente corretos
* Exemplos conceituais:

  * violação de regra de negócio
  * permissão insuficiente
  * estado inválido do recurso

---

## 13. Benefícios da Definição de Regras

Este documento demonstra:

✅ domínio realista
✅ preocupação com integridade
✅ visão de backend robusto
✅ preparo para sistemas críticos
✅ maturidade arquitetural

---


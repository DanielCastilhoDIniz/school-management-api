# Domínio Acadêmico – Modelagem Conceitual

## 1. Contexto

Esta aplicação tem como objetivo prover uma **API REST para gerenciamento educacional**, atendendo instituições de ensino com diferentes estruturas pedagógicas e administrativas.

O domínio acadêmico envolve regras próprias, vocabulário específico e relações complexas entre entidades. Uma modelagem conceitual clara é essencial para:

* refletir corretamente a realidade institucional
* evitar ambiguidades semânticas
* permitir evolução do sistema
* reduzir refatorações futuras

Este documento descreve o **modelo conceitual do domínio**, independente de tecnologia ou implementação.

---

## 2. Princípios de Modelagem

As decisões deste domínio seguem os seguintes princípios:

* **Aderência ao mundo real**: entidades representam conceitos institucionais reais
* **Separação de responsabilidades**: cada entidade tem um papel claro
* **Baixo acoplamento**: evitar dependências desnecessárias
* **Flexibilidade institucional**: suportar variações entre escolas
* **Persistência histórica**: preservar registros acadêmicos

Esses princípios orientam todas as decisões descritas a seguir.

---

## 3. Instituição

A **Instituição** representa a entidade educacional responsável pelo funcionamento do sistema.

Responsabilidades conceituais:

* definir regras acadêmicas e administrativas
* determinar o tipo de período avaliativo
* agrupar alunos, professores e turmas
* servir como limite de escopo de dados

A existência explícita da instituição permite:

* suporte futuro a múltiplas instituições
* isolamento de dados
* customização de regras pedagógicas

---

## 4. Usuário vs. Entidades Acadêmicas

Uma decisão central deste domínio é a **separação entre identidade de acesso e papel acadêmico**.

* **Usuário**: identidade autenticável no sistema
* **Aluno / Professor / Gestor**: entidades do domínio acadêmico

Essa separação:

* evita acoplamento entre autenticação e regras pedagógicas
* permite usuários sem papel acadêmico direto
* facilita manutenção e segurança

---

## 5. Aluno

O **Aluno** representa o indivíduo no contexto acadêmico.

Características conceituais:

* vínculo com uma instituição
* histórico acadêmico próprio
* participação em turmas por meio de matrículas
* possível associação a responsáveis

O aluno não pertence diretamente a uma turma, mas se relaciona por meio de matrículas, permitindo histórico e mobilidade.

---

## 6. Professor

O **Professor** representa o docente no domínio acadêmico.

Responsabilidades:

* ministrar aulas
* registrar conteúdos lecionados
* aplicar avaliações
* lançar notas

O professor pode atuar em múltiplas turmas e disciplinas, respeitando o período letivo.

---

## 7. Turma

A **Turma** representa uma unidade organizacional de ensino.

Características:

* vinculada a uma instituição
* associada a um período letivo
* composta por alunos matriculados
* associada a uma ou mais disciplinas
* possui professores responsáveis

A turma é o principal ponto de convergência do domínio acadêmico.

---

## 8. Matrícula

A **Matrícula** representa o vínculo formal entre aluno e turma.

Responsabilidades:

* registrar ingresso do aluno
* controlar status (ativa, transferida, cancelada, concluída)
* manter histórico acadêmico

Decisão importante:

> O aluno nunca pertence diretamente à turma — o vínculo é sempre mediado pela matrícula.

Isso permite:

* reenturmações
* transferências
* histórico consistente

---

## 9. Disciplina

A **Disciplina** representa o conteúdo curricular.

Características:

* nome e identificação
* carga horária
* associação a turmas
* ministrada por professores

Separar disciplina de turma:

* evita duplicação de dados
* facilita reutilização curricular
* melhora clareza do domínio

---

## 10. Aula / Registro de Aula

A **Aula** (ou Registro de Aula) representa uma aula efetivamente ministrada.

Responsabilidades:

* data da aula
* conteúdo abordado
* turma
* disciplina
* professor responsável

Esses registros são essenciais para:

* controle pedagógico
* auditoria
* relatórios acadêmicos

---

## 11. Período Avaliativo

O **Período Avaliativo** representa a divisão do calendário acadêmico para avaliação.

Exemplos:

* bimestre
* trimestre
* quadrimestre
* semestre

Decisão arquitetural:

> O tipo de período avaliativo é **configurável por instituição**, não fixo no sistema.

Isso garante flexibilidade institucional.

---

## 12. Avaliação

A **Avaliação** representa instrumentos de verificação de desempenho.

Características:

* associada a uma disciplina
* vinculada a um período avaliativo
* aplicada em uma turma
* pode possuir peso ou critério específico

Exemplos:

* provas
* trabalhos
* atividades contínuas

---

## 13. Nota

A **Nota** representa o resultado de uma avaliação para um aluno.

Responsabilidades:

* vínculo com aluno
* vínculo com avaliação
* valor obtido
* observações adicionais

Separar avaliação de nota:

* permite múltiplas avaliações por período
* facilita regras de cálculo
* mantém clareza conceitual

---

## 14. Relacionamentos Principais

Visão lógica simplificada do domínio:

* Instituição → possui → Alunos, Professores, Turmas
* Turma → possui → Matrículas
* Matrícula → vincula → Aluno ↔ Turma
* Turma → associa → Disciplinas
* Professor → ministra → Disciplinas / Turmas
* Aula → registra → Turma + Disciplina + Professor
* Avaliação → pertence → Disciplina + Período
* Nota → pertence → Aluno + Avaliação

Essa visão serve como base para o diagrama de dados.

---

## 15. Consequências da Modelagem

### Benefícios

* domínio claro e expressivo
* aderência à realidade educacional
* facilidade de evolução
* suporte a histórico e auditoria
* redução de refatorações futuras

### Trade-offs

* maior esforço inicial de modelagem
* necessidade de documentação contínua
* cuidado na implementação das relações

Esses custos são aceitáveis diante da robustez obtida.

---

## 16. Considerações Finais

A modelagem do domínio acadêmico apresentada neste documento estabelece uma **base sólida, extensível e alinhada com práticas profissionais**, permitindo que a API evolua com segurança, clareza e consistência.

Este documento orienta diretamente:

* modelagem de dados
* definição de endpoints
* regras de negócio
* controle de acesso contextual

---
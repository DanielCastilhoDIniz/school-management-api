# Visão de Domínio – Sistema de Gestão Educacional

## 1. Visão Geral do Domínio

Este sistema tem como objetivo gerenciar instituições educacionais, contemplando o controle acadêmico e administrativo de alunos, professores, turmas, classes, matrículas, registros de aulas, avaliações e notas.

O domínio foi modelado para atender diferentes modelos institucionais de avaliação (bimestre, trimestre, quadrimestre ou semestre), garantindo flexibilidade acadêmica, integridade dos dados e rastreabilidade histórica.

O sistema é projetado para operar como backend desacoplado, fornecendo uma API REST para consumo por aplicações web ou mobile.

---

## 2. Entidades do Domínio

### Instituição

Representa a organização educacional (escola, faculdade ou centro educacional).

Responsabilidades:

* Definir regras acadêmicas globais
* Configurar o modelo de período avaliativo
* Manter cadastros institucionais ativos

---

### Aluno

Representa o discente vinculado à instituição.

Responsabilidades:

* Manter dados pessoais e acadêmicos
* Possuir histórico de matrículas
* Receber avaliações e notas

---

### Professor

Representa o docente da instituição.

Responsabilidades:

* Ministrar aulas
* Registrar conteúdos ministrados
* Lançar avaliações e notas

---

### Classe (Série / Ano / Semestre)

Representa o nível educacional ou etapa acadêmica.

Responsabilidades:

* Definir o conjunto de disciplinas
* Organizar a progressão acadêmica

---

### Turma

Representa uma instância de uma classe em um período letivo específico.

Responsabilidades:

* Agrupar alunos matriculados
* Centralizar registros acadêmicos
* Controlar o período letivo

Estados possíveis:

* Planejada
* Ativa
* Encerrada

---

### Matrícula

Representa o vínculo formal entre um aluno e uma turma.

Responsabilidades:

* Controlar ingresso, permanência e desligamento
* Garantir unicidade aluno–turma
* Manter histórico acadêmico

Estados possíveis:

* Ativa
* Trancada
* Cancelada
* Concluída

---

### Disciplina

Representa uma matéria curricular associada a uma classe e ministrada em turmas.

Responsabilidades:

* Organizar conteúdo programático
* Receber avaliações
* Possuir registros de aulas

---

### Registro de Aula

Representa uma aula ministrada por um professor.

Responsabilidades:

* Registrar data e conteúdo
* Associar professor, turma e disciplina
* Compor carga horária

---

### Avaliação

Representa um instrumento avaliativo aplicado aos alunos.

Responsabilidades:

* Definir tipo e peso
* Pertencer a um período avaliativo
* Compor médias finais

Estados possíveis:

* Criada
* Aplicada
* Encerrada

---

### Nota

Representa o desempenho do aluno em uma avaliação.

Responsabilidades:

* Registrar resultado individual
* Respeitar escala definida pela instituição

---

## 3. Relacionamentos Principais

* Uma Instituição possui vários Alunos, Professores e Classes
* Uma Classe possui várias Turmas
* Uma Turma possui várias Matrículas
* Uma Matrícula vincula um Aluno a uma Turma
* Uma Turma possui várias Disciplinas
* Uma Disciplina possui Avaliações e Registros de Aula
* Uma Avaliação gera várias Notas

---

## 4. Regras de Negócio

1. Um aluno não pode possuir mais de uma matrícula ativa na mesma turma
2. Apenas alunos com matrícula ativa podem receber notas
3. Professores só podem registrar aulas em turmas às quais estejam vinculados
4. Avaliações só podem ser criadas dentro de períodos letivos ativos
5. Avaliações encerradas não podem ser alteradas
6. O modelo de período avaliativo é definido pela instituição e aplicado às turmas

---

## 5. Períodos Avaliativos

O sistema suporta os seguintes modelos, configuráveis por instituição:

* Bimestre
* Trimestre
* Quadrimestre
* Semestre

Todos os cálculos de média e consolidação de notas respeitam o modelo definido.

---

## 6. Considerações Arquiteturais

* O domínio é independente de frameworks e infraestrutura
* Regras de negócio não devem residir na camada de interface
* O modelo permite extensão para módulos como frequência, recuperação e histórico escolar
* A separação clara de responsabilidades reduz acoplamento e facilita manutenção

---

## 7. Objetivo para Portfólio

Este projeto tem como finalidade demonstrar capacidade de:

* Modelagem de domínio orientada ao negócio
* Organização conceitual de sistemas complexos
* Pensamento arquitetural aplicado a backend
* Preparação de APIs REST profissionais

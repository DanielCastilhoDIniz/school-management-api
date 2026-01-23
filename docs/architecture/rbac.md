# Controle de Acesso Baseado em Papéis (RBAC)

## 1. Contexto

Esta aplicação consiste em uma **API REST para gerenciamento educacional**, com múltiplos tipos de usuários e diferentes níveis de acesso aos recursos do sistema.

O domínio educacional impõe requisitos específicos de controle de acesso, como:

* separação clara de responsabilidades
* proteção de dados acadêmicos sensíveis
* restrição de ações conforme função institucional
* possibilidade de crescimento e customização por instituição

Diante disso, tornou-se necessário um modelo de autorização estruturado, previsível e extensível.

---

## 2. Decisão Arquitetural

Optou-se pela adoção de um modelo de **RBAC (Role-Based Access Control)** para controle de autorização da API.

Nesse modelo:

* usuários são associados a **papéis**
* papéis agregam **permissões**
* permissões controlam ações sobre recursos

A autenticação (identidade) é tratada separadamente da autorização (acesso), garantindo menor acoplamento e maior flexibilidade.

---

## 3. Princípios Adotados

As decisões de RBAC seguem os seguintes princípios:

* **Negação por padrão**: nenhum acesso é concedido implicitamente
* **Permissões explícitas**: toda ação permitida é declarada
* **Separação de responsabilidades**: autenticação ≠ autorização
* **Menor privilégio**: cada papel possui apenas o necessário
* **Evolução controlada**: novos papéis não exigem reestruturação

Esses princípios reduzem riscos de segurança e facilitam manutenção.

---

## 4. Entidade Usuário

O **usuário** representa uma identidade autenticável no sistema.

Características conceituais:

* credenciais de autenticação
* estado da conta (ativo, inativo, suspenso)
* associação com um ou mais papéis
* possível vínculo com entidades do domínio (aluno, professor, gestor)

O usuário **não é sinônimo de papel**, nem representa diretamente uma entidade acadêmica.

Essa separação evita acoplamento entre identidade e domínio.

---

## 5. Papéis do Sistema

Papéis representam **funções institucionais**, não indivíduos.

Papéis iniciais definidos:

### Administrador do Sistema

* gerenciamento global da aplicação
* configuração institucional
* gestão de usuários, papéis e permissões

### Gestor Escolar

* gestão acadêmica e administrativa
* criação e organização de turmas
* acompanhamento de desempenho escolar

### Professor

* registro de aulas
* lançamento de notas
* criação e aplicação de avaliações
* acesso às turmas sob sua responsabilidade

### Aluno

* visualização de notas e avaliações
* acesso a registros acadêmicos próprios
* consulta de informações permitidas

### Responsável (opcional)

* acesso restrito às informações do aluno vinculado
* acompanhamento de desempenho acadêmico

Os papéis são **extensíveis**, permitindo criação de novos perfis conforme necessidades institucionais.

---

## 6. Permissões

Permissões representam **ações específicas** que podem ser executadas sobre recursos do sistema.

Exemplos conceituais:

* criar turma
* matricular aluno
* registrar aula
* lançar nota
* visualizar histórico acadêmico
* administrar usuários

Características das permissões:

* são atômicas
* não pertencem diretamente ao usuário
* são atribuídas aos papéis
* podem ser reutilizadas entre papéis

Isso garante granularidade e evita duplicação de regras.

---

## 7. Associação entre Usuários e Papéis

Um usuário pode:

* possuir múltiplos papéis
* atuar em diferentes contextos
* ter permissões resultantes da união de seus papéis

Exemplos:

* um professor também pode ser gestor
* um gestor pode ter acesso restrito à sua instituição
* um administrador não atua necessariamente no domínio acadêmico

Esse modelo permite flexibilidade sem perda de controle.

---

## 8. Contexto e Regras Adicionais

Embora o RBAC seja o modelo principal, algumas permissões podem depender de **contexto**, como:

* turma
* disciplina
* instituição
* período letivo

O RBAC pode ser complementado por:

* validações contextuais
* regras de escopo
* restrições por vínculo

Essas regras não substituem o RBAC, mas o refinam.

---

## 9. Segurança e Boas Práticas

Decisões reforçadas neste modelo:

* validação de permissões sempre no backend
* nenhuma confiança em regras apenas no frontend
* auditoria facilitada por papéis claros
* prevenção de escalonamento indevido de privilégios

O controle de acesso é tratado como **parte crítica da API**, não como detalhe.

---

## 10. Consequências da Decisão

### Benefícios

* clareza organizacional
* segurança reforçada
* facilidade de manutenção
* escalabilidade institucional
* alinhamento com sistemas reais

### Trade-offs

* maior esforço inicial de modelagem
* necessidade de documentação contínua
* atenção na definição das permissões

Esses custos são considerados aceitáveis diante da robustez obtida.

---

## 11. Considerações Finais

O modelo RBAC adotado fornece uma base sólida para o controle de acesso da aplicação, permitindo crescimento, personalização e segurança sem comprometer a clareza arquitetural.

Essa decisão posiciona o projeto de acordo com **boas práticas profissionais de engenharia de software**, especialmente em sistemas educacionais e institucionais.

---

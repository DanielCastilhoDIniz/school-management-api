
# Educational Management API

## Visão Geral

Este projeto consiste no desenvolvimento de uma **API REST para Gestão Educacional**, voltada ao controle acadêmico de instituições de ensino, contemplando processos como matrículas, organização de turmas, registro de aulas, avaliações e lançamento de notas.

O foco principal do projeto é **backend**, com ênfase em **arquitetura, modelagem de domínio, regras de negócio e segurança**, seguindo práticas utilizadas em sistemas reais de médio e grande porte.

---

## Problema Resolvido

Instituições educacionais lidam com múltiplas entidades interdependentes, como alunos, professores, turmas, disciplinas, matrículas e avaliações, cada uma com regras próprias e estados bem definidos.

Este projeto busca resolver esse problema por meio de:

* uma modelagem clara do domínio educacional;
* uma API REST orientada a casos de uso;
* controle de acesso baseado em papéis e regras de negócio;
* separação adequada de responsabilidades no backend.

---

## Abordagem Arquitetural

Antes de qualquer implementação, o projeto foi planejado seguindo uma abordagem **orientada a domínio**, incluindo:

* Definição formal do domínio educacional
* Modelagem lógica de dados
* Design do contrato da API REST
* Definição de perfis de acesso e permissões (RBAC)
* Planejamento da estrutura de aplicações (apps)

Essa abordagem garante:

* previsibilidade na implementação;
* facilidade de manutenção;
* escalabilidade futura;
* redução de acoplamento entre componentes.

---

## Persistência de Dados

O projeto utiliza **PostgreSQL** como sistema gerenciador de banco de dados relacional, por ser amplamente adotado em aplicações backend profissionais, oferecendo robustez, consistência e suporte avançado a dados relacionais.

A conexão entre a aplicação Django e o PostgreSQL é realizada por meio de um **driver dedicado**, conforme as práticas recomendadas no ecossistema Python.
Em ambiente de desenvolvimento, é utilizado o pacote `psycopg2-binary`, priorizando simplicidade de instalação e produtividade.

As configurações de banco de dados são carregadas exclusivamente a partir de **variáveis de ambiente**, garantindo:

* separação entre código e configuração;
* segurança de informações sensíveis;
* facilidade de adaptação entre ambientes (desenvolvimento, testes e produção).

---

## Gerenciamento de Configurações Sensíveis

Seguindo boas práticas de segurança, informações sensíveis como:

* credenciais de banco de dados;
* chaves secretas;
* configurações de ambiente;

**não são versionadas no repositório**.

O projeto adota o uso de variáveis de ambiente, com um arquivo `.env.example` disponibilizado apenas como referência estrutural, permitindo que cada ambiente defina suas próprias configurações sem expor dados críticos.

Essa abordagem reduz riscos de vazamento de informações e facilita a implantação em diferentes contextos.

---

## Autenticação e Segurança

Esta API adota **autenticação baseada em JWT (JSON Web Token)**, seguindo uma abordagem **stateless**, adequada para arquiteturas REST desacopladas e múltiplos clientes (web, mobile e integrações externas).

A estratégia de autenticação foi definida com foco em **segurança, escalabilidade e boas práticas de mercado**, utilizando dois tipos de tokens:

* **Access Token**
  Utilizado para autenticar as requisições à API, com tempo de vida curto, reduzindo o impacto de eventuais vazamentos.

* **Refresh Token**
  Utilizado exclusivamente para renovação do access token, com tempo de vida maior, evitando a necessidade de autenticação frequente do usuário.

A renovação dos tokens ocorre de forma controlada, garantindo sessões seguras sem comprometer a experiência do usuário.
Quando aplicável, o processo de logout pode implicar a invalidação do refresh token, reforçando o controle de acesso.

Essa abordagem permite uma API mais segura, escalável e alinhada aos padrões modernos de desenvolvimento backend.

---

## Escopo Funcional

A API contempla, entre outros, os seguintes contextos:

* Gestão de instituições
* Cadastro de alunos e professores
* Organização acadêmica (classes, disciplinas e turmas)
* Matrículas e controle de estados
* Registro de aulas
* Avaliações periódicas (bimestre, trimestre, semestre, conforme a instituição)
* Lançamento e consulta de notas
* Controle de acesso por perfil (administrador, professor, aluno)

---

## Documentação do Projeto

Toda a fase de análise e planejamento está documentada no diretório `docs/`, incluindo:

* Definição do domínio educacional
* Modelagem conceitual e lógica de dados (ERD)
* Mapeamento do domínio para modelos Django
* Design dos endpoints REST
* Estratégia de autenticação
* Controle de acesso baseado em papéis (RBAC)
* Estrutura dos apps do backend

Esses documentos servem como base para a implementação e evidenciam o processo de engenharia adotado.

---

## Stack Tecnológica

O projeto utiliza uma stack consolidada para desenvolvimento de APIs REST backend:

- **Linguagem:** Python 3.12
- **Framework Web:** Django
- **API REST:** Django REST Framework (DRF)
- **Banco de Dados:** PostgreSQL
- **Autenticação:** JWT (JSON Web Token)
- **Gerenciamento de Configurações:** Variáveis de ambiente (.env)
- **Documentação da API:** OpenAPI / Swagger
- **Controle de Acesso:** RBAC (Role-Based Access Control)

A escolha das tecnologias prioriza estabilidade, maturidade do ecossistema e alinhamento com práticas adotadas em aplicações backend profissionais.


## Status do Projeto

🚧 **Em desenvolvimento**

O projeto encontra-se em fase de implementação incremental, seguindo um roteiro técnico previamente definido, com foco em qualidade, clareza arquitetural e boas práticas de backend.

---

## Objetivo Profissional

Este projeto tem como objetivo demonstrar:

* capacidade de análise e modelagem de sistemas complexos;
* domínio de conceitos fundamentais de backend;
* organização e disciplina no desenvolvimento de software;
* preparo para atuar em projetos reais de APIs REST.


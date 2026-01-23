
# Autenticação e Autorização

## 1. Contexto

Esta aplicação consiste em uma **API REST para gerenciamento educacional**, destinada a ser consumida por diferentes tipos de clientes, como aplicações web, aplicativos móveis e possíveis integrações externas.

O sistema deve atender a requisitos como:

* múltiplos perfis de usuários (alunos, professores, gestores, administração)
* acesso seguro a recursos sensíveis
* escalabilidade horizontal
* desacoplamento entre backend e frontend

Diante desse cenário, não é desejável manter estado de sessão no servidor, nem depender de mecanismos acoplados ao ciclo de vida de uma única aplicação cliente.

---

## 2. Decisão Arquitetural

Optou-se pela adoção de **autenticação baseada em JWT (JSON Web Token)**, seguindo um modelo **stateless**, alinhado às boas práticas modernas para APIs REST.

A estratégia utiliza dois tipos de tokens:

* **Access Token**
* **Refresh Token**

Essa separação permite equilibrar **segurança**, **usabilidade** e **controle de acesso**, sem comprometer a experiência do usuário ou a escalabilidade do sistema.

---

## 3. Access Token

O **access token** é utilizado para autenticar requisições aos endpoints protegidos da API.

Características conceituais:

* tempo de vida curto
* enviado a cada requisição autenticada
* não contém informações sensíveis
* utilizado apenas para autorização de acesso

A curta duração do access token reduz o impacto de possíveis vazamentos, limitando a janela de uso indevido.

---

## 4. Refresh Token

O **refresh token** tem como objetivo permitir a renovação do access token sem exigir que o usuário realize uma nova autenticação completa.

Características conceituais:

* tempo de vida maior que o access token
* utilizado exclusivamente para emissão de novos access tokens
* não deve ser usado para acesso direto a recursos protegidos

Essa abordagem melhora a experiência do usuário ao evitar logins frequentes, mantendo um nível elevado de segurança.

---

## 5. Renovação de Tokens

A renovação dos tokens ocorre de forma **controlada e explícita**, mediante solicitação do cliente.

Princípios adotados:

* o refresh token é validado antes da emissão de um novo access token
* access tokens expirados não são renovados automaticamente sem validação
* não há renovação silenciosa infinita

Esse modelo evita sessões indefinidas e reforça o controle sobre o ciclo de vida das credenciais.

---

## 6. Logout e Invalidação

Quando aplicável, o processo de logout pode implicar a **invalidação do refresh token**, impedindo sua reutilização para obtenção de novos access tokens.

Esse mecanismo:

* reduz riscos em caso de comprometimento do token
* permite maior controle sobre sessões ativas
* prepara o sistema para requisitos de segurança mais rigorosos

A invalidação explícita é especialmente relevante em ambientes institucionais e educacionais.

---

## 7. Autorização e Permissões

A autenticação via JWT é **independente da lógica de autorização**.

As permissões de acesso aos recursos são tratadas separadamente, com base em:

* papéis do usuário
* contexto da requisição
* regras de negócio específicas

Essa separação garante:

* maior flexibilidade
* menor acoplamento
* evolução segura das regras de acesso

---

## 8. Consequências da Decisão

### Benefícios

* arquitetura stateless
* facilidade de escalar horizontalmente
* compatibilidade com múltiplos clientes
* alinhamento com padrões amplamente adotados no mercado

### Custos e Trade-offs

* aumento moderado da complexidade
* necessidade de controle explícito do ciclo de vida dos tokens
* maior responsabilidade na definição de políticas de segurança

Esses trade-offs são considerados aceitáveis diante dos benefícios para um sistema de médio a grande porte.

---

## 9. Considerações Finais

A estratégia de autenticação adotada foi definida visando **robustez, clareza arquitetural e alinhamento com práticas profissionais**, permitindo que a API evolua de forma segura e sustentável conforme o crescimento do sistema.

---

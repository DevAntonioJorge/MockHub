# 📘 Documentação Técnica - ServiceHub

## 🧩 Visão Geral

O **ServiceHub** é uma plataforma backend que funciona como um **marketplace de mocks** — uma ferramenta onde desenvolvedores podem criar, registrar, simular e testar microserviços fake com comportamento personalizável. Ideal para desenvolvimento frontend, automação de testes e validações de fluxos sem depender de APIs reais.

## 🚀 Objetivos do Projeto

* Ajudar devs a simular APIs personalizadas com facilidade.
* Permitir colaboração entre devs em um ambiente de mocks controlado.
* Fornecer métricas e logs das chamadas simuladas.
* Implementar RBAC (controle de acesso baseado em papéis).

## 👥 Personas

### 👤 João, Dev Backend Júnior

* Quer testar seus sistemas com APIs simuladas.
* Cria endpoints com resposta customizada para testar integrações.

### 👩‍💻 Carla, QA

* Precisa validar fluxos de erro e comportamento do frontend.
* Usa mocks para simular cenários como 401, 500, etc.

### 👨‍🏫 Marcos, Dev Sênior/Admin

* Coordena a equipe, quer ter controle sobre todos os serviços.
* Administra usuários, visualiza logs e propõe padrões.

## 📌 Funcionalidades

* Cadastro e login com autenticação JWT.
* Criação de microserviços fake:

  * Definir método, rota, payload esperado e resposta mockada.
  * Latência simulada.
* Registro de logs de requisições.
* RBAC: permissões para admin e usuário.
* Listagem e edição apenas dos próprios serviços (ou todos, se admin).
* Painel de logs por microserviço.
* Validação opcional do payload com JSON Schema.

## 🧱 Requisitos

### ✅ Requisitos Funcionais (RF)

* RF01: Cadastro e autenticação de usuários.
* RF02: Criação, leitura, atualização e exclusão de microserviços fake.
* RF03: Simulação de requisições com resposta customizada.
* RF04: Armazenamento e visualização de logs por serviço.
* RF05: RBAC com distinção entre usuários e administradores.

### 🛠️ Requisitos Não Funcionais (RNF)

* RNF01: API RESTful.
* RNF02: Autenticação com JWT.
* RNF03: Senhas armazenadas com bcrypt.
* RNF04: Containerização com Docker.
* RNF05: Documentação da API (Swagger).

## 🏗️ Arquitetura do Sistema

* Backend: Go ou FastAPI
* Banco de dados: PostgreSQL
* Cache: Redis (opcional)
* Mensageria: RabbitMQ/Kafka (opcional para logs)
* Autenticação: JWT + RBAC

```
Frontend/Cliente REST
      ↓
API Gateway (FastAPI / Go)
      ↓
Service Controller → [PostgreSQL / Redis]
      ↓
Request Logger (assíncrono)
```

## 🗃️ Modelagem de Dados

### Usuário

```json
{
  "id": "uuid",
  "name": "string",
  "email": "string",
  "password_hash": "string",
  "role": "admin | user"
}
```

### Microserviço (MockService)

```json
{
  "id": "uuid",
  "owner_id": "uuid",
  "name": "string",
  "route": "/fake-endpoint",
  "method": "GET | POST | PUT | DELETE",
  "request_schema": "json",
  "response_payload": "json",
  "response_code": "int",
  "latency_ms": "int"
}
```

### Log de Requisição

```json
{
  "id": "uuid",
  "service_id": "uuid",
  "timestamp": "datetime",
  "request_payload": "json",
  "response_payload": "json",
  "status_code": "int",
  "latency_ms": "int"
}
```

## 🔐 Autenticação e Segurança

* Autenticação via JWT.
* Middleware de verificação de token em todas as rotas protegidas.
* Hash de senha com bcrypt.
* Controle de permissões baseado em papel (admin/user).

## 🔁 Endpoints da API (Exemplo)

### Auth

* `POST /auth/register`
* `POST /auth/login`

### Serviços

* `GET /services`
* `POST /services`
* `GET /services/{id}`
* `PUT /services/{id}`
* `DELETE /services/{id}`

### Simulação

* `POST /simulate/{service_id}`

### Logs

* `GET /services/{id}/logs`

## 📊 Logs e Observabilidade

* Toda requisição simulada gera log:

  * Payload recebido
  * Payload retornado
  * Status HTTP
  * Tempo de resposta

* Futuros upgrades:

  * Exportação CSV
  * Integração com Prometheus e Grafana

## 🧪 Casos de Uso

| Código | Nome               | Descrição                                 |
| ------ | ------------------ | ----------------------------------------- |
| CU01   | Registrar usuário  | Cadastro de novos usuários                |
| CU02   | Login              | Geração de token JWT                      |
| CU03   | Criar mock         | Cadastro de novo serviço fake             |
| CU04   | Editar mock        | Alterar rota, método, schema ou resposta  |
| CU05   | Deletar mock       | Remoção de serviço                        |
| CU06   | Listar serviços    | Retorna todos os serviços do usuário      |
| CU07   | Simular requisição | Responde conforme configuração do serviço |
| CU08   | Registrar log      | Armazena log da simulação                 |
| CU09   | Consultar logs     | Listar logs filtrados por serviço         |

## 🔍 Concorrência

### 🧪 Mockoon

* Roda localmente (app desktop)
* Foco em dev solo
* Sem colaboração ou logs persistentes

### 🧪 Beeceptor

* Simulação de APIs online
* Suporte a headers, latência e respostas
* Sem controle de acesso por usuário nem RBAC

### 🧪 Postman Mock Server

* Mock de APIs integrados a coleções
* Excelente para times grandes
* Depende de conta Postman (e plano gratuito limitado)

### ✅ Diferenciais do ServiceHub

* Multiusuário com RBAC
* Registro de logs por requisição
* API 100% self-hosted
* Personalização completa do comportamento
* Potencial de uso privado por squads, agências e devs freelancers

## 🧰 Tecnologias Utilizadas

| Tecnologia   | Função                    |
| ------------ | ------------------------- |
| Go / FastAPI | Backend                   |
| PostgreSQL   | Banco de dados            |
| Redis        | Cache (opcional)          |
| RabbitMQ     | Log assíncrono (opcional) |
| JWT          | Autenticação              |
| bcrypt       | Segurança das senhas      |
| Docker       | Empacotamento             |

## 🛠️ Como Rodar o Projeto

```bash
git clone https://github.com/seu-user/servicehub
cd servicehub
docker-compose up --build
```

Acesse em `http://localhost:8000`.

## 🧱 Melhorias Futuras

* Interface Web Admin (Next.js/Nuxt)
* Compartilhamento público de serviços
* Versionamento de mocks
* Rate Limiting
* GraphQL API
* Exportação de logs CSV
* Testes automatizados

---

📌 **Status:** Rascunho inicial completo.
Quer continuar a partir dessa base com Swagger, testes ou front?

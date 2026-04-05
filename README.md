# Auth API – FastAPI

# Auth API – FastAPI

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Bibliotecas de Segurança](#bibliotecas-de-segurança)
- [Funcionalidades](#funcionalidades)
- [Base de Dados](#base-de-dados)
- [Instalação](#instalação)

API de autenticação desenvolvida com **FastAPI** para gerenciamento de usuários e administradores.  
A aplicação utiliza **JWT (JSON Web Token)** para autenticação e **HTTP Bearer Token** para proteger rotas administrativas.

Para fins de demonstração, os dados são armazenados em uma **base de dados fake (lista em memória)**.

---

# Tecnologias Utilizadas

- Python 3.12+
- FastAPI
- Uvicorn
- python-jose (JWT)
- Pydantic
- HTTPBearer Security
- Docker

---

# Bibliotecas de Segurança

A autenticação utiliza:

- **JWT** para geração de tokens
- **HTTPBearer** para proteção de rotas
- **HTTPAuthorizationCredentials** para leitura do token enviado no header
- **JWTError** para tratamento de erros de autenticação

---

# Funcionalidades

## Autenticação de Usuários

- Registro de usuários
- Login com geração de token JWT
- Autenticação baseada em token

## Administração

Rotas acessíveis apenas por administradores autenticados:

- Listar usuários
- Listar administradores
- Buscar administrador por email
- Atualizar usuário
- Deletar usuário por ID
- Deletar usuário por email

---

# Base de Dados 

A aplicação utiliza uma lista em memória simulando um banco de dados:
```python

admin_mock_1 = Admin(id=1, email="admin@example.com", password="hashed_password", type="admin", name="Admin User", last_name="Test")
admin_mock_2 = Admin(id=2, email="admin2@example.com", password="hashed_password", type="admin", name="Admin", last_name="User2")
admin_mock_3 = Admin(id=3, email="admin3@example.com", password="hashed_password", type="admin", name="Admin", last_name="User3")
.
.
.
user_mock_5 = User(id=11, email="user5@example.com", password="hashed_password", type="user", name="Pedro", last_name="Oliveira")

fake_db: List[User] = [admin_mock_1, admin_mock_2, admin_mock_3, admin_mock_4, admin_mock_5, admin_mock_6, user_mock_1, user_mock_2, user_mock_3, user_mock_4, user_mock_5]
```
# Instalação
## Clone o repositório
```bash
$ git clone https://github.com/caioarodrigues/auth-api.git
```

## Crie um arquivo .env neste mesmo diretório:
```env
JWT_SECRET=supersecret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## Faça o build com Docker
```bash
$ make build 
```

## Execute dentro de um container do Docker
```bash
$ make run 
```

## Documentação com as rotas da API

http://127.0.0.1:8000/docs
 
http://127.0.0.1:8000/redoc
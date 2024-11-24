# **SportSync | PI do 4º semestre de 2024 | DSM - Fatec Araras**

**SportSync** é uma plataforma desenvolvida em Django para facilitar a gestão de eventos esportivos, focada em organizadores e atletas amadores.

## Participantes

<p align="center">
  <a href="https://github.com/igornsferreira">
    <img src="https://avatars.githubusercontent.com/igornsferreira" width="15%" alt="Igor Ferreira">
  </a>
  <a href="https://github.com/isabalmeida">
    <img src="https://avatars.githubusercontent.com/isabalmeida" width="15%" alt="Isabela Almeida">
  </a>
  <a href="https://github.com/marcelosalvador">
    <img src="https://avatars.githubusercontent.com/marcelosalvador" width="15%" alt="Marcelo Salvador">
  </a>
</p>

## Configuração do Ambiente e Execução do Projeto

Este projeto utiliza **Python**, **Django**, e **SQLite** para o banco de dados. Siga as etapas abaixo para configurar seu ambiente de desenvolvimento e rodar a aplicação localmente.

### Pré-requisitos

Antes de começar, verifique se você tem as seguintes ferramentas instaladas:

- **Python** (versão 3.8 ou superior)
- **Django** (instalado via pip)
- **SQLite** (geralmente incluído com a instalação do Python)

### Configuração do Ambiente e Execução (Windows)

1. **Clone o repositório do projeto**:
    
    ```bash
    git clone https://github.com/igornsferreira/fatec-dsm-pi-4sem.git
    ```

2. **Acesse o diretório do projeto**:
    
    ```bash
    cd fatec-dsm-pi-4sem
    ```

3. **Crie e ative o ambiente virtual**:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate.bat  # Windows
    ```

4. **Instale as dependências do projeto**:
    
    ```bash
    pip install -r requirements.txt
    ```

5. **Crie um arquivo `.env` com as variáveis necessárias**:

    No diretório raiz do projeto, crie um arquivo `.env` com o seguinte conteúdo:

    ```env
    SECRET_KEY='sua_chave_secreta_aqui'
    DEBUG=True
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='sua_google_oauth2_key'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='seu_google_oauth2_secret'
    GOOGLE_CLIENT_ID='seu_google_client_id'
    GOOGLE_CLIENT_SECRET='seu_google_client_secret'
    ```

6. **Aplique as migrações do Django**:

    ```bash
    python manage.py migrate
    ```

7. **Crie um superusuário**:

    Para acessar o painel administrativo do Django, crie um superusuário com o comando:

    ```bash
    python manage.py createsuperuser
    ```

8. **Configure o provedor Google no Django Admin**:
   
   Após rodar o servidor pela primeira vez, acesse o Django Admin (geralmente em `http://127.0.0.1:8000/admin/`), e registre o provedor Google da seguinte forma:
   
   - **Vá até `Social Applications`** no painel administrativo.
   - **Crie um novo aplicativo social**, escolhendo o **Google** como provedor.
   - Preencha os campos conforme abaixo, utilizando as chaves do `.env`:
   
     | Campo            | Valor (exemplo)                                        |
     |------------------|--------------------------------------------------------|
     | provider         | google                                                 |
     | name             | Google OAuth                                           |
     | client_id        | (SOCIAL_AUTH_GOOGLE_OAUTH2_KEY)                        |
     | secret           | (SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET)                     |
     | key              | (SOCIAL_AUTH_GOOGLE_OAUTH2_KEY)                        |
     | provider_id      | (Valor padrão)                                         |
     | settings         | (Deixe vazio)                                          |
   

9. **Inicie o servidor Django**:

    ```bash
    python manage.py runserver
    ```

Agora você deve ser capaz de acessar a aplicação no seu navegador através de `http://127.0.0.1:8000/`.
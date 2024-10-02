# SportSync | PI do 4º semestre de 2024 | DSM - Fatec Araras

**SportSync** é uma plataforma desenvolvida em Django com o objetivo de facilitar a gestão de eventos esportivos para organizadores e atletas amadores. 

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

Este projeto está sendo desenvolvido utilizando **Python**, **Django** e **SQLite** como banco de dados. Siga as instruções abaixo para configurar seu ambiente de desenvolvimento e executar o projeto.

### Pré-requisitos

Antes de começar, verifique se você possui os seguintes pré-requisitos instalados:

- **Python** (versão 3.8 ou superior)
- **Django** (instalado via `pip`)
- **SQLite** (geralmente incluído com a instalação do Python)

### Configuração do Ambiente e Execução (Windows)

Siga os passos abaixo para configurar o ambiente e iniciar a aplicação:

1. **Clone o repositório do projeto**:
    ```bash
    git clone https://github.com/igornsferreira/fatec-dsm-pi-4sem.git
    ```

2. **Navegue até o diretório do projeto**:
    ```bash
    cd fatec-dsm-pi-4sem
    ```

3. **Crie um ambiente virtual Python e ative-o**:
    ```bash
    python -m venv venv
    venv\Scripts\activate.bat
    ```

4. **Instale as dependências do projeto**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Aplique as migrações do Django**:
    ```bash
    python manage.py migrate
    ```

6. **Inicie o servidor Django**:
    ```bash
    python manage.py runserver
    ```

Agora você deve ser capaz de acessar a aplicação no seu navegador.

# Job Application Tracker

Este é um projeto pessoal que estou criando para compor meu portfólio. Consiste em um site em que é possível manter registro de candidaturas a vagas de emprego.

## Comandos

### Iniciar aplicação backend

Para criar a aplicação backend pela primeira vez:

1. Navegue até o diretório raiz do backend:

   ```bash
   cd backend
   ```

2. Crie e ative o ambiente virtual para instalar os pacotes:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # No Windows
   ```

3. Crie os containers no Docker:

   ```bash
   docker-compose up --build
   ```

4. Caso a pasta `data` tenha sido rastreada pelo Git, remova-a do controle de versão:
   ```bash
   git rm --cached -r data
   ```

### Rodar aplicação backend já criada

Se a aplicação já foi criada anteriormente e deseja-se rodá-la novamente:

1. Navegue até o diretório raiz do backend:

   ```bash
   cd backend
   ```

2. Ative o ambiente virtual:

   ```bash
   .\venv\Scripts\activate  # No Windows
   ```

3. Inicie os containers no Docker:

   ```bash
   docker-compose up
   ```

4. Para rodar um comando Django com a aplicação em execução:
   ```bash
   docker-compose run --rm djangoapp (comando django)
   ```
   Exemplo:
   ```bash
   docker-compose run --rm djangoapp python startapp new_app
   ```

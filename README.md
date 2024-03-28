# Job-Application-Tracker

Esse é um projeto pessoal que estou criando para compor meu portfólio. Consiste em um site em que é possível você manter registro de duas candidaturas de vagas de emprego.

## Comandos

### Iniciar aplicação backend

Para criar a aplicação backend pela primeira vez:  
(Ir para root do backend)  
cd backend

(Criar o ambiente virtual para instalar os pacotes)  
python -m venv venv

(Ativar o ambiente virtual no Windows, em outros so o comando é um pouco diferente)  
.\venv\Scripts\activate

(Criar os containers no docker)  
docker-compose up --build

Com isto a aplicação será criada e estará rodando através de containers do docker e já estará rodando.

### Rodar aplicação backend já criada

Uma vez que você já tenha feito os passos para iniciar a aplicação e deseja rodar ela posteriormente:  
(Ir para root do backend)  
cd backend

(Ativar o ambiente virtual no Windows, em outros so o comando é um pouco diferente)  
.\venv\Scripts\activate

(Rodar os containers no docker)  
docker-compose up

(Para rodar um comando django com a aplicação rodando)  
docker-compose run (comando django)  
Ex: docker-compose run python startapp new_app

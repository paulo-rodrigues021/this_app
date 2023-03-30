# this_app

## Architecture
# todo desenhar arquitetura

The `department/` endpoint displays an user-friendly webpage 
The `employee/` endpoint displays an user-friendly webpage 

## Deployment

### Installing the project
Run all migrations:
```bash
./manage.py migrate
```

Run application:
```bash
python manage.py runserver
```

### Running the application

### Creating Admin
# todo definir como criar um superuser e acessar a parte admin


## API

### Installing requests
###### ref: # todo ref da lib requests do python

### Department Endpoints

### Employee Endpoints


## Testing
Explicar como rodar os testes

### Unit tests

### Integration tests


## Alternatives
# todo caso nao de pra usar pytest no projeto, lista-lo como alternativa
# todo descrever todos os porques das alternativas

### Web layer: WSI vs ASGI
###### ref: # todo colocar ref do 

### Python + Env Manager
###### ref: # todo colocar ref do poetry
###### ref: # todo colocar ref do pyenv

### ORM
###### ref: # todo colocar ref do sqlalchemy



## TODO
- Escrever uma versao que usa FastAPI
    - explicar as diferencas
    - usar Pydantic Base Models
    - Verificar injecao de dependencia
    - Usar as rotas de fastAPI para renderizar HTML
- Limpar o banco de dados
- Settar logs
- Escrever testes

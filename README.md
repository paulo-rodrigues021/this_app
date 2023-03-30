# this_app

## TODO
- Escrever uma versao que usa FastAPI
    - explicar as diferencas
    - usar Pydantic Base Models
    - Verificar injecao de dependencia
    - Usar as rotas de fastAPI para renderizar HTML
- Instalar loguru
- Escrever testes

## Architecture
# todo desenhar arquitetura

The `department/` endpoint displays an user-friendly webpage 
The `employee/` endpoint displays an user-friendly webpage 


## UUID
###### ref: https://pypi.org/project/shortuuid/
Using `shortuuid` to create unique identifiers for our registers.


## Deployment

Run all migrations:
```bash
./manage.py migrate
```

Run application:
```bash
python manage.py runserver
```

## Super User
usarname: Paulo
email: guest@guest.com
password: guest

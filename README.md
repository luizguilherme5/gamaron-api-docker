![logo-wide-gamaron](https://previews.123rf.com/images/chuckchee/chuckchee1605/chuckchee160500001/56731287-pixel-art-characters-8-bit-game-characters-warriors-monsters-mage-sorcerer-humans-and-orcs-we-love-8.jpg)

# Gamaron

Uma API open source escrita em Python, utilizando Django Rest Framework. É desenhado para ser extendível, escalável, simples e mutável.

Esta API é desenhada para comunicar-se, utilizando uma arquitetura REST entre um banco de dados relacional de forma independente uma aplicação Django Rest de forma otimizada para ReactJS, que é o framework escolhido para desenvolvimento da aplicação Gamaron, feita pela mesma equipe.

## Vantagens da utilização da Gamaron API

* É open source
* Fácil de modificar e adaptar
* Fácil de instalar
* Feito com Docker e Docker Compose para deploy simples
* Builds automatizadas

## Instalação

A instalação é feita baseada na imagem oficial do Python para Docker, porém com algumas depedências instaladas, entre elas, o Django e o Django REST.

### Docker Compose

Para rodar a API basta ter o Docker e o Docker Compose instalados e então rodar os seguintes comandos:

```bash
# Clonar este repositório 
git clone https://github.com/luizguilherme5/gamaron-api-docker

# Construir o projeto
sudo docker-compose -f local.yml build

# Criar as migrações
sudo docker-compose -f local.yml run --rm django python3 manage.py makemigrations

# Rodar as migrações
sudo docker-compose -f local.yml run --rm django python3 manage.py migrate

# Criar um super usuário
sudo docker-compose -f local.yml run --rm django python3 manage.py createsuperuser

# Testar o linting
sudo docker-compose -f local.yml run --rm django flake8

# Verificar os testes unitários
sudo docker-compose -f local.yml run --rm django py.test

# Rodar o servidor
sudo docker-compose -f local.yml up

# Para acessar, abra no navegador em:
localhost:8000/api
```



# Contribuindo

Contribuir para a aplicação é muito simples e fortemente encorajado! Então se você conhece um pouquinho sobre Python ou APIs REST você estará ajudando não só a equipe de desenvolvimento, com o Gamaron de uma forma muito simples.

Todos os contribuidores, incluindo a equipe de desenvolvimento e os fundadores do projeto da aplicação móvel, contribuem usando o seguinte processo:

* Fork o projeto principal para sua conta (se você não for um contribuidor da equipe de desenvolvimento)
* Crie uma branch para features
* Realize suas alterações ou acréscimos ao projeto
* Crie um pull request para o projeto principal
* Testes e a cobertura dos testes serão checados automaticamente
* Um dos responsáveis pelo projeto irá revisar suas alterações e mesclará seu pull request

Para mais informações acesse a [documentação para contribuição]()
Caso precise de ajuda, crie uma issue, também seguindo o [padrão estabelecido]!

-------

## Contribuidores

Este projeto existe graças aos contribuidores. [Seja um deles!](/docs/contributing.md).

# SWAPI - Flask [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

##### Projeto Python + Micro-framework Flask onde seu funcionamento consiste no consumo da API http://swapi.dev/ (Antigo https://swapi.co/), que fornece dados sobre personagens, filmes e afins sobre a franquia de filmes StarWars.

https://flaskswapi.herokuapp.com/
 
![swapisite](https://user-images.githubusercontent.com/31486060/80264821-c4d2e680-866b-11ea-941a-e534df1ca91a.png)

### Funcionalidades
___
- ##### Listagem de personagens com exibição de informações
- ##### Busca de filmes, veículos, naves estrelares e planetas por nome
- ##### Ordenação da melhor nave estelar para pior com base em score

### Tecnologias
___

- ##### Editor: [Visual Studio Code](https://code.visualstudio.com/) (VsCode)  


- ##### Back-end:
    ##### [Python](https://www.python.org/) 3.6.0
    ##### [Micro-framework Flask](https://flask.palletsprojects.com/en/1.1.x/) 1.1.2  

    
- ##### Front-end:
    ##### [Bootstrap 4](https://getbootstrap.com/)
    ##### [View Engine Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    ##### [DataTables](https://datatables.net/) (Interaction controls to your HTML tables)  

    ![DataTable](https://user-images.githubusercontent.com/31486060/80246396-bc19ea80-8642-11ea-87b7-70b3c11707ef.png)


- ##### Ambiente de Produção: [Docker](https://www.docker.com/)
- ##### Hospedagem: [Heroku](https://www.heroku.com/)
- ##### Padrão de Arquitetura do Projeto: Model-View-Controller  
  
 
### Estrutura do Projeto \(Project Structure\)
```text
├── swapi/
│   │
│   ├── app/
│   │   │ 
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   │
│   │   ├── controllers/
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-36.pyc
│   │   │   │   ├── default.cpython-36.pyc
│   │   │   │   
│   │   │   ├── __init__.py
│   │   │   ├── default.py
│   │   │   │
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   ├── datatables.css
│   │   │   │   ├── datatables.min.css
│   │   │   │
│   │   │   ├── js/
│   │   │   │   ├── datatables.js
│   │   │   │   ├── datatables.min.js
│   │   │   │
│   │   │ 
│   │   ├── templates/
│   │   │   ├── films.html
│   │   │   ├── homeworld.html
│   │   │   ├── index.html
│   │   │   ├── rankingstarships.html
│   │   │   ├── starships.html
│   │   │   ├── vehicles.html
│   │   │
│   │   ├── __init__.py
│   │
│   ├── .gitignore
│   ├── Dockerfile
│   ├── heroku.yml
|   ├── Procfile
│   ├── README.md
|   ├── requirements.txt
│   ├── run.py
```

### Instalação e Execução
___
- ##### Instalar o Git de acordo com sua versão [Download Git](https://git-scm.com/downloads)

- ##### Clonar repositório pelo terminal ou fazer download do projeto em ZIP:  


- ~~~
  git clone https://github.com/pdrodavi/swapi-flask-py.git
  ~~~
  
- ##### [Download do Projeto em ZIP](https://github.com/pdrodavi/swapi-flask-py/archive/master.zip)
  
- ##### Instalar o Python 3.6.0 [Download](https://www.python.org/downloads/release/python-360/)
  
- ##### Executar o comando abaixo no diretório raiz pelo terminal para instalar as dependências:


-  ~~~
   pip install -r requirements.txt
   ~~~
  
- ##### Executar o comando abaixo no diretório raiz para executar o arquivo que inicia o projeto:


-  ~~~
   python run.py
   ~~~

___  
### Construção da imagem Docker
- ##### Executar o comando abaixo no diretório raiz onde se encontra o arquivo Dockerfile. O comando "build" é o responsável por gerar a imagem, o parametro "-t" informa que a imagem pertence ao seu usuário e em seguida você define um nome para sua imagem (lembre-se de retirar os sinais operadores <> e deixar apenas o nome) e por fim o ponto serve para indicar que o arquivo Dockerfile está no diretório corrente:


-  ~~~
   docker build -t <nome-da-sua-imagem> .
   ~~~
  

  
### License MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

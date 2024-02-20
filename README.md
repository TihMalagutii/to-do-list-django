# To-Do List
> Django

O projeto em questão é uma aplicação web desenvolvida em Django para criação e gerenciamento de listas de tarefas, conhecidas como "to-do lists". Essa aplicação oferece uma interface amigável e intuitiva para que os usuários possam adicionar, editar e excluir tarefas e disciplinas, bem como marcar como concluídas.

![telaDisciplinas](https://github.com/TihMalagutii/to-do-list-django/assets/110874943/4f627578-c971-40ef-a649-c23c4efb30f4)

![telaTarefas](https://github.com/TihMalagutii/to-do-list-django/assets/110874943/b673b3ba-2c03-41f2-aa0e-96adb9f2e021)

Além disso, o projeto inclui recursos como autenticação de usuário, garantindo que apenas usuários autenticados possam acessar e manipular suas listas de tarefas. Os usuários podem criar uma conta, fazer login e, assim, acessar suas listas de tarefas personalizadas.

![telaLogin](https://github.com/TihMalagutii/to-do-list-django/assets/110874943/271aecc7-06f2-43c5-b828-75e078b3948a)

![telaCadastro](https://github.com/TihMalagutii/to-do-list-django/assets/110874943/5fb1bd31-1107-46cd-840d-84cc1bf63fa3)

A aplicação também possui funcionalidades de busca e filtragem, permitindo aos usuários encontrar rapidamente tarefas específicas dentro de suas listas. Isso é útil especialmente em listas maiores ou quando se deseja localizar tarefas específicas com facilidade.

<h1>Instruções para a execução correta</h1>

Versão do python utilizada no projeto: 3.11
<br><br>
Após a instalação do projeto, abra o terminal(cmd) na pasta principal.
<br>
<br>
Se não tiver o pipenv instalado, execute o comando:<br> python -m pipenv install
<br><br>
Após instalar o pipenv execute o comando:<br> python -m pipenv shell
<br><br>
E inicie o projeto normalmente com:<br> python manage.py runserver

Caso não tenha nenhum usuario cadastrado, pode cadastrar normalmente pela pagina de cadastro, <br>
ou se quiser um usuario admin para que libere a função de imprimir as disciplinas, crie um super user:<br><br>
Interrompa o programa e execute o codigo:<br> python manage.py createsuperuser
<br><br>
Após isso é so iniciar o programa novamente e logar com o super user.

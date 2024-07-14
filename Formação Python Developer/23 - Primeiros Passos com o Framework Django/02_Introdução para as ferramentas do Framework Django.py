'''
MTV (Model-Template-View) é um padrão de arquitetura comumente usado no framework
Django para desenvolvimento web. Ele separa a lógica da aplicação em três camadas
distintas, cada uma com uma responsabilidade específica:

* Model (Modelo):
Define a estrutura dos dados da sua aplicação.
É mapeado para tabelas em seu banco de dados relacional usando um ORM (Object-Relational Mapper).
Exemplos de modelos em um site de notícias: Noticia (título, conteúdo, autor), Categoria (nome).

* Template (Template):
Define a apresentação do conteúdo para o usuário final.
Utiliza HTML, CSS e linguagens de templating como Jinja2 (usada no Django) para renderizar o layout e inserir dados dinâmicos.
Exemplo: Template de exibição de notícias, onde seriam inseridos o título, conteúdo e autor recuperados do modelo Noticia.

* View (Visualização):
Atua como intermediário entre o Model e o Template.
É responsável por:
Receber requisições HTTP do usuário (por exemplo, acesso a uma página específica).
Consultar o Model para recuperar dados relevantes.
Processar esses dados se necessário (por exemplo, formatação).
Selecionar o Template apropriado.
Passar os dados recuperados do Model para o Template.
Retornar a resposta final renderizada pelo Template para o usuário.
'''

'''
controller/controlado django
No Django, o termo "controller" geralmente se refere à camada de "View" no padrão de arquitetura
Model-Template-View (MTV), que é um padrão comumente utilizado no framework.
No entanto, é importante esclarecer que o Django não utiliza a terminologia "controller" da mesma
forma que outros frameworks, como o MVC (Model-View-Controller). No Django, a camada de "View"
assume as responsabilidades que normalmente são atribuídas a um controller em outros frameworks.
'''

'''
# models - orm django
Em Django, models (modelos) e ORM (Object-Relational Mapper) trabalham juntos
para gerenciar a interação entre sua aplicação web e o banco de dados relacional.
Vamos entender cada um deles separadamente:

* Models (Modelos)
Os modelos do Django definem a estrutura dos dados da sua aplicação.
Eles funcionam como uma representação Python de tabelas em seu banco de dados relacional.
Cada modelo define os campos que armazenam os dados (por exemplo, título, conteúdo, autor para um modelo de notícia).
Cada campo possui um tipo específico (texto, data, inteiro, etc.) que define o tipo de dado que ele pode armazenar.
Os modelos também podem especificar relações entre si (relacionamentos um-para-um, muitos-para-um, muitos-para-muitos).

* ORM (Object-Relational Mapper)
O ORM do Django é uma ferramenta poderosa que facilita a interação com o banco de dados relacional.
Ele permite que você trabalhe com seus dados usando objetos Python, em vez de escrever consultas SQL diretamente.
O ORM traduz automaticamente as operações em objetos Python para consultas SQL equivalentes que o banco de dados entende.
Veja alguns dos recursos oferecidos pelo ORM do Django:

Criar, ler, atualizar e deletar dados (CRUD)
Consultas complexas
Relacionamentos
'''

'''
views (request/response)
Em Django, as views (visualizações) são o coração da sua aplicação web.
Elas lidam com requisições HTTP recebidas do navegador do usuário e são
responsáveis por gerar a resposta adequada. Essa resposta pode ser qualquer
coisa, desde uma simples página HTML até um payload JSON complexo para uma API.
'''

'''
templates - resposta da views
No Django, templates (templates) são arquivos HTML que definem a estrutura
e o layout da interface do usuário para sua aplicação web. As views (visualizações),
por outro lado, são responsáveis por gerar a resposta final que será enviada para
o navegador do usuário. Essa resposta pode incluir conteúdo renderizado de um template
'''

'''
crud - criar / recuperar / atualizar / excluir
O CRUD (Create, Read, Update, Delete) é um conjunto fundamental de operações para
gerenciar dados em um banco de dados. No Django, o framework oferece ferramentas e
recursos poderosos para simplificar e agilizar essas operações em suas aplicações web.
'''

'''
BATERIAS
No contexto do Django, o termo "baterias" (em inglês, "batteries") se refere à
filosofia de design do framework que oferece um conjunto completo de ferramentas
e funcionalidades prontas para uso, como autenticação de usuários, administração
de conteúdo, gerenciamento de URLs, sistema de templates e um ORM
(Object-Relational Mapper) poderoso.

Essa filosofia tem como objetivo agilizar o desenvolvimento web e reduzir a
quantidade de código repetitivo que os desenvolvedores precisam escrever.
O Django fornece as "baterias" que você precisa para construir a base de sua
aplicação web, permitindo que você se concentre em escrever o código específico
do seu projeto.
'''

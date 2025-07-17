from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
# objeto site recebe o conteudo da requisição http do site.

soup = BeautifulSoup(site, 'html.parser')
# objeto soup baixa do site o html

print(soup.prettify())
print()
print(soup.head)
print()
print(soup.body)

# soup.prettify transforma o html em string

div = soup.find("div", class_="faq _margin-t-20")
print('IMPRESSÃO DO TEXTO DA DIV CLASS=FAQ_MARGIN-T-20')
print(div.get_text(strip=True, separator=' '))
print()

clima = div.find('p')
print('IMPRESSÃO DO TEXTO DA TAG P DENTRO DA DIV CLASS=FAQ_MARGIN-T-20')
print(clima.get_text(strip=True, separator=' '))

# print(soup.title.string)

# primeira tag a
print(soup.a)

# primeira tag p
print(soup.p)

# pesquisa na pagina
print(soup.find('topografia.'))

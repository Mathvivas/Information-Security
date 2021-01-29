from bs4 import BeautifulSoup
import requests

# Objeto site está recebendo o conteúdo da requisição http do site.
site = requests.get('https://www.climatempo.com.br/').content

# Objeto soup está baixanddo do site o html
soup = BeautifulSoup(site, 'html.parser')

# Transforma o html em string e o print vai exibir o html
#print(soup.prettify())

print(soup.title)       # Printa toda a tag
print(soup.title.string)
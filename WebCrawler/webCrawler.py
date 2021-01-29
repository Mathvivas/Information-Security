import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

# Define o WebCrawler
def start(url):
    wordlist = []   # Armazena o conteúdo do site
    sourceCode = requests.get(url).text

    soup = BeautifulSoup(sourceCode, 'html.parser')

    # Text in given web-page is stored under
    # The <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)

        clean_wordlist(wordlist)

# Remove símbolos indesejados
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%*()_+-={}[]^:;.,<>?/\|" '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')     # Substitui os símbolos por nada

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

# Top palavras mais utilizadas no site
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Palavras com mais ocorrências no site
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print(f'{key} : {value}')

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')

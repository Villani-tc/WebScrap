import requests
from bs4 import BeautifulSoup
import csv


def Busca_Kabum(produto_nome):
    base_url = 'https://www.kabum.com.br'
    url = 'https://www.kabum.com.br/busca/'
    url = url + produto_nome
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    site = BeautifulSoup(response.text, 'html.parser')
    produtos = site.findAll('div', attrs={'class':'sc-ff8a9791-7 dZlrn productCard'})
    with open('Busca_DUMP\kabum.csv','w',encoding='utf-8') as file:
        writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_NONE)
        for produto in produtos:
            produto_titulo = produto.find('span', attrs= {'class':'sc-d99ca57-0 iRparH sc-ff8a9791-16 kRYNji nameCard'}).text
            produto_preco = produto.find('span', attrs={'class': 'sc-3b515ca1-2 jTvomc priceCard'}).text
            produto_link = produto.find('a', attrs= {'class':'sc-ff8a9791-10 cUkkYl'})
            produto_link = str(base_url + str(produto_link['href']))
            print('Título do Produto: ' + produto_titulo )
            print('Preço do Produto: ' + produto_preco )
            print('Link: ' + produto_link )
            data = [produto_titulo, produto_preco,produto_link , 'Kabum']
            writer.writerow(data)


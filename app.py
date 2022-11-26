import requests
from bs4 import BeautifulSoup


url = 'https://lista.mercadolivre.com.br/'
produto_nome = 'mi band 7'
response = requests.get(url+produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})

for produto in produtos:

    produto_titulo = produto.find('h2', attrs = {'class': 'ui-search-item__title shops__item-title'}).text
    produto_preco = produto.find('span', attrs={'class':'price-tag-fraction'}).text    
    produto_preco_cents = produto.find('span', attrs={'class':'price-tag-cents'})
    produto_preco_cents = str(produto_preco_cents)
    produto_preco_cents = produto_preco_cents[30:32]
    final_preco = produto_preco + ','+ produto_preco_cents
    link = produto.find('a',attrs={'class':'ui-search-link'})
    link = link['href']
    parcelas = produto.find('span', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--BLACK'})
    if (parcelas):
        parcelas = produto.find('span', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--BLACK'}).text
        parcelas = str(parcelas)
        parcelas =parcelas[2:5]
        parcelas_valor = produto.find('div', attrs={'class': 'ui-search-price ui-search-price--size-x-tiny ui-search-color--BLACK shops__price'}).text
        parcelas_valor = str(parcelas_valor)
        parcelas_valor = parcelas_valor[25:]
    else:
        parcelas = None

    print('Título do Produto: ' + produto_titulo )
    if (produto_preco_cents):
        print('Preço do Produto: ' + final_preco )
    else:
        print('Preço do Produto: ' + produto_preco + ',00')
    
    if parcelas == None:
        print('Sem Parcelamento')
        
    else: 
        print('Número de Parcelas ' + parcelas + ' No valor de ' + parcelas_valor)

    print('Link: ' + link)
    print('\n\n')
    





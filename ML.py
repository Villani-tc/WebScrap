import requests
from bs4 import BeautifulSoup
import csv


def Busca_ML(produto_nome):

    url = 'https://lista.mercadolivre.com.br/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url+produto_nome,headers=headers)
    site = BeautifulSoup(response.text, 'html.parser')
    produtos_1 = site.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})
    produtos_2 = site.findAll('div', attrs={'class':'ui-search-result__wrapper shops__result-wrapper'}) #rtx 2060 problem
    produtos_link = site.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default andes-card--animated'})  
    if produtos_1 == None:
        with open('mercadolivre.csv','w',) as file:
            writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_NONE)
            for produto in produtos_1:
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
                    final_preco = produto_preco + ',00'
                    print('Preço do Produto: ' + final_preco )
                
                if parcelas == None:
                    print('Sem Parcelamento')
                    
                else: 
                    print('Número de Parcelas ' + parcelas + ' No valor de ' + parcelas_valor)

                    print('Link: ' + link)
                data = [produto_titulo, final_preco ,link , 'MercadoLivre']
                writer.writerow(data)
            
    else:
        with open('Busca_DUMP\mercadolivre.csv','w',encoding='utf-8') as file:
            writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_NONE)
            for proc in produtos_2:
                produto_titulo = proc.find('h2', attrs = {'class': 'ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title'}).text
                produto_preco = proc.find('span', attrs={'class':'price-tag-amount'}).text
                parcelas =proc.find('span', attrs={'class':'ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--LIGHT_GREEN'})
                if (parcelas):
                    parcelas =proc.find('span', attrs={'class':'ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--LIGHT_GREEN'}).text
                    parcelas = str(parcelas)
                    parcelas = parcelas[2:15] 
                else:
                    parcelas = "Sem parcelamento"
                for links in produtos_link:
                    link = links.find('a',attrs={'class':'ui-search-link'})
                    link = link['href'] 
                print('Título do Produto: ' + produto_titulo )
                print('Preço do Produto: ' + produto_preco )
                print('Número de Parcelas ' + parcelas )
                print('Link: ' + link)
                print('\n\n')
                data = [produto_titulo, produto_preco ,link , 'MercadoLivre']
                writer.writerow(data)


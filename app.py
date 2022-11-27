from ML import Busca_ML
from Kabum import Busca_Kabum
import random as rn
import pandas as pd
produto_nome = 'RTX 2060'
try:
    Busca_ML(produto_nome)
except:
    print('Scrap não disponível ainda para essa secção do ML')

Busca_Kabum(produto_nome)
first_csv = pd.read_csv('Busca_DUMP\kabum.csv',sep=';',encoding='UTF-8',names=['Titulo Produto', 'Preço do Produto', 'Link', 'Site'])
second_csv = pd.read_csv('Busca_DUMP\mercadolivre.csv',sep=';',encoding='UTF-8',names=['Titulo Produto', 'Preço do Produto', 'Link', 'Site'])
df = pd.concat([first_csv,second_csv])
df.to_csv('output.csv',sep=';',encoding='UTF-8')
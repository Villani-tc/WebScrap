from ML import Busca_ML
from Kabum import Busca_Kabum
import random as rn
import pandas as pd
import glob 
import csv

produto_nome = 'RTX 2060'
try:
    Busca_ML(produto_nome)
except:
    print('Scrap não disponível ainda para essa secção do ML')

Busca_Kabum(produto_nome)
data = []
init = pd.DataFrame(data=data, index=None, columns=['Titulo Produto', 'Preço do Produto', 'Link', 'Site'], dtype=None, copy=None)
init.to_csv('init.csv',encoding='UTF-8')
data_main  = glob.glob( str ( 'Busca_DUMP' ) +  '/*.csv' , recursive = True )
init = pd.read_csv('init.csv')
for data in data_main:
        data_csv = pd.read_csv(data,sep=';',encoding='UTF-8',names=['Titulo Produto', 'Preço do Produto', 'Link', 'Site'])
        df = pd.concat([data_csv,init])
        print(df)
df.to_csv('output.csv',sep=';',encoding='UTF-8')

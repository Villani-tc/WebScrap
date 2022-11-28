
from ML import Busca_ML
from Kabum import Busca_Kabum
import random as rn
import pandas as pd
import glob 
import csv

produto_nome = 'rtx 2060'
try:
    Busca_ML(produto_nome)
except:
    print('Scrap não disponível ainda para essa secção do ML')

Busca_Kabum(produto_nome)

#Assembly de dados

all_filenames = [i for i in glob.glob( str ( 'Busca_DUMP' ) +  '/*.csv')]
combined_csv = pd.concat([pd.read_csv(f,sep = '|',dtype={'Preço': 'float'})  for f in all_filenames ],ignore_index=True)
#combined_csv['Preço']=combined_csv.column.astype('float64')
print(combined_csv.dtypes)

#export to csv
#combined_csv.to_csv( "combined_csv.csv", sep="|", index=False)


#Tratamento
combined_csv = combined_csv.sort_values(['Preço'], ignore_index=True)
combined_csv.to_csv( "combined_csv.csv", sep="|", index=False)

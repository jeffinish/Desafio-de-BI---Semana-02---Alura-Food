# Importando Bibliotecas

import pandas as pd
import numpy as np
import json

# Importando base de dados
df_1 = pd.read_json(r'G:\My Drive\1. ESTUDO\Desafio de BI - Semana 02 - Alura Food\Dados Brutos\file1.json')
df_2 = pd.read_json(r'G:\My Drive\1. ESTUDO\Desafio de BI - Semana 02 - Alura Food\Dados Brutos\file2.json')
df_3 = pd.read_json(r'G:\My Drive\1. ESTUDO\Desafio de BI - Semana 02 - Alura Food\Dados Brutos\file3.json')
df_4 = pd.read_json(r'G:\My Drive\1. ESTUDO\Desafio de BI - Semana 02 - Alura Food\Dados Brutos\file4.json')

info_restaurants = []
## Trantando o primeiro arquivo
df_1_clean = df_1[df_1.results_shown > 0][['restaurants','results_shown']] # Considerando apenas as colunas que possuem informações dos clientes
info_restaurants_1 = [] #Array vazio para guardarmos as informações do loop do arquivo em questao
# validate = 0
for i in df_1_clean.index:
    a = df_1_clean.loc[i]
    info_restaurants_1.extend(a.restaurants)
    # validate += a.results_shown
    # print(f"Quantidade de registros obtidos:{len(info_restaurants_1)}| Quantidade de registros esperados:{validate}")

info_restaurants.extend(info_restaurants_1)

## Tratando o segundo arquivo
df_2_clean = df_2[df_2.results_shown > 0][['restaurants','results_shown']] # Considerando apenas as colunas que possuem informações dos clientes
info_restaurants_2 = [] #Array vazio para guardarmos as informações do loop do arquivo em questao
# validate = 0
for i in df_2_clean.index:
    a = df_2_clean.loc[i]
    info_restaurants_2.extend(a.restaurants)
    # validate += a.results_shown
    # print(f"Quantidade de registros obtidos:{len(info_restaurants_2)}| Quantidade de registros esperados:{validate}")

info_restaurants.extend(info_restaurants_2)

## Tratando o terceiro arquivo
df_3_clean = df_3[df_3.results_shown > 0][['restaurants','results_shown']] # Considerando apenas as colunas que possuem informações dos clientes
info_restaurants_3 = [] #Array vazio para guardarmos as informações do loop do arquivo em questao
# validate = 0
for i in df_3_clean.index:
    a = df_3_clean.loc[i]
    info_restaurants_3.extend(a.restaurants)
    # validate += a.results_shown
    # print(f"Quantidade de registros obtidos:{len(info_restaurants_3)}| Quantidade de registros esperados:{validate}")

info_restaurants.extend(info_restaurants_3)

## Tratando quarto arquivo
df_4_clean = df_4[df_4.results_shown > 0][['restaurants','results_shown']] # Considerando apenas as colunas que possuem informações dos clientes
info_restaurants_4 = [] #Array vazio para guardarmos as informações do loop do arquivo em questao
# validate = 0
for i in df_4_clean.index:
    a = df_4_clean.loc[i]
    info_restaurants_4.extend(a.restaurants)
    # validate += a.results_shown
    # print(f"Quantidade de registros obtidos:{len(info_restaurants_4)}| Quantidade de registros esperados:{validate}")

info_restaurants.extend(info_restaurants_4)

restaurants = pd.json_normalize(info_restaurants)
# restaurants.info()

# Validando os dados
restaurants['restaurant.R.res_id'].drop_duplicates()
restaurants.sort_values(by=['restaurant.R.res_id'])
id53 = restaurants[restaurants['restaurant.R.res_id'] == 53].reset_index(drop=True)
id53.loc[0] == id53.loc[1]

id53[['restaurant.apikey','restaurant.zomato_events','restaurant.order_deeplink','restaurant.order_url']]
restaurants[restaurants['restaurant.R.res_id'] == 53]

restaurants['restaurant.R.res_id'].value_counts()[:10]

id18400530 = restaurants[restaurants['restaurant.R.res_id'] == 18400530].reset_index()
id18400530.dropna(axis=1,how='all',inplace=True)
id18400530.shape[0]
id18400530.info()

i=0
a = []
while i < (id18400530.shape[0]-1):
        t = (id18400530.loc[i] == id18400530.loc[i+1]).sum()
        print(t)
        i+=1

id18224282 = restaurants[restaurants['restaurant.R.res_id'] == 18224282].reset_index()
id18224282.dropna(axis=1,how='all',inplace=True)
id18224282.shape[0]
id18224282.info()
id18224282['restaurant.zomato_events'][0] == id18224282['restaurant.zomato_events'][1]

i=0
a = []
while i < (id18224282.shape[0]-1):
        t = (id18224282.loc[i] == id18224282.loc[i+1]).sum()
        print(t)
        i+=1

(id18400530.loc[0] == id18400530.loc[1]).sum()
ind = np.where(~(id18400530.loc[0] == id18400530.loc[1]))

ind[:]
a =list(*ind)
id18400530.iloc[:,a]

# Tratamento final das colunas

restaurants.dropna(axis='columns',how='all',inplace=True)
restaurants.rename(columns=lambda x: x.replace("restaurant.",""),inplace=True)
restaurants.drop(columns=['photos_url','apikey','deeplink','book_url','switch_to_order_menu','offers','zomato_events','establishment_types','events_url','order_deeplink','order_url'],inplace=True)
restaurants.drop(columns=['R.res_id'],inplace=True)

restaurants.insert(0,'id',restaurants.pop('id'))
restaurants.drop_duplicates(subset=['id'],inplace=True)

## Teste para expandir a coluna cuisines
restaurants['cuisines_0']
a = restaurants[['cuisines_0']]
b = restaurants[['cuisines_1']]
pd.concat([a,b],ignore_index=True)

restaurants=restaurants.join(restaurants['cuisines'].str.split(',',expand=True)).rename(columns={0:'cuisines_0',1:'cuisines_1',2:'cuisines_2',3:'cuisines_3',4:'cuisines_4',5:'cuisines_5',6:'cuisines_6',7:'cuisines_7'})


# Lidando com os espaços em branco
a = restaurants.drop_duplicates(subset=['cuisines_0','cuisines_1','cuisines_2','cuisines_3','cuisines_4','cuisines_5','cuisines_6','cuisines_7'])[['cuisines_0','cuisines_1','cuisines_2','cuisines_3','cuisines_4','cuisines_5','cuisines_6','cuisines_7']]

unique_cuisines = []
for i in list:
    t = a[i]
    t
    unique_cuisines = pd.concat([unique_cuisines,t],axis=0)

unique_cuisines.str.strip().drop_duplicates().tolist()
unique_cuisines.drop_duplicates().tolist()

cols = ['cuisines_0','cuisines_1','cuisines_2','cuisines_3','cuisines_4','cuisines_5','cuisines_6','cuisines_7']
restaurants[cols] = restaurants[cols].apply(lambda x: x.str.strip())

restaurants.info()

restaurants_india = restaurants[restaurants['location.country_id'] == 1]

restaurants_india.to_csv(r'G:\My Drive\1. ESTUDO\Desafio de BI - Semana 02 - Alura Food\Dados Tratados\restaurants.csv',sep=';',index=False)

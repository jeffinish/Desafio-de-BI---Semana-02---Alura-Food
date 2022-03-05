# Desafio de BI - Semana-02 - Alura-Food

## Etapa 01 - Visão Geral dos Dados e Primeiros Tratamentos

Foram fornecidos 4 arquivos *.json* com informações extraidas através da API do aplicativo *Zomato*.

Após primeira análise, pode-se notar que o arquivo é extraido com as seguintes informações:


| |results_found  |restaurants  |results_shown  |results_start  |message code |	status  |
|-|-|-|-|-|-|-|
|0  |17151.0 |[{'restaurant': {'has_online_delivery': 1, 'ph... |20.0	|1.0	|NaN	|NaN	|NaN
|1  |4748.0	 |[{'restaurant': {'has_online_delivery': 0, 'ph...	|20.0	|1.0	|NaN	|NaN	|NaN
|2  |13786.0 |[{'restaurant': {'has_online_delivery': 0, 'ph...	|20.0	|1.0	|NaN	|NaN	|NaN
|3  |10224.0 |[{'restaurant': {'has_online_delivery': 0, 'ph...	|20.0	|1.0	|NaN	|NaN	|NaN
|4  |7039.0  |[{'restaurant': {'has_online_delivery': 0, 'ph...	|20.0 |1.0	|NaN	|NaN	|NaN
|...  |...  |...	|...	|...	|...	|...	|...
|474  |NaN  |NaN	|NaN	|NaN	|API limit exceeded	|440.0
|475  |NaN  |NaN	|NaN	|NaN	|API limit exceeded	|440.0
|476  |NaN  |NaN	|NaN	|NaN	|API limit exceeded	|440.0
|477  |NaN  |NaN	|NaN	|NaN	|API limit exceeded	|440.0
|478  |NaN  |NaN	|NaN	|NaN	|API limit exceeded	|440.0

No primeiro arquivo, temos 76 linhas que apresentam as colunas `restaurants` e `results_found` não nulas e elas são as de nosso interesse. Além disso, quando olhamos para a coluna `restaurants`, vemos que ela possui informações dos restautantes em formato de dicionário, que podem ser facilmente trabalhadas utilizando o formato .json com as seguintes informações:
```
{'restaurant': {'has_online_delivery': 0,
   'photos_url': 'https://www.zomato.com/OdeonSocial/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop',
   'url': 'https://www.zomato.com/OdeonSocial?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
   'price_range': 3,
   'apikey': 'b90e6a8c738410315a20c449fe2eb1b1',
   'user_rating': {'rating_text': 'Very Good',
    'rating_color': '5BA829',
    'votes': '1959',
    'aggregate_rating': '4.1'},
   'R': {'res_id': 18246991},
   'name': 'Odeon Social',
   'cuisines': 'Continental, American, Asian, North Indian',
   'is_delivering_now': 0,
   'deeplink': 'zomato://restaurant/18246991',
   'menu_url': 'https://www.zomato.com/OdeonSocial/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop',
   'average_cost_for_two': 1600,
   'book_url': 'https://www.zomato.com/OdeonSocial/book?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1',
   'switch_to_order_menu': 0,
   'offers': [],
   'has_table_booking': 1,
   'location': {'latitude': '28.6342487678',
    'address': '1st Floor, 23, Odeon Building, Radial 5, D Block, Connaught Place, New Delhi',
    'city': 'New Delhi',
    'country_id': 1,
    'locality_verbose': 'Connaught Place, New Delhi',
    'city_id': 1,
    'zipcode': '',
    'longitude': '77.2209088504',
    'locality': 'Connaught Place'},
   'featured_image': 'https://b.zmtcdn.com/data/pictures/1/18246991/34f289fd1eb24993ce308a3d47da94ea_featured_v2.jpg',
   'zomato_events': [{'event': {'display_date': '05 April - 21 May',
      'end_time': '01:00:00',
      'date_added': '2017-04-05 14:48:46',
      'start_date': '2017-04-05',
      'photos': [{'photo': {'photo_id': 185864,
         'order': 0,
         'type': 'NORMAL',
         'url': 'https://b.zmtcdn.com/data/zomato_events/photos/b73/ec1691986700e9839313d9353b2e4b73_1491383926.jpg',
         'md5sum': 'ec1691986700e9839313d9353b2e4b73',
         'uuid': 1491383890952953,
         'thumb_url': 'https://b.zmtcdn.com/data/zomato_events/photos/b73/ec1691986700e9839313d9353b2e4b73_1491383926.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A'}},
       {'photo': {'photo_id': 185879,
         'order': 1,
         'type': 'NORMAL',
         'url': 'https://b.zmtcdn.com/data/zomato_events/photos/3ce/8cda41e10df03e71d09faa00f64143ce_1491384649.jpg',
         'md5sum': '8cda41e10df03e71d09faa00f64143ce',
         'uuid': 1491384637585845,
         'thumb_url': 'https://b.zmtcdn.com/data/zomato_events/photos/3ce/8cda41e10df03e71d09faa00f64143ce_1491384649.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A'}}],
      'share_url': 'http://www.zoma.to/r/18246991',
      'description': "It's #IPL season and we're screening 'em all! Come one and all to witness the drama and pair it with our On Tap offer on beer - Stella + Hoegaarden! ",
      'title': 'IPL Match Screenings',
      'display_time': '10:00 am - 01:00 am',
      'book_link': '',
      'restaurants': [],
      'disclaimer': 'Restaurants are solely responsible for the service; availability and quality of the events including all or any cancellations/ modifications/ complaints.',
      'friendly_start_date': '05 April',
      'is_end_time_set': 1,
      'event_id': 118168,
      'end_date': '2017-05-21',
      'event_category': 0,
      'friendly_end_date': '21 May',
      'is_active': 1,
      'start_time': '10:00:00',
      'is_valid': 1,
      'event_category_name': ''}}],
   'currency': 'Rs.',
   'id': '18246991',
   'thumb': 'https://b.zmtcdn.com/data/pictures/1/18246991/34f289fd1eb24993ce308a3d47da94ea_featured_v2.jpg',
   'establishment_types': [],
   'events_url': 'https://www.zomato.com/OdeonSocial/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1'}}
```

Felizmente, para lidar com isso, podemos utilizar o método `json_normalize` da biblioteca Pandas para transformar estas cada uma destas linhas em um dataframe com as informações de todos os restaurantes. A estratégia adotada neste caso vai ser concatenar as informações de todas as colunas dos 4 arquivos e no final criarmos apenas um dataframe.

O primeiro arquivo nos retornou 1200 registros que foram obtidos em 59 requisições de 20 estabelecimentos e uma de 40. Além disso, este arquivo possui 38 colunas. O segundo arquivo, por sua vez, possui 10602 registros que foram obtidos em 539 requisições de tamanhos variados. Para o teceiro arquivo, temos 8686 registros obtidos em 437 requisções também de tamanhos variados. Finalmente, para o quarto arquivo, temos 8865 registros obtidos em 454 requisições. Ao todo, temos 29352 registros.

## Etapa 02 - Análisando um pouco mais

Como obtido na fase anterior, os arquivos disponibilizados possuem 29532 registros, mas será que todos estes são distintos? Poderiamos estar lidando com diversos registros duplicados o que faria com que qualquer análise posterior levasse à conclusões incorretas.

Para verificar isto, utlizando o método `drop_duplicates` encontramos que dentre os registros, existem apenas 9157 ID's distintos e em particular, existem IDs que se repetem mais de 300 vezes:

|ID |Quantidade de Repetições|
|-|-|
|18400530|    337|
|18224282|    229|
|3700050|     190|
|801269|      190|
|18483082|    190|
|16668008|    189|
|18483252|    190|
|16654702|    189|
|17211719|    189|
|18366580|    189|

e esta repetição merece uma análise um pouco mais detalhada. Olhando para o ID 18400530 ao remover todas as colunas nulas, restam 35 colunas e todas as entradas possuem as mesmas informações. Por outro lado, ao analisar o id 18224282, este possui uma coluna a mais preenchida, mas ainda, todos os 229 registros possuem os mesmos dados.

## Etapa 03 - Concluindo o tratamento e exportando os dados

Para finalizar o tratamento de dados, vamos selecionar e tratar as colunas separadamente para facilitar a criação do dashboard. Este tratamento seguiu as seguintes etapas:

1. Utilizar o método `dropna` com argumento `how=All` para remover colunas totalmente nulas;
2. Utilizar o método `rename` juntamente com o `replace` para ajustar o nome das colunas;
3. Utilizar o método `drop` para remover colunas desnecessárias para as análises;
4. Utilizar o método `drop_duplicates` a partir da coluna `id` como filtro;
5. Separamos a coluna `cuisines` em mutiplas colunas utilizando `split` e `strip`;
6.

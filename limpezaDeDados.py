import pandas as pd

df_original = pd.read_csv('./dados/Airbnb_Open_Data.csv', low_memory=False)
df = df_original.copy()

# Excluindo colunas que não serão utilizadas

df = df.drop(columns = ['license']) # feito a remoção da coluna license

# novas colunas reordenadas

df = df[
        ['id', 'NAME', 'host id', 'host_identity_verified', 'host name',
        'neighbourhood group', 'neighbourhood', 'lat', 'long', 'country',
        'country code', 'instant_bookable', 'cancellation_policy', 'room type',
        'Construction year', 'price', 'service fee', 'minimum nights',
        'number of reviews', 'last review']
        ]  

# substituindo espaços por underline e deixando tudo em minúsculas

df.columns = df.columns.str.replace(' ', '_').str.lower()  

# criando um dataframe com os valores duplicados

df_duplicados = df.duplicated().sum() 


'''
        print para saber o indice de valores duplicados para saber se vale a pena excluir a coluna
        print('% do df composto por valores duplicados:' , round((df.duplicated().sum() / len(df)) * 100, 2))

'''

# removendo os valores duplicados

df.drop_duplicates(inplace=True)  

#analisando a tabela price e service_fee usando loc para separar uma fatia 


df['price'] = df['price'].str.strip(" $").str.replace(',','')
df['price'] = df['price'].astype('Int64')

df['service_fee'] = df['service_fee'].str.strip(" $").str.replace(',','')
df['service_fee'] = df['service_fee'].astype('Int64')

'''
        print(df.loc[5:10, ['price' , 'service_fee']])

        print(df[['price','service_fee']].dtypes)

#analisando as colunas 'construction_year', 'minimum_nights' e 'number_of_reviews'

print(df[['construction_year', 'minimum_nights' , 'number_of_reviews']].dtypes)

'''

#as colunas estão como float 64, mas podem ser usadas como Int64, visto que representam números inteiros


df[['construction_year', 'minimum_nights', 'number_of_reviews']] = df[['construction_year','minimum_nights', 'number_of_reviews']].astype('Int64')

print(df[['construction_year', 'minimum_nights', 'number_of_reviews']].dtypes)



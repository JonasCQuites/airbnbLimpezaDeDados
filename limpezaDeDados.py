import pandas as pd

df_original = pd.read_csv('./dados/Airbnb_Open_Data.csv')
df = df_original.copy()
'''
print(df.shape) # número de linhas e colunas
print(df.dtypes) # tipos de dados de cada coluna
print(df.columns) # número de colunas
print(df.isna().sum()) #soma do número de valores ausentes por coluna
print(df.duplicated().sum()) #soma do número de valores duplicados no dataframe

'''

# Excluindo colunas que não serão utilizadas

print(df[df['license'].isna() == False])
adsaposkdp


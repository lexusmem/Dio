import pandas as pd
import os
# etl - Manipulando dados com panda

# leitura de arquivo csv
# url = 'C:\dados\coord_predio_vertices.csv'
url = (r"C:\Users\lexus\Documents\Estudos\Dio\Formação Python Developer\28 - Fundamentos de ETL (Extract, Transform, Load) com Python\coord_predio_vertices.csv")
df1 = pd.read_csv(url)
print(df1.head())

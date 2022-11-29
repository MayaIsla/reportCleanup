import openpyxl
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os


df = pd.read_csv('C:\\Users\\Downloads\\Acq_Report2.csv')
df2 = df[['Description']]



for x in df['Description']:
    soup = BeautifulSoup(x,features="lxml")
    NewValue = soup.get_text()

for index, row in df2.iterrows():
    df2.columns.str.replace(' ', '')
    df2.loc[index, 'Description'] = [NewValue]

#Mess of df stuff to get the df to print correctly
df3 = df2[['Description']]
df3['Description Summary'] = df3['Description'].str.strip()
df4 = df.merge(df3)
df4 = df4.drop(columns=['Description'])
print(df4)
#Save the df to a csv file
df4.to_csv('C:\\Users\\Downloads\\Acq_Report2.csv', index=False)
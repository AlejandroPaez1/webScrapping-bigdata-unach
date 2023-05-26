#utf-8
import pandas as pd
import requests
from bs4 import BeautifulSoup


# python 3 -m pip install scikit-learn
archivo ="./docs/artes.csv"
df = pd.read_csv(archivo)
print(df.shape[0])

Lcoleccion=[]
listaLink =[]

LisTitle =[]
LisDate =[]
LisMedium =[]
LisReference =[]
lisNumber = []

lista=[]
lista1=[]
lista2=[]
lista3=[]
lista4=[]

url = 'https://www.artic.edu/collection?artist_ids=Jos%C3%A9%20Clemente%20Orozco'
page= requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

for var in soup.find('ul',class_='o-pinboard o-pinboard--2-col@xsmall o-pinboard--2-col@small o-pinboard--3-col@medium o-pinboard--4-col@large o-pinboard--4-col@xlarge').find_all('li')[0:]:
        nombre = var.find('span',class_='m-listing__meta').get_text()
        lista.append(nombre)
        link = var.find_all('a')        

        for nota in link:
                links=nota.get('href')
                listaLink.append(links)

                response = requests.get(links)
                soup = BeautifulSoup(response.content, "html.parser")
                
                dls = soup.find('dl',class_="deflist o-blocks__block")
                #title, date, medium, reference number
                dd_list = dls.find_all('dd')
                title = dd_list[1].text
                # print(title)
                lista1.append(title)

                fecha = dd_list[3].text
                # print(fecha)
                lista2.append(fecha)
                
                medium = dd_list[4].text
                # print(medium)
                lista3.append(medium)
                
                referencia = dd_list[7].text
                # print(referencia)
                lista4.append(referencia)
      



#Titulo,Fecha,Medium,Referencia,Link

Lcoleccion = [valor.replace('\n','').strip() for valor in lista] 
LisTitle = [valor.replace('\n','').strip() for valor in lista1] 
LisDate = [valor.replace('\n','').strip() for valor in lista2] 
LisMedium = [valor.replace('\n','').strip() for valor in lista3] 
LisReference = [valor.replace('\n','').strip() for valor in lista4] 

print(f"el nombre es {Lcoleccion}, {listaLink}")


print("tam de titulo",len(LisTitle))
print("tam de fecha",len(LisDate))
print("tam de medium",len(LisMedium))
print("tam de reference",len(LisReference))
print(len(Lcoleccion))
print(len(listaLink))

df = pd.DataFrame({'Titulo':LisTitle,'fecha': LisDate,'Medium': LisMedium,'Referencia': LisReference,'Link': listaLink,})
df.to_csv(archivo, index=False,encoding = "UTF-8")



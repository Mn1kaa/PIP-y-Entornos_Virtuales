import csv
import re
import matplotlib.pyplot as grafica
list_name_population=list()
def read_csv(path): ##Lee el csv y regresa una lista de diccionarios

  with open(f'./charts/{path}','r')as csvfile:
    reader= csv.reader(csvfile,delimiter=',')
    header=next(reader)
    data=[]
    name_population_dict={}
    

    population=[]
    for row in reader:
      iterable =zip(header,row)
      country_dict= {key: value for key, value in iterable}
      data.append(country_dict)
    
    for diccionario in data:
      
      for key,value in diccionario.items():
        a=0
        if key=="Country/Territory" or re.findall("^[0-9]+",key):
          name_population_dict[key]=value
          c=name_population_dict.copy() #SUMAMENTE IMPORTANTE COPIAR EL DICCIONARIO PORQUE DE LO CONTRARIO GENERA ERROR EN MOEMORIA
          
        
      list_name_population.append(c)

  pais=input("De que pais quieres consultar el crecimiento poblacional")
  for country in list_name_population:
   if country['Country/Territory']== pais:
      print(country['Country/Territory'])
    
      labels=["2022","2020","2015","2010","2000","1990","1980","1970"]
      reverse=list(reversed(labels))
      values=[int(country['2022 Population']),int(country['2020 Population']),int(country['2015 Population']),
      int(country['2010 Population']),int(country['2000 Population']),int(country['1990 Population']),int(country['1980 Population']),int(country['1970 Population'])]## si no usas el int los toma como string
      reverse2=list(reversed(values))

      fig,ax = grafica.subplots()
      ax.bar(reverse,reverse2)
      grafica.savefig(f'./charts/imgs/{pais}.png')
      grafica.close()



      
      ##grafica.show()
   continue

  


  ##print(len(list_name_population)) #Imprimo para cerciorarme que todos los pasies se hayan registrado ya que python no me muestra todos los datos en la terminal no se porque

 
            
  return    'f se guardo tu imagen de {pais}, correctamente =)'

if __name__ == '__main__':
  read_csv()
  
  
 
  
  
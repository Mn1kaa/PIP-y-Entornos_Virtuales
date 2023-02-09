
import Grafic_Country_Generator as grafic


file= input("¿Qué archivo csv quieres leer ?")

try :
    file in f'./charts'
except: 
    "This file doesn't exist in the current directory... Try again"
    



def run():
    grafic.read_csv(file)

if __name__  == '__main__':
    run()
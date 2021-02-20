from pyhunter import PyHunter
from openpyxl import Workbook
import getpass


def Busqueda(organizacion):
    #Cantidad de resultados esperados de la búsqueda
    #El límite MENSUAL de Hunter es 50, cuidado!
    resultado = hunter.domain_search(company = organizacion, limit = 1,emails_type = 'personal')
    return resultado


def GuardarInformacion(datosEncontrados,organizacion):
    libro=Workbook()
    hoja=libro.create_sheet(organizacion)
    libro.save("Hunter" + organizacion + ".xlsx")
    #Agrega el codigo necesario para guardar en formato tabla
    #dentro del libro de Excel, información que consideres relevante
    hoja["B2"]="Correo"
    hoja["B3"]=datosEncontrados["emails"][0]["value"]
    hoja["C2"]="Nombre"
    hoja["C3"]=datosEncontrados["emails"][0]["first_name"]
    hoja["D2"]="Apellido"
    hoja["D3"]=datosEncontrados["emails"][0]["last_name"]
    #de lo obtenido en la búsqueda.
    libro.save("Hunter" + organizacion + ".xlsx")


print("Script para buscar información")
apikey=getpass.getpass("Ingresa tu API key: ")
hunter=PyHunter(apikey)
orga=input("Dominio a investigar: ")
datosEncontrados=Busqueda(orga)
if datosEncontrados==None:
    exit()
else:
    print(datosEncontrados)
    print(type(datosEncontrados))
    GuardarInformacion(datosEncontrados,orga)

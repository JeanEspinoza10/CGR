import requests
import time
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def hacer_get_cada_dos_segundos():
    try:
        url = 'http://52.14.172.100/get'
        # Realizar la solicitud GET
        response = requests.get(url)
        
        # Verificar el estado de la respuesta
        if response.status_code == 200:
            data = response.json()

            if data:
                # Obtenemos el nombre de la aplicacion:
                url = f'https://caupruebas.contraloria.gob.pe/proactivanet/api/Incidents/{data["Id"]}'
                params = {
                    "$fields": "PadCategories_id"
                }
                headers = {
                    'Accept': 'application/json',
                    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb250cmFsb3JpYVxcNjM4NDAiLCJvdnIiOiJmYWxzZSIsImF1dCI6IjAiLCJuYmYiOjE3MTgzNzYyOTYsImV4cCI6MTc0OTkxMjI5NiwiaWF0IjoxNzE4Mzc2Mjk2LCJpc3MiOiJwcm9hY3RpdmFuZXQiLCJhdWQiOiJhcGkifQ.kABrjG2Zf1LsEOjO2LnOR2IqlY0bmq-N7LkbFo9KTg4',
                    'Accept-Language': 'es'
                }

                response = requests.get(url, params=params, headers=headers, verify=False)
                categoria_id = response.json()["PadCategories_id"]

                

                # Obtenemos el nombre de la categoria

                url = "https://caupruebas.contraloria.gob.pe/proactivanet/api/Categories"
                params = {
                    "Id": categoria_id
                }

                response = requests.get(url, params=params, headers=headers, verify=False)

                # Si la solicitud fue exitosa, imprime el contenido de la respuesta
                name_categoria = response.json()[0]["Name"]


                # Ruta al archivo JSON en el directorio actual
                ruta_archivo = './data.json'

                # Abrir y leer el archivo JSON
                with open(ruta_archivo, 'r') as archivo:
                    especialistas = json.load(archivo)            

                
                url = f'https://caupruebas.contraloria.gob.pe/proactivanet/api/Incidents/{data["Id"]}/customFields'
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb250cmFsb3JpYVxcNjM4NDAiLCJvdnIiOiJmYWxzZSIsImF1dCI6IjAiLCJuYmYiOjE3MTgzNzYyOTYsImV4cCI6MTc0OTkxMjI5NiwiaWF0IjoxNzE4Mzc2Mjk2LCJpc3MiOiJwcm9hY3RpdmFuZXQiLCJhdWQiOiJhcGkifQ.kABrjG2Zf1LsEOjO2LnOR2IqlY0bmq-N7LkbFo9KTg4',
                    'Accept-Language': 'es'
                }

                fieldscustom = especialistas[name_categoria]           
                print(fieldscustom)

                # 1
                data = [
                    {
                        "CustomField_id": "EE46B3D2-4C4B-4CEC-8144-E86A5E1F489C",
                        "Value": fieldscustom[0]
                    }
                ]
                response = requests.put(url, headers=headers, json=data,verify=False)

                # 2
                data = [
                    {
                        "CustomField_id": "B6BB775C-73C4-4686-91DD-926A5E9CFA2B",
                        "Value": fieldscustom[1]
                    }
                ]
                response = requests.put(url, headers=headers, json=data,verify=False)


                # 3
                data = [
                    {
                        "CustomField_id": "D7193D42-5FCE-4180-A77A-82E82774AE0C",
                        "Value": fieldscustom[2]
                    }
                ]
                response = requests.put(url, headers=headers, json=data,verify=False)

                
      
        else:
            print(f"Error al realizar la solicitud GET: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    
    # Esperar 2 segundos antes de realizar la próxima solicitud
    time.sleep(2)
    hacer_get_cada_dos_segundos()

# Iniciar la ejecución
hacer_get_cada_dos_segundos()
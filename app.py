from flask import Flask
from flask import  request, jsonify
from controller.webScrapn import agregarCP,modificarCP
from helpers.categories import Categories
from flask_cors import CORS
import os
import json
import requests

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Healtcheck"

post_path = '/campos_personalizados/agregar'
@app.route(post_path, methods=['POST'])
def usuarios_post():
    try:
        data = request.get_json()


        if data:
            campo = data["nombre_cp"]
            valor = data["valor_cp"]
            sistema = data["sistema"]
            name = f"{sistema} / {valor}"
            if len(name) >50:
                print(len(name))
                return jsonify({"error":"reducir tamaño de string"}),400
            
            response = agregarCP(name=campo,valor=name)    

            return jsonify({"mensaje":response})
        else:
            ValueError("colocar los datos")
    except Exception as e:
        return jsonify({"error": str(e)}),400


post_path = '/campos_personalizados/retirar'
@app.route(post_path, methods=['DELETE'])
def usuarios_delete():
    try:
        data = request.get_json()


        if data:
            campo = data["nombre_cp"]
            valor = data["valor_cp"]
            sistema = data["sistema"]
            
            name = f"{sistema} / {valor}"
            
            respose = modificarCP(name=campo,buscar_element=name)    

            return jsonify({"mensaje":respose})
        else:
            ValueError("colocar los datos")
    except Exception as e:
        return jsonify({"error": str(e)}),400

post_path = '/categorias'
@app.route(post_path, methods=['POST'])
def categorias():
    try:

        data = request.get_json()
        categoriesFunctions = Categories()

        sistema = data["sistema"]

        result = categoriesFunctions.addCategorie(nameCategorie = sistema, id_categorie_father ="cf2914f4-0167-40e1-96fb-c075370a77b3")
        result_row = categoriesFunctions.addCategorie(nameCategorie = sistema, id_categorie_father ="80c487df-495e-46cc-891e-81f8bd61d51f")

        return jsonify({
            "mensaje": "cateogiras cargada correctametne"
        })

    except Exception as e :
        return jsonify({"error": str(e)})

post_path ='/webhook'
@app.route(post_path, methods=['POST','GET'])
def webhook():
    try:
        
        data = request.get_json()
    

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

        try:
            response = requests.get(url, params=params, headers=headers,verify=False)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa

            # Si la solicitud fue exitosa, imprime el contenido de la respuesta
            categoria_id = response.json()["PadCategories_id"]
        except requests.exceptions.RequestException as e:
            print(f"Error al hacer la solicitud: {e}")

        # Obtenemos el nombre de la categoria

        url = "https://caupruebas.contraloria.gob.pe/proactivanet/api/Categories"
        params = {
            "Id": categoria_id
        }

        response = requests.get(url, params=params, headers=headers,verify=False)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa

        # Si la solicitud fue exitosa, imprime el contenido de la respuesta
        name_categoria = response.json()["Name"]


        # Nombre de categoria añadimos


        url = f'https://caupruebas.contraloria.gob.pe/proactivanet/api/Incidents/{data["Id"]}/customFields'
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb250cmFsb3JpYVxcNjM4NDAiLCJvdnIiOiJmYWxzZSIsImF1dCI6IjAiLCJuYmYiOjE3MTgzNzYyOTYsImV4cCI6MTc0OTkxMjI5NiwiaWF0IjoxNzE4Mzc2Mjk2LCJpc3MiOiJwcm9hY3RpdmFuZXQiLCJhdWQiOiJhcGkifQ.kABrjG2Zf1LsEOjO2LnOR2IqlY0bmq-N7LkbFo9KTg4',
            'Accept-Language': 'es'
        }
        data = [
            {
                "CustomField_id": "D7193D42-5FCE-4180-A77A-82E82774AE0C",
                "Value": f"{name_categoria} / nombre de especialista"
            }
        ]
            

        # Realizar la solicitud PUT
        response = requests.put(url, headers=headers, json=data,verify=False)

        # Verificar el código de respuesta
        if response.status_code == 200:
            print('Datos actualizados exitosamente.')
        else:
            print(f'Error al actualizar datos. Código de estado: {response.status_code}')
            print(response.text)  # Mostrar la respuesta del servidor en caso de error


        return jsonify({'message': 'Datos guardados correctamente'}), 200


    except Exception as e:
        return jsonify('Error en webhook')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





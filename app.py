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



        url = f'https://celsoalexdiaz.proactivanet.com/panet/api/Incidents/{data["Id"]}/customFields/3454d179-bf74-47a4-bfbe-0a9ed77f0543'

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqZWFuLmVzcGlub3phQHNvbHV0aW9udGVjaC5jb20ucGUiLCJvdnIiOiJmYWxzZSIsImF1dCI6IjAiLCJuYmYiOjE3MTcwNDU2ODMsImV4cCI6MTc0ODU4MTY4MywiaWF0IjoxNzE3MDQ1NjgzLCJpc3MiOiJwcm9hY3RpdmFuZXQiLCJhdWQiOiJhcGkifQ.QAUcqs1DJjBcQW59diOINBWvndnZob3-KS-2t2F9ahA',
            'Accept-Language': 'es'
        }

        data = {
            'Value': '2'
        }

        # Realizar la solicitud PUT
        response = requests.put(url, headers=headers, json=data)

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





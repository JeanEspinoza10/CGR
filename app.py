from flask import Flask
from flask import  request, jsonify
from controller.webScrapn import agregarCP,modificarCP
from helpers.categories import Categories
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


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
        return jsonify(data)
    except Exception as e:
        return jsonify('Error en webhook')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





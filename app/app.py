
from flask import Flask
from flask_restful import Resource, Api

from flask import jsonify, Blueprint, request
from datetime import datetime

from database import setup, datos

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

setup.create_table() #crea la tabla

class Insertar(Resource):
    def post(self):
        lugar = request.json['lugar'].upper()
        especie = request.json['especie'].upper()
        avist = request.json['avistamiento'].upper()

        pais = request.json['pais'].upper()
        dep = request.json['departamento'].upper()
        ciudad = request.json['ciudad'].upper()

        nombre_cientifico = request.json['nombrecientifico'].upper()
        latitub = request.json['latitub'].upper()
        longitub = request.json['longitub'].upper()
        autor = request.json['autor'].upper()
        nota = request.json['nota'].upper()

        reino = request.json['reino'].upper()
        filo = request.json['filo'].upper()
        clase = request.json['clase'].upper()
        orden = request.json['orden'].upper()
        familia = request.json['familia'].upper()
        genero = request.json['genero'].upper()
        
        nombre_comun = request.json['nombre_comun'].upper()

        created_date = datetime.now().strftime("%x") #mes/dia/año    
        created_time = datetime.now().strftime("%H/%M/%S") #Tiempo /hour/min/seg

        id = datos.insert_data_esp_marinas(lugar, especie, avist, created_date, created_time)
        id_2 = datos.insert_data_lugares(id, pais, dep, ciudad, lugar)
        id_3 = datos.insert_data_avistamiento(id, nombre_cientifico, lugar, latitub, longitub, autor, nota)
        id_4 = datos.insert_data_cat_taxonomica(id,reino,filo,clase,orden,familia,genero,especie)
        id_5 = datos.insert_data_especies(id, nombre_comun, nombre_cientifico, especie)
        print(f'Id insertado {id_2}')

        return {"resouesta": f"{id}, {id_2},{id_3} {id_4 }, {id_5}"}

class Eliminar(Resource):
    def delete(self):
        id = int(request.json['id'])
        print(f'{type(id)} y el valor = {id}')
        eliminado = datos.delete_especies(id)
        datos.delete_cat_taxonomica(id)
        datos.delete_avistamientos(id)
        datos.delete_lugares(id)
        datos.delete_especies_marinas(id)
        return {f"eliminado": f"correcto {eliminado}"}

class Actualizar(Resource):
    def put(self):
        id = int(request.json['id'])
        lugar = request.json['lugar'].upper()
        especie = request.json['especie'].upper()
        avist = request.json['avistamiento'].upper()

        pais = request.json['pais'].upper()
        dep = request.json['departamento'].upper()
        ciudad = request.json['ciudad'].upper()

        nombre_cientifico = request.json['nombrecientifico'].upper()
        latitub = request.json['latitub'].upper()
        longitub = request.json['longitub'].upper()
        autor = request.json['autor'].upper()
        nota = request.json['nota'].upper()

        reino = request.json['reino'].upper()
        filo = request.json['filo'].upper()
        clase = request.json['clase'].upper()
        orden = request.json['orden'].upper()
        familia = request.json['familia'].upper()
        genero = request.json['genero'].upper()
        
        nombre_comun = request.json['nombre_comun'].upper()

        created_date = datetime.now().strftime("%x") #mes/dia/año    
        created_time = datetime.now().strftime("%H/%M/%S") #Tiempo /hour/min/seg



        datos.update_data_esp_marinas(id,lugar,especie,avist, created_date, created_time)
        datos.update_data_lugares(id,pais,dep,ciudad,lugar)
        datos.update_data_avistamiento(id, nombre_cientifico, lugar, latitub, longitub, autor, nota)
        datos.update_data_cat_taxonomica(id,reino,filo,clase,orden,familia,genero,especie)
        datos.update_data_especies(id, nombre_comun, nombre_cientifico, especie)
        return {"id":f"{id}"}

class Consulta_avistamiento(Resource):
    def get(self, especie):
        print(f'{type(especie)} - {especie}')
        data = datos.consulta_especies(especie)
        if data:
            return jsonify({"datos":data})
        return{"messages":"Error"}
#Rutas de las Apis
api.add_resource(Insertar,"/insertar") #http://127.0.0.1:5000/insertar
api.add_resource(Eliminar,"/eliminar") #http://127.0.0.1:5000/eliminar
api.add_resource(Actualizar,"/actualizar") #http://127.0.0.1:5000/actualizar
api.add_resource(Consulta_avistamiento, "/consulta/<string:especie>")#http://127.0.0.1:5000/consultar/nombre

if __name__ == '__main__':
    app.run(debug=True)
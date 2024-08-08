from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from

from services.converter import Converter

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class RetrievePerson(Resource):
    @swag_from('swagger3.yml')
    def post(self):
        # Obtener datos del cuerpo de la solicitud
        data = request.get_json() 
        # Validar los datos de la solicitud (esto se puede mejorar con validaciones adicionales)
        if 'PersonIdentification' not in data:
            return jsonify({
                "status_code": "400",
                "status": "BadRequest",
                "message": "Missing PersonIdentification in request"
            }), 400        
        internal_data = Converter.request_to_internal_3(data)
        #aqui vendria la respuesta de una api externa se entra a simular
        internal_response = {
            "documentType": internal_data['documentType'],
            "documentNumber": internal_data['documentNumber'],
            "given_name": "Javier",
            "middle_name": "Salazar",
            "mobile_phone_number": "123456789",
            "personal_email_address": "obusxavo@gmail.com"
        }
        response = Converter.internal_to_response_3(internal_response)
        return jsonify(response)
    
class RetrievePersonAccount(Resource):
    @swag_from('swagger1.yml')
    def post(self):
        # Obtener datos del cuerpo de la solicitud
        data = request.get_json() 
        # Validar los datos de la solicitud (esto se puede mejorar con validaciones adicionales)
        if 'PersonIdentification' not in data:
            return jsonify({
                "status_code": "400",
                "status": "BadRequest",
                "message": "Missing PersonIdentification in request"
            }), 400
        internal_data = Converter.request_to_internal_1(data)
        #aqui vendria la respuesta de una api externa se entra a simular
        internal_response = {
            "id_cuenta": "123456789",
            "tipo_moneda": "USD"
        }
        response = Converter.internal_to_response_1(internal_response)
        return jsonify(response)
    
class RetrieveAccount(Resource):
    @swag_from('swagger2.yml')
    def post(self):
        # Obtener datos del cuerpo de la solicitud
        data = request.get_json() 
        # Validar los datos de la solicitud (esto se puede mejorar con validaciones adicionales)
        if 'Account' not in data:
            return jsonify({
                "status_code": "400",
                "status": "BadRequest",
                "message": "Missing PersonIdentification in request"
            }), 400        
        internal_data = Converter.request_to_internal_2(data)
        #aqui vendria la respuesta de una api externa se entra a simular
        internal_response = {
            "numero_cuenta": internal_data['numero_cuenta'],
            "tipo_moneda_cuenta": "USD",
            "estado_cuenta": "active",
            "tipo_cuenta": "saving"
        }
        response = Converter.internal_to_response_2(internal_response)
        return jsonify(response)


api.add_resource(RetrievePerson, '/employee-data-management/v1.0/retrieve')
api.add_resource(RetrievePersonAccount, '/savings-account/v1.0/initiate')
api.add_resource(RetrieveAccount, '/savings-account/v1.0/retrieve')

if __name__ == '__main__':
    app.run(debug=True)
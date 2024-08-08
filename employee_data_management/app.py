from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from

from services.converter import Converter

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class RetrievePerson(Resource):
    @swag_from('swagger.yml')
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

        
        internal_data = Converter.request_to_internal(data)

        #aui vendria la respuesta de una api externa se entra a simular
        internal_response = {
            "documentType": internal_data['documentType'],
            "documentNumber": internal_data['documentNumber'],
            "given_name": "Javier",
            "middle_name": "Salazar",
            "mobile_phone_number": "123456789",
            "personal_email_address": "obusxavo@gmail.com"
        }

        response = Converter.internal_to_response(internal_response)

        return jsonify(response)

api.add_resource(RetrievePerson, '/employee-data-management/v1.0/retrieve')

if __name__ == '__main__':
    app.run(debug=True)
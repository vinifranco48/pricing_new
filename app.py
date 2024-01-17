from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import joblib 
import pandas as pd
from flasgger import Swagger, swag_from
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
modelo = joblib.load('modelo_treinado2.joblib')
CORS(app)
swagger = Swagger(app)

class Pricing(Resource):
   
    @swag_from('swagger/predict.yml')
    def post(self):
        
        try:
            args = request.get_json(force=True)

            if not isinstance(args, dict):
                return jsonify({'error': 'Entrada inválida'})

            input_df = pd.DataFrame(args, index=[0])

            expected_columns = ['product_name_lenght', 'product_description_lenght', 'product_photos_qty',
                                'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm',
                                'product_category_name']
            if not set(input_df.columns) == set(expected_columns):
                return jsonify({'error': 'Colunas incorretas no DataFrame'})

            predict = modelo.predict(input_df)[0]

            return jsonify({'previsao': float(predict)})

        except Exception as e:
            return jsonify({'error': f'Erro durante a previsão: {str(e)}'})
    

api.add_resource(Pricing, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
# Precificação com Machine Learning
## README
Este repositório contém uma aplicação Flask para precificação de produtos utilizando um modelo de machine learning. A aplicação foi containerizada com Docker para facilitar a reprodução em diferentes ambientes.

## Estrutura do Projeto
O projeto está organizado da seguinte forma:
- Dockerfile: Define a construção da imagem Docker para a aplicação.
- requirements.txt: Lista as dependências necessárias para a aplicação, que são instaladas durante a construção da imagem Docker.
- app.py: O arquivo principal que contém a aplicação Flask e a lógica para predição de preços.
- modelo_treinado2.joblib: O modelo treinado utilizado para fazer previsões.
## Como Executar
Certifique-se de ter o Docker instalado em seu ambiente. Para construir e executar a aplicação, siga os passos abaixo:

1. Clone este repositório:

 ```
git clone https://github.com/vinifranco48/pricing_new.git
 ```

 Construa a imagem Docker:
 
   ```
   docker build -t api_model
   ``` 

 Execute a aplicação:
 ```
docker run -p 5000:5000 api_model
 ```
## Utilização da API
A API expõe um endpoint para fazer previsões de preços. Envie uma solicitação POST para http://localhost:5000/predict com os dados necessários no formato JSON. Veja o arquivo swagger/predict.yml para detalhes sobre a estrutura da solicitação.

Exemplo de solicitação usando cURL:

```
curl -X POST -H "Content-Type: application/json" -d '{"product_name_length": 10, "product_description_length": 150, "product_photos_qty": 3, "product_weight_g": 500, "product_length_cm": 20, "product_height_cm": 10, "product_width_cm": 15, "product_category_name": "lazer_esporte"}' http://localhost:5000/predict

```

## Observações
Certifique-se de ter todas as dependências listadas em requirements.txt instaladas em seu ambiente antes de construir a imagem Docker.

Este projeto utiliza o Gunicorn como servidor web para a aplicação Flask.

O arquivo modelo_treinado2.joblib é necessário para fazer previsões e deve ser fornecido ou treinado antes de executar a aplicação.

Este é um guia básico para começar com a aplicação. Sinta-se à vontade para personalizar conforme necessário e explorar mais funcionalidades do Flask e Docker.

FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia os arquivos do projeto para o diretório de trabalho
COPY . /app



# Define o diretório de trabalho como /app
WORKDIR /app

# Expõe a porta em que a aplicação Flask estará rodando
EXPOSE 5000

# Comando para iniciar a aplicação quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


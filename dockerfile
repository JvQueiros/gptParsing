FROM python:3.13.0

# Define o diretório de trabalho
WORKDIR /

# Copia os arquivos para o container
COPY uploads/ .
COPY requirements.txt .
COPY . /garantiasia
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta onde o Flask vai rodar
EXPOSE 8000

# Executa o Gunicorn
WORKDIR /garantiasia
CMD ["uvicorn", "main:app", "--reload"]
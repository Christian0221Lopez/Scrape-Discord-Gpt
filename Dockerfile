FROM python

WORKDIR /main

# Copiar todos los archivos al directorio de trabajo
COPY . .

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]


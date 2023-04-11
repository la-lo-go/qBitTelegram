FROM python:3.12.0a7-slim-bullseye

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [“python”, “./main.py”] 

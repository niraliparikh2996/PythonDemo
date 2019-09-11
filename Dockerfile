FROM rajivmehtajs/pythonbox:v0

RUN apt-get update

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

COPY . .

# RUN python app/server.py

EXPOSE 5000

CMD ["python", "server.py", "serve"]

# CMD ["python", "server.py"]

FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python ./scripts/create_db.py
RUN python ./scripts/populate_db.py

CMD [ "python", "./scripts/create_db.py" ]
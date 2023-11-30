FROM python:3

ARG PORT

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python ./scripts/create_db.py
RUN python ./scripts/populate_db.py

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server:app"]
FROM python:3

ENV TOKEN=""

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]
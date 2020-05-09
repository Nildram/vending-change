FROM tiangolo/meinheld-gunicorn-flask:python3.8

COPY ./change_calculator /app/change_calculator
COPY ./static /app/static
COPY ./rest.py /app/main.py
COPY ./requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt


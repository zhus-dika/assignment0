FROM ubuntu

RUN apt-get update && apt-get install -y git python3 python3-pip

ADD requirements.txt /requirements.txt

ADD README.md /README.md

RUN pip install -r requirements.txt

ADD print_hello /bin/print_hello

RUN chmod +x /bin/print_hello

ARG uid

RUN useradd deploy2022user

WORKDIR /home/deploy2022user

USER deploy2022user

ADD main.py /home/deploy2022user/main.py

CMD ["uvicorn", "--host", "--port", "8898", "0.0.0.0", "main:app"]

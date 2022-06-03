FROM deeppavlov/base-gpu:0.12.1

ARG CONFIG
ARG COMMIT=0.13.0
ARG PORT

ENV CONFIG=$CONFIG
ENV PORT=$PORT

COPY . /src
RUN pip install -r /src/requirements.txt

WORKDIR /src

CMD gunicorn --workers=1 --timeout 500 --graceful-timeout 500 server:app -b 0.0.0.0:3555

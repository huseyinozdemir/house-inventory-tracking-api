FROM python:3.7.3-alpine
MAINTAINER Medglobal

# Bu, Python'a Docker kapsayıcılarında Python çalıştırırken önerilen arabelleğe alınmamış modda çalışmasını söyler.
# Bunun nedeni Python'un çıktıları tamponlamasına izin vermemesidir.
# Sadece doğrudan onları yazdırır.
ENV PYTHONUNBUFERRED 1

# Gereksinimlerin yuklenmesi
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# uygulamaları çalıştıracak kullanıcıyı oluşturalım.
RUN adduser -D user
	

FROM python:3

RUN useradd -ms /bin/sh -u 1001 app

USER app

WORKDIR /var/www/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . .

CMD python src/app.py

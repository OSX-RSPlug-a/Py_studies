FROM python:3.11-slim

WORKDIR /app

SHELL ["/bin/bash", "-c"]

EXPOSE 5000

STOPSIGNAL SIGTERM

ONBUILD COPY requiments.txt /app/
ONBUILD RUN pip install -r requiments.txt
ONBUILD COPY . /app

HEALTHCHECK --interval=30s --timeout=5s \
            --retries=3 CMD curl --fail \
            http://localhost:5000/ || exit 1

CMD ["python", "app.py"]

FROM PYTHON:3.9

WORKDIR /app/

COPY . /app/

COPY requirements.txt /app/requirements.txt

COPY entrypoint.sh /app/entrypoint.sh

RUN sudo apt update -y && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["sh", "/app/entrypoint.sh"]

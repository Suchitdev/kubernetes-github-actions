FROM python:3.13

RUN useradd -m appuser

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

USER appuser

CMD ["python","app.py"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
CMD curl --fail http://localhost:5000/ || exit 1
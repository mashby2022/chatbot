FROM python:3.9.13
WORKDIR /ML-tests
COPY ./requirements.txt /ML-tests/requirements.txt
RUN pip install --no-cache-dir --upgrade -r/ML-tests/requirements.txt
COPY . .
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "7860", "app:app"]
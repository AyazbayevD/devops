FROM python:3.9-slim-buster
WORKDIR .
COPY pyproject.toml .
COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
EXPOSE 5000
CMD ["poetry", "run", "python", "main.py"]
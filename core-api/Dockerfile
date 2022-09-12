FROM python:3.9-slim

RUN apt-get update

# --- VirtualEnv Configuration ---
RUN python3.9 -m venv /home/core/venv
ENV PATH="/home/core/venv/bin:$PATH"

# --- Requirements Installation ---
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir /home/core/code
WORKDIR /home/core/code
COPY . .

ENV VIRTUAL_ENV=/home/core/venv

# --- Run WSGI ---
CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]

FROM python:3.9-slim

RUN apt-get update

# --- VirtualEnv Configuration ---
RUN python3.9 -m venv /home/auth/venv
ENV PATH="/home/auth/venv/bin:$PATH"

# --- Requirements Installation ---
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir /home/auth/code
WORKDIR /home/auth/code
COPY . .

ENV VIRTUAL_ENV=/home/auth/venv

# --- Run WSGI ---
CMD ["hypercorn","-b", "0.0.0.0:5050", "main:app"]

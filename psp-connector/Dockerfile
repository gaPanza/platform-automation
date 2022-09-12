FROM python:3.9-slim

RUN apt-get update

# --- VirtualEnv Configuration ---
RUN python3.9 -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

# --- Requirements Installation ---
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir /home/myuser/code
WORKDIR /home/myuser/code
COPY . .

ENV VIRTUAL_ENV=/home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

# --- Run APP ---
CMD ["python", "main.py"]

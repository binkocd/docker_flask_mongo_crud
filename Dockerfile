# Define OS.
FROM python:alpine 

# Configure working directory.
WORKDIR /app

# Copying pip requirements.
COPY requirements.txt /app

# Installing python/pip dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copying project files.
COPY ["server.py", "/app"]

# Exposing an internal port.
EXPOSE 5001

# Command to get flask app running.
CMD ["python3", "./server.py"]
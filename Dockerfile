  FROM python:3.9

  ENV PYTHONBUFFERED=1
  WORKDIR /application

  # Install necessary packages and dependencies
  RUN apt-get update --yes --quiet \
    && apt-get install -y build-essential curl \
    && curl -sL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs --no-install-recommends \
    && apt-get install -y ffmpeg


  COPY wait-for-db.sh /application/wait-for-db.sh
  RUN chmod +x /application/wait-for-db.sh
  # Install Python dependencies
  COPY requirements.txt requirements.txt
  RUN python3 -m pip install --upgrade pip
  RUN python3 -m pip install setuptools~=57.5.0
  RUN python3 -m pip install -r requirements.txt

  # Copy application code
  COPY . .

  # Collect static files
  RUN python3 manage.py collectstatic --no-input

  # Create an entrypoint script to run multiple commands
  COPY entrypoint.sh /application/entrypoint.sh
  RUN chmod +x /application/entrypoint.sh

ENV PYTHONUNBUFFERED=1

  # Set entrypoint
  ENTRYPOINT ["/application/entrypoint.sh"]

# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project files into the Docker image
COPY . /code/

# Collect static files (if any)
RUN python manage.py collectstatic --noinput

# Copy entrypoint script
COPY entrypoint.sh /code/

# Make entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]

# Default command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Use the official Python image as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirement.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirement.txt

# Copy the Django project files to the working directory
COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]

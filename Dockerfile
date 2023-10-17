# Use the official Python 3 image as the base
FROM python:3-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install the application dependencies
RUN pip install -r requirements.txt

# Copy the entire "Modules" directory along with your other application files
COPY Modules/ /app/Modules/
COPY main.py sources.json /app/

# Define the command to be executed when the container starts
CMD ["python", "main.py"]

# Use an official Python image as a base
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY app.py /app/
COPY hangman.py /app/
COPY wordle.py /app/
COPY words.py /app/

# Expose the port your server is listening on
EXPOSE 12345

# Run the Python script
CMD ["python", "app.py"]

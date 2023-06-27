FROM python:3.12.0a7-slim-bullseye

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Move to the source directory
WORKDIR /src

# Copy the source code from the working directory 
COPY /src .

# Run the application
CMD ["python", "/src/main.py"] 

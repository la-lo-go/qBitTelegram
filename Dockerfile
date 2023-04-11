FROM python:3.12.0a7-slim-bullseye

# Set the environment variables
ENV QBIT_HOST=XXX.XXX.X.XXX
ENV QBIT_PORT=XXXX
ENV QBIT_USERAME=username
ENV QBIT_PASS=password
ENV TELEGRAM_TOKEN=XXXXX:XXXXX-XXXXXXXXXXX
ENV ADMINS='["usernam_admin1", "usernam_admin2"]'

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Move to the source directory
WORKDIR /src

# Copy the source code from the working directory 
COPY . .

# Run the application
CMD [“python”, “./main.py”] 

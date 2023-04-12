FROM python:3.12.0a7-slim-bullseye

# Optionaly you can change here the values of the environment
# variables (read the README file for more information)
ENV QBIT_HOST=XXX.XXX.X.XXX
ENV QBIT_PORT=XXXX
ENV QBIT_USERAME=admin
ENV QBIT_PASS=admin
ENV TELEGRAM_TOKEN=XXXXX:XXXXX-XXXXXXXXXXX
ENV ADMINS=username_admin1,username_admin2

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Move to the source directory
WORKDIR /src

# Copy the source code from the working directory 
COPY /src .

# Run the application
CMD ["python", "/src/main.py"] 

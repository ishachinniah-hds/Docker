# Use the official Python image as the base image
FROM python:3.9
 
# RUN mkdir -p /
# Set the working directory in the container
# WORKDIR /
 
# Copy the files into the container
COPY ./* /
# Copy the requirements file into the container
#COPY requirements.txt requirements.txt
 
# Install dependencies
RUN pip install --no-cache-dir -r /requirements.txt

RUN chmod +x openlit.sh

ENTRYPOINT /openlit.sh
 
# Copy the rest of the application code into the container
#COPY . .
 
# Expose the port your application listens on
#EXPOSE 8000
 
# Define the command to run when the container starts
CMD ["python3", "app.py"]
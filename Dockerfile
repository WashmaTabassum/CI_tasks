#use an official python runtime as a parent image
FROM python:3.10-slim
#set the working directory in the container
WORKDIR /app
#intall python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
#copy the current directory content into the container at /app
COPY . .
#make port 7860 available to the world outside this container
EXPOSE 7860
#run the application
CMD ["python", "-u", "ui.py"]
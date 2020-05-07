FROM mongo:latest

# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install Django
RUN pip3 install pymongo
RUN pip3 install requests

EXPOSE 27017
EXPOSE 8080
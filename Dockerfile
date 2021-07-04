FROM python:latest 

ADD ./requirements.txt .  
RUN pip3 install -r requirements.txt 
RUN mkdir src 
ADD ./srcsrc /src 
WORKDIR src 


 

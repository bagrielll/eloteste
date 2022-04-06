FROM python:3.8-alpine
COPY . /eloteste 
WORKDIR /eloteste
RUN pip install -r requirements.txt
EXPOSE 3000
ENTRYPOINT [ "python" ]
CMD ["main.py" ]
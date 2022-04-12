FROM python:3.8-alpine
COPY . /eloteste/sonda
WORKDIR /eloteste/sonda
RUN pip install -r sonda/requirements.txt
EXPOSE 3000
ENTRYPOINT [ "python" ]
CMD ["sonda/main.py" ]
FROM  httpd:2.4

WORKDIR /home/ubuntu/.ssh/k8syaml/

COPY . .

EXPOSE 3000

CMD [ "httpd","index.html" ]
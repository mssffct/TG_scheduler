FROM node:16

WORKDIR /app/

RUN apt-get update

COPY ./tg-scheduler/package*.json /app/

RUN npm install --force

COPY ./tg-scheduler /app/

RUN npm run build

WORKDIR /var/www/html/
RUN rm -rf /var/www/html/*


RUN rm -rf /etc/nginx/sites-enabled/
COPY nginx/nginx.conf /etc/nginx/sites-enabled/default

RUN cp -r /app/dist/* /var/www/html

CMD ["nginx", "-g", "daemon off;"]
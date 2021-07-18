FROM node:lts-alpine

WORKDIR /nodes

COPY ./nodes/package.json /nodes/package.json
COPY ./nodes/package-lock.json /nodes/package-lock.json
RUN npm install
RUN npm install axios

COPY ./nodes /nodes

CMD npm run serve
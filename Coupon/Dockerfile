FROM node:12-alpine
LABEL 'Maintainer' 'Mubashir AR'
WORKDIR /app
COPY ./package.json .
RUN cat package.json
RUN npm install
RUN ls node_modules
RUN npm install -g nodemon
COPY . .
CMD ls node_modules && npm start
# syntax=docker/dockerfile:1

# base image
FROM node:16.17.1

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY ./package.json /app/package.json
RUN npm install
RUN npm install @vue/cli -g

# copy files
COPY . /app 

CMD ["npm", "run", "serve" ]

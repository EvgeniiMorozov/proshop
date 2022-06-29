FROM node:16.14.0-alpine

WORKDIR /usr/src/app

COPY package.json ./
#COPY package-lock.json ./
RUN npm install  --legacy-peer-deps react-paypal-button-v2

COPY . ./

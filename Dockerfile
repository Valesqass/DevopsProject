FROM node:lts

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV PORT=6000

EXPOSE 6000

CMD ["npm", "start"]
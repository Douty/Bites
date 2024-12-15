FROM node:22-alpine


WORKDIR /app/firebase-emulator

COPY firebase.json ./
COPY .firebaserc ./

RUN npm install -g firebase-tools

EXPOSE 9099

CMD ["firebase", "emulators:start"]
# Specify a base image
FROM node:16-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY ./frontend/package.json ./frontend/package-lock.json* /app/
RUN npm install --production

# Bundle app source
COPY ./frontend /app/

# Expose port and start application
EXPOSE 3000
CMD ["npm", "start"]
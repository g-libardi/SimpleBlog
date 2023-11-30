# Use an official Node.js image as a parent image
FROM node:current-alpine as builder

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Build the production-ready static files
RUN npm run build

# Use a smaller image for serving the application
FROM nginx:alpine

# Copy the built files from the builder stage to the nginx server
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose the port that the nginx server will run on
EXPOSE 80

# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]
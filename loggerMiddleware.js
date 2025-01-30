const express = require('express');
const app = express();

// Middleware function to log requests
app.use((req, res, next) => {
  console.log(`Received a ${req.method} request to ${req.url}`);
  next(); // Call next() to move to the next middleware or route handler
});

// Middleware function to check if the request contains a specific header
app.use((req, res, next) => {
  if (req.headers.authorization) {
    console.log('Authorization header present');
  } else {
    console.log('Authorization header not present');
  }
  next();
});

// Route handler
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Starting the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

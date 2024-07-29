// Assuming `connection` is your already established MySQL connection
const express = require('express');
const app = express();

app.get('/markers', (req, res) => {
  const query = 'SELECT * FROM locations'; // Replace with your actual query
  connection.query(query, (error, results) => {
    if (error) {
      console.error('Error fetching data:', error);
      res.status(500).send('Server error');
    } else {
      res.json(results);
    }
  });
});

const port = 3000; // Or your desired port
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

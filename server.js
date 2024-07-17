const express = require('express');
const fs = require('fs');
const app = express();
const port = process.env.PORT || 3000;

app.get('/data', (req, res) => {
  fs.readFile('data.json', (err, data) => {
    if (err) throw err;
    res.json(JSON.parse(data));
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

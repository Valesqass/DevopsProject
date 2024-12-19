const express = require('express');
const app = express();
const port = process.env.PORT || '6000';

app.get('/', (req, res) => {
    res.json({message: "docker c'est facile"})
})

app.listen(port, () => {
    console.log(`App is listening on port : ${port}`);
});
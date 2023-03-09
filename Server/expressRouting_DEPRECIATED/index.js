const express = require('express');
const cors = require('cors');
const path = require('path');
const bodyParser = require('body-parser');
const ClientFolderPath = path.resolve('./Client');
const {initRoutes} = require('./initRoutes')


const app = express();
app.use(express.json())
app.use(cors());
app.use(express.static(ClientFolderPath));
app.use(bodyParser.urlencoded());

initRoutes(app);

const port = process.env.PORT || 3002;
app.listen(port, () => {
    console.log('server listening on port 3002')
})

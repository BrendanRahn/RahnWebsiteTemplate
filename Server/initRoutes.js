const path = require('path');
const ClientFolderPath = path.resolve('./Client');
const {validateLogin} = require('./src/controllers/loginController')

function initRoutes (app) {

    console.log(path.resolve('./'))


    //change default ( / ) to webpage name when web server is implemented
    app
        .route('/login')
        .get((req, res) => {
            res.sendFile(path.join(ClientFolderPath, 'loginPage.html'))
        })
        .post((req, res) => {
            if (validateLogin(req, res) == true) {
                res.status(200).send({message: 'valid-login'})
            } else {
               res.status(401).send({message: 'invalid-login'})
            }
        });

    app
        //have to handle auth here otherwise you can bypass it entirely
        //have authIsVaild variable(s) in controller and set to true when login is passed
        //if false redirect to login
        .route('/home')
        .get((req, res) => {
            res.sendFile(path.join(ClientFolderPath, 'homePage.html'))
        });

    app
        .route('/')
        .get((req, res) => {
            res.send("LEDLE")
        });
}

module.exports = {
    initRoutes
}
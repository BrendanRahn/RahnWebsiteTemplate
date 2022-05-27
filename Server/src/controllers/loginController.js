
function decryptLogin(encryptedData) {

    //TODO: implement login decryption

    return(encryptedData)


}

function validateLogin(req, res) {

    let encryptedData = req.body;

    let loginData = decryptLogin(encryptedData);

    //if database were implemented would check username against database record
    if (loginData.username == 'admin' && loginData.password == 'admin') {
        return true
    }

    return false


}

module.exports = {
    validateLogin
}
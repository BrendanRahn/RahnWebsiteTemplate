function handleLogin() {

    let loginData = {
        username: document.getElementById('usernameInputField').value,
        password: document.getElementById('passwordInputField').value
    }

    let encryptedData = loginDataEncrypt(loginData);


    console.log(encryptedData);
    fetch('/login/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(encryptedData)
    })
    
    .then((res) => {
        return res.json(res)
    })
    //explain what this handles
    .then((resData) => { 
        if (resData.message == 'valid-login') {
            window.location.href = 'http://localhost:5000/'
        } else if (resData.message == 'invalid-login') {
            document.getElementById('invalidLoginDiv').style.display = 'block';
            
        }
        
    })
 
    
}

//in reality function would not be named so obviosuly 
function loginDataEncrypt (loginData) {

    //TODO: implement data encryption

    return(loginData);

}

function formSubmissionSuccess() {

    console.log("form submitted :)")
}
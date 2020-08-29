window.onload = () =>{
    // used to display and hide nave bar
    let askBtn = document.getElementById('submitQuestion');
    let chatArea = document.getElementById('chatArea');
    chatArea .append('Hello, Is there anything I can help you with? ');

    askBtn.onclick = () => {
        let question = document.getElementById('yourQ').value;
        if(!question)
            return;
        else
            chatArea.append('\n' + question);
        document.getElementById('yourQ').value = '';
    
        const reqOptions = {
            method:'GET',
            query: JSON.stringify(question)
        };
        // continued conversation
        fetch('http://127.0.0.1:5000/convo?question='+question, reqOptions).then((response)=>{
                return response.text();
            }).then((res) => {
                chatArea.append('\n' + res);
            }).catch((err)=>{
                console.log('Error fetching path /hello \n', err);
            });
        
    
    }

    let mailbtn = document.getElementById('sendMail');
    mailbtn.onclick = () =>{
        mailbtn.href += '&body='+document.getElementById('lname').value + ', ' + document.getElementById('fname').value
        + '\n' + document.getElementById('email').value
        + '\n' +document.getElementById('mail_txt').value;
        
        console.log(mailbtn.href);
    }

}
/*
    setUserOnServer(){
        return new Promise((resolve, reject) => {
            const reqOptions = {
                method:'GET',
                headers: { 'Content-Type': 'application/json' },
                params: JSON.stringify(this.state.username)
            };
    
            fetch('/setUser/'+this.state.username,reqOptions).then((response)=>{
                console.log("User is set ", response);
                if(response.status === 200)
                    return response.json();
                reject(false);

            }).then((data)=>{
                console.log('Received list ', data);
                resolve(data);
            }).catch((err)=>{
                console.log('Error on setUser: ',err);
                reject(false);

            });

        })
    }
*/

/*

            <section id="Questions" class="main-section">
            
                <div class='chat'>
                    <textarea id='chatArea' class='conversation' readonly>
                        <div class='chat-container'>
                            <p> Hello there, anything I can help with? </p>
                            
                        </div>
                    </textarea>

                    <div>   
                        <label for='yourQ'> Got a Question: </label>
                        <input id='yourQ'></input>
                        <button id='submitQuestion' type='submit'> Ask Away </button>
                    </div>
                </div>
                
            </section>
*/
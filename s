			function loadChat() {
  ajaxGetRequest("/chat", renderChat);
}


function renderChat(jsonData){
  let newline = "<br>";
  let chat = "";
  let chatDiv = document.getElementById("chat");
  let messages = JSON.parse(jsonData);
  for (let messageObj of messages) {
    chat = chat + messageObj["message"] + newline;
  }
  chatDiv["innerHTML"] = chat;
}

function sendMessage(){
  let age = document.getElementById("age")
  // Get the message and let the user "know" it was
  // sent by making the textbox be blank
  let message = age["value"];
  age.value = "";
  let toSend = {"message": message};
  jsonBlob = JSON.stringify(toSend);
  ajaxPostRequest("/send", jsonBlob)

}

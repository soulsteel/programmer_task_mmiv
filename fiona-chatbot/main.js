function printLetterByLetter(destination, message, speed){
    var i = 0;

    let resDiv = document.getElementById(destination);
    const p = document.createElement("p");
    resDiv.appendChild(p);

    var interval = setInterval(function(){
        //let resDiv = document.getElementById(destination).innerHTML += message.charAt(i);
        p.innerHTML += message.charAt(i);

        i++;
        if (i > message.length){
            clearInterval(interval);
        }
    }, speed);
}

const form = document.querySelector("#chat-form");

async function sendData() {
    const response = await fetch("/processUserInput.php", {

    });

    const result = await response.json();
    printLetterByLetter("result", result.data, 100);

}

form.addEventListener("submit", (event) => {
    event.preventDefault();
    sendData();
});

// main.js

const logFile = "Server.log";
const logElement = document.getElementById("log");

  fetch(logFile)
    .then(response => response.text())
    .then(logText => {
      const logLines = logText.split("\n");
      const logHTML = logLines.map(line => `<p>${line}</p>`).join("");
      logElement.innerHTML = logHTML;
    })
    .catch(error => {
      console.error(`Error reading log file: ${error}`);
      logElement.innerText = "Error reading log file.";
    });
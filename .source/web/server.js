const CHECKED_CLASS = 'checked';
const CLICK_CLASS = 'clicked';
const HIDDEN_CLASS = 'hidden';
const LOG_CLASSES = ["info", "warn", "error"];
window.lastcommand = '';
window.enablescroll = 1;


const initialize = async () => {
    window.load = await eel.windowLoad()();
    document.title = (window.load.serverName);
    await console_display();
}

if (document.readyState === "loading") {
    process = 0
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }

async function console_display() {
    setInterval(async () => {
            const output = await eel.captureOutput()();
            if(!output) {
                return;
            }
            const newoutput = output.output
            const textarea = document.getElementById('console');
            const content = textarea.innerHTML || textarea.textContent;
            const newelement = parseHTML(newoutput);
            textarea.appendChild(newelement)
            // const newcontent = `${content}\n${newoutput}`.split('\n').slice(-2137).join('\n')
            // textarea.innerHTML = newcontent;
            if (window.enablescroll == 1) {
                textarea.scrollTop = textarea.scrollHeight;
            }
        }
    , (window.load.consoleInterval * 300));
}

async function executeCommand(event) {
    const consoleinput = document.getElementById("consoleInput");
    if (event.target === consoleinput) {
        if (event.key === "Enter") {
            event.preventDefault();
            const command = consoleinput.value;
            window.lastcommand = command;
            consoleinput.value = "";
            // await eel.executeCommand(input=(command))();
            await eel.executeCommand(input=command)();
            if (window.enablescroll == 1) {
                textarea.scrollTop = textarea.scrollHeight;
            };
        };
        if (event.key === "Tab") {
            event.preventDefault();
            const test = window.lastcommand;
            consoleinput.value = test;
        };
    };
};
async function buttonClick(event) {
    console.log(event)
    button = event.target
    if (button.classList.contains(CHECKED_CLASS)) {
        button.classList.remove(CHECKED_CLASS);
    } else {
        button.classList.add(CHECKED_CLASS);
    };
    if (button.id == "scroll") {
        if (window.enablescroll == 0){
            window.enablescroll = 1;
        } else {
            window.enablescroll = 0;
        };
    } else {
        const id = button.id.replace('sort_','')

        for (const log_type of LOG_CLASSES) {
            if (id.includes(log_type)) {
                const elements = document.querySelectorAll('.'+log_type);
                console.log(log_type)
                if (button.classList.contains(CHECKED_CLASS)) {
                    for (element of elements) {
                        element.classList.add(HIDDEN_CLASS);
                    };
                } else {
                    for (element of elements) {
                        element.classList.remove(HIDDEN_CLASS);
                    };
                };
            };
        };
    };
};
function parseHTML(html) {
    var t = document.createElement('template');
    t.innerHTML = html;
    return t.content;
};
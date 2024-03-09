const CHECKED_CLASS = 'checked';
const CLICK_CLASS = 'clicked';
window.lastcommand = '';


const initialize = async () => {
    window.load = await eel.windowLoad()();
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
            const newcontent = `${content}\n${newoutput}`.split('\n').slice(-2137).join('\n')
            textarea.innerHTML = newcontent;
            if (enableScroll = 1){
                textarea.scrollTop = textarea.scrollHeight;
            }
        }
    , (window.load.consoleInterval * 600));
}

async function executeCommand(event) {
    console.log(event)
    const consoleinput = document.getElementById("consoleInput");
    if (event.target === consoleinput) {
        if (event.key === "Enter") {
            event.preventDefault();
            const command = consoleinput.value;
            window.lastcommand = command;
            consoleinput.value = "";
            // await eel.executeCommand(input=(command))();
            await eel.executeCommand(input=command)();
            if (window.enablescroll === 1){
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
    if (event.target.id === "scroll") {
        if (window.enablescroll === 0){
            window.enablescroll = 1;
        } else {
            window.enablescroll = 0;
        };
    };
};









const CHECKED_CLASS = 'checked';
const CLICK_CLASS = 'clicked';

const initialize = async () => {
    // when site loads go to python
    await eel.windowLoad()();
    await display_servers();
    const checkboxes = document.querySelectorAll(".checkbox");
    for (const checkbox of checkboxes) {
        checkbox.classList.add(CHECKED_CLASS)
        checkbox.addEventListener("click", function (event) {
            event.stopPropagation();
            event.preventDefault();
            const isChecked = checkbox.classList.contains(CHECKED_CLASS);
            if (process == 0) {
                if (isChecked) {
                    checkbox.classList.remove(CHECKED_CLASS);
                    eel.buttonClick(state=('unchecked'), eid=(event.target.id))
                } else {
                    checkbox.classList.add(CHECKED_CLASS);
                    eel.buttonClick(state=('checked'), eid=(event.target.id))
                    
                };
            } else {
                alert("can't change this settings while the servers are starting!")
            }
        });
    }
    const start = document.querySelector(".start-text-main");
    const start_bottom = document.querySelector(".start-text-bottom");
    start.addEventListener("click", function (event) {
        process = 1
        event.stopPropagation();
        event.preventDefault();
        start.classList.add(CLICK_CLASS);
        start.setAttribute('disabled', 'true');
        eel.startClick()(function callback(errors = "test") {
            start.classList.remove(CLICK_CLASS)
            start.setAttribute('disabled', 'false');
            start.removeAttribute('disabled');
            process = 0
        });
    });
    const buttons = document.querySelectorAll(".button");
    for (const button of buttons) {
        button.addEventListener("click", function (event) {
            event.stopPropagation();
            event.preventDefault();
            eel.buttonClick(state=('none'), eid=(event.target.id))

         });
    }
}










// PYTON NIE MOŻE ZNALEŚĆ TEJ FUNKCJI
// eel.expose();
// async function startstop() {
//     const lol = document.querySelectorAll(".start-text-main")
//     for (const starttext of lol) {
//         const isClicked = checkbox.classList.contains(CLICK_CLASS);
//         starttext.classList.remove(CLICK_CLASS);
//     }
// }











if (document.readyState === "loading") {
    process = 0
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }




async function display_servers() {
    const servers = await eel.getServers()();
    console.log(servers);
    for (const enabledServer of servers.enabledServers) {
        console.log(enabledServer);
        const html = document.getElementById('enabled-server');
        const cloned = html.cloneNode(true);
        const clonedId = `enabled-server-${enabledServer}`
        cloned.id = clonedId;
        cloned.style.display = '';
        html.parentElement.append(cloned)
        const editable = document.querySelector(`#${clonedId}`);
        editable.querySelector('#server-name').textContent = servers.server[enabledServer] + (':');
        editable.querySelector('input#server-id').id = enabledServer;
        editable.querySelector('label#server-id').id = enabledServer;
    }
}

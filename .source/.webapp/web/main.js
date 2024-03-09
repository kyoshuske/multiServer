const CHECKED_CLASS = 'checked';
const CLICK_CLASS = 'clicked';

const initialize = async () => {
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

    const start_all = document.querySelector(".start-text-all");
    const start = document.querySelector(".start-text-main");
    const start_bottom = document.querySelector(".start-text-bottom");
    start.addEventListener("click", function (event) {
        process = 1
        event.stopPropagation();
        document.getElementById("start-text").innerHTML="starting";
        document.getElementById("start-text-bottom").innerHTML="please wait";
        event.preventDefault();
        start.classList.add(CLICK_CLASS);
        start_bottom.classList.add(CLICK_CLASS);
        start_all.classList.add(CLICK_CLASS);
        start.setAttribute('disabled', 'true');
        eel.startClick()(function callback(errors = "test") {
            document.getElementById("start-text").innerHTML="start";
            document.getElementById("start-text-bottom").innerHTML="selected servers";
            start.classList.remove(CLICK_CLASS)
            start_bottom.classList.remove(CLICK_CLASS)
            start_all.classList.remove(CLICK_CLASS)
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

if (document.readyState === "loading") {
    process = 0
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }

async function display_servers() {
    const servers = await eel.getServers()();
    for (const enabledServer of servers.enabledServers) {
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
        editable.querySelector('div#server-id').id = enabledServer;
    }
}
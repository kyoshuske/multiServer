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

    const server_start_buttons = document.querySelectorAll(".start-button");
    for (const start_button of server_start_buttons) {
        start_button.addEventListener("click", function (event) {
            if (!start_button.classList.contains(CLICK_CLASS)) {
                start_button.innerHTML="starting";
                start_button.classList.add(CLICK_CLASS);
                start_button.setAttribute('disabled', 'true');
                eel.serverStartClick(id=(start_button.id))(function callback() {
                
                    start_button.classList.remove(CLICK_CLASS);
                    start_button.setAttribute('disabled', 'true');
                    start_button.innerHTML="start";
            });
            }
        });
    }
};
if (document.readyState === "loading") {
    process = 0
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }

async function display_servers() {
    const servers = await eel.getServers()();
    const html = document.getElementById('server-id');
    html.style.display = 'none';
    for (const id of servers.id) {
        const cloned = html.cloneNode(true);
        const clonedId = `server-id-${id}`
        console.log('Loaded server. Data: [id: ' + id + ', name: ' + servers.name[id] + ', icon: ' + servers.icon[id] + ']')


        cloned.id = clonedId;
        cloned.style.display = '';


        html.parentElement.append(cloned)
        const editable = document.querySelector(`#${clonedId}`);
        editable.querySelector('p.text-server').textContent = servers.name[id];
        editable.querySelector('.server-icon').src = servers.icon[id];
        editable.querySelector('.start-button').id = id;
        editable.querySelector('.button-logs').setAttribute( 'onClick', 'openFile('+id+')' );
        console.log(editable);
        console.log('---------------------------------------------------');
    };
    html.remove();
}

async function changeTab(x) {
    const tab_to_change = document.getElementById('tab-' + x);
    tab_to_change.classList.add(CHECKED_CLASS);
    console.log('clicked tab-button: ' +  x);
    const tabs = document.querySelectorAll(".navbar-tab");
    for (const tab_to_hide of tabs) {
        const ret = tab_to_hide.id.replace('tab-','')
        const content = document.querySelector('.page-' + ret);
        content.style.display = tab_to_change !== tab_to_hide ? "none" : '';
        if (tab_to_change !== tab_to_hide) {
            tab_to_hide.classList.remove(CHECKED_CLASS);
        }
    };
}
async function openFile(x) {
    eel.serverFileClick(id=x)
};
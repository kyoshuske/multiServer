const CHECKED_CLASS = 'checked';
const CLICK_CLASS = 'clicked';

const initialize = async () => {
    await eel.windowLoad()();
    await display_servers();

    const server_start_buttons = document.querySelectorAll(".start-button");
    for (const start_button of server_start_buttons) {
        start_button.addEventListener("click", function (event) {
            if (!start_button.classList.contains(CLICK_CLASS)) {
                start_button.innerHTML="starting";
                start_button.classList.add(CLICK_CLASS);
                start_button.setAttribute('disabled', 'true');
                console.log('clicked start-button: ' +  start_button.id);
                eel.serverStartClick(id=(start_button.id))(function callback() {
                    start_button.classList.remove(CLICK_CLASS);
                    start_button.setAttribute('disabled', 'true');
                    start_button.innerHTML="start";
            });
            }
        });
    }
    const proxy_start_button = document.querySelector(".proxy-button");
    proxy_start_button.addEventListener("click", function (event) {
        eel.startProxy()
    });
};
if (document.readyState === "loading") {
    process = 0;
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }

async function display_servers() {
    const servers = await eel.getServers()();
    const server_template = document.getElementById('server-id');
    server_template.style.display = 'none';
    for (const id of servers.id) {
        const cloned = server_template.cloneNode(true);
        const clonedId = `server-id-${id}`;
        console.log('Loaded server. Data: [id: ' + id + ', name: ' + servers.name[id] + ', icon: ' + servers.icon[id] + ']');
        cloned.id = clonedId;
        cloned.style.display = '';
        server_template.parentElement.append(cloned);
        const editable = document.querySelector(`#${clonedId}`);
        editable.querySelector('p.text-server').textContent = servers.name[id];
        editable.querySelector('.server-icon').src = servers.icon[id];
        editable.querySelector('.start-button').id = id;
        editable.querySelector('.button-logs').setAttribute( 'onClick', 'openFile('+id+')' );
        console.log(editable);
        console.log('---------------------------------------------------');
    };
    server_template.remove();
}

async function changeTab(x) {
    const tab_to_change = document.getElementById('tab-' + x);
    tab_to_change.classList.add(CHECKED_CLASS);
    console.log('clicked tab-button: ' +  x);
    const tabs = document.querySelectorAll(".navbar-tab");
    for (const tab_to_hide of tabs) {
        const ret = tab_to_hide.id.replace('tab-','');
        const content = document.querySelector('.page-' + ret);
        content.style.display = tab_to_change !== tab_to_hide ? "none" : '';
        if (tab_to_change !== tab_to_hide) {
            tab_to_hide.classList.remove(CHECKED_CLASS);
        }
    };
}
async function python(code) {
    await eel.executePythonCode(code)();
}
async function openFile(x) {
    // const server_template = document.getElementById('server-id-1');
    // server_template.id = 'server-id'
    // for (const element of server_template.parentElement.childNodes) {
    //     element.remove();
    //     console.log('test: '+element+'/'+server_template.parentElement.childNodes.length)
    //     if (`#${element.id}`.includes('server-id') == true) {
    //         if (element !== server_template) {
    //             element.remove();
    //         };
    //     };


    // };
    // display_servers();
    eel.serverFileClick(id=x);
};
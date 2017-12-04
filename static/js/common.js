const selected_portal = $('#id_name');
const messages = $('#messages');
const selected_portals = $('.selected_portals')
const sel_portal = document.getElementById('select_portal');
const name_inp = document.getElementById('id_name');
let list_portal_name = document.getElementById('portal_name');
let list_portals = document.getElementById('list_portals');

sel_portal.addEventListener('change', function () {
    name_inp.value = this.value;
}, false);

list_portals.addEventListener('click', (e) => {
    let target = e.target;
    if (target.getAttribute("id") == 'portal_name') {
        let portal_name = target.innerHTML;
        let availabel_portals = $(selected_portals).children()
        console.log(availabel_portals);
        for (let i = 0; i < availabel_portals.length; i++) {
            if (availabel_portals[i].value == portal_name) {
                $(availabel_portals[i]).remove()
                return true;
            } else {
                $(selected_portals).append(
                    `<input type="text" value="${portal_name}" name="selected_portal">`
                );
            }
        }
    }
}, false);

(function set_default_portal() {
    selected_portal.val(sel_portal[0].value)
})();

// Hide message after 4 seconds
(function hideMessage() {
    setTimeout(function () {
        messages.fadeOut('slow');
    }, 4000);
})();


$('.the_portal').click(function (event) {
    elem = $(this);
    $(elem).toggleClass('the_portal_disable');
    $(elem).children('span').toggleClass('lamp_disable');
});


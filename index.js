// on the press of d, the theme will change to dark, by way of adding a class to the body
// on the press of l, the theme will change to light, by way of removing the class from the body
// on the press of h, all keyboard shortcuts will be displayed in an absolute positioned div

document.addEventListener('keydown', function(event) {
    if (event.key === 'd') {
        document.body.classList.add('dark');
    } else if (event.key === 'l') {
        document.body.classList.remove('dark');
    } else if (event.key === 'h') {
        if (document.querySelector('.keyboard-shortcuts')) {
            document.querySelector('.keyboard-shortcuts').remove();
        } else {
            let div = document.createElement('div');
            div.className = 'keyboard-shortcuts';
            div.innerHTML = `
            <ul>
                <li><strong>d</strong>: dark theme</li>
                <li><strong>l</strong>: light theme</li>
                <li><strong>h</strong>: display keyboard shortcuts</li>
            </ul>
            `;

            document.body.appendChild(div);
        }

    }
    });

// add navigation to the page
document.addEventListener('DOMContentLoaded', function() {
    let nav = document.createElement('nav');
    
    // < for back, > for forward
    nav.innerHTML = `
    <a href="javascript:back()">&lt;</a>
    <a href="javascript:fwd()">&gt;</a>
    `;

    nav.classList.add('navigation');

    document.body.appendChild(nav);
});

function back() {
    history.back();
}

function fwd() {
    history.forward();
}
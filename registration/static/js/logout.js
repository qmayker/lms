// import Cookies from 'js-cookie'

let csrftoken =  Cookies.get('csrftoken')
console.log(csrftoken)

document.addEventListener('DOMContentLoaded', (e)=>{
    const logoutButton = document.querySelector('.registration .logout');
    const postData = {
        method: 'POST',
        mode: 'same-origin',
        headers : {
            'X-CSRFToken': csrftoken
        }
    }

    if(!logoutButton){
        return
    }
    const urlPath = logoutButton.dataset.url;

    logoutButton.addEventListener('click', e=>{
        e.preventDefault();
        const logoutUrl = new URL(window.origin);
        logoutUrl.pathname = urlPath;
        fetch(logoutUrl, postData)
        window.location.href = "/";
    })
})
console.log('inside fetch example');


function getUsers(){
    x = document.forms["front"]["number"].value;
    url = "https://reqres.in/api/users/" + x;
    console.log('clicked');
    console.log(url);
    fetch(url).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(user) {

    const curr_main = document.querySelector("main");
    const section = document.createElement('section');
    section.innerHTML = `
    <img src="${user.avatar}" alt="Profile Picture"/>
    <div>
        <span>${user.first_name} ${user.last_name}</span>
        <br>
        <a href="mailto:${user.email}">Send Email</a>
    </div>
    `;
    curr_main.appendChild(section);
}

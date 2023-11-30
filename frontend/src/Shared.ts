
import { ref  } from "vue";

export const logged_in = ref(false);
export const auth_token = ref(null)
const user = ref('');
export const all_posts = ref([]);


let API_URL = import.meta.env.API_URL;
if (API_URL === undefined) {
    API_URL = "http://localhost:5000";
}

function fetch_posts() {
    let data = fetch(`${API_URL}/posts`)
        .then(response => response.json())
        .then(data => all_posts.value = data);
    console.log(data);
}
fetch_posts();

export function login(username: string, password: string) {
    let res = fetch(`${API_URL}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    });
    res.then((res) => {
        if (res.status === 200) {
            logged_in.value = true;
            res.json().then((data) => {
                auth_token.value = data.token;
                console.log(data.token);
                user.value = username;
            })
        }
    })
}

export function register(name: string, username: string, password: string) {
    let res = fetch(`${API_URL}/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            username: username,
            password: password
        })
    });
    res.then((res) => {
        if (res.status === 200) {
            console.log("Registered successfully");
        }
    })
}

export function new_post(content: string) {
    return fetch(`${API_URL}/new_post`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: user.value,
            content: content,
            token: auth_token.value
        })
    }).then(async (res) => {
        if (res.status === 201) {
            let data = await res.json();
            console.log(data);
            all_posts.value.unshift(data as never);
            return true;
        } else {
            console.log("Error creating post");
            return false;
        }
    });
}
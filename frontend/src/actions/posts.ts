import { apiData, postsData, authData } from "../store";


export const posts = {

    fetchAll: () => {
        let data = fetch(`${apiData.URL}/posts`)
            .then(response => response.json())
            .then(data => postsData.all.value = data);
        console.log(data);
    },
    
    publish: (content: string) => {
        return fetch(`${apiData.URL}/new_post`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                content: content,
                username: authData.current_user.value,
                token: authData.token.value
            })
        }).then(async (res) => {
            if (res.ok) {
                let data = await res.json();
                console.log(data);
                postsData.all.value.unshift(data as never);
                return true;
            } else {
                console.log("Error creating post");
                return false;
            }
        });
    },

    
}
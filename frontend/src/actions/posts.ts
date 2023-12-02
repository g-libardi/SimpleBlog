import { apiData, postsData, authData } from "../store";
import { notes } from "./notes";

export interface Post {
    id: number;
    content: string;
    username: string;
    created_at: string;
}

export const posts = {
    fetchAll: async () => {
        try {
            let res = await fetch(`${apiData.URL}/posts`);
            let data = await res.json();
            if (!res.ok) {
                notes.error(data.error);
                return;
            }
            postsData.all.value = data;
        } catch (error) {
            console.error("An error occurred while fetching posts:", error);
        }
    },
    
    publish: async (content: string) => {
        try {
            let res = await fetch(`${apiData.URL}/new_post`, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    content: content,
                    username: authData.current_user.value,
                    token: authData.token.value
                })
            });
            let data = await res.json();
            if (!res.ok) {
                notes.error(data.error);
                return;
            }
            console.log(data);
            postsData.all.value.unshift(data);
            return;
        } catch (error) {
            console.error("Error creating post:", error);
            return;
        }
    },
}
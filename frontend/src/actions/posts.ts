import { apiData, postsData, authData } from "../store";

export interface Post {
    id: number;
    content: string;
    username: string;
    created_at: string;
}

export const posts = {
    fetchAll: async () => {
        try {
            let response = await fetch(`${apiData.URL}/posts`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            let data = await response.json() as Post[];
            postsData.all.value = data;
        } catch (error) {
            console.error("An error occurred while fetching posts:", error);
        }
    },
    
    publish: async (content: string) => {
        try {
            let response = await fetch(`${apiData.URL}/new_post`, {
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
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            let data: Post = await response.json();
            console.log(data);
            postsData.all.value.unshift(data);
            return true;
        } catch (error) {
            console.error("Error creating post:", error);
            return false;
        }
    },
}
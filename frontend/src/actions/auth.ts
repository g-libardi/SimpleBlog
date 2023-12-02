
import { apiData, authData } from "../store";

export const auth = {

    getCreds: () => {
        return {
            username: authData.current_user.value,
            token: authData.token.value
        }
    },
    
    login: async (username: string, password: string) => {
        try {
            let res = await fetch(`${apiData.URL}/login`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });
    
            if (!res.ok) {
                throw new Error(`HTTP error! status: ${res.status}`);
            }

            authData.logged_in.value = true;
            let data = await res.json();
            authData.token.value = data.token;
            console.log(data.token);
            authData.current_user.value = username;

        } catch (error) {
            console.error("An error occurred:", error);
        }
    },
    
    register: async (name: string, username: string, password: string) => {
        try {
            let res = await fetch(`${apiData.URL}/register`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    name: name,
                    username: username,
                    password: password
                })
            });
            
            if (!res.ok) {
                throw new Error(`HTTP error! status: ${res.status}`);
            }
            let data = await res.json();
            console.log(data);
        } catch (error) {
            console.error("An error occurred:", error);
        }
    },
}

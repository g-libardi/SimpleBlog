
import { apiData, authData } from "../store";
import { notes } from "./notes";

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
    
            let data = await res.json();
            if (!res.ok) {
                notes.error(data.error);
                console.log(data.error);
                return;
            }

            authData.logged_in.value = true;
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
            let data = await res.json();
            if (!res.ok) {
                notes.error(data.error);
            }
            
            console.log(data);
        } catch (error) {
            console.error("An error occurred:", error);
        }
    },
}

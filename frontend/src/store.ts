
import { ref } from "vue";
import { Note } from "./actions/notes";

export const authData = {
    logged_in: ref(false),
    current_user: ref(''),
    token: ref(null),
}

export const apiData = {
    URL: () => {
        let url = import.meta.env.VITE_API_URL;
        if (url === undefined) {
            url = "http://localhost:5000";
        }
        return url;
    }
}

export const postsData = {
    all: ref([]),
    forYou: ref([]),
    user: ref([]),
}

export const notesData = {
    notes: ref<Note[]>([]),
}

import { ref } from "vue";
import { Note } from "./actions/notes";
import { Post } from "./actions/posts";

export const authData = {
    logged_in: ref(false),
    current_user: ref(''),
    token: ref(null),
}

export const apiData = {
    URL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : 'http://localhost:5000',
}

export const postsData = {
    all: ref<Post[]>([]),
    forYou: ref<Post[]>([]),
    user: ref<Post[]>([]),
}

export const notesData = {
    notes: ref<Note[]>([]),
}
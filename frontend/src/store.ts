
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
    all: ref<Post[]>([
        {
            id: 1,
            content: "Hello, world!",
            username: "john_doe",
            created_at: "2022-01-01T12:00:00Z",
        },
        {
            id: 2,
            content: "Testing post example",
            username: "jane_smith",
            created_at: "2022-01-02T09:30:00Z",
        },
        {
            id: 3,
            content: "This is another post",
            username: "bob_johnson",
            created_at: "2022-01-03T18:15:00Z",
        },
    ]),
    forYou: ref<Post[]>([]),
    user: ref<Post[]>([]),
}

export const notesData = {
    notes: ref<Note[]>([]),
}
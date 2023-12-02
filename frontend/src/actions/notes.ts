import { notesData } from "../store";

export enum NoteType {
    Error = 'Error',
    Info = 'Info',
    Warning = 'Warning',
}

export interface Note {
    msg: string;
    type: NoteType;
}

export const notes = {
    notify: (message: string, type: NoteType) => {
        const note: Note = { msg: message, type: type };
        notesData.notes.value.push(note);
        notes.removeCallback(note, 5000);
    },
    info: (message: string) => {
        notes.notify(message, NoteType.Info);
    },
    error: (message: string) => {
        notes.notify(message, NoteType.Error);
    },
    warning: (message: string) => {
        notes.notify(message, NoteType.Warning);
    },
    removeCallback: (note: Note, time: number) => {
        setTimeout(() => {
            const index = notesData.notes.value.indexOf(note);
            if (index !== -1) notesData.notes.value.splice(index, 1);
        }, time);
    },
    clear: () => {
        notesData.notes.value = [];
    },
}
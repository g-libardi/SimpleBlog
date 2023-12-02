<script setup lang="ts">
import { notesData } from '../store';
import { NoteType } from '../actions/notes';


</script>

<template>
    <div class="fixed top-0 left-0 w-full z-50 flex flex-col">
        <div v-for="note in notesData.notes.value"
        class="w-full h-10 flex justify-center items-center"
        :class="{
            'bg-rose-600': note.type == NoteType.Error,
            'bg-sky-600': note.type == NoteType.Info,
            'bg-yellow-600': note.type == NoteType.Warning,
            }">
            <p>{{ note.msg }}</p>
        </div>
    </div>
</template>
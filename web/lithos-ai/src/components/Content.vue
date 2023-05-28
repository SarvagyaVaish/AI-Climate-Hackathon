<template>
  <header class="bg-white shadow">
    <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">

      <div class="grid grid-cols-12">
        <div class="col-span-9">
          <h1 class="text-3xl font-bold tracking-tight text-gray-900">Call Assistant</h1>
        </div>

        <div class="col-span-1">
          <div role="status" :hidden="!loading">
            <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
              viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor" />
              <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill" />
            </svg>
            <span class="sr-only">Loading...</span>
          </div>

        </div>

        <div class="col-span-2">
          <Menu as="div" class="w-full relative inline-block text-left">
            <div>
              <MenuButton
                class="inline-flex w-full justify-center rounded-md bg-gray-800 px-4 py-2 text-sm font-medium text-white">
                Select Call
                <ChevronDownIcon class="ml-2 -mr-1 h-5 w-5 text-violet-200 hover:text-violet-100" aria-hidden="true" />
              </MenuButton>
            </div>

            <transition enter-active-class="transition duration-100 ease-out"
              enter-from-class="transform scale-95 opacity-0" enter-to-class="transform scale-100 opacity-100"
              leave-active-class="transition duration-75 ease-in" leave-from-class="transform scale-100 opacity-100"
              leave-to-class="transform scale-95 opacity-0">
              <MenuItems
                class="absolute right-0 mt-2 w-52 origin-top-right divide-y divide-gray-100 rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <div class="px-1 py-1">
                  <MenuItem v-slot="{ active }">
                  <button @click="loadConversation1" :class="[
                    active ? 'bg-violet-500 text-white' : 'text-gray-900',
                    'group flex w-full items-center rounded-md px-2 py-2 text-sm',
                  ]">
                    {{ conversations.conv1.name }}
                  </button>
                  </MenuItem>

                  <MenuItem v-slot="{ active }">
                  <button @click="loadConversation2" :class="[
                    active ? 'bg-violet-500 text-white' : 'text-gray-900',
                    'group flex w-full items-center rounded-md px-2 py-2 text-sm',
                  ]">
                    {{ conversations.conv2.name }}
                  </button>
                  </MenuItem>
                </div>
              </MenuItems>
            </transition>
          </Menu>
        </div>
      </div>
    </div>
  </header>

  <div class="mx-auto max-w-7xl px-4 pb-0 pt-6 sm:px-6 lg:px-8 text-xl text-gray-900">
    <h1>{{ selectedConv.name }}</h1>
  </div>

  <div class="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8">
    <iframe id="airtable" class="airtable-embed"
      src="https://airtable.com/embed/shrEICyiJ29fyHdCv?backgroundColor=gray&layout=card&viewControls=on" frameborder="0"
      onmousewheel="" width="100%" height="360" style="background: transparent; border: 1px solid #ccc;"></iframe>
  </div>

  <div v-if="questions.length > 0">

    <div class="grid grid-cols-2">
      <div class="col-span-1">
        <div class="mx-auto max-w-7xl px-4 pb-0 pt-6 sm:px-6 lg:px-8 text-xl text-gray-900">
          <h1>Follow Up Questions</h1>
        </div>
        <div class="mx-auto max-w-7xl px-4 pb-0 pt-6 sm:px-6 lg:px-8 text-base text-gray-900">
          <ul class="list-disc list-inside">
            <li v-for="question in questions">
              {{ question }}
            </li>
          </ul>
        </div>
      </div>

      <div class="col-span-1">
        <div class="mx-auto max-w-7xl pb-0 pt-6 lg:px-8 text-xl text-gray-900">
          <h1>Weather</h1>
          <div class="pt-6 text-base text-gray-400">Coming soon</div>
        </div>
      </div>
    </div>
  </div>

  <div class="my-32"></div>
</template>

<script>
import { completion } from "./../api/openai";
import { parse } from "./../api/service";
import CallSelector from "./CallSelector.vue"
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { ChevronDownIcon } from '@heroicons/vue/20/solid'

export default {
  components: { CallSelector, Menu, MenuButton, MenuItem, MenuItems, ChevronDownIcon },

  props: {
    // text: { type: str, required: true },
  },

  emits: [
    // "event",
  ],

  data() {
    return {
      conversations: {
        conv1: {
          name: "May 27th  ·  Morning Dew"
        },
        conv2: {
          name: "May 25th  ·  Harvest Hill"
        }
      },
      selectedId: "conv1",
      loading: false,
      questions: [],
    };
  },

  mounted() {
  },

  computed: {
    selectedConv() {
      return this.conversations[this.selectedId];
    }
  },

  methods: {
    loadConversation(conv_id) {
      this.selectedId = conv_id;
      const fn = async () => {
        this.loading = true;
        const response = await parse(conv_id);
        var src = document.getElementById("airtable").src;
        document.getElementById("airtable").src = src;
        this.loading = false;

        this.questions = response.questions;
        console.log(this.questions);
      }
      fn();
    },

    loadConversation1() {
      console.log("Conversation #1");
      this.loadConversation("conv1");
    },

    loadConversation2() {
      console.log("Conversation #2");
      this.loadConversation("conv2");
    },
  },
}
</script>

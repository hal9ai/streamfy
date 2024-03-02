<template>
  <span>
    Yodd! {{ args.name }}! &nbsp;
    <button @click="onClicked">Click Me!</button>
    <b-field label="Add some tags">
      <b-taginput
        ref="tagel"
        v-model="tags"
        :data="suggestions"
        autocomplete
        :allow-new="true"
        :open-on-focus="focusOpen"
        type="is-info"
        placeholder="Contains what?"
        aria-close-label="Remove"
        @focus="focused"
        @blur="blured">
      </b-taginput>
    </b-field>
  </span>
</template>

<script>
import { ref, onMounted } from "vue"
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"

const tagel = ref(null)

export default {
  name: "Streamfy",
  props: ["args"], // Arguments that are passed to the plugin in Python are accessible in prop "args"
  data() {
    return {
      focusOpen: false,
    }
  },
  methods: {
    focused() {
      this.focusOpen = true;
      Streamlit.setFrameHeight(400);
    },
    blured() {
      Streamlit.setFrameHeight();
    }
  },
  setup() {
    useStreamlit() // lifecycle hooks for automatic Streamlit resize

    const numClicks = ref(0)
    const onClicked = () => {
      numClicks.value++
      Streamlit.setComponentValue(numClicks.value)
    }

    const tags = [];
    const suggestions = ["Albertson", "Abogadro", "C", "D", "E", "F", "G"]

    return {
      tags,
      numClicks,
      onClicked,
      suggestions,
    }
  },
}
</script>

<style>
  .dropdown-menu.is-opened-top {
    bottom: none !important;
  }
</style>

<template>
  <span>
    <b-field label="Add some tags">
      <b-taginput
        ref="tagRef"
        v-model="tags"
        :data="suggestions"
        autocomplete
        :allow-new="true"
        :open-on-focus="true"
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
      if (this.tagRef) {
        const menu = this.tagRef.$el.querySelector('.dropdown-menu');
        menu.style.bottom = 'auto';
      }

      Streamlit.setFrameHeight(300);
    },
    blured() {
      setTimeout(() => Streamlit.setFrameHeight(80), 200);
    }
  },
  setup() {
    useStreamlit() // lifecycle hooks for automatic Streamlit resize

    const tagRef = ref(null);

    const tags = [];
    const suggestions = ["Albertson", "Abogadro", "C", "D", "E", "F", "G"]

    return {
      tags,
      suggestions,
      tagRef,
    }
  },
}
</script>

<style>
  .dropdown-menu.is-opened-top {
    bottom: none !important;
  }
</style>

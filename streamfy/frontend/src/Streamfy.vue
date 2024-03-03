<template>
  <span>
    <b-field label="Add some tags">
      <b-taginput
        ref="tagRef"
        v-model="tags"
        :data="data"
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
  props: ["args"],
  data() {
    return {
      tags: [],
      focusOpen: false,
      data: this.args.data ?? [],
      placeholder: this.args.placeholder ?? '',
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
  watch: {
    tags() {
      Streamlit.setComponentValue([...this.tags]);
    }
  },
  setup() {
    useStreamlit() // lifecycle hooks for automatic Streamlit resize

    const tagRef = ref(null);

    return {
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

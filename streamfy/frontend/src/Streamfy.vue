<template>
  <span>
    <b-field ref="tagField" :label="label">
      <b-taginput
        v-if="args.component == 'taginput'"
        v-model="tags"
        :data="args.data"
        autocomplete
        :allow-new="true"
        :open-on-focus="true"
        type="is-info"
        :placeholder="args.placeholder"
        aria-close-label="Remove"
        @focus="focused"
        @blur="blured">
      </b-taginput>
      <b-table
        v-else-if="args.component == 'table'"
        v-bind="args"
        :mobile-cards="args['has_mobile_cards'] != undefined ? args['has_mobile_cards'] : false"
        >
      </b-table>
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
      jdata: undefined,
    }
  },
  methods: {
    focused() {
      if (this.tagField) {
        const menu = this.tagField.$el.querySelector('.dropdown-menu');
        menu.style.bottom = 'auto';
      }

      Streamlit.setFrameHeight(300);
      setTimeout(() => Streamlit.setFrameHeight(), 200);
    },
    blured() {
      setTimeout(() => Streamlit.setFrameHeight(), 200);
    }
  },
  watch: {
    tags() {
      Streamlit.setComponentValue([...this.tags]);
    },
  },
  setup() {
    useStreamlit()

    const tagField = ref(null);

    return {
      tagField,
    }
  },
}
</script>

<style>
  .dropdown-menu.is-opened-top {
    bottom: none !important;
  }
</style>

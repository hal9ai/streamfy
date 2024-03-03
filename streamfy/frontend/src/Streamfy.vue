<template>
  <span>
    <b-field ref="field" :label="label">
      <b-breadcrumb
        v-if="args.component == 'breadcrumb' && args.items != undefined"
      >
        <b-breadcrumb-item
          v-for="item in args.items"
          :key="item.text"
          v-bind="item"
          @click="click(item)"
        >{{item.text}}
        </b-breadcrumb-item>
      </b-breadcrumb>
      <b-button 
        v-else-if="args.component == 'button'"
        v-bind="args"
        @click="click(args)">
        {{ args.text}}
      </b-button>
      <b-taginput
        v-else-if="args.component == 'taginput'"
        v-model="result"
        v-bind="args"
        @focus="focused"
        @blur="blured"
      >
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
      result: [],
      jdata: undefined,
    }
  },
  methods: {
    focused() {
      if (this.field) {
        const menu = this.field.$el.querySelector('.dropdown-menu');
        menu.style.bottom = 'auto';
      }

      Streamlit.setFrameHeight(300);
      setTimeout(() => Streamlit.setFrameHeight(), 200);
    },
    blured() {
      setTimeout(() => Streamlit.setFrameHeight(), 200);
    },
    click(value) {
      this.result = value
    },
  },
  watch: {
    result() {
      if (this.result?.length)
        Streamlit.setComponentValue([...this.result]);
      else if (typeof(this.result) == 'object')
        Streamlit.setComponentValue(Object.assign({}, this.result));
      else
        Streamlit.setComponentValue(this.result);
    },
  },
  setup() {
    useStreamlit()

    const field = ref(null);

    return {
      field,
    }
  },
}
</script>

<style>
  .dropdown-menu.is-opened-top {
    bottom: none !important;
  }
</style>

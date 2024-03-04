<template>
  <span>
    <b-field
      ref="field" :label="label"
      :style="{'padding': ['clockpicker', 'colorpicker'].includes(args.component) ? '0 0 20px 20px' : ''}"
    >
      <b-breadcrumb
        v-if="args.component == 'breadcrumb' && args.items != undefined"
      >
        <b-breadcrumb-item
          v-for="(item, i) in args.items" :key="i"
          v-bind="item"
          @click="click(item)"
        >{{item.text}}
        </b-breadcrumb-item>
      </b-breadcrumb>
      <b-button 
        v-else-if="args.component == 'button'"
        v-bind="args"
        @click="click(args)"
      >
        {{ args.text}}
      </b-button>
      <b-carousel
        v-else-if="args.component == 'carousel'"
        v-bind="args"
      >
        <b-carousel-item
          v-for="(item, i) in args.items" :key="i"
        >
          <a class="image" @click="click(item)">
            <img :src="item">
          </a>
        </b-carousel-item>
        <template #list="props">
          <b-carousel-list
            v-model="props.active"
            :data="args.items"
            @switch="props.switch($event, false)"
            as-indicator 
          />
        </template>
      </b-carousel>
      <b-autocomplete
        v-else-if="args.component == 'autocomplete'"
        v-model="result"
        v-bind="args"
        @focus="focused"
        @blur="blured"
      >
      </b-autocomplete>
      <b-checkbox
        v-else-if="args.component == 'checkbox'"
        v-model="result"
        v-bind="args"
      >
        {{ args.text}}
      </b-checkbox>
      <b-clockpicker
        v-else-if="args.component == 'clockpicker'"
        v-model="result"
        v-bind="args"
        inline
        @focus="focused"
        @blur="blured"
      >
      </b-clockpicker>
      <b-colorpicker
        v-else-if="args.component == 'colorpicker'"
        v-model="result"
        v-bind="args"
        inline
        @focus="focused"
        @mousedown="focused"
        @blur="blured"
      >
      </b-colorpicker>
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
    setTimeout(() => Streamlit.setFrameHeight(), 1000);
    return {
      result: undefined,
    }
  },
  methods: {
    focused() {
      if (this.field) {
        const menu = this.field.$el.querySelector('.dropdown-menu');
        menu.style.bottom = 'auto';
      }

      Streamlit.setFrameHeight(300);
      setTimeout(() => Streamlit.setFrameHeight(), 5000);
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
      if (this.result?.isArray && this.result.isArray()) {
        Streamlit.setComponentValue([...this.result]);
      }
      else if (this.result?.constructor?.toString()?.includes("Array")) {
        Streamlit.setComponentValue([...this.result]);
      }
      else if (this.result?.constructor == Object) {
        Streamlit.setComponentValue(Object.assign({}, this.result));
      }
      else {
        Streamlit.setComponentValue(this.result);
      }
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

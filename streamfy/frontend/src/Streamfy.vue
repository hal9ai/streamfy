<template>
  <span>
    <b-field
      ref="field"
      :label="args.label"
      :type="args.type"
      :message="args.message"
      :class="'sy-' + args.component + ' ' + args['class-name']"
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
        @blur="blured"
      >
      </b-colorpicker>

      <b-datepicker
        v-else-if="args.component == 'datepicker'"
        v-model="result"
        v-bind="args"
        inline
        @focus="focused"
        @blur="blured"
      >
      </b-datepicker>

      <b-input
        v-else-if="args.component == 'input'"
        v-model="result"
        v-bind="args"
      >
      </b-input>

      <b-numberinput
        v-else-if="args.component == 'numberinput'"
        v-model="result"
        v-bind="args"
      >
      </b-numberinput>

      <b-radio
        v-else-if="args.component == 'radio'"
        v-for="(radio, i) in args.radios" :key="i"
        v-model="result"
        :native-value="radio.text"
        v-bind="radio"
      >
        {{radio.text}}
      </b-radio>

      <b-rate
        v-else-if="args.component == 'rate'"
        v-model="result"
        v-bind="args"
      >
      </b-rate>

      <b-select
        v-else-if="args.component == 'select'"
        v-model="result"
        v-bind="args"
      >
        <option
          v-for="(option, i) in args.data" :key="i"
          :value="option.text"
          v-bind="option"
        >
          {{ option.text }}
        </option>
      </b-select>

      <b-slider
        v-else-if="args.component == 'slider'"
        v-model="result"
        v-bind="args"
      >
      </b-slider>

      <b-switch
        v-else-if="args.component == 'switch'"
        v-model="result"
        v-bind="args"
      >
        {{ args.text }}
      </b-switch>

      <b-taginput
        v-else-if="args.component == 'taginput'"
        v-model="result"
        v-bind="args"
        @focus="focused"
        @blur="blured"
        :data="filtered"
        @typing="filteredData"
      >
      </b-taginput>

      <b-message 
        v-else-if="args.component == 'message'"
        v-model="result"
        v-bind="args"
      >
        {{ args.text }}
      </b-message>

      <b-notification 
        v-else-if="args.component == 'notification'"
        v-model="result"
        v-bind="args"
      >
        {{ args.text }}
      </b-notification>

      <b-progress
        v-else-if="args.component == 'progress'"
        v-model="result"
        v-bind="args"
      >
      </b-progress>

      <b-steps
        v-else-if="args.component == 'steps'"
        :mobile-mode="false"
        v-model="result"
        v-bind="args"
      >
        <b-step-item
          v-for="(step, i) in args.steps" :key="i"
          clickable
          v-bind="step"
        >
          {{ step.text }}
        </b-step-item>
      </b-steps>

      <b-table
        v-else-if="args.component == 'table'"
        v-bind="filterKeys(args, ['columns'])"
        :mobile-cards="args['has_mobile_cards'] != undefined ? args['has_mobile_cards'] : false"
      >
        <b-table-column
          v-for="(column, i) in args.columns" :key="i"
          v-slot="props"
          sortable
          :label="column.field"
          v-bind="column"
        >
          <span v-bind="column">
          {{ props.row[column.field] }}
          </span>
        </b-table-column>
        
        <template #footer v-if="args.footer">
          <th
            v-for="(label, key, i) in args.footer" :key="i"
          >
            <div class="th-wrap">
              {{ label }}
            </div>
          </th>
        </template>
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
      result: this.args.default,
      filtered: undefined,
    }
  },
  methods: {
    focused() {
      if (this.field) {
        const menu = this.field.$el.querySelector('.dropdown-menu');
        if (menu) {
          menu.style.bottom = 'auto';
        }

        const background = this.field.$el.querySelector('.background');
        if (background) {
          background.style.opacity = 0;
        }
      }

      if (this.args.component == 'datepicker') {
        Streamlit.setFrameHeight(440);
      }
      else {
        Streamlit.setFrameHeight(300);
        setTimeout(() => Streamlit.setFrameHeight(), 200);
      }
    },
    blured() {
      setTimeout(() => Streamlit.setFrameHeight(), 200);
    },
    click(value) {
      this.result = value
    },
    filteredData(text) {
      if (this.args.component != 'taginput') return;
      if (!this.args.data) return;

      const result = this.result;
      this.filtered = this.args.data
        .filter(e => {
          return !result.includes(e)
        })
        .filter((datum) => {
          return datum
            .toString()
            .toLowerCase()
            .indexOf(text.toLowerCase()) >= 0
        })
    },
    filterKeys(args, keysToExclude) {
      const filteredDict = {};
      Object.keys(args).forEach((key) => {
        if (!keysToExclude.includes(key)) {
          filteredDict[key] = args[key];
        }
      });
      return filteredDict;
    },
  },
  watch: {
    result: {
      immediate: true,
      handler: function() {
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

        this.filteredData('');
      },
    }
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

  .sy-clockpicker,
  .sy-colorpicker,
  .sy-datepicker {
    padding: 0 0 20px 20px;
  }

  .sy-slider {
    padding: 30px 20px 10px 20px;
  }

  .sy-taginput .dropdown-content {
    margin-bottom: 20px;
  }


  .is-orange .pagination-list a,
  .is-orange .taginput .is-info.taginput-container.is-focusable {
    border-color: #DB8765 !important;
  }

  .is-orange a.pagination-link.is-current {
    background: #DB8765;
    border-color: #DB8765;
  }

  .is-orange .tag:not(body).is-info {
    background: #DB8765 !important;
  }

  .is-orange span.icon.has-text-info {
    color: #DB8765 !important;
  }

  .is-orange .taginput {
    border-color: #DB8765;
  }
</style>

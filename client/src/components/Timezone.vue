<template>
  <div>
    <h4>{{ this.header }}</h4>
    <select @change="onSelect($event.target.value)">
      <option v-for="value in options" v-bind:key="value">{{ value }}</option>
    </select>
      <p><b>{{ this.localTime }}</b></p>
  </div>
</template>;

<script lang="ts">
import axios from 'axios';
import { Component, Vue } from 'vue-property-decorator';
import timezones from './list-of-timezones';

@Component
export default class Timezone extends Vue {
  header = 'Select a timezone';

  localTime = '';

  selectedTimezone = '';

  path = 'http://localhost:5000/local-time-in-timezone';

  options = timezones;

  onSelect(value: string) {
    this.selectedTimezone = value;
    this.getTime();
  }

  getTime() {
    axios
      .get(this.path, {
        params: { selectedTimezone: this.selectedTimezone },
      })
      .then((res) => {
        this.localTime = `Local time in selected timezone - ${res.data.timezone} hrs`;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  }
}
</script>

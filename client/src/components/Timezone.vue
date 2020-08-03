<template>
  <div class="timezone-container">
    <div class="item">
      <form id="selector-form" @submit.prevent="submitForm">
        <label><strong>{{ this.header }}</strong></label>
        <select @change="onSelect($event.target.value)">
          <option v-for="value in options" v-bind:key="value">{{ value }}</option>
        </select>
        <br>
        <button id="submit-button">Submit</button>
      </form>
    </div>
    <p id="outcome"><strong>{{ this.localTime }}</strong></p>
  </div>
</template>

<style>
  .timezone-container {
    margin-top:3%;
    display: flex;
    flex-flow: column wrap;
    justify-content: center;
  }

  #submit-button {
    border: none;
    color: white;
    padding: 2px 15px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 20px 2px;
    cursor: pointer;
    background-color: #4CAF50;
  }
</style>

<script lang="ts">
import axios from 'axios';
import { Component, Vue } from 'vue-property-decorator';
import timezones from './list-of-timezones';

@Component
export default class Timezone extends Vue {
  header = 'Select a timezone ';

  localTime = '';

  selectedTimezone = '';

  path = 'http://localhost:5000/local-time-in-timezone';

  options = timezones;

  onSelect(value: string): void {
    this.selectedTimezone = value;
    this.localTime = ''; // reset outcome
  }

  submitForm(): void {
    this.getTime(this.selectedTimezone);
  }

  getTime(timezone: string): void {
    axios
      .get(this.path, {
        params: { selectedTimezone: timezone },
      })
      .then((res) => {
        this.localTime = `Local time in selected timezone - ${res.data.timezone} hrs`;
      })
      .catch((error) => {
        this.localTime = 'Server returned an error! Please try again and make sure the server is running!';
        // eslint-disable-next-line
        console.error(error);
      });
  }
}
</script>

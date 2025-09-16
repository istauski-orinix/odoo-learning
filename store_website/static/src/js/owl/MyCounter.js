// static/src/js/owl/MyCounter.js
import { Component, useState } from "@odoo/owl";

export class MyCounter extends Component {
  setup() {
    this.counter = useState({ value: 0 });
  }
  increment() {
    this.counter.value++;
  }
}
MyCounter.template = "store_website.MyCounterTemplate";
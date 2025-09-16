// static/src/js/owl/MountMyCounter.js
import { mount } from "@odoo/owl";
import { MyCounter } from "./MyCounter";

document.addEventListener("DOMContentLoaded", async () => {
  const el = document.querySelector("#owl-counter");
  if (el) {
    await mount(MyCounter, { target: el });
  }
});
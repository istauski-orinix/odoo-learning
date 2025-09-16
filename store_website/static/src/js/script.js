console.log("Store Website JS loaded!");

document.addEventListener("DOMContentLoaded", () => {
  const banner = document.querySelector(".store-home");
  if (banner) {
    banner.insertAdjacentHTML("beforeend", "<p>JS injection success!</p>");
  }
});
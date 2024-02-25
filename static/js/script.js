const body = document.querySelector("body");
const sidebar = document.querySelector(".sidebar");
const mainContent = document.querySelector(".main-content"); // Select the main content area
const submenuItems = document.querySelectorAll(".submenu_item");
const sidebarOpen = document.querySelector("#sidebarOpen");
const sidebarClose = document.querySelector(".collapse_sidebar");
const sidebarExpand = document.querySelector(".expand_sidebar");

sidebarOpen.addEventListener("click", () => {
  sidebar.classList.toggle("close");
  // Toggle the margin of main content area when sidebar is toggled
  if (sidebar.classList.contains("close")) {
    mainContent.style.marginLeft = "80px";
  } else {
    mainContent.style.marginLeft = "350px";
  }
});

sidebarClose.addEventListener("click", () => {
  sidebar.classList.add("close", "hoverable");
  // Adjust the margin of main content area when sidebar is closed
  mainContent.style.marginLeft = "80px";
});

sidebarExpand.addEventListener("click", () => {
  sidebar.classList.remove("close", "hoverable");
  // Adjust the margin of main content area when sidebar is expanded
  mainContent.style.marginLeft = "350px";
});

sidebar.addEventListener("mouseenter", () => {
  if (sidebar.classList.contains("hoverable")) {
    sidebar.classList.remove("close");
  }
});

sidebar.addEventListener("mouseleave", () => {
  if (sidebar.classList.contains("hoverable")) {
    sidebar.classList.add("close");
  }
});

if (window.innerWidth < 768) {
  sidebar.classList.add("close");
  // Adjust the margin of main content area when sidebar is closed initially on small screens
  mainContent.style.marginLeft = "80px";
} else {
  sidebar.classList.remove("close");
  // Adjust the margin of main content area when sidebar is open initially on larger screens
  mainContent.style.marginLeft = "350px";
}

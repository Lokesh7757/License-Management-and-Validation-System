// script.js
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        const licenseKey = form.querySelector("[name='license_key']").value;
        if (!licenseKey) {
            alert("Please enter a license key.");
            event.preventDefault();
        }
    });
});

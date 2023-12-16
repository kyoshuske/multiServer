const CHECKED_CLASS = 'checked';

const initialize = () => {
    const checkboxes = document.querySelectorAll(".checkbox");
    for (const checkbox of checkboxes) {
        checkbox.addEventListener("click", function (event) {
            event.stopPropagation();
            event.preventDefault();
            const isChecked = checkbox.classList.contains(CHECKED_CLASS);
            if (isChecked) {
                checkbox.classList.remove(CHECKED_CLASS)
            } else {
                checkbox.classList.add(CHECKED_CLASS);
            }
        });
    }
}

if (document.readyState === "loading") {
    // Loading hasn't finished yet
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    // `DOMContentLoaded` has already fired
    initialize();
  }

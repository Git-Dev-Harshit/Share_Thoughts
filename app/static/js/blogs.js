document.addEventListener("DOMContentLoaded", function () {
  var dropdownElementList = [].slice.call(
    document.querySelectorAll(".dropdown-toggle")
  );
  var dropdownList = dropdownElementList.map(function (dropdownToggleEl) {
    return new bootstrap.Dropdown(dropdownToggleEl);
  });

  // Optional: Close dropdown when clicking outside
  document.addEventListener("click", function (event) {
    var isDropdownButton = event.target.matches('[data-bs-toggle="dropdown"]');
    if (!isDropdownButton && !event.target.closest(".dropdown")) {
      var dropdowns = document.getElementsByClassName("dropdown-menu show");
      for (var i = 0; i < dropdowns.length; i++) {
        dropdowns[i].classList.remove("show");
      }
    }
  });
});

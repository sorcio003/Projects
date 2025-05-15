function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/lista_libri";
    });
  }

  function deleteWish_List(noteId) {
    fetch("/delete-wish-list", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/wish_list";
    });
  }

// function to set a given theme/color-scheme
function setTheme(themeName) {
  localStorage.setItem('theme', themeName);
  document.documentElement.className = themeName;

  const navbar = document.querySelector('.navbar-toggler');
  if (themeName === 'theme-light') {
    navbar.classList.remove('navbar-light');
    navbar.classList.add('navbar-dark');
  } else {
    navbar.classList.remove('navbar-dark');
    navbar.classList.add('navbar-light');
  }
}

// function to toggle between light and dark theme
function toggleTheme() {
  if (localStorage.getItem('theme') === 'theme-dark') {
      setTheme('theme-light');
  } else {
      setTheme('theme-dark');
  }
}

// Immediately invoked function to set the theme on initial load
(function () {
  if (localStorage.getItem('theme') === 'theme-dark') {
      setTheme('theme-dark');
  } else {
      setTheme('theme-light');
  }
})();


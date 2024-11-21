const loginBtn = document.querySelector("#login");
const logoutBtn = document.querySelector("#logout");
const joinBtn = document.querySelector("#join");
const logo = document.querySelector("body > header > nav > h1");

if (loginBtn !== null) {
  loginBtn.style.cursor = 'pointer';
  loginBtn.addEventListener('click', function() {
    location.href = "/member/login/";
  });
}

if (joinBtn !== null) {
  joinBtn.style.cursor = 'pointer';
  joinBtn.addEventListener('click', function() {
    location.href = "/member/join1/";
  });
}

if (logoutBtn !== null) {
  logoutBtn.style.cursor = 'pointer';
  logoutBtn.addEventListener('click', function() {
    if (confirm("로그아웃 하시겠습니까?")) {
      location.href = "/member/logout/";
    }
  });
}


logo.style.cursor = "pointer";
logo.addEventListener("click", function() {
  location.href = "/";
});
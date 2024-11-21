const submitBtn = document.querySelector("#submitBtn");
const logo = document.querySelector(".logo");
const loginBtn = document.querySelector("body > header > ul > li:nth-child(3)");

submitBtn.addEventListener("click", function() {
  const id = document.querySelector("input[name='id']");
  if (id.value.length < 2) {
    alert("아이디 길이는 2 이상이어야 합니다.");
    return false;
  }
  loginFrm.submit();
});

logo.style.cursor = "pointer";
logo.addEventListener("click", function() {
  location.href = "/";
});

loginBtn.style.cursor = 'pointer';
loginBtn.addEventListener('click', function() {
  location.href = "/member/login/";
});
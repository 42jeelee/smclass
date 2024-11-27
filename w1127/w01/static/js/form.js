$(function() {

  $("#registerBtn").click(function() {
    const id = $("#id").val();
    const pw = $("#pw").val();
    const name = $("#name").val();
    const nickname = $("#nickname").val();
    const tel = $("#tel").val();
    const emsg = $("#emsg");
    
    if (id.length < 2 || pw.length < 2) {
      emsg.text("아이디 또는 비밀번호는 2자 이상 입력하셔야 합니다.");
      return false;
    }
    
    if (name.length == 0 || nickname.length == 0) {
      emsg.text("이름 또는 닉네임은 입력하셔야 합니다.");
      return false;
    }
    
    if (!/^010-?([0-9]{4})-?([0-9]{4})$/.test(tel)) {
      emsg.text("전화번호가 잘못 입력되었습니다. ex) 010-0000-0000");
      return false;
    }

    $("#registerFrm").submit();
  });
  
  $("#loginBtn").click(function() {
    const id = $("#id").val();
    const pw = $("#pw").val();
    const emsg = $("#emsg");

    if (id.length < 2 || pw.length < 2) {
      emsg.text("아이디 또는 비밀번호는 2자 이상 입력하셔야 합니다.");
      return false;
    }

    $("#loginFrm").submit();
  })
  
  $("#cancleBtn").click(function() {
    if ($("#cancleBtn").parent().parent().attr("id") == "registerFrm" && !confirm("지금 나가시면 모든 데이터를 잃습니다. 나가시겠습니까?")) {
      return false;
    }
    location.href = "/";
  });
});
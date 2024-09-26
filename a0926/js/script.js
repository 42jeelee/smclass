// 1. ajax 데이터 가져오기

$(function(){
  let count = 1;
  let id_num = 0;
  let isUpdateForm = false;
  $.ajax({
    url: "js/stuData.json",
    type: "get",
    data: "",
    dataType: "json",
    success:(data)=>{
      for (let i=0;i<data.length;++i){
        $("#tbody").append(`
          <tr id='${count}'>
            <td>${data[i].no}</td>
            <td>${data[i].name}</td>
            <td>${data[i].kor}</td>
            <td>${data[i].eng}</td>
            <td>${data[i].math}</td>
            <td>${data[i].kor+data[i].eng+data[i].math}</td>
            <td>${((data[i].kor+data[i].eng+data[i].math)/3).toFixed(2)}</td>
            <td><button class='updateBtn'>수정</button><button class='delBtn'>삭제</button></td>
          </tr>
        `);
        ++count;
      }
    },
    error:()=>{
      alert("실패");
    }
  });

  $(document).on("click", ".updateBtn", function(){
    if (isUpdateForm) {
      showErrorForm("이미 수정중입니다.");
      return;
    }
    $("#create").hide();
    $("#update").show();
    $("#updateCancel").show();

    let tr = $(this).closest("tr");
    let tds = tr.children();

    id_num = tr.attr("id");
    $("#name").val(tds[1].innerText);
    $("#kor").val(tds[2].innerText);
    $("#eng").val(tds[3].innerText);
    $("#math").val(tds[4].innerText);

    $("html").animate({scrollTop: $("#wrap").offset().top}, 400);
    isUpdateForm = true;
  });

  $(document).on("click", "#update", function(){
    $("#create").show();
    $("#update").hide();
    $("#updateCancel").hide();

    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());

    if ($("#name").val()<1 || $("#kor").val()<1 || $("#eng").val()<1 || $("#math").val()<1){
      showErrorForm("모든 폼을 입력하셔야 합니다.");
      return false;
    }

    $("#"+id_num).html(`
      <td>${id_num}</td>
      <td>${name}</td>
      <td>${kor}</td>
      <td>${eng}</td>
      <td>${math}</td>
      <td>${kor+eng+math}</td>
      <td>${((kor+eng+math)/3).toFixed(2)}</td>
      <td><button class='updateBtn'>수정</button><button class='delBtn'>삭제</button></td>
    `);

    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
    $("#inputError").hide();

    $("html").animate({scrollTop: $("#"+id_num).offset().top - 400}, 400);

    $("#"+id_num).css("background", "skyblue");
    setTimeout(()=>$("#"+id_num).css("background",""), 2000);
    isUpdateForm = false;
  });

  $(document).on("click", "#updateCancel", function(){
    $("#create").show();
    $("#update").hide();
    $("#updateCancel").hide();

    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
    $("#inputError").hide();
    isUpdateForm = false;
  });

  $(document).on("click", ".delBtn", function(){
    let tr = $(this).closest("tr");
    tr.css("background", "pink");
    setTimeout(()=>tr.remove(), 1000);
  });

  $("#create").click(function(){
    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());

    if ($("#name").val()<1 || $("#kor").val()<1 || $("#eng").val()<1 || $("#math").val()<1){
      showErrorForm("모든 폼을 입력하셔야 합니다.");
      return false;
    }
    
    $("tbody").append(`
      <tr>
        <td>${count}</td>
        <td>${name}</td>
        <td>${kor}</td>
        <td>${eng}</td>
        <td>${math}</td>
        <td>${kor+eng+math}</td>
        <td>${((kor+eng+math)/3).toFixed(2)}</td>
        <td><button class='updateBtn'>수정</button><button class='delBtn'>삭제</button></td>
      </tr>
    `);
    $("#inputError").hide();
    ++count;
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
  });

  $("#toTopBtn").click(()=>$("html").animate({scrollTop: 0}, 400));

  function showErrorForm(msg){
    $("#inputError").text(msg);
    $("#inputError").show();
  }

  $(window).scroll(function(){
    if($(this).scrollTop() < 150){
      $("#inputError").css("position", "");
      $("#inputError").css("font-size", "");
    }else{
      $("#inputError").css("position", "fixed");
      $("#inputError").css("top", "10px");
      $("#inputError").css("left", "10px");
      $("#inputError").css("font-size", "16px");
    }
  });
});
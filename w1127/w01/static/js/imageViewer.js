$(function() {
  $("#img-file").change(function() {
    if (this.files && this.files[0]) {
      let reader = new FileReader();
  
      reader.onload = function(e) {
        $("#img-view").css({
          "background-image": `url(${e.target.result})`,
          "background-size": "cover",
          "background-position": "center",
        });
      }
      
      reader.readAsDataURL(this.files[0]);
    } else {
      $("#img-view").removeAttr("style");
    }
  });
});
var sel_file;

        $(document).ready(function() {
            $("#input_img").on("change", handleImgFileSelect);
        });

        function handleImgFileSelect(e) {
            var files = e.target.files;
            var filesArr = Array.prototype.slice.call(files);

            filesArr.forEach(function(f) {
                if(!f.type.match("image.*")) {
                    alert("확장자는 이미지 확장자만 가능합니다.");
                    return;
                }

                sel_file = f;

                var reader = new FileReader();
                reader.onload = function(e) {
                    $("#img").attr("src", e.target.result);
                }
                reader.readAsDataURL(f);
            });
        }
/*
  $(document).ready(function(){
    $("#input_img").on("change", function(e){
      handleImgFileSelect(e);
      let w = $("#img").width();
      console.log(w)
      if ( w > 350) {
        $("#img").width('350px');
      }
      console.log('image changed')
    });

  });

  function handleImgFileSelect(e){
    var files = e.target.files;
    var filesArr = Array.prototype.slice.call(files);

    filesArr.forEach(function(f){
      if(!f.type.match("image.*")){
        alert("확장자는 이미지 확장자만 가능합니다.");
        return;
      }
      sel_file = f;

      var reader = new FileReader();
      reader.onload = function(e){
        $("#img").attr("src", e.target.result);
      }
      reader.readAsDataURL(f);
    });

  }
*/

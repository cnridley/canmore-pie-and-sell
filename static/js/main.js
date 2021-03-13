$(document).ready(function(){
    $('#Sold').hide();
    //Check or Uncheck All checkboxes
   $(".show").click(function(){
       if ($(this).prop("checked") == true){
      $('#Sold').show();
    } else if ($(this).prop("checked") == false) {
        $('#Sold').hide();
    }
    });
});
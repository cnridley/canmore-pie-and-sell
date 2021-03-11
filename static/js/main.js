$(document).ready(function(){
   // Check or Uncheck All checkboxes
   $("#Soldout").change(function(){
     var checked = $(this).is(':checked');
     if(checked){
       $("#Sold").show();
     }else{
       $(".checkbox").hide();
     }
   );
   });
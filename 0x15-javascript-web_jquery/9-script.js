$(document).ready(function(){
  $.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function(data){
    let hello = data.hello;
    $("DIV#hello").text(hello);
  });
});

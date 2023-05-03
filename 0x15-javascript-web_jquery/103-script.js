$(document).ready(function(){
  $('#btn_translate').click(function(){
    let langCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function(data){
      $('#hello').html(data.hello);
    });
  });
  $('#language_code').keypress(function(e){
    if(e.which == 13){
      $('#btn_translate').click();
    }
  });
});

$(document).ready(function(){
  $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data){
    let movies = data.results;
    let list = $("UL#list_movies");
    $.each(movies, function(index, movie){
      list.append(`<li>${movie.title}</li>`);
    });
  });
});

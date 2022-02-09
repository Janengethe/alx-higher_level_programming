$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/4/?format=json', function (response, status) {
    if (status === 'success') {
      $('DIV#character').text(response.name);
    }
  });
});

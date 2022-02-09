$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (response, status) {
    if (status === 'success') {
      $('DIV#hello').text(response.hello);
    }
  });
});

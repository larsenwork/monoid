$(function() {

  function loadTheme(theme) {
    var themeName = $('a[href="#'+ theme +'"]');

    if (themeName.length == 0)
    {
      theme = 'default';
      themeName = $('a[href="#'+ theme +'"]');
    }

    $('link.theme').attr('disabled', true);
    $('link' + '.' + theme).attr('disabled', false);

    $('.scheme').text('Preview: ' + themeName.text() );
  }

  $(window).hashchange( function(){
    var theme = location.hash ? location.hash.replace('#', '') : 'default';
    loadTheme(theme);
  });

  $(window).hashchange();
});

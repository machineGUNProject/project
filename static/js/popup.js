$('.terms_of_use_btn').on('click', function(e) {
  e.preventDefault();
  var el = $($(this).attr('href'));
  if (!el.hasClass('open')) {
    el.addClass('open');
  } else {
    el.removeClass('open');
  }
});

$('.btn_popup_close').on('click', function(e) {
  $(this).closest('.Popup_page').removeClass('open');
});

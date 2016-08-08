$(document).ready(function() {
    var tis = $('.table-of-contents .list-group-item');

    $(document).scroll(function() {
      if (!$(window).scrollTop())
        $(tis).removeClass('last-clicked');
    });

    $(tis).click(function() {
      $(tis).removeClass('last-clicked');
      $(this).addClass('last-clicked');
    });
});

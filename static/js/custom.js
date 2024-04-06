$(window).scroll(function () {
    let $height = $(window).scrollTop();

    if ($height > 70) {
        $('#main-nav').addClass('sticky-custom');
    } else {
        $('#main-nav').removeClass('sticky-custom');
    }
});


$(document).ready(function () {

    $('#menu-click').click(function (e) {
        e.preventDefault();
        $('#sidebar-wrapper').toggleClass('toggled');
        $('.overlay-menu').toggleClass('d-block');
    });

    $('.overlay-menu').click(function (e) {
        e.preventDefault();
        $('.overlay-menu').toggleClass('d-block');
        $('#sidebar-wrapper').toggleClass('toggled');
    });

    $('.close-menu').click(function (e) {
        e.preventDefault();
        $('.overlay-menu').toggleClass('d-block');
        $('#sidebar-wrapper').toggleClass('toggled');
    });

    $('#click-search').click(function (e) {
        e.preventDefault();
        $('#mainNav').addClass('search-open');
        $('.overlay-search').addClass('d-block');
    });
    
    $('.overlay-search').click(function (e) {
        e.preventDefault();
        $('#mainNav').removeClass('search-open');
        $('.overlay-search').removeClass('d-block');
    });

    $('#sidebar-wrapper .supermenu-activo').click(function () {
        $(this).toggleClass('abierto');
    })

});



//function persiaNumber() {
//    jQuery('*').persiaNumber({});
//}



function owlslider() {
    jQuery('#owl-slider').owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        autoplayTimeout: 8000,
        animateOut: 'fadeOut',
    });
}

function owlproduct() {
    jQuery('#owl-Services').owlCarousel({
        items: 8,
        loop: true,
        nav: true,
        autoplay: true,
        smartSpeed: 1000,
        autoplayTimeout: 3000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 2
            },
            356: {
                items: 3
            },
            454: {
                items: 4
            },
            552: {
                items: 5
            },
            768: {
                items: 4
            },
            935: {
                items: 5
            },
            992: {
                items: 3
            },
            1068: {
                items: 4
            },
            1303: {
                items: 5
            }
        }
    });
}

function owlPopular() {
    jQuery('#owl-Popular').owlCarousel({
        items: 6,
        loop: true,
        nav: true,
        autoplay: true,
        smartSpeed: 1000,
        autoplayTimeout: 5000,
        responsiveClass: true,
        responsive: {
            0: { items: 2 },
            338: { items: 3 },
            480: { items: 4 },
            550: { items: 5 },
            768: { items: 3 },
            1200: { items: 3 }
        }
    });
}

function owlDoctors() {
    jQuery('#owl-Doctors').owlCarousel({

        items: 8,
        loop: true,
        autoplay: true,
        smartSpeed: 1000,
        autoplayTimeout: 5000,
        nav: true,


        responsiveClass: true,
        responsive: {
            0: { items: 1 },
            500: { items: 2 },
            660: { items: 3 },
            880: { items: 4 },
            992: { items: 3 },
            1300: { items: 4 }
        }
    });
}



/*************************
All function are called here 
*************************/
$(document).ready(function () {

    //persiaNumber(),
    owlslider(),
    owlproduct(),
    owlPopular(),
    owlDoctors();

});



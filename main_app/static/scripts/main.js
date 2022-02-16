$(".navbar-burger").click(function () {
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
    });
    $(".dropdown").click(function (event) {
    $(this).toggleClass("is-active");
    });

$cartoonbg = $(".cartoon");
$planetsbg = $(".planets");
$starsbg = $(".stars")
$catsbg = $(".cats")
$tacosbg = $(".tacos")
$vaporwavebg = $(".vaporwave")

function vaporwave() {
    $(".postdetails").css({"backgroundImage": "url('https://as1.ftcdn.net/v2/jpg/02/69/54/06/500_F_269540608_E4kaGPd1OkzEN46Y8iSabWwWV8Cjrz6v.jpg')"});
}
function planets() {
    $(".postdetails").css({"backgroundImage": "url('https://st3.depositphotos.com/12371120/19349/i/450/depositphotos_193493152-stock-photo-colorful-watercolor-planets-seamless-pattern.jpg')"});
}
function stars() {
    $(".postdetails").css({"backgroundImage": "url('https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/universe-with-planets-and-stars-seamless-pattern-cosmos-starry-night-sky-jelena-obradovic.jpg')"});
}
function cartoon() {
    $(".postdetails").css({"backgroundImage": "url('https://static.vecteezy.com/system/resources/previews/003/207/722/non_2x/colorful-space-planet-seamless-pattern-in-cartoon-style-vector.jpg')"});
}
function cats() {
    $(".postdetails").css({"backgroundImage": "url('https://static.vecteezy.com/system/resources/thumbnails/000/674/924/small/PATTERN-0004.jpg')"});
}
function tacos() {
    $(".postdetails").css({"backgroundImage": "url('https://i.pinimg.com/736x/c3/30/81/c330810cb9b271a715270fabdab59ff8.jpg')"});
}
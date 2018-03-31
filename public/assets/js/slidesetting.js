/**
 * Created by liuchen on 2016年7月28日22:03:46.
 */
function showpic(showindex) {
    $('#slider').find('a').each(function (index, element) {
        if (index == showindex) {
            $(".bullets span").eq(index).addClass("active");
            $(element).fadeIn(250);
        } else {
            $(".bullets span").eq(index).removeClass("active");
            $(element).fadeOut(250);
        }
    });
}
var indexpic = 0;
var totalnum = $(".bullets span").length;
$(document).ready(function () {
    showpic(0);
    var interval = setInterval("play()", 5000);
    $(".bullets").click(function (e) {
        var index = $(e.target).index();
        showpic(index);
        indexpic = index;
    });

    $("#slider").hover(function () {
        clearInterval(interval);
    }, function () {
        interval = setInterval("play()", 5000);
    })
});
function play() {
    indexpic++;
    indexpic %= totalnum;
    showpic(indexpic);
}
$("#search").click(function () {
    var content = $("#s-content").val();
    location.href = "search/q?content=" + content
});

$('#s-content').keypress(function (e) {
    if (e.which == 13) {
        $('#search').click();
    }
});
$(function () {
    $('.del').click(function (e) {
        if (!confirm('确定删除文章？')) {
            return;	
        }
        var target = $(e.target);
        var date = target.siblings("td").eq(2).text();
        var title_en = target.siblings("td").eq(3).text();
        $.ajax({
                type: 'DELETE',
                url: '/admin/posts/?title_en=' + title_en + '&date=' + date
            })
            .done(function (results) {
                if (results.success === 1) {
                    if (target.parent().length > 0) {
                        target.parent().remove()
                    }
                }
            })
    });

    $('#add-new-post').on('click', function () {
        window.location.href = '/admin/addpost';
    })
});
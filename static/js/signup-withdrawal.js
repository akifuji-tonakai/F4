$(function () {
    $('.agree').click(function () {
        if ($('.agree').prop('checked')) {
            $('#submit').prop('disabled', false);
        } else {
            $('#submit').prop('disabled', true);
        }
    });
});

$(function () {
    $('#withdrawal').on('click', function () {
        alert('退会しました')
    });
});

$(function () {
    $('.pc-image').click(function () {
        var imgData = $('[data-pc-img]').data('pc-img')
        var imgNow = parseInt(imgData)
        $(this).addClass('hidden')
        imgNow++;
        if (imgNow === 5) {
            var imgNext = 1
        } else {
            var imgNext = imgNow
        }
        $('#pc-image' + imgNext).removeClass('hidden')
        $('[data-pc-img]').data('pc-img', imgNext)

    });


});

$(function (){
    $('.and-image').click(function (){
        var thisId = $(this).prop('id')
        $(this).toggle()
        if (thisId === "and-image1") {
            $('#and-image2').toggle()
        } else {
            $('#and-image1').toggle()
        }
    })
})


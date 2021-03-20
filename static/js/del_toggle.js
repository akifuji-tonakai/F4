$(function (){
    $('.del-toggle').on('click', function (){
        $('.del-check-box').toggle()
        $('.del-submit').toggle()
        $(this).toggle()
    })
})
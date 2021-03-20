// 同意ボタンon-offで送信ボタンable-disable
$(function () {
    $('.agree').click(function () {
        if ($('.agree').prop('checked')) {
            $('#submit').prop('disabled', false);
            $('.confirm-select').css('display', 'flex');
        } else {
            $('#submit').prop('disabled', true);
            $('.confirm-select').css('display', 'none');
        }
    });
});

// 画像をクリックすると、下の確認画面に格納される
$(function (){
    $('.image').on('click', function (){
        if ($(this).hasClass('un-click')){
            $(this).removeClass('un-click').addClass('click-border');
            // フェイクdivを使い、画像の縦幅を保持させる　(別の画像の縦幅に依存させない ＝これをしないとconfirm-selectの縦に依存するため)
            $('.confirm-select').append('<div class="fake">');
            $(this).clone('false').addClass('mirror').removeClass('click-border image').appendTo($('.fake'));
            $('.fake').removeClass('fake');
            // classフェイクを消す
        } else if ($(this).hasClass('click-border')){
            $(this).removeClass('click-border').addClass('un-click');
            var thisId = $(this).attr('id');
            $('.confirm-select').find('#'+ thisId).remove();
        }
    });
});

// 下にクローンが表示された　それをクリックすると上のボタンと連動して消える
$(function (){
    // $('.mirror').click(function(){
    $(document).on('click', '.mirror', function(){
        var mirrorId = $(this).attr('id');
        $('.choice-box').find('#'+ mirrorId).removeClass('click-border').addClass('un-click');
        // チェックボックスもチェックが外れる
        $('.choice-box').find('#choice'+ mirrorId ).prop("checked", !$('#choice'+mirrorId).prop("checked"));
        $(this).remove();
    });
});

// $(function(){
//     console.log($('.image').length)
// });
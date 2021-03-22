$(function(){
    // dom取得
    var totalManageElement = $('input#id_chara_set-TOTAL_FORMS');
    // valueをintに
    var currentFileCount = parseInt(totalManageElement.val());
    $('button#add').on('click', function(){


         var nameElement = $('<input>', {
            type: 'text',
            name: 'chara_set-' + currentFileCount + '-chara_name',
            id: 'id_chara_set-' + currentFileCount + '-chara_name',
            maxlength: '10'
        });
        var labelChara = $('<label />', {
            for: 'id_chara_set-' + currentFileCount + '-chara_name',
        }).append('キャラ名：');

         var pChara = $('<p>').append(labelChara, nameElement);



        var fileElement = $('<input>', {
            type: 'file',
            name: 'chara_set-' + currentFileCount + '-photo',
            accept: 'image/*',
            id: 'id_chara_set-' + currentFileCount + '-photo',
        });
        var fileHidden1 = $('<input>', {
            type: 'hidden',
            name: 'chara_set-' + currentFileCount + '-content',
            id: 'id_chara_set-' + currentFileCount + '-content',
        });
        var fileHidden2 = $('<input>', {
            type: 'hidden',
            name: 'chara_set-' + currentFileCount + '-id',
            id: 'id_chara_set-' + currentFileCount + '-id',
        });
        var labelPhoto = $('<label />', {
            for: 'id_chara_set-' + currentFileCount + '-photo',
        }).append('キャラ画像：');

        var pPhoto = $('<p>').append(labelPhoto, fileElement, fileHidden1, fileHidden2);


        var labelSubclass = $('<label />', {
            for: 'id_chara_set-' + currentFileCount + '-subclass'
        }).append('サブクラス：');
        var preSelect = $('select#id_chara_set-0-subclass').children('option').clone(false)
        var boxSelect = $('<select>',{
            name: 'chara_set-' + currentFileCount + '-subclass',
            id: 'id_chara_set-' + currentFileCount + '-subclass',
        }).append(preSelect);
        var selectHidden1 = $('<input>',{
            type: 'hidden',
            name: 'chara_set-' + currentFileCount + '-content',
            id: 'id_chara_set-' + currentFileCount + '-content',
        });
        var selectHidden2 = $('<input>',{
            type: 'hidden',
            name: 'chara_set-' + currentFileCount + '-id',
            id: 'id_chara_set-' + currentFileCount + '-id',
        });

        var pSubclass = $('<p>').append(labelSubclass, boxSelect, selectHidden1, selectHidden2)


        $('form').append(pChara, pPhoto, pSubclass, '<hr>')
        $('#submit').addClass('mirror').clone(false).removeClass('mirror').appendTo('form')
        $('.mirror').remove()
        setTimeout(function() {
        window.scroll(0,$(document).height());
        },0);

        currentFileCount++;
        totalManageElement.attr('value', currentFileCount);
    });
});

// $(function(){
//      var totalManageElement = $('input#id_chara_set-TOTAL_FORMS');
// //     // valueをintに
//      var currentFileCount = parseInt(totalManageElement.val());
//      $('button#add').on('click', function(){
//          currentFileCount++;
//          totalManageElement.val(currentFileCount);
//      })
// })
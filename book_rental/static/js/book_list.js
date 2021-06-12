// book_noを付与
function book_no_assignment(cont_type ,book_no='') {
    // 削除処理の場合
    if(cont_type == 'del'){
      var element = document.getElementById("del_no");
      book_no = element.name;
    }

    const form = document.getElementById("bookListForm");
    // エレメントを作成
    var ele = document.createElement('input');
    // データを設定
    ele.setAttribute('type', 'hidden');
    ele.setAttribute('name', 'book_no');
    ele.setAttribute('value', book_no);
    // 要素を追加
    form.appendChild(ele);
    // エレメントを作成
    var ele2 = document.createElement('input');
    // データを設定
    ele2.setAttribute('type', 'hidden');
    ele2.setAttribute('name', 'cont_type');
    ele2.setAttribute('value', cont_type);
    // 要素を追加
    form.appendChild(ele2);
    // 送信
    form.submit();
}

//削除モーダル
function book_delete(cont_type ,book_no='') {
    $("#del_pk").text(book_no);
    var element = document.getElementById("del_no");
    element.name = book_no;
}

window.onload = function() {
    // selectタグ選択
    var value = document.getElementById("search_key_temp").value;
    if(value){
        var select = document.getElementById("search_key");
        if(value.indexOf('book_no') != -1){
            select.options[1].selected = true;
        } else if(value.indexOf('name') != -1){
            select.options[2].selected = true;
        } else if(value.indexOf('publisher') != -1){
            select.options[3].selected = true;
        } else if(value.indexOf('category') != -1){
            select.options[4].selected = true;
        }
    }
}
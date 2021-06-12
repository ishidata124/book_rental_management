// book_noを非活性
window.onload = function() {
    document.getElementById("id_book_no").setAttribute("disabled", true);
}

// 送信
function book_edit_submit() {
    const form = document.getElementById("bookForm");
    document.getElementById("id_book_no").removeAttribute("disabled");
    // 送信
    form.submit();
}

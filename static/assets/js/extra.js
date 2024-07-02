function comment(comment_id) {
    $('#comment_hidden').val(comment_id);
    document.getElementById('comment_form').scrollIntoView({behavior:'smooth'})
}
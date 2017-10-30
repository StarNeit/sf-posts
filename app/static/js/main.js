$(function() {
    $('#get_posts_basic').bind('click', function(e) {
        if ($('#user_id').val().trim().length == 0){
            alert("Please input Stackoverflow User ID");
            $('#user_id').focus();
            return;
        }
        $('#main-form').attr('action', "/success_basic_mission");
        $('#main-form').submit();
    });
    $('#get_posts_oauth').bind('click', function(e) {
        if ($('#user_id').val().trim().length == 0){
            alert("Please input Stackoverflow User ID");
            $('#user_id').focus();
            return;
        }
        $('#main-form').attr('action', "/success_oauth_mission");
        $('#main-form').submit();
    });
  });
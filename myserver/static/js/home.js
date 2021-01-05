function home()
{
    var user_id = document.getElementsByName("user_id")
    var s2 = ""
    s2 = s2.concat("http://127.0.0.1:8000/polls/" ,user_id[0].innerHTML)
    window.location.href=s2;
}
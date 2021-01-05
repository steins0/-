function jumpurl(num)
{
    var user_id = document.getElementsByName("user_id")
    var id = document.getElementById(num);
    //console(id.innerHTML)
    //console.log(user_id[0].innerHTML)
    //console.log(id.innerHTML)
    var s2 = ""
    s2 = s2.concat("http://127.0.0.1:8000/polls/movie/" , id.innerHTML,"/",user_id[0].innerHTML);
    console.log(s2)
    window.location.href=s2;
}
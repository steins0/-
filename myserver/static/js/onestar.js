
function onestar(num)
{
    var user_id = document.getElementsByName("user_id")
    //console.log(user_id[0].innerHTML)
    var movie_id = document.getElementsByName("movie_id")
    //console.log(movie_id[0].innerHTML)
    var s2 = ""
    s2 = s2.concat("http://127.0.0.1:8000/polls/movie/" , movie_id[0].innerHTML,"/",user_id[0].innerHTML,"/",num);
    window.location.href=s2
    //alert(s2)
}
function osnestar()
{
    alert("一星")
    window.location.href="http://127.0.0.1:8000/polls/movie/1/2/20";
}
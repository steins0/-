function login()
{
    var username = document.getElementById("username");
    var password = document.getElementById("password");

    if (username.value == "")
    {
        alert("请输入用户名");
    }
    else if(username.value == "admin" && password.value == "123456")
    {
        window.location.href="index.html";
    }
    else{
        alert("错误，请重试");
    }
}

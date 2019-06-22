
function localfunc(data)
{
    console.log("this is local func.");
    console.log("data is:" + data);
}

function test_jsonp()
{
	var callback = "localfunc"
	var fullURL = "http://127.0.0.1:5000/getCheatUsers/" + callback;
	var script = document.createElement('script');
  	script.setAttribute('src', fullURL);
  	document.getElementsByTagName('head')[0].appendChild(script); 
}

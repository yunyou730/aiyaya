var baseUrl = "http://gj1111myl:3031"
var widgetUidMap = new Array();

function initView()
{
	document.getElementById("sample_uid_cell").style.visibility = "hidden"
	checkEnable();
}

function jsonp(url)
{
	var script = document.createElement('script');
  	script.setAttribute('src', url);
  	document.getElementById("req").appendChild(script);
}

function getFullUrl(url)
{
	return baseUrl + url;
}

function checkEnable()
{
	var url = getFullUrl("/checkEnable/check_callback");
	jsonp(url);
}

function toggle()
{
	var url = getFullUrl("/toggle/check_callback");
	jsonp(url);	
}

function viewUid()
{
	console.log("view uid");
	var url = "/getList/view_callback"
	url = getFullUrl(url);
	jsonp(url,"view_callback");
}

function addUid()
{
	var uid = document.getElementById("new_uid").value
	console.log("new uid:" + uid)
	if(uid != "")
	{
		url = "/add/" + uid + "/add_callback"
		url = getFullUrl(url);
		jsonp(url,"add_callback");
	}
	else
	{
		alert("empty uid")
	}
}

function remUid(uid)
{
	var url = getFullUrl("/rem/" + uid + "/rem_callback");
	jsonp(url);
}

function logout()
{
	var url = getFullUrl("/logout/logout_callbak");
	jsonp(url);
}

function add_callback(resp)
{
	if(callback_prehandler(resp))
	{
		return;
	}
	document.getElementById("new_uid").value = "";
	refresh_list(resp);
}

function view_callback(resp)
{
	if(callback_prehandler(resp))
	{
		return;
	}	
	refresh_list(resp);
}

function rem_callback(resp)
{
	if(callback_prehandler(resp))
	{
		return;
	}	
	refresh_list(resp);
}

function check_callback(resp)
{
	if(callback_prehandler(resp))
	{
		return;
	}	
	refreshEnable(resp);
}

function logout_callbak(resp)
{
	window.location.href = "./login.html"
}

function refreshCell(cell,uid)
{
	widgetUidMap[cell.id] = uid;
	var label = cell.getElementsByTagName("label")[0]
	label.innerHTML = "uid:" + uid;
	var remfunc = function()
	{
		remUid(uid);
	}
	var btn = cell.getElementsByTagName("button")[0];
	btn.onclick = remfunc;
}

function refreshEnable(enableFlag)
{
	var div = document.getElementById("enable_state");
	div.innerHTML = enableFlag;
}

function refresh_list(uids)
{
	console.log(uids);
	var listView = document.getElementById("uid_listview");
	listView.innerHTML = "";
	var cellSample = document.getElementById("sample_uid_cell");

	listView.innerHTML = "";	// clear

	var uidCounter = 0;
	for(var uid in uids)
	{
		var cellId = "cell_" + uidCounter;
		var cloneCell = document.getElementById(cellId);
		if (cloneCell == null)
		{
			cloneCell = cellSample.cloneNode(true);	
			listView.appendChild(cloneCell);			

			cloneCell.id = cellId;
			cloneCell = document.getElementById(cellId);
			cloneCell.style.visibility = "visible"

			refreshCell(cloneCell,uid);
		}
		uidCounter++;
	}
}

function callback_prehandler(resp)
{
	console.log(resp);
	if(resp["not_login"])
	{
		alert("not login!");
		window.location.href = "./login.html"
		return true;	
	}
}


var urlInput = $('urlPlay')[0];
var str = $('#st')[0];
var en = $('#end')[0];
var sta = $('#sta')[0];
var endt = $('#endt')[0];
function IdGetter(url)
{
	return url.split('v=')[1];
};
function PlayVideo()
{
	$('#StartEnd').slideUp(2000);
	document.getElementById('playerDiv').style.display = 'block';
	document.getElementById('1').style.display = 'none';
	document.getElementById('2').style.display = 'none';
	var player = $('#iframe')[0];
	player.setAttribute('src','http://www.youtube.com/embed/'+IdGetter($('#urlPlay').val())+"?autoplay=1"); 
};
function PlayVideoLoop()
{
	document.getElementById('playerDiv').style.display = 'block';
	document.getElementById('1').style.display = 'none';
	document.getElementById('2').style.display = 'none';
	var player = $('#iframe')[0];
	player.setAttribute('src','http://www.youtube.com/embed/'+IdGetter($('#urlPlay').val())+"?autoplay=1&loop=1&playlist="+IdGetter($('#urlPlay').val())); 
};

function PlayStart(start,end)
{
	$(Starter).slideUp(2000);
	document.getElementById('playerDiv').style.display = 'block';
	document.getElementById('1').style.display = 'none';
	document.getElementById('2').style.display = 'none';
	var player = $('#iframe')[0];
	player.setAttribute('src','http://www.youtube.com/embed/'+IdGetter($('#urlPlay').val())+"?autoplay=1&start="+$('#st').val()+"&end="+$('#end').val()); 
};
function Fader()
{
	$('#StartEnd').slideDown(2000);
};
function Fader2()
{
	$('#StartEnd').slideUp(2000);
	$('#Starter').slideDown(2000);
};
function AjaxDeleteSuriLocal()
{
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/url/delete/local',
		data:$('#suri-delete-url-local').serialize(),
		success: function(response)
		{
			//AjaxGetAllPlayLists();
			location.reload();
		},
		error:function(response)
		{
			alert('cant delete the url');
		},
	});
};

function AjaxGetAllPlayLists()
{
	$.ajax({
		type:'GET',
		url: 'http://127.0.0.1:5000/api/playlist/getap',
		success: function(response)
		{
			$('container_body').html = response;
		},
		error:function(response)
		{
			alert('you are not logged in');
			console.log('Error');
		},
	});
};
function AjaxAdder()
{
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/addurl/global',
		data:$('#AddFL').serialize(),
		success: function(response)
		{
			console.log('added');
			location.reload();
			//AjaxGetAllPlayLists();
		},
		error:function(response)
		{
			alert('check the details of the url');
			console.log(response);
		},
	});
};
function AjaxEditSuri()
{
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/playlist/edit',
		data:$('#suri-edit').serialize(),
		success: function(response)
		{
			location.reload();
			//AjaxGetAllPlayLists();
		},
		error:function(response)
		{
			alert('check the details of the playlist');
			console.log(response);
		},
	});
};
function AjaxAddSuri()
{
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/addurl/local',
		data:$('#suri-adder').serialize(),
		success: function(response)
		{
			location.reload();
			//AjaxGetAllPlayLists();
		},
		error:function(response)
		{
			alert('check the details of the url');
			console.log(response);
		},
	});
};
function AjaxDeleteSuri()
{
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/playlist/delete',
		data:$('#suri-delete').serialize(),
		success: function(response)
		{
			location.reload();
			//AjaxGetAllPlayLists();
		},
		error:function(response)
		{
			console.log(response);
		},
	});
};
function AjaxEditUrlglobal()
{
	console.log('yes1')
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/url/edit/global',
		data : $('#suri-edit-url-global').serialize(),
		success:function(response)
		{
			location.reload();
			//AjaxGetAllPlaylists();
		},
		error:function(response)
		{
			alert('check the details of the url you are editing');
			console.log(response);
		},
	});
	console.log('yes2')
};
function AjaxDeleteUrlglobal()
{
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/url/delete/global',
		data : $('#suri-delete-url-global').serialize(),
		success:function(response)
		{
			location.reload();
			//`AjaxGetAllPlaylists();
		},
		error:function(response)
		{
			alert('check the details of the url');
			console.log(response);
		},
	});
};
function AjaxDeleteUrllocal()
{
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/url/delete/local',
		data : $('#suri-delete-url-local').serialize(),
		success:function(response)
		{
			location.reload();
			//AjaxGetAllPlaylists();
		},
		error:function(response)
		{
			alert('check the details of the url');
			console.log(response);
		},
	});
};
function PlayListAdder()
{
	$.ajax({
		type:'POST',
		url:'http://127.0.0.1:5000/api/playlist/create',
		data:$('#creator').serialize(),
		success: function(response)
		{
			location.reload();
			//AjaxGetAllPlayLists();
		},
		error:function(response)
		{
			alert('check the details of the playlist');
			console.log(response);
		},
	});
};

function PlayListImages(arr,tableId,titles)
{
	var table = document.getElementById(tableId);
	var k=0;
	var i;
	var str = ''; 
	str+='<table>';
	for(j=6;j<arr.length;j+=6){
		str+='<tr>';
		for(i=j-6;i<j;i++)
		{
			arr[i] = IdGetter(arr[i]);
			str+='<td><img onclick="resize()" src='+"http://img.youtube.com/vi/"+arr[i]+"/0.jpg id=";
			str+=arr[i]+'suri'+tableId+' style='+'margin:20px;height:125px;width:175px'+'><br/>';
			str+='<div align='+'center'+'>'+'<h3>'+titles[i]+'</h3>'+'</div>';
			str+='</td>';
		}
		str+='</tr>';
		k+=6;
	}
	console.log("plist-yes")
	str+='<tr>';
	while(k<arr.length){
		arr[k] = IdGetter(arr[k]);
		str+='<td><img onclick="resize()" src='+"http://img.youtube.com/vi/"+arr[k]+"/0.jpg id=";
		str+=arr[k]+'suri'+tableId+' style='+'margin:20px;height:125px;width:175px'+'><br/>';
		str+='<div align='+'center'+'>'+'<h3>'+titles[k]+'</h3>'+'</div>';
		str+='</td>';
		k++;
	}
	str+='</tr></table>';
	table.innerHTML = str;
	addListeners(arr,tableId);
	console.log("plist-yes2")
};
function PlayAll(arr)
{
	var str = '';
	for(var i=0;i<arr.length;i++)
		str+=arr[i]+',';
	document.getElementById('playerDiv').style.display = 'block';
	$('#all').slideUp(2000);
	var player = $('#iframe')[0];
	player.setAttribute('src','http://www.youtube.com/embed/'+arr[0]+"?autoplay=1&playlist="+str); 
};
function recent_modify(id)
{
	obj={'url_id': id};
	$.ajax({
		type:'POST',
		url:'http://127.0.0.1:5000/api/url/modify',
		data:obj,
		success: function(response)
		{
			location.reload();
		},
		error:function(response)
		{
			//alert('check the details of the playlist');
			console.log(response);
		},
	});
};


function addListeners(arr,tableId)
{
	for(i=0;i<arr.length;i++)
	{
		var a = document.getElementById(arr[i]+'suri'+tableId);
		a.addEventListener('click',
			function()
			{
				document.getElementById('playerDiv').style.display = 'block';
				document.getElementById('Next').style.display = 'block';
				var player = $('#iframe')[0];
				player.setAttribute('src','http://www.youtube.com/embed/'+this.id.split('suri')[0]+"?autoplay=1");
			});
		a.addEventListener('mouseover',
			function()
			{
				document.getElementById(this.id).style.cursor = 'pointer';
			});
	}
};
function slider()
{	
	$('#custom').slideUp(2000);
};
function formShower()
{
	$('#surendra').slideDown(2000);
};
function SelectPopulator(id,obj)
{
	var str = '';
	for(var i in obj)
		str+='<option selected='+'"selected"'+'>'+i+'</option>';
	document.gerElementById(id).innerHTML = str;
}
function Search(arr_titles,arr_urls)
{
	var val = $('#search-item').val();
	val = val.trim();
	for(i=0;i<arr_titles.length;i++)
		for(j=0;j<arr_titles.length;j++)
		if(arr_titles[i][j] == val)
	{
		document.getElementById('playerDiv').style.display = 'block';
		document.getElementById('1').style.display = 'none';
		document.getElementById('2').style.display = 'none';
		var player = $('#iframe')[0];
		player.setAttribute('src','http://www.youtube.com/embed/'+IdGetter(arr_urls[i][j])+"?autoplay=1"); 
		return;
	};
}
function Next(arr_urls,arr_titles)
{
	var val = document.getElementById('iframe').src;
	val = val.split('/embed')[1];
	val = val.split('?')[0];
	val = val.split('/')[1];
	val = 'https://www.youtube.com/watch?v='+val;
	for(i=0;i<arr_titles.length;i++)
		for(j=0;j<arr_titles.length;j++)
		if(arr_urls[i][j] == val && j != arr_urls[i].length-1)
	{
		document.getElementById('playerDiv').style.display = 'block';
		document.getElementById('1').style.display = 'none';
		document.getElementById('2').style.display = 'none';
		var player = $('#iframe')[0];
		player.setAttribute('src','http://www.youtube.com/embed/'+IdGetter(arr_urls[i][j+1])+"?autoplay=1"); 
		return;
	}
	else if(arr_urls[i][j] == val)
	{
		alert('You Have Already reached the last video');
	}
}
function Previous(arr_urls,arr_titles)
{
	var val = document.getElementById('iframe').src;
	val = val.split('/embed')[1];
	val = val.split('?')[0];
	val = val.split('/')[1];
	val = 'https://www.youtube.com/watch?v='+val;
	for(i=0;i<arr_titles.length;i++)
		for(j=0;j<arr_titles.length;j++)
		if(arr_urls[i][j] == val && j != 0)
	{
		document.getElementById('playerDiv').style.display = 'block';
		document.getElementById('1').style.display = 'none';
		document.getElementById('2').style.display = 'none';
		var player = $('#iframe')[0];
		player.setAttribute('src','http://www.youtube.com/embed/'+IdGetter(arr_urls[i][j-1])+"?autoplay=1"); 
		return;
	}
	else if(arr_urls[i][j] == val)
	{
		alert('You are watching the first video');
	}
}
function PlayerClose()
{
	var val = document.getElementById('iframe').src;
	val = val.split('/embed')[1];
	val = val.split('?')[0];
	val = val.split('/')[1];
	val = 'https://www.youtube.com/watch?v='+val;
	recent_modify(val);
	document.getElementById('iframe').src = '';
	location.reload(); 
}
$(document).ready(
	function()
	{
		$.ajax({
			type:'GET',
			url:'http://127.0.0.1:5000/api/get',
			success: function(response)
			{
				AutoPopulate(response);
			},
			error:function(response)
			{
				console.log(response);
			},
		});
	}
);
function AutoPopulate(obj)
{
	console.log(obj['urls'],' ',obj['id'].length,' ',obj['names']);
	for(var i=0;i<obj['id'].length;i++)
	{
		console.log('i: ',i,' ',obj['urls'][i],' ',obj['id'][i],' ',obj['names'][i]);
		PlayListImages(obj['urls'][i],obj['id'][i],obj['names'][i]);
	}
	return;
}

function resize(){
	var x = $(document).height();
	$("#lefty").height(x);
}

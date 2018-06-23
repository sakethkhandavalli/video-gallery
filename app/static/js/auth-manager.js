var enter = function()
{
	$.ajax({
		type:'GET',
		url: '/api/playlist/getap',
		success: function(response)
		{
			$(".fade").hide();
		//	$('#container_body').html(response);
			console.log('hello world');
			window.location.href='/api/playlist/getap';
		},
		error:function(response)
		{
			console.log(response);
		},
	});
};

var login = function ()
{

	$.ajax({
		type:'POST',
		url: '/api/login',
		data:$('#login').serialize(),
		success: function(response)
		{
			enter();
			console.log('hello world');
			return response;
		},
		error:function(response)
		{
			alert('invalid credentials');
			console.log(response);
		},
	});
};

/*var showlogin = function ()
{

	$.ajax({
		type:'GET',
		url: '/api/showlogin',
		success: function(response)
		{
			$('#container_login').html(response);
		},
		error:function(response)
		{
			console.log(response);
		},
	});
};*/

var showhome = function()
{
	$.ajax({
		type:'GET',
		url: '/api/front',
		success: function(response)
		{
			$('#container_body').html(response);
			$('#container_login').html(null);
			console.log('yes');
		},
		error:function(response)
		{
			console.log(response);
		},
	});
};
var showroot = function()
{
	$.ajax({
		type:'GET',
		url: '/api/front',
		success: function(response)
		{
			window.location.href='/';
			$('#container_body').html(response);
			$('#container_login').html(null);
			console.log('yes');
		},
		error:function(response)
		{
			console.log(response);
		},
	});
};
var autorun = function()
{
	showhome();
}();


var register = function ()
{

	$.ajax({
		type:'POST',
		url: '/api/register',
		data:$('#register').serialize(),
		success: function(response)
		{
			console.log(response);
		},
		error:function(response)
		{
			alert('check the details');
			console.log(response);
		},
	});
};

/*var showregister = function()
{
	$.ajax({
		type:'GET',
		url:'/api/showregister',
		success: function(response)
		{
			$('#container_login').html(response);
		},
		error:function(response)
		{
			console.log(response,"yes");
			console.log(response);
		},
	});
};*/

var logout = function () 
{
    $.ajax({
       	type: 'POST', 
        url: '/api/logout',
        success: function (response) 
	{
//        	loginState = null;        	
		console.log("logged out");
		showroot();
        },
	error: function(response)
	{
		alert('didnt logout');
		console.log("error");
	},
    });

}

var all = function()
{
	$.ajax({
		type:'GET',
		url:'/api/show',
		success: function(response)
		{
			$('#container_body').html(response);
		},
		error:function(response)
		{
			console.log(response,"yes");
		},
	});
};

var enter_playlist = function()
{
	$.ajax({
		type:'GET',
		url: 'http://127.0.0.1:5000/api/playlist/single',
		data : ('#goto-playlist').serialize(),
		success: function(response)
		{
			$(".fade").hide();
		//	$('#container_body').html(response);
			console.log('hello world');
			window.location.href='/api/playlist/single';
		},
		error:function(response)
		{
			console.log(response);
		},
	});
};

function AjaxRenderPlaylist()
{
//	obj={'playlist_id':id};
	$.ajax({
		type:'POST',
		url: 'http://127.0.0.1:5000/api/playlist/call',
	//	data:obj,
		data : $('#goto-playlist').serialize(),
		success: function(response)
		{
			enter_playlist();
			return response;
		},
		error:function(response)
		{
			console.log('Error');
		},
	});
};

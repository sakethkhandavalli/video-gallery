function GetImages(arr,tableId,titles)
{
	var table = document.getElementById(tableId);
	var k=0;
	var str = ''; 
	str+='<table>';
	for(j=6;j<arr.length;j+=6){
		str+='<tr>';
		for(var i=j-6;i<j;i++)
		{
			arr[i] = IdGetter(arr[i]);
			str+='<td><img src='+"http://img.youtube.com/vi/"+arr[i]+"/0.jpg id=";
			str+=arr[i]+' style='+'margin:20px'+'><br/>';
			str+='<div align='+'center'+'>'+'<h3>'+titles[i]+'</h3>'+'</div>';
			str+='</td>';
		}
		str+='</tr>';
		k+=6;
	}
	str+='<tr>';
	while(k<arr.length){
			arr[i] = IdGetter(arr[i]);
			str+='<td><img src='+"http://img.youtube.com/vi/"+arr[i]+"/0.jpg id=";
			str+=arr[i]+' style='+'margin:20px'+'><br/>';
			str+='<div align='+'center'+'>'+'<h3>'+titles[i]+'</h3>'+'</div>';
			str+='</td>';
			k++;
	}
	str+='</tr></table>';
	table.innerHTML = str;
	addListeners(arr);
};

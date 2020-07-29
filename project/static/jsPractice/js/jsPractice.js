function changeImage()
	{
		element=document.getElementById('myimage')
		if (element.src.match("background"))
		{
			element.src="/static/jsPractice/img/left_img.jpg";
		}
		else
		{
			element.src="/static/jsPractice/img/background.jpg";
		}
	}
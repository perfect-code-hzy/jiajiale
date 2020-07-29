window.onload=function(){
	var pictures = document.getElementsByClassName('picture');
	var points = document.getElementsByClassName('point');
	var goPreBtn = document.getElementById('goPre');
	var goNextBtn = document.getElementById('goNext');
	var swiper = document.getElementById('wrapper');


	//index表示第几张图片在展示
	var index = 0;
	var clearActive = function(){
		for(var i=0; i<pictures.length; i++){
			pictures[i].className = "picture";
		}
		for(var i=0; i<points.length; i++){
			points[i].className = "point";
		}
	}
	var goIndex = function(){
		clearActive();
		pictures[index].className = "picture active";
		points[index].className = "point active";
	}
	var goPre = function(){
		if (index == 0){
			index = 3;
		}else{
			index--;
		}
		goIndex();
	}
	var goNext = function(){
		if (index == 3){
			index = 0;
		}else{
			index++;
		}
		goIndex();
	}
	goPreBtn.addEventListener('click', function(){
		goPre();
	})
	goNextBtn.addEventListener('click', function(){
		goNext();
	})


	for (var i=0; i<points.length; i++){
		points[i].addEventListener('click', function(){
			var pointIndex = this.getAttribute("data-index");
			index = pointIndex;
			goIndex();
		})
	}


//	//默认开启定时器每一秒钟切换下一张图片
//	time=setInterval(function(){
//		goNext();
//	},2000);
//	//鼠标移入图片关闭定时器
//	pictures[index].addEventListener("mouseover",function(){
//		clearInterval(time);
//	});
//	//鼠标移出图片开启定时器，继续执行默认操作
//	pictures[index].addEventListener("mouseout",function(){
//		time=setInterval(function(){
//			goNext();
//		},2000);
//	})
	//默认开启定时器每一秒钟切换下一张图片
	time=setInterval(function(){
		goNext();
	},2000);
	//鼠标移入图片关闭定时器
	swiper.onmouseover = function(){
		clearInterval(time);
	};
	//鼠标移出图片开启定时器，继续执行默认操作
	swiper.onmouseout = function(){
		time=setInterval(function(){
			goNext();
		},2000);
	};
}

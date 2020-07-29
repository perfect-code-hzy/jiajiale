////处理点击详情与评论切换
//$('#tag_detail').click(function(){
//	$('#tag_comment').removeClass('active')
//	$(this).addClass('active')
//	$('#tab_detail').show()
//	$('#tab_comment').hide()
//})
//
//$('#tag_comment').click(function(){
//	$('#tag_detail').removeClass('active')
//	$(this).addClass('active')
//	$('#tab_comment').show()
//	$('#tab_detail').hide()
//})

 $(document).ready(function(){
	//计算商品的总价
	update_goods_amount();


	function update_goods_amount(){
		//获取商品的单价和数量
		price = $('.show_pirze').children('em').text();
		count = $('.num_show').val();
		//计算商品的总价，先将获取的值转换为浮点数和整数
		price = parseFloat(price);
		count = parseInt(count);
		amount = price*count;
		//设置商品的总价，并设置转换为保留两位小数的字符串
		$('.total').children('em').text(amount.toFixed(2)+'元');
	};

	//增加与减少商品数量，直接对相应的元素设置其click事件为函数，可不对函数进行命名
	$('.add').click(function(){
		//获取商品原有的数目，并对其数目进行更新
		count = $('.num_show').val();
		count = parseInt(count)+1;
		$('.num_show').val(count);
		//更新总价
		update_goods_amount();
	});
	$('.minus').click(function(){
		//获取商品原有的数目，并对其数目进行更新
		count = $('.num_show').val();
		count = parseInt(count)-1;
		if (count <= 0){count = 1;};
		$('.num_show').val(count);
		//更新总价
		update_goods_amount();
	});

	//手动输入商品的数量
	$('.num_show').blur(function(){
		//获取用户输入的数目
		count = $(this).val();
		//检验count是否合法
		if(isNaN(count) || count.trim().length==0 || parseInt(count)<=0){count=1};
		//重新设置商品的数目
		$(this).val(parseInt(count));
		//更新商品的总价
		update_goods_amount();
	});

	//获取add_cart div元素(添加按钮)左上角的坐标
	var $add_x = $('#add_cart').offset().top;
	var $add_y = $('#add_cart').offset().left;
	//获取show_count div元素(右上角购物车栏)左上角的坐标
	var $to_x = $('#show_count').offset().top;
	var $to_y = $('#show_count').offset().left;


	$('#add_cart').click(function(){
		//获取商品id及数量
		track_id = $(this).attr('track_id');
		flag = $(this).attr('flag');
		count = $('.num_show').val();
		csrf = $("input[name='csrfmiddlewaretoken']").val();
		//组织参数，发起ajax post请求
		params = {'track_id':track_id, 'flag':flag, 'count':count, 'csrfmiddlewaretoken':csrf};
		$.post('/cartAdd/', params, function (data) {
			if(data.res==6){
				//添加成功警告
				alert(data.errmsg)
			}
			else if(data.res==0){
				alert(data.errmsg)
				window.location.href = "http://127.0.0.1:8000/login/"
			}
			else{
				alert(data.errmsg)
			};
		})
	})
})
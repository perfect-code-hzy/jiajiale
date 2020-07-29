$(document).ready(function(){
	$('#order_btn').click(function() {
		// 获取用户选择的地址ID，支付方式，商品ID
		address = $(this).attr('address');
		pay_method = $('input[name="pay_style"]:checked').val();
		cart_track_ids = $(this).attr('cart_track_ids');
		csrf = $("input[name='csrfmiddlewaretoken']").val();
		params = {'address':address, 'pay_method': pay_method, 'cart_track_ids': cart_track_ids, 'csrfmiddlewaretoken': csrf};
		// 发起ajax post请求
		$.post('/orderCommit/', params, function(data){
			if (data.res == 6){
				//创建成功
				localStorage.setItem('order_finish',2);
				$('.popup_con').fadeIn('fast', function() {setTimeout(function(){
					$('.popup_con').fadeOut('fast',function(){
					window.location.href = "http://127.0.0.1:8000/userOrder/1/"
					});
			},3000)

		});
			}
			else{
				alert(data.errmsg)
			}
		});

	});
})
$(document).ready(function(){
    //修改购物车
    var addShoppings = document.getElementsByClassName("add")
    var minusShoppings = document.getElementsByClassName("minus")

    for (var i = 0; i < addShoppings.length; i++){
        add = addShoppings[i]
        add.addEventListener("click", function(){
        	csrf = $("input[name='csrfmiddlewaretoken']").val();
            goods_id = this.getAttribute("ga")
            params = {'goods_id':goods_id, 'csrfmiddlewaretoken':csrf};
            $.post("/changeCart/0/",params, function(data){
                if (data.status == "success"){
                    //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(goods_id).innerHTML = data.data
                    document.getElementById(goods_id+"price").innerHTML = data.price
                    document.getElementById("totalPrice").innerHTML = data.total_price
                    document.getElementById("totalNum").innerHTML = data.total_num
                }
            })
        })
    }


    for (var i = 0; i < minusShoppings.length; i++){
        minus = minusShoppings[i]
        minus.addEventListener("click", function(){
        	csrf = $("input[name='csrfmiddlewaretoken']").val();
            goods_id = this.getAttribute("ga")
            params = {'goods_id':goods_id, 'csrfmiddlewaretoken':csrf};
            $.post("/changeCart/1/",params, function(data){
                if (data.status == "success"){
                    //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(goods_id).innerHTML = data.data
                    document.getElementById(goods_id+"price").innerHTML = data.price
                    document.getElementById("totalPrice").innerHTML = data.total_price
                    document.getElementById("totalNum").innerHTML = data.total_num
                    if(data.data == 0) {
                        //window.location.href = "http://127.0.0.1:8000/cart/"
                        var li = document.getElementById(goods_id+"li")
                        li.parentNode.removeChild(li)
                    }
                }
            })
        })
    }



    var isChooses = document.getElementsByClassName("isChoose")
    for (var j = 0; j < isChooses.length; j++){
        isChoose = isChooses[j]
        isChoose.addEventListener("click", function(){
        	csrf = $("input[name='csrfmiddlewaretoken']").val();
            goods_id = this.getAttribute("goodsid")
            params = {'goods_id':goods_id, 'csrfmiddlewaretoken':csrf};
            $.post("/changeCart/2/", params, function(data){
                if (data.status == "success"){
                    //window.location.href = "http://127.0.0.1:8000/cart/"
                    var s = document.getElementById(goods_id+"a")
                    s.innerHTML = data.data
                    document.getElementById("totalPrice").innerHTML = data.total_price
                    document.getElementById("totalNum").innerHTML = data.total_num
                }
            })
        },false)
    }

//全选
//	var allChoose = document.getElementsByClassName("allChoose")
//	allChoose.addEventListener("click", function(){
//        	csrf = $("input[name='csrfmiddlewaretoken']").val();
//            $.post("/changeCart/3/", csrf, function(data){
//                if (data.status == "success"){
//                    window.location.href = "http://127.0.0.1:8000/cart/"
//                }
//            })
//        },false)


//    var ok = document.getElementById("ok")
//    ok.addEventListener("click", function(){
//
//        var f = confirm("是否确认下单？")
//        if (f){
//        	csrf = $("input[name='csrfmiddlewaretoken']").val();
//            $.post("/saveOrder/",{'csrfmiddlewaretoken':csrf}, function(data){
//                if (data.status == "success"){
//                    window.location.href = "http://127.0.0.1:8000/userOrder/"
//                }
//            })
//        }
//    },false)
})
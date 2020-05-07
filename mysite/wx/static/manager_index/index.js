function pageClick(k) {
	$(k).parent().find("div").removeClass("active");
	$(k).addClass("active");
	$("#flTitle").text($(k).text());
//	for(var i=1;i<4;i++){
//	    var curC=document.getElementById("n"+i);
//	    var curB=document.getElementById("p"+i);
//	    if(k==i){
//	        curC.style.display='block';
//	        curB.style.display='block';
//	    }
//	    else{
//			curC.style.display="none";
//			curB.style.display='none';
//	    }
//	}
}

function swap_tab(n){  //鼠标触发事件
	for(var i=1;i<4;i++){
		var curC=document.getElementById("n"+i);
//		var curB=document.getElementById("p"+i);
//        var mores = document.getElementById("j"+i);
		if(n==i){
			curC.style.display="block";
//			curB.className="cli1";
//			mores.style.display = "block";
		}
		else{
			curC.style.display="none";
//			curB.className="cli2";
//            mores.style.display = "none";
	    }

	}
}

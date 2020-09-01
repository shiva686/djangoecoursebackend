let hamburger = document.getElementsByClassName('humbarger');
    hamburger[0].addEventListener('click',(e)=>{
    	let dashboard_nav = document.getElementsByClassName('dashboard-list');
    	if(dashboard_nav[0].classList.contains('dashboard-nav')){
    		dashboard_nav[0].classList.remove('dashboard-nav');
    	}
    	else{
    		dashboard_nav[0].classList.add('dashboard-nav')
    	}
    })
let back = document.getElementsByClassName('back');
    back[0].addEventListener('click',(e)=>{
    	let dashboard_nav = document.getElementsByClassName('dashboard-list');
    	if(dashboard_nav[0].classList.contains('dashboard-nav')){
    		dashboard_nav[0].classList.remove('dashboard-nav');
    	}
    	else{
    		dashboard_nav[0].classList.add('dashboard-nav')
    	}
    })


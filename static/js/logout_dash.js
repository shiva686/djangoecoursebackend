let logout_admin_ = document.getElementsByClassName('logout')
logout_admin_[0].addEventListener('click',()=>{
    
    fetch('http://localhost:8000/api/admin/logout').then(res=>{
    	if(res.ok){
         window.location.assign('/admin/login')
    	}
    	else{
    		alert('something went wrong')
    	}
    }).catch(e=>alert('something went wrong'))
})
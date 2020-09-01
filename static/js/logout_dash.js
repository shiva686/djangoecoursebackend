let logout_admin_ = document.getElementsByClassName('logout')
logout_admin_[0].addEventListener('click',()=>{
    
    fetch('https://djangoecourses.herokuapp.com/api/admin/logout').then(res=>{
    	if(res.ok){
         window.location.assign('/admin/login')
    	}
    	else{
    		alert('something went wrong')
    	}
    }).catch(e=>alert('something went wrong'))
})
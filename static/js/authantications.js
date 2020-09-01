let token = document.cookie;
let cookiearray = token.split(';');
let promise = new Promise((resolve , error)=>{
let length = cookiearray.length
let value;
for (let i=0; i<length; i++){
  let name = cookiearray[i].split('=')[0];
  if(name == 'token'){
  	value = cookiearray[i].split('=')[1];
  } 
 }
   resolve(value)
})
promise.then(value =>{
	fetch('https://djangoecourses.herokuapp.com/api/admin/authlogin',{
    method:'POST',
    headers:{
    	'Content-Type': 'application/json',
    },
 }).then(res=>{
	if(!res.ok){
		window.location.assign('/admin/login')
	}
  }).catch(e=>window.location.assign('/admin/login'))
})


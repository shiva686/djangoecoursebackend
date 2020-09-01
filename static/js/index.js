let backend = 'https://djangoecourses.herokuapp.com/api/adminlogin'
let submit = document.getElementById('submit')
    submit.addEventListener('click',(e)=>{
    let password = document.getElementById('password')
    let email = document.getElementById('email');
      if(email.value != '' && password.value != ''){
      	   if(email.value.includes('@') && password.value.length>6 && password.value.length<16){
              let data ={
              	email:email.value,
              	password:password.value
              }
              fetch(backend,{
                method: 'POST', // or 'PUT'
                   headers: {
                    'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                 }).then(res=>{
                 	if(res.ok){return res.json()
                 	}
                    else{ 
                    let danger = document.getElementsByClassName('err')
      	   	         danger[0].classList.add('err-show');
                       }
                     }).then(res=>{
                     	if(res != undefined){
                        document.cookie="token = "+ res
                  	   	window.location.assign('/admin/dashboard');
                        }
                     });
      	   }else{
      	   	 let warning = document.getElementsByClassName('bg-warning')
      	   	 warning[0].classList.add('wrg-show')
      	   }
      }
      else{
      	   	 let warning = document.getElementsByClassName('bg-warning')
      	   	 warning[0].classList.add('wrg-show')
      	   }
     });


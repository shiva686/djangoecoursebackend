let backend = 'http://localhost:8000/api/admin/changepassword' 
let submit = document.getElementsByClassName('change');
submit[0].addEventListener('click' , ()=>{
    let oldpassword = document.getElementsByClassName('oldpassword')
    let newpassword = document.getElementsByClassName('newpassword')
    let comfirmpassword = document.getElementsByClassName('comfirmpassword')
    if(oldpassword[0].value.length > 6  && newpassword[0].value == comfirmpassword[0].value){
       if(newpassword[0].value.length > 6 && newpassword[0].value.length < 16){
           let data = {
           	  password:oldpassword[0].value,
           	  newpassword:newpassword[0].value
           }
           fetch(backend,{
           	  method: 'POST', 
                 headers: {
                  'Content-Type': 'application/json',
                 },
                 body:JSON.stringify(data)
              }).then(res=>{
              	 if(res.ok){
                    return res.json()
              	 }
              	 else{
                    alert('something went wrong')
              	 }
              }).then(res=>{
              	  if(res != undefined){
              	  	alert('sucessfully changed password');
              	  }
              })
       }
       else{
       	 alert('password length should be 6 or more digits')
       }
    }
}) 
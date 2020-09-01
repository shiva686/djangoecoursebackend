fetch('http://localhost:8000/api/admin_students_list')
.then(res=>{
	if(res.ok){
		return res.json()
	}
}).then(res=>{
if(res != undefined){
	  let i = 0;
	  while(res != null){
        if(res[i]!=undefined){
        document.getElementById("student_list").innerHTML +='<div class="numberofstudent"><div class="header-buttons"><p value='+i+' class="student_list">'+res[i].id+'</p><div class="pd"><i class="fa fa-trash edit" aria-hidden="true"></i></div></div><hr class="listofcourses" /></div>'
        }
	   else{
	   	 break;
	   }
       i++;
	  }
	 }

let numberofstudent = document.getElementsByClassName('student_list')
let modal_body = document.getElementsByClassName('modal-body')
let len = numberofstudent.length
let btn_model = document.getElementsByClassName('btn_model')
let deletee = document.getElementsByClassName('edit')
for(let i=0; i<len; i++){
	numberofstudent[i].addEventListener('click',()=>{
		btn_model[0].click()
		let j = numberofstudent[i].getAttribute('value')
		modal_body[0].innerHTML = '<table><tr><td><p>studen id</p></td><td><p class="td">'+res[j].id+'</p></td></tr><tr><td><p>name</p></td><td><p class="td">'+res[j].name+'</p></td></tr><tr><td><p>email</p></td><td><p class="td">'+res[j].email+'</p></td></tr></table>'
	})
	deletee[i].addEventListener('click',()=>{
		let j = numberofstudent[i].getAttribute('value')
		let data={
			"email":res[j].email
		}
		fetch('http://localhost:8000/api/deleteuser',{
			method:'POST',
			headers:{
				'Content-Type':'application/json'
			},
			body:JSON.stringify(data)
		}).then(res=>{
			if(res.ok){
				alert('sucessfully deleted')
				window.location.reload();
			}
			else{
				alert('something went wrong')
			}
		})
	});
}



}).catch(e=>console.log(e))

let signup_submit = document.getElementsByClassName('signup_submit')
let name = document.getElementsByClassName('name')
let email = document.getElementsByClassName('email')
let password = document.getElementsByClassName('password')
let corfirm_password = document.getElementsByClassName('corfirm_password')
signup_submit[0].addEventListener('click',()=>{
  if(name[0].value != "" && email[0].value !=""){
  	 if(password[0].value.length>6 && password[0].value.length <16){
  	 	if(password[0].value == corfirm_password[0].value){
  	 		let data ={
  	 			'name':name[0].value,
  	 			'email':email[0].value,
  	 			'password':password[0].value
  	 		}
  	 		fetch('http://localhost:8000/api/usersignup',{
  	 			method:'POST',
  	 			headers:{
  	 				'Content-Type':'application/json'
  	 			},
  	 			body: JSON.stringify(data)
  	 		}).then(res=>{
  	 			if(res.ok){
  	 				alert('sucessfully added')
  	 				window.location.reload();
  	 			}
  	 			else{
  	 				alert('something went wrong')
  	 			}
  	 		})
  	 	}
  	 }
  }
})
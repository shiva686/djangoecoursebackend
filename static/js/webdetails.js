
let webnamesubmi = document.getElementsByClassName('webnamesubmit')
let webname = document.getElementsByClassName('webname')
let about = document.getElementsByClassName('About')
webnamesubmi[0].addEventListener('click',()=>{
   let data ={
     "websitename":webname[0].value,
     "aboutwebsite":about[0].value
	}
   fetch('https://djangoecourses.herokuapp.com/api/addwebsitedetails',{
   	method:'POST',
   	headers: {
   		'Content-Type': 'application/json'
   	},
   	body:JSON.stringify(data)
   }).then(res=>{
   	  if(res.ok){
   	  	alert('successfully changed')
   	  }
   }).catch(e => window.location.assign('/admin/login'))
});
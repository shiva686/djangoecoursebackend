
let webnamesubmit = document.getElementsByClassName('webnamesubmit')
let webname = document.getElementsByClassName('webname')
let About = document.getElementsByClassName('About')
webnamesubmit[0].addEventListener('click',()=>{
   let data ={
     "websitename":webname,
     "aboutwebsite":About
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
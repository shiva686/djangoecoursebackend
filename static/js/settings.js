let backend = 'https://djangoecourses.herokuapp.com/api/admin/websitedetails'
let webnamesubmit = document.getElementsByClassName('webnamesubmit');

webnamesubmit[0].addEventListener('click',()=>{
    let websitename = document.getElementsByClassName('webname')
    let aboutwebsite = document.getElementsByClassName('About')
    if(websitename[0].value != '' && aboutwebsite[0].value.length>100){
    	 let data = {
    	 	websitename:websitename[0].value,
    	 	aboutwebsite:aboutwebsite[0].value
    	 }
    	 fetch(backend,{
    	 	method:'POST',
    	 	headers: {
    	 	  'Content-Type':'application/json'
    	 	},
    	 	body:JSON.stringify(data)
    	 }).then(res=>{
    	 	if(res.ok){
    	 		return res.json()
    	 	}else{
    	 		alert('something went wrong')
    	 	}
    	 })
    	 .then(res=>{
    	 	 if(res != undefined){
    	 	 	 alert('sucessfully changed')
    	 	 }
    	 })
    }
})
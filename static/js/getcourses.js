try{
fetch('https://djangoecourses.herokuapp.com/api/admin/courses')
.then(res=>{
	  if(res.ok){
            return res.json()
      }else{
	    alert('Something went wrong')
      }
    })
.then(res=>{
	if(res != undefined){
	  let i = 1;
	  while(res != null){
	   if(res[i]!=undefined){
         document.getElementById("list_of_title").innerHTML += ('<div class="header-buttons"><input class="list" type="checkbox" name="list"/><p style="list-style:none;cursor:pointer" value='+res[i].id +' class="title-list">'+res[i].title +'</p><div class="pd"><i class="fa fa-pencil edit" aria-hidden="true"></i><p class="Publish">'+res[i].status+'</p></div></div><hr class="listofcourses"/>');
	   }
	   else{
	   	 break;
	   }
       i++;
	  }
	 }
}).catch(error => { console.log('request failed', error); });
 
let lis = document.getElementsByClassName('lis');
let selectall = document.getElementsByClassName('selectall');
let list = document.getElementsByClassName('list')
selectall[0].addEventListener('click',()=>{
	if(!lis[0].checked){
	  lis[0].checked = true
      for(let i=0; i<list.length; i++){list[i].checked=true}
    }else{
      lis[0].checked = false
      for(let i=0; i<list.length; i++){list[i].checked=false}
    }
})
let deletecourse= document.getElementsByClassName('delete')
deletecourse[0].addEventListener('click',()=>{
let promise = new Promise((resolve, reject)=>{
    
    let data={}
	let list = document.getElementsByClassName('list')
	let j=0;
	for(let i=0; i<list.length; i++)
	{   
		if(list[i].checked){ 
		  let title_list = document.getElementsByClassName('title-list');
          data[j]={
          	'id':title_list[i].getAttribute('value')
          }
          j++
	 }
   }
   resolve(data)
})
promise.then(data=>{
 
   if(data != undefined && data != {}){
   let backend = "https://djangoecourses.herokuapp.com/api/admin/deletecourse"
   fetch(backend ,{
		 	method: 'POST',
		 	headers:{
		 	  'Content-Type': 'application/json',
		 	},
		 	body:JSON.stringify({data})
		 })
		 .then(res=>{if(res.ok){return res.json()}else{alert('something went wrong')}})
		 .then(res=>{
		 	if(res != undefined){
               alert('content has deleted')
               window.location.reload()
		 	}
		 })
	}
   })
})

}catch(e){
	 	 alert('Something went wrong')
	  }
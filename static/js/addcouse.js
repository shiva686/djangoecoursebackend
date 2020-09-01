let backend = 'http://localhost:8000/api/admin/addcourses'

let add = document.getElementsByClassName('add')
if(add.length != 0){
add[0].addEventListener('click',(e)=>{
   window.location.assign('/admin/addcourse/addnewcourse')
})
}


let next = document.getElementsByClassName('next')
if(next.length != 0){

    next[0].addEventListener('click',()=>{
     let title = document.getElementsByClassName('title')
     let shortdescription = document.getElementsByClassName('short_description')
     let description = document.getElementsByClassName('description')
     let thumbail = document.getElementsByClassName('thumbail')

     if(thumbail[0].files[0] != undefined){
 
             let promise =  new Promise((reslove,reject)=>{
                  var reader = new FileReader();
                  reader.readAsDataURL(thumbail[0].files[0])
                  reader.onload=()=>reslove(reader.result)
              })
            promise.then((value)=>{
              let data= new FormData;
                data.set('title',title[0].value);
                data.set('shortdescription',shortdescription[0].value)
                data.set('description',description[0].value)
                data.set('thumbail',value)

              fetch(backend,{
                method:'post',
                body:data
               }).then(res=>{
                  if(res.ok){
                    return res.json()
                  }else{
                    alert('something went wrong')
                  }
              }).then(res=>{
                if(res != undefined){
                   window.location.assign('/admin/uploadvideos/'+res)
                }
              }).catch(e => alert('something went wrong'))
         })
         // window.location.assign('/admin/uploadvideos/id')
      }

    })
}


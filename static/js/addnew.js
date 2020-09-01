let backend = 'http://localhost:8000/api/admin/addcourses'
let add = document.getElementsByClassName('add')
if(add.length != 0){
add[0].addEventListener('click',(e)=>{
   window.location.assign('/admin/addcourse/addnewcourse')
})
}
let backend = 'https://djangoecourses.herokuapp.com/api/admin/addcourses'
let add = document.getElementsByClassName('add')
if(add.length != 0){
add[0].addEventListener('click',(e)=>{
   window.location.assign('/admin/addcourse/addnewcourse')
})
}
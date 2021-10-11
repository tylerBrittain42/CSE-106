// const student_list = a();
// console.log(student_list)

// console.log("a");
// console.log(student_list)



function getStudent(stuName){



  
}

function jsonToList() {
  return fetch("https://amhep.pythonanywhere.com/grades")
    .then((res) => {
      const results = res.json();
      // console.log(typeof results);
      // console.log(results);
      return results;
    })
    .then((results) => {
      const llist = []
      for (let i of Object.keys(results)) {
        llist.push({i:results[i]})
      }
      // console.log(llist)
      return llist
    })
}

async function a(){
  res= await fetch("https://amhep.pythonanywhere.com/grades")
  data = await res.json()
  const llist = []

  for( let i of Object.keys(data)){
    llist.push({i:data[i]})
  }



}
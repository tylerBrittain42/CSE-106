// const student_list = a();
// console.log(student_list)

// console.log("a");
// console.log(student_list)

//DONT FORGET TO HANDLE ERRORS

const form = document.querySelector("#user-actions");
form.addEventListener("submit", handleAction);
// getStudent('Robert Miller')

function handleAction() {
  const action = form.elements.action.value;
  const name = form.elements.name.value;
  const grade = form.elements.grade.value

  switch (action) {
    case "get":
      console.log("get clicked");
      getStudent(name);
      break;
    case "create":
      addStudent(name, grade);
      break;
    case "update":
      updateStudent(name, grade);
      break;
    case "delete":
      deleteStudent(name);
      break;
    default:
      console.log("error: invalid action");
  }

  event.preventDefault();
}

function getStudent(stu_name) {
  const stu_grade = form.elements.grade;
  fetch(
    "https://amhep.pythonanywhere.com/grades/" + stu_name.replace(" ", "%20")
  )
    .then((res) => {
      if (!res.ok) {
        throw new Error();
      }
      else
        return res.json();
    })
    .then((data) => {
      stu_grade.value = data[stu_name];
    })
    .catch(() => {
      stu_grade.value = 'Error caught'
      console.log("getStudent error caught");
    });
}

// assuming valid inputs
// Error handling not implemented
function addStudent(stu_name, stu_grade) {
  console.log("addStudent called");
  console.log(`${stu_name} has a grade of ${stu_grade}`)

  req_params = {
    method: 'POST',
    headers:{
      "Content-Type": "application/json"
    },
    body: JSON.stringify({"name":stu_name,"grade":Number(stu_grade)})
  }

  fetch("https://amhep.pythonanywhere.com/grades",req_params)
  .then((res) => {
    console.log(res.status)
  })

}

function updateStudent(stu_name, stu_grade) {
  console.log("updatestudent called");
  req_params ={
    method: 'PUT',
    headers:{
      "Content-Type":"application/json"
    },
    body:JSON.stringify({"grade":stu_grade})
  }
  fetch(
    "https://amhep.pythonanywhere.com/grades/" + stu_name.replace(" ", "%20"), req_params
  )
  .then((res) => {
    console.log(res.status)
  })


}

function deleteStudent(stu_name) {
  console.log("deleteStudent called");

  req_params ={
    method: 'DELETE',
    headers: {
      'Content-Type':'application/json'
    }
  }
  fetch(
    "https://amhep.pythonanywhere.com/grades/" + stu_name.replace(" ", "%20"), req_params
  )
  .then((res) => {
    console.log(res.status)
  })


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
      const llist = [];
      for (let i of Object.keys(results)) {
        llist.push({ i: results[i] });
      }
      // console.log(llist)
      return llist;
    });
}

async function a() {
  res = await fetch("https://amhep.pythonanywhere.com/grades");
  data = await res.json();
  const llist = [];

  for (let i of Object.keys(data)) {
    llist.push({ i: data[i] });
  }
}


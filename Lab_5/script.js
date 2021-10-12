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

  switch (action) {
    case "get":
      console.log("get clicked");
      getStudent(name);
      break;
    case "create":
      addStudent();
      break;
    case "update":
      updateStudent();
      break;
    case "delete":
      deleteStudent();
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

function addStudent() {
  console.log("addStudent called");
}

function updateStudent() {
  console.log("updatestudent called");
}

function deleteStudent() {
  console.log("deleteStudent called");
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

function req_format(string) {
  string.replace(" ", "%20");
}

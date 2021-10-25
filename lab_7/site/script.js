//DONT FORGET TO HANDLE ERRORS

const form = document.querySelector("#user-actions");
form.addEventListener("submit", handleAction);

function handleAction() {
  const action = form.elements.action.value;
  const name = form.elements.name.value;
  const grade = form.elements.grade.value;

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

// error handling completed
function getStudent(stu_name) {
  const stu_grade = form.elements.grade;
  fetch(
    " http://127.0.0.1:5000/grades/" + stu_name.replace(" ", "%20")
  )
    .then((res) => {
      if (!res.ok) {
        throw new Error(res.status);
      } else return res.json();
    })
    .then((data) => {
      stu_grade.value = data[stu_name];
    })
    .catch((status) => {
      console.log(status);
      alert(status);
    });
}

// assuming valid inputs
// Error handling not implemented
function addStudent(stu_name, stu_grade) {
  console.log("addStudent called");
  console.log(`${stu_name} has a grade of ${stu_grade}`);

  req_params = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name: stu_name, grade: Number(stu_grade) }),
  };

  fetch(" http://127.0.0.1:5000/grades", req_params)
    .then((res) => {
      if (!res.ok) {
        throw new Error(res.status);
      } else {
        console.log(res.status);
      }
    })
    .catch((status) => {
      console.log(status);
      alert(status);
    });
}

function updateStudent(stu_name, stu_grade) {
  console.log("updatestudent called");
  req_params = {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ grade: stu_grade }),
  };
  fetch(
    " http://127.0.0.1:5000/grades/" + stu_name.replace(" ", "%20"),
    req_params
  )
    .then((res) => {
      if (!res.ok) {
        throw new Error(res.status);
      } else {
        console.log(res.status);
      }
    })
    .catch((status) => {
      console.log(status);
      alert(status);
    });
}

function deleteStudent(stu_name) {
  console.log("deleteStudent called");

  req_params = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  };
  fetch(
    " http://127.0.0.1:5000/grades/" + stu_name.replace(" ", "%20"),
    req_params
  )
    .then((res) => {
      if (!res.ok) {
        throw new Error(res.status);
      } else {
        console.log(res.status);
      }
    })
    .catch((status) => {
      console.log(status);
      alert(status);
    });
}

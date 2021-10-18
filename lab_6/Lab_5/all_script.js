// jsonToList()
// a()

createTable();

async function createTable() {
  const stu_table = document.querySelector("#all-grades");

  res = await fetch("https://amhep.pythonanywhere.com/grades");
  data = await res.json();
  for (let i of Object.keys(data)) {
    appendRow(stu_table, i, data[i]);
  }
}

function appendRow(table, name, grade) {
  const row = document.createElement("tr");

  const name_node = document.createElement("th");
  name_node.innerText = name;

  const grade_node = document.createElement("th");
  grade_node.innerText = grade;

  row.appendChild(name_node);
  row.appendChild(grade_node);
  table.appendChild(row);
}

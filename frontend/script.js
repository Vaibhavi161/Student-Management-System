// ============================================================
// BACKEND API URL
// ============================================================

const API_URL = "https://student-management-system-5-lopi.onrender.com/students";


// ============================================================
// CREATE STUDENT - POST
// ============================================================

document.getElementById("studentForm").addEventListener("submit", async function (event) {

    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const course = document.getElementById("course").value.trim();
    const marks = Number(document.getElementById("marks").value);

    try {

        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                course: course,
                marks: marks
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert("Error: " + JSON.stringify(data));
            return;
        }

        alert("Student added successfully!");

        document.getElementById("studentForm").reset();

        getStudents();

    } catch (error) {

        console.error(error);
        alert("Could not connect to backend.");

    }

});


// ============================================================
// GET ALL STUDENTS - GET
// ============================================================

async function getStudents() {

    try {

        const response = await fetch(API_URL);

        const result = await response.json();

        if (!response.ok) {
            alert("Error: " + JSON.stringify(result));
            return;
        }

        const students = result.data;

        const tableBody = document.getElementById("studentTableBody");

        tableBody.innerHTML = "";

        students.forEach(function (student) {

            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${student.id}</td>
                <td>${student.name}</td>
                <td>${student.course}</td>
                <td>${student.marks}</td>

                <td>

                    <button
                        class="update-btn"
                        onclick="updateStudent(
                            ${student.id},
                            '${student.name}',
                            '${student.course}',
                            ${student.marks}
                        )">
                        Update
                    </button>

                    <button
                        class="delete-btn"
                        onclick="deleteStudent(${student.id})">
                        Delete
                    </button>

                </td>
            `;

            tableBody.appendChild(row);

        });

    } catch (error) {

        console.error(error);
        alert("Could not connect to backend.");

    }

}


// ============================================================
// UPDATE STUDENT - PUT
// ============================================================

async function updateStudent(id, oldName, oldCourse, oldMarks) {

    const name = prompt("Enter student name:", oldName);

    if (name === null) {
        return;
    }

    const course = prompt("Enter course:", oldCourse);

    if (course === null) {
        return;
    }

    const marks = prompt("Enter marks:", oldMarks);

    if (marks === null) {
        return;
    }

    try {

        const response = await fetch(`${API_URL}/${id}`, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name.trim(),
                course: course.trim(),
                marks: Number(marks)
            })

        });

        const result = await response.json();

        if (!response.ok) {

            alert(
                "Update failed: " +
                JSON.stringify(result)
            );

            return;
        }

        alert("Student updated successfully!");

        getStudents();

    } catch (error) {

        console.error(error);
        alert("Could not connect to backend.");

    }

}


// ============================================================
// DELETE STUDENT - DELETE
// ============================================================

async function deleteStudent(id) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this student?"
    );

    if (!confirmDelete) {
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/${id}`,
            {
                method: "DELETE"
            }
        );

        const result = await response.json();

        if (!response.ok) {

            alert(
                "Delete failed: " +
                JSON.stringify(result)
            );

            return;
        }

        alert("Student deleted successfully!");

        getStudents();

    } catch (error) {

        console.error(error);
        alert("Could not connect to backend.");

    }

}


// ============================================================
// LOAD STUDENTS WHEN PAGE OPENS
// ============================================================

getStudents();

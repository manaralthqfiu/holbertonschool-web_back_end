const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.toString().split('\n');

    const students = lines.slice(1).filter((line) => line.trim() !== '');
    console.log(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach((student) => {
      const studentData = student.split(',');
      const field = studentData[3];
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(studentData[0]);
    });

    const keys = Object.keys(fields).sort();
    keys.forEach((key) => {
      console.log(`Number of students in ${key}: ${fields[key].length}. List: ${fields[key].join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;

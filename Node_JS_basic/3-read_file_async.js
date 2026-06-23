const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

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

      resolve();
    });
  });
}

module.exports = countStudents;

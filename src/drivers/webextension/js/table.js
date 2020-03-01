const cveTable = document.getElementById('cveTable')

function createTable(pkg, version) {
  fetch('http://localhost:5000/' + pkg + '/' + version).then(
    (response) => {
      if (response.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' +
          response.status)
        return
      }
      return response.json()
    })
    .then(
      (data) => {
        for (let i = 0; i < data.length; i++) {
          const row = cveTable.insertRow(0)
          const cell = row.insertCell(0)
          cell.innerHTML = data[i]
        }
      })
}

createTable('nginx', '1.8')

const cveTable = document.getElementById('cveTable')
console.log(window.location.search)
const dict = window.location.search.split('d=')[1]
console.log(dict)

function addToTable (pkg, version) {
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

for (var a in dict) {
  const name = dict[a].name
  var version = dict[a].version
  if (version.length == 0) {
    // do something
  }

  console.log(dict[a].name + ' ' + dict[a].version)
  addToTable(name, version)
}

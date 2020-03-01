const cveTable = document.getElementById('cveTable')
const jsonString = decodeURIComponent(window.location.search.split('d=')[1])
const dict = JSON.parse(jsonString)
console.log(dict)

function addToTable (pkg, version) {
  console.log('https://us-central1-wappalyzer-slo.cloudfunctions.net/http/' + pkg + '/' + version)
  fetch('https://us-central1-wappalyzer-slo.cloudfunctions.net/http/' + pkg + '/' + version).then(
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
        console.log(data)
        for (let i = 0; i < data.length; i++) {
          console.log('inserting')
          const row = cveTable.insertRow(0)
          const cell = row.insertCell(0)
          cell.onclick = () => {
            window.location = 'http://cve.mitre.org/cgi-bin/cvename.cgi?name=' + data[i]
          }
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

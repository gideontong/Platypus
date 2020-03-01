function createTable (pkg, version) {
  console.log('Hello1')
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
        console.log(data)
        console.log(data[0])
        for (let i = 0; i < data.length; i++) {
          console.log(data[i])
        }
      }
    )
}

createTable('nginx', '1.8')

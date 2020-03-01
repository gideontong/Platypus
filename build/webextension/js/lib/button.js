
const b = document.getElementById('button')
console.log(b)
b.onclick = function () {
    console.log('yes2')
    chrome.tabs.create({ url: chrome.extension.getURL('table.html') })
}

function renderPdf (item) {
  let iframe = document.createElement('iframe')
  iframe.setAttribute('width', '100%')
  iframe.setAttribute('height', '1200px')
  iframe.setAttribute('allowfullscreen', true)
  iframe.setAttribute('src', item.dataset.file)

  // Remove existing document viewer
  if (document.querySelector('#documentViewerContainer iframe')) {
    document.querySelector('#documentViewerContainer iframe').remove()
  }

  document.getElementById('documentViewerContainer').appendChild(iframe)

  if (item.dataset.description) {
    document.getElementById('documentDescription').innerText = item.dataset.description
  } else {
    document.getElementById('documentDescription').innerText = ''
  }
}

// From: https://gomakethings.com/how-to-get-all-of-an-elements-siblings-with-vanilla-js/
function getSiblings (elem) {
  // Setup siblings array and get the first sibling
  var siblings = []
  var sibling = elem.parentNode.firstChild

  // Loop through each sibling and push to the array
  while (sibling) {
    if (sibling.nodeType === 1 && sibling !== elem) {
      siblings.push(sibling)
    }
    sibling = sibling.nextSibling
  }
  return siblings
}

document.addEventListener('DOMContentLoaded', function () {
  // Set the first tab active. Done here because it may vary depending on what assets are
  // available for a given family.
  document.querySelector('#nav-tab a:first-child').classList.add('active')
  document.querySelector('#nav-tabContent div:first-child').classList.add('show', 'active')

  // Render the first document without requiring a click.
  let docs = document.getElementById('documentList')
  if (docs.childElementCount > 0) {
    docs.firstElementChild.classList.add('active')
    renderPdf(docs.firstElementChild)
  }

  // Render the selected PDF from list.
  document.querySelectorAll('#documentList a').forEach(item => {
    item.addEventListener('click', event => {
      event.preventDefault()
      getSiblings(item).forEach(sib => {
        sib.classList.remove('active')
      })
      item.classList.add('active')
      renderPdf(item)
    })
  })
})

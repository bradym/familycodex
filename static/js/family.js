/* Inform standardjs that these are global variables so it won't complain.  */
/* global bootstrap, history, location                                      */

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

// Adapted from: https://www.viperswebdesign.com/blog/how-to-add-deep-linking-to-the-bootstrap-5-tabs-component
function deepLinking () {
  // deep linking - load tab on refresh
  let url = location.href.replace(/\/$/, '')
  if (location.hash) {
    const currentTab = document.querySelector(`#nav-tab a[href="${window.location.hash}"]`)
    const curTab = new bootstrap.Tab(currentTab)
    curTab.show()
    url = location.href.replace(/\/#/, '#')
    history.pushState(null, null, url)
    setTimeout(() => {
      window.scrollTop = 0
    }, 400)
  }

  // change url based on selected tab
  const selectableTabList = [].slice.call(document.querySelectorAll('a[data-bs-toggle="tab"]'))
  selectableTabList.forEach((selectableTab) => {
    selectableTab.addEventListener('click', function () {
      var newUrl
      const hash = selectableTab.getAttribute('href')
      newUrl = url.split('#')[0] + hash
      history.pushState(null, null, newUrl)
    })
  })
}

window.onhashchange = deepLinking

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

  // Display the first story without requiring a click.
  let stories = document.getElementById('storyList')
  if (stories !== null && stories.childElementCount > 0) {
    let tabTrigger = stories.firstElementChild
    let tab = new bootstrap.Tab(tabTrigger)
    tab.show()
  }

  deepLinking()
})

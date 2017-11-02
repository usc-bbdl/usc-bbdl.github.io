function tagNames(){
  return([
    '.athletics',
    '.neuroscience',
    '.computation_and_modeling',
    '.robotics',
    '.clinical_research',
    '.biomechanics',
    '.manipulation'
    ])
  }
function show(className) {
  affectDisplay(className, 'block')
}
function hide(className) {
  affectDisplay(className, 'none')
}
function getElements(className){
  return(document.querySelectorAll(className))
}
function affectDisplay(className, newValue){
  Array.prototype.map.call(getElements(className),
    function(element){
      changeDisplay(element, newValue)
    }
  )
}
function changeDisplay(element, newValue){
  element.style.display = newValue;
}
function hideMultiple(classNames) {
  classNames.map(hide)
}
function showAll() {
  tagNames().map(show)
}
function hideAll() {
  hideMultiple(tagNames())
}
function showOnly(className){
  hideAll()
  show(className)
}

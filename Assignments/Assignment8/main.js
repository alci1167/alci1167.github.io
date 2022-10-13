var customName = document.getElementById('customname');
var randomize = document.querySelector('.randomize');
var story = document.querySelector('.story');

function randomValueFromArray(array){
  const random = Math.floor(Math.random()*array.length);
  return array[random];
}

var storyText = 'It was 0 fahrenheit outside, so :insertx: stayed home and sat by the fireplace. When the wood stopped burning, :inserty: appeared. They stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 90 pounds, and it was a cold day.';
var insertX = ['Wellington the Skellington', 'Small Big Daddy', 'Chuy the Chihuahua'];
var insertY = ['Big Foot', 'Mr.Freeze', 'a huge Frosty the Snowman'];
var insertZ = ['turned to stone', 'was spontaneously covered in frostbite', 'turned into an ice cube'];

randomize.addEventListener('click', result);

function result() {
  
  var newstory = storyText;
  var xItem = randomValueFromArray(insertX);
  var yItem = randomValueFromArray(insertY);
  var zItem = randomValueFromArray(insertZ);
  newstory = newstory.replace(':insertx:', xItem);
  newstory = newstory.replace(':inserty:', yItem);
  newstory = newstory.replace(':insertz:', zItem);
  newstory = newstory.replace(':insertx:', xItem);

  if(customName.value !== '') {
    const name = customName.value;
    newstory = newstory.replace('Bob', name);
  }

  if(document.getElementById('uk').checked) {
    const weight = Math.round(90*0.0714286)+' stone';
    const temperature =  Math.round((0-32)*5/9)+' centigrade';
    newstory = newstory.replace('0 fahrenheit', temperature)
    newstory = newstory.replace('90 pounds', weight)
  }

  story.textContent = newstory;
  story.style.visibility = 'visible';
}

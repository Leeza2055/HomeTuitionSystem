//  console.log("it from rating js");

//get all the stars
const one = document.getElementById('one');
const two = document.getElementById('two');
const three = document.getElementById('three');
const four = document.getElementById('four');
const five = document.getElementById('five');

const form = document.querySelector('.rate-form');
const confirmBox = document.getElementById('confirm-box');

const csrf = document.getElementsByName('csrfmiddlewaretoken');

console.log(form.getElementsByTagName('label'));
// const children = form.children;

const handleStarSelect = (size) => {
    const children = form.getElementsByTagName('label');
    // console.log(children[0]);
    for (let i=0; i< children.length; i++) {
        if(i < size){
            children[i].classList.add('checked')
            // console.log(children[i]);
        }
        else{
            children[i].classList.remove('checked')
            // console.log(children[i]);
        }
    }
}

//function that will add css to selected star
const handleSelect = (selection) => {
    switch(selection){
        case 'one': {
            // one.classList.add('checked')
            // two.classList.remove('checked')
            // three.classList.remove('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
            handleStarSelect(1);
            return
        }
        case 'two': {
            handleStarSelect(2);
            return
        }
        case 'three': {
            handleStarSelect(3);
            return
        }
        case 'four': {
            handleStarSelect(4);
            return
        }
        case 'five': {
            handleStarSelect(5);
            return
        }
    }
}

if(one) {
    const arr = [one, two, three, four, five];
    //event listener which will select star when the mouse is over the star
    arr.forEach(item => item.addEventListener('mouseover', (event)=>{
        // console.log(event.target.id)
        handleSelect(event.target.id)
        }))
}

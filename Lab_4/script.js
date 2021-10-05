// a (operation) b
let operation = '+'
let a = 0
let b = 0
let display_val = 0

createListeners()

const display = document.getElementById('display')
display.innerText = display_val
// console.log(display)




function createListeners() {

    // Gather all buttons
    const buttons = document.querySelectorAll('.grid-item')
    
    // assigning listeners to each
    buttons.forEach(ele => {
        ele.addEventListener('click', () => {
            // console.log('pre-op')
            // console.log(`sum:${sum}\ndispaly:${display_val}\nop:${operation}`)

            //manipulating everything based on inner text value
            const val = ele.innerText

            // change operation
            if (val === 'x' || val === '/' || val === '+' || val === '-'){
                sum = display_val
                display_val = 0
                operation = val
            }
            else if(val === '(-)'){
                display_val *= -1
            }
        
            else if(val === 'CLR'){
                sum = 0
                display_val = 0
                operation = '+'
            }
            else if(val === 'ENTER'){
                display_val = execute(sum,display_val,operation)
            }
            else if(val === '.'){
                console.log('HANDLE ME')
            }
            else{
                appendVal(val)
            }
            //Enter
            //Else (numeric)
            display.innerText = display_val
            console.log('post-op')
            console.log(`sum:${sum}\ndispaly:${display_val}\nop:${operation}`)

        })
    });
}

function appendVal(val){
    display_val = Number(display.innerText) * 10 + Number(val)
}









function execute(a, b, op){

    // ensure values are num not string
    a = Number(a)
    b = Number(b)

    switch (op) {
        case '+':
            return add(a,b)
        case '-':
            return subtract(a,b)
        case '/': 
            return divide(a,b)
        case '*':
            return multiply(a,b)
        default:
            return 'EXECUTE ERROR'
    }
}

function add(a, b){
    return a + b
}

function subtract(a,b){
    return a - b
}

function multiply(a, b){
    return a * b
}

function divide(a, b){
    return a / b
}










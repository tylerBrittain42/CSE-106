// a (operation) b
let operation = '+'
let a = '0'
let b = '0'
let display_val = 0
let last = 'ENTER'
let bool = false
createListeners()

const display = document.getElementById('display')
display.innerText = display_val
// console.log(display)




function createListeners() {

    // Gather all buttons
    const buttons = document.querySelectorAll('.grid-item')
    let last = false
    
    // assigning listeners to each
    buttons.forEach(ele => {
        ele.addEventListener('click', () => {


            //manipulating everything based on inner text value
            const val = ele.innerText

            // change operation
            if (val === 'x' || val === '/' || val === '+' || val === '-'){
                if (last !== 'ENTER')
                    a = String(execute(a,b,operation))
                b = ''
                operation = val
            }
            else if(val === '(-)'){
                if (b !== '')
                    b *= -1
                else{
                    a *= -1
                    bool = true
                }
                console.log('neg')
            }
        
            else if(val === 'CLR'){
                a = 0
                b = 0
                operation = '+'
            }
            else if(val === 'ENTER'){
                a = String(execute(a,b,operation))
            }
            // else if(val === '.'){
            //     console.log('HANDLE ME')
            // }
            else{
                appendVal(val)
            }
            //Enter
            //Else (numeric)
            last = val
            display.innerText = ((val === 'ENTER' || val === 'x' || val === '/' || val === '+' || val === '-' || bool === true) ? a:b)
            console.log('post-op')
            console.log(`a:${a}\nb:${b}\nop:${operation}`)
            bool = false

        })
    });
}

function appendVal(val){
    b = String(b)
    if (b.charAt(0) === '0')
        b = b.substr(1,b.length)
    b += val 
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
        case 'x':
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










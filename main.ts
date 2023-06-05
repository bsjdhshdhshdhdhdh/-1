let x = 12
let y = 8
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showNumber(x + y)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    basic.showNumber(18 + x * y)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    basic.showNumber((x / y) ** 2)
})

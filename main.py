x=12
y=8
def on_button_pressed_a():
    pass
    basic.show_number(x+y)

input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    pass
    basic.show_number(18+x*y)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_button_pressed_ab():
    pass
    basic.show_number((x/y)**2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
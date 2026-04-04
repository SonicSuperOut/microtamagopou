"""

KERNEL SUPREMO MICROTAMAGOPOU V2.0 - BY AZULSONIC

"""
"""

180 TRILHÕES DE GRAUS: ESCOLA, HOSPITAL, PASSEIO E VISITA

"""
# LOGO TOUCH: HARDWARE CHECK DE STATUS

def on_logo_pressed():
    basic.show_string("F:")
    basic.show_number(fome)
    basic.show_string("I:")
    basic.show_number(inteligencia)
    basic.show_string("H:")
    basic.show_number(saude)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# BOTÃO A: INTERAGIR (CADA LOCAL DÁ UM EXECUTE DIFERENTE)

def on_button_pressed_a():
    global fome, inteligencia, felicidade, saude
    if not (vivo):
        control.reset()
    if local == "CASA":
        fome = max(0, fome - 5)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.show_string("COMER")
    elif local == "ESCOLA":
        inteligencia += 10
        felicidade += 0 - 5
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_string("ESTUDANDO")
    elif local == "PASSEIO":
        felicidade += 20
        fome += 5
        basic.show_icon(IconNames.PITCHFORK)
        basic.show_string("UHUU!")
    elif local == "HOSPITAL":
        saude = 100
        basic.show_icon(IconNames.HEART)
        basic.show_string("CURADO")
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

# AGITAR: VISITA (SINAL DE RÁDIO DE 180°C)

def on_gesture_shake():
    global felicidade
    if vivo:
        basic.show_icon(IconNames.STICK_FIGURE)
        basic.show_string("VISITA!")
        felicidade += 15
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# BOTÃO B: TROCAR DE LOCAL (SINAL DE RÁDIO DO MAPA)

def on_button_pressed_b():
    global local
    if local == "CASA":
        local = "ESCOLA"
    elif local == "ESCOLA":
        local = "PASSEIO"
    elif local == "PASSEIO":
        local = "HOSPITAL"
    else:
        local = "CASA"
    basic.show_string(local)
input.on_button_pressed(Button.B, on_button_pressed_b)

sono = 0
inteligencia = 0
fome = 0
vivo = False
local = ""
saude = 0
saude = 100
felicidade = 100
# CASA, ESCOLA, PASSEIO, HOSPITAL
local = "CASA"
vivo = True
basic.show_icon(IconNames.HAPPY)
# LOOP DE VIDA (SINAL DE RÁDIO DE 1 BILHÃO DE GIGAS)

def on_every_interval():
    global fome, sono, saude, vivo
    if vivo:
        fome += 2
        sono += 1
        if fome > 15:
            saude += 0 - 5
        if saude <= 0:
            vivo = False
            basic.show_icon(IconNames.SKULL)
loops.every_interval(10000, on_every_interval)

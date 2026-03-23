/**
 * KERNEL SUPREMO MICROTAMAGOPOU V2.0 - BY AZULSONIC
 */
/**
 * 180 TRILHÕES DE GRAUS: ESCOLA, HOSPITAL, PASSEIO E VISITA
 */
// LOGO TOUCH: HARDWARE CHECK DE STATUS
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("F:")
    basic.showNumber(fome)
    basic.showString("I:")
    basic.showNumber(inteligencia)
    basic.showString("H:")
    basic.showNumber(saude)
})
// BOTÃO A: INTERAGIR (CADA LOCAL DÁ UM EXECUTE DIFERENTE)
input.onButtonPressed(Button.A, function () {
    if (!(vivo)) {
        control.reset()
    }
    if (local == "CASA") {
        fome = Math.max(0, fome - 5)
        basic.showIcon(IconNames.SmallDiamond)
        basic.showString("COMER")
    } else if (local == "ESCOLA") {
        inteligencia += 10
        felicidade += 0 - 5
        basic.showIcon(IconNames.Chessboard)
        basic.showString("ESTUDANDO")
    } else if (local == "PASSEIO") {
        felicidade += 20
        fome += 5
        basic.showIcon(IconNames.Pitchfork)
        basic.showString("UHUU!")
    } else if (local == "HOSPITAL") {
        saude = 100
        basic.showIcon(IconNames.Heart)
        basic.showString("CURADO")
    }
    basic.showIcon(IconNames.Happy)
})
// AGITAR: VISITA (SINAL DE RÁDIO DE 180°C)
input.onGesture(Gesture.Shake, function () {
    if (vivo) {
        basic.showIcon(IconNames.StickFigure)
        basic.showString("VISITA!")
        felicidade += 15
    }
})
// BOTÃO B: TROCAR DE LOCAL (SINAL DE RÁDIO DO MAPA)
input.onButtonPressed(Button.B, function () {
    if (local == "CASA") {
        local = "ESCOLA"
    } else if (local == "ESCOLA") {
        local = "PASSEIO"
    } else if (local == "PASSEIO") {
        local = "HOSPITAL"
    } else {
        local = "CASA"
    }
    basic.showString(local)
})
let sono = 0
let inteligencia = 0
let fome = 0
let vivo = false
let local = ""
let saude = 0
saude = 100
let felicidade = 100
// CASA, ESCOLA, PASSEIO, HOSPITAL
local = "CASA"
vivo = true
basic.showIcon(IconNames.Happy)
// LOOP DE VIDA (SINAL DE RÁDIO DE 1 BILHÃO DE GIGAS)
loops.everyInterval(10000, function () {
    if (vivo) {
        fome += 2
        sono += 1
        if (fome > 15) {
            saude += 0 - 5
        }
        if (saude <= 0) {
            vivo = false
            basic.showIcon(IconNames.Skull)
        }
    }
})

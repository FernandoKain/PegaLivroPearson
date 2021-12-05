#Ainda testando o envio para o Git
import pyautogui
import time

# 2 segundos de espera para cada linha de código
# pyautogui.PAUSE = 1.5

# Alterna abas antes de começar o código
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

time.sleep(1)

# ----------------------------------------------------------------------------------------------
# Inicia a automação
# ----------------------------------------------------------------------------------------------
for i in range(20):
    # Expandir Navegador
    pyautogui.press('F11')

    pyautogui.click(1600, 600)
    pyautogui.keyDown('ctrl')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.keyUp('ctrl')

    pyautogui.hotkey('shift', 'winleft', 's')
    time.sleep(1)
    pyautogui.mouseDown(642, 80, button='left')
    pyautogui.moveTo(1270, 960)
    pyautogui.mouseUp(1270, 960, button='left')
    time.sleep(1)

    pyautogui.keyDown('ctrl')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.keyUp('ctrl')


    #Mudar de página
    pyautogui.press('right')
    # pyautogui.click(x=1840, y=575)

    # Voltar navegador ao normal para clicar no arquivo word
    pyautogui.press('F11')
    time.sleep(1)
    pyautogui.click(x=1210, y=1170)

    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

    time.sleep(1)
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

    pyautogui.press('enter')
    time.sleep(1)


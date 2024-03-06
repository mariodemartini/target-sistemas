import random

def descobrir_interruptores():
    lampadas = [False, False, False]

    lampadas[0] = True

    lampadas[1] = True

    for i, estado in enumerate(lampadas):
        if estado:
            print(f"Lâmpada {i + 1} está acesa.")
        else:
            print(f"Lâmpada {i + 1} está apagada.")

    if lampadas[1]:
        print("O segundo interruptor controla a lâmpada acesa.")
    elif lampadas[0]:
        print("O primeiro interruptor controla a lâmpada acesa.")
    else:
        print("O terceiro interruptor controla a lâmpada acesa.")

descobrir_interruptores()

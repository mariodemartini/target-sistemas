def inverter_string(s):
    resultado = ""
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]

    return resultado

msg = input(str('Digite sua mensagem: '))
resultado_invertido = inverter_string(msg)
print(f"Original: {msg}")
print(f"Invertido: {resultado_invertido}")

numero = int(input("Introduce un número entre 0 y 99999: "))

unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
decenas = ["", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
veinteish = ["veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
excepciones = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
cientos = ["ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

resultado = ""

if 0 <= numero < 10:
    resultado = unidades[numero]
elif 10 <= numero < 20:
    resultado = excepciones[numero - 10]
elif 20 <= numero < 30:
    resultado = veinteish[numero - 20]
elif 30 <= numero < 100:
    d = numero // 10
    u = numero % 10
    resultado = decenas[d-1] + (" y " + unidades[u] if u != 0 else "")
elif 100 <= numero < 1000:
    c = numero // 100
    r = numero % 100
    if c == 1 and r == 0:
        resultado = "cien"
    else:
        resultado = cientos[c - 1]
        if r > 0:
            if 0 <= r < 10:
                resultado += " " + unidades[r]
            elif 10 <= r < 20:
                resultado += " " + excepciones[r - 10]
            elif 20 <= r < 30:
                resultado += " " + veinteish[r - 20]
            elif 30 <= r < 100:
                d = r // 10
                u = r % 10
                resultado += " " + decenas[d-1] + (" y " + unidades[u] if u != 0 else "")
elif 1000 <= numero < 100000:
    m = numero // 1000
    r = numero % 1000
    
    if m == 1:
        resultado = "mil"
    else:
        if 0 <= m < 10:
            resultado = unidades[m] + " mil"
        elif 10 <= m < 20:
            resultado = excepciones[m - 10] + " mil"
        elif 20 <= m < 30:
            resultado = veinteish[m - 20] + " mil"
        elif 30 <= m < 100:
            d = m // 10
            u = m % 10
            resultado = decenas[d-1] + (" y " + unidades[u] if u != 0 else "") + " mil"
        elif 100 <= m < 1000:
            c = m // 100
            r_m = m % 100
            if c == 1 and r_m == 0:
                resultado = "cien mil"
            else:
                resultado = cientos[c - 1] + " mil"
                if r_m > 0:
                    if 0 <= r_m < 10:
                        resultado += " " + unidades[r_m]
                    elif 10 <= r_m < 20:
                        resultado += " " + excepciones[r_m - 10]
                    elif 20 <= r_m < 30:
                        resultado += " " + veinteish[r_m - 20]
                    elif 30 <= r_m < 100:
                        d = r_m // 10
                        u = r_m % 10
                        resultado += " " + decenas[d-1] + (" y " + unidades[u] if u != 0 else "")
    
    if r > 0:
        if 0 <= r < 10:
            resultado += " " + unidades[r]
        elif 10 <= r < 20:
            resultado += " " + excepciones[r - 10]
        elif 20 <= r < 30:
            resultado += " " + veinteish[r - 20]
        elif 30 <= r < 100:
            d = r // 10
            u = r % 10
            resultado += " " + decenas[d-1] + (" y " + unidades[u] if u != 0 else "")
        elif 100 <= r < 1000:
            c = r // 100
            r_c = r % 100
            resultado += " " + cientos[c - 1]
            if r_c > 0:
                if 0 <= r_c < 10:
                    resultado += " " + unidades[r_c]
                elif 10 <= r_c < 20:
                    resultado += " " + excepciones[r_c - 10]
                elif 20 <= r_c < 30:
                    resultado += " " + veinteish[r_c - 20]
                elif 30 <= r_c < 100:
                    d = r_c // 10
                    u = r_c % 10
                    resultado += " " + decenas[d-1] + (" y " + unidades[u] if u != 0 else "")

print(resultado.strip())


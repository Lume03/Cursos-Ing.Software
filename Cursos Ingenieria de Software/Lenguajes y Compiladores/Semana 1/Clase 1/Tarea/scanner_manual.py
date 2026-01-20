def scanner_manual():
    # === CONFIGURACIÓN ===
    nombre_archivo = "codigo_prueba.c"
    
    # Lista de palabras reservadas de C
    reservadas = {
        'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 
        'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 
        'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 
        'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
    }
    
    # Caracteres que consideramos operadores o separadores
    simbolos_operadores = "+-*/%=!&|^~<>?:;,(){}[]"

    # === LECTURA DEL ARCHIVO ===
    try:
        f = open(nombre_archivo, 'r')
        contenido = f.read()
        f.close()
    except:
        print(f"Error: No se pudo abrir el archivo '{nombre_archivo}'")
        return

    # === VARIABLES PARA ESTADÍSTICAS ===
    elementos_encontrados = [] # Guardará tuplas (tipo, valor)
    stats = {
        "Palabra Reservada": 0,
        "Variable": 0,
        "Numero Entero": 0,
        "Numero Real": 0,
        "Operador": 0,
        "total" : 0
    }

    # === LÓGICA DEL SCANNER (PARSER MANUAL) ===
    i = 0
    n = len(contenido)
    
    print(f"{'ORDEN':<10} | {'TIPO':<20} | {'VALOR'}")
    print("-" * 50)
    
    orden_contador = 1

    while i < n:
        char = contenido[i]

        # 1. Ignorar Espacios en blanco, tabs, saltos de linea
        if char in ' \t\n\r':
            i += 1
            continue

        # 2. Manejo de COMENTARIOS y Operador '/'
        if char == '/':
            # Mirar el siguiente caracter si existe
            if i + 1 < n:
                sig = contenido[i+1]
                
                # Caso // (Comentario de línea)
                if sig == '/': 
                    i += 2
                    # Avanzar hasta el salto de línea
                    while i < n and contenido[i] != '\n':
                        i += 1
                    continue
                
                # Caso /* (Comentario de bloque)
                elif sig == '*':
                    i += 2
                    # Avanzar hasta encontrar */
                    while i < n - 1:
                        if contenido[i] == '*' and contenido[i+1] == '/':
                            i += 2
                            break
                        i += 1
                    continue
        
        # 3. Identificadores (Variables) y Palabras Reservadas
        # Empiezan con letra o guion bajo
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '_':
            inicio = i
            # Mientras siga siendo letra, numero o _
            while i < n and (
                ('a' <= contenido[i] <= 'z') or 
                ('A' <= contenido[i] <= 'Z') or 
                ('0' <= contenido[i] <= '9') or 
                contenido[i] == '_'
            ):
                i += 1
            
            palabra = contenido[inicio:i]
            
            tipo = "Variable"
            if palabra in reservadas:
                tipo = "Palabra Reservada"
            
            # Registrar
            stats[tipo] += 1
            elementos_encontrados.append((tipo, palabra))
            print(f"{orden_contador:<10} | {tipo:<20} | {palabra}")
            orden_contador += 1
            continue

        # 4. Números (Enteros y Reales)
        if '0' <= char <= '9':
            inicio = i
            es_real = False
            
            while i < n:
                c = contenido[i]
                if '0' <= c <= '9':
                    i += 1
                elif c == '.':
                    if es_real: break # Ya tenía punto, paramos (ej: 1.2.3)
                    es_real = True
                    i += 1
                else:
                    break
            
            numero = contenido[inicio:i]
            
            # Verificación extra: si termina en punto (ej "123."), lo tratamos como real igual
            tipo = "Numero Real" if es_real else "Numero Entero"
            
            stats[tipo] += 1
            elementos_encontrados.append((tipo, numero))
            print(f"{orden_contador:<10} | {tipo:<20} | {numero}")
            orden_contador += 1
            continue

        # 5. Operadores
        if char in simbolos_operadores:
            # Intentar agrupar operadores dobles (==, ++, <=, &&, etc)
            # Nota: Esto es básico, agrupa si el siguiente también es operador
            op = char
            if i + 1 < n and contenido[i+1] in simbolos_operadores:
                # Excluir parentesis y corchetes de agrupacion
                if char not in "(){}[];," and contenido[i+1] not in "(){}[];,":
                     op += contenido[i+1]
                     i += 1 
            
            tipo = "Operador"
            stats[tipo] += 1
            elementos_encontrados.append((tipo, op))
            print(f"{orden_contador:<10} | {tipo:<20} | {op}")
            orden_contador += 1
            i += 1
            continue

        # Caracter no reconocido (avanzamos para evitar bucle infinito)
        i += 1

    # === IMPRIMIR ESTADÍSTICAS ===
    print("\n" + "="*40)
    print(f"{'ESTADÍSTICAS FINALES':^40}")
    print("="*40)
    for k, v in stats.items():
        print(f"{k:<25}: {v}")

# Bloque principal de ejecución
if __name__ == "__main__":
    scanner_manual()
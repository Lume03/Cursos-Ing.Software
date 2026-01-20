Es un lenguaje formal diseñado para especificar un conunto de instrucciones , conocido como programa a un computador.

- **Imperativa:** Te centras en el **CÓMO** (los pasos exactos para conseguir algo).
    
- **Declarativa:** Te centras en el **QUÉ** (el resultado que quieres obtener).

### Cuadro Comparativo

|**Característica**|**Programación Imperativa**|**Programación Declarativa**|
|---|---|---|
|**Enfoque**|**Cómo** se hace. Das instrucciones paso a paso.|**Qué** se quiere. Describes el resultado final.|
|**Control de Flujo**|Tú controlas los bucles (`for`, `while`) y estados.|El lenguaje/framework decide cómo recorrer los datos.|
|**Estado**|**Mutable**. Las variables cambian de valor constantemente.|**Inmutable**. Se prefiere crear nuevos datos en vez de modificar los viejos.|
|**Legibilidad**|Puede ser largo y difícil de leer si es complejo.|Suele ser más corto, expresivo y fácil de entender ("se lee como inglés").|
|**Ejemplos Reales**|Receta de cocina paso a paso, ensamblaje manual.|Pedir comida en un restaurante, SQL, HTML.|
|**Lenguajes Típicos**|C, C++, Java (estilo clásico), Python (bucles).|SQL, HTML, Haskell, React, Python (List Comprehensions).|

---

### Ejemplos de Código

Vamos a resolver el **mismo problema** con ambos enfoques: _De una lista de números, queremos obtener solo los pares._

#### 1. Enfoque Imperativo (Python)

Aquí le dices a la máquina: "Crea una lista vacía, recorre número por número, verifica si es par, y si lo es, agrégalo".

Python

```
numeros = [1, 2, 3, 4, 5, 6]
pares = []                  # 1. Crear estado mutable (lista vacía)

for n in numeros:           # 2. Controlar el flujo manualmente (bucle)
    if n % 2 == 0:          # 3. Instrucción condicional explícita
        pares.append(n)     # 4. Modificar el estado

print(pares) # Resultado: [2, 4, 6]
```

#### 2. Enfoque Declarativo (Python)

Aquí le dices a la máquina: "Quiero una lista con los números que sean pares". No te preocupas por cómo se crea la lista o cómo se recorre.

Python

```
numeros = [1, 2, 3, 4, 5, 6]

# Simplemente declaras QUÉ quieres (filtrar)
pares = list(filter(lambda n: n % 2 == 0, numeros))

print(pares) # Resultado: [2, 4, 6]
```

#### 3. El ejemplo definitivo: SQL

SQL es el rey de lo declarativo. Tú nunca le dices a la base de datos "abre el archivo, ve a la fila 3, mira el nombre...". Solo pides el dato:

SQL

```
-- Declarativo puro: "Dame los usuarios activos"
SELECT * FROM usuarios WHERE estado = 'activo';
```

---

### Analogía para entenderlo mejor

- **Imperativo (Taxi):** "Siga derecho 200 metros, gire a la derecha en la señal de pare, avance tres cuadras y pare en la casa azul." (Tú diriges cada movimiento).
    
- **Declarativo (Uber/Maps):** "Llévame a la Calle Falsa 123." (Tú defines el destino, el conductor/app decide la mejor ruta).
    
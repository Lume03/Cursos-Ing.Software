#### Sistema de comunicacion absado en reglas y que es utilizado en un determinado contexto.

# 🔤 Teoría de Lenguajes Formales: Conceptos Base

> **Analogía General:**
> - **Símbolo:** Una letra (a).
> - **Alfabeto:** El teclado disponible ($\Sigma$).
> - **Cadena:** Una palabra escrita ($w$).
> - **Lenguaje:** El diccionario válido ($L$).

---

## 1. Los Componentes Fundamentales

### A. El Símbolo

Es la unidad mínima e indivisible de información.

- **Ejemplos:** $a$, $B$, $5$, $@$.
    

### B. El Alfabeto ($\Sigma$)

Es un conjunto **finito** y **no vacío** de símbolos. Siempre se denota con la letra griega Sigma mayúscula.

- **Ejemplos:**
    
    - Alfabeto Binario: $\Sigma = \{0, 1\}$
        
    - Alfabeto Español: $\Sigma = \{a, b, c, ..., z\}$
        

### C. La Cadena (String o Palabra)

Es una secuencia finita de símbolos tomados de un alfabeto. Se suelen denotar con letras minúsculas del final del alfabeto ($w, u, v$).

- **Ejemplo:** Si $\Sigma = \{0, 1\}$, entonces $w = 01101$ es una cadena.
    

#### 👻 La Cadena Vacía ($\epsilon$ o $\lambda$)

Es una cadena que **no tiene símbolos**.

- **Longitud:** $|\epsilon| = 0$
    
- **Propiedad:** Es el "elemento neutro" de la concatenación (como el 0 en la suma o el 1 en la multiplicación).
    

---

## 2. Operaciones con Cadenas

Supongamos dos cadenas: $w = gallo$ y $v = pinto$.

### A. Longitud ($|w|$)

Es el número de símbolos que tiene la cadena.

- $|w| = 5$
    
- $|\epsilon| = 0$
    

### B. Concatenación ($w \cdot v$ o simplemente $wv$)

Es unir dos cadenas, una detrás de la otra. **El orden importa**.

- $w \cdot v = gallopinto$
    
- $v \cdot w = pintogallo$
    
- $w \cdot \epsilon = w$ (Concatenar con la vacía no hace nada).
    

### C. Potencia ($w^n$)

Es concatenar la cadena consigo misma $n$ veces.

- $w^2 = gallogallo$
    
- $w^0 = \epsilon$ (Cualquier cadena elevada a la cero es la cadena vacía).
    

### D. Inversa o Refleja ($w^R$)

Es la cadena escrita al revés.

- Si $w = amor$, entonces $w^R = roma$.
    

---

## 3. El Lenguaje ($L$)

### Definición Formal

Un lenguaje $L$ es simplemente un conjunto de cadenas formadas sobre un alfabeto $\Sigma$.

$$L \subseteq \Sigma^*$$

Puede ser:

1. **Finito:** $L = \{hola, mundo\}$
    
2. **Infinito:** $L = \{a, aa, aaa, aaaa...\}$ (Todas las potencias de 'a').
    
3. **Vacío:** $L = \emptyset$ (Un conjunto sin ninguna cadena).
    

> **⚠️ OJO CON ESTA TRAMPA DE EXAMEN:**
> 
> - $\{\epsilon\}$: Es un lenguaje que contiene una cadena (la vacía). **No está vacío.**
>     
> - $\emptyset$: Es un lenguaje que **no tiene nada**.
>     

---

## 4. Operaciones con Lenguajes

Aquí es donde la cosa se pone interesante para los compiladores. Supongamos dos lenguajes:

- $L = \{a, b\}$
    
- $M = \{1, 2\}$
    

### A. Unión ($L \cup M$)

Son todas las cadenas que están en $L$ **O** en $M$.

- $L \cup M = \{a, b, 1, 2\}$
    

### B. Concatenación de Lenguajes ($LM$)

Combina cada cadena de $L$ con cada cadena de $M$.

$$LM = \{xy \mid x \in L, y \in M\}$$

- Resultado: $\{a1, a2, b1, b2\}$
    

### C. Potencia de un Lenguaje ($L^n$)

- $L^0 = \{\epsilon\}$
    
- $L^1 = L$
    
- $L^2 = LL$ (Concatenar el lenguaje consigo mismo).
    
    - Ejemplo $L=\{0,1\}$ -> $L^2 = \{00, 01, 10, 11\}$
        

---

## 5. Las Clausuras (¡VITAL!)

Estas son la base de las **Expresiones Regulares** que verás después.

### A. Clausura de Kleene ($L^*$)

Representa cero o más repeticiones de las cadenas de $L$. Es la unión infinita de todas las potencias.

$$L^* = L^0 \cup L^1 \cup L^2 \cup L^3 ...$$

- **En español:** "Cualquier combinación posible de símbolos del alfabeto, incluyendo la cadena vacía".
    
- Si $\Sigma = \{a\}$, entonces $\Sigma^* = \{\epsilon, a, aa, aaa, aaaa, ...\}$
    

### B. Clausura Positiva ($L^+$)

Representa una o más repeticiones. Excluye la posibilidad de "cero veces" (a menos que $\epsilon$ ya estuviera en el lenguaje original).

$$L^+ = L^1 \cup L^2 \cup L^3 ...$$

- **Relación:** $L^+ = LL^*$
    

---

### Resumen Visual de Fórmulas

|**Operación**|**Notación**|**Significado**|
|---|---|---|
|**Concatenación**|$w \cdot v$|Pegar cadenas.|
|**Potencia 0**|$w^0$|$\epsilon$ (Cadena vacía).|
|**Universo**|$\Sigma^*$|Todas las cadenas posibles (infinito).|
|**Kleene (Estrella)**|$L^*$|Repetir 0 a n veces (incluye $\epsilon$).|
|**Positiva**|$L^+$|Repetir 1 a n veces.|

¿Quieres que hagamos un ejercicio práctico de **Concatenación vs Unión** para asegurarnos de que quedó claro?
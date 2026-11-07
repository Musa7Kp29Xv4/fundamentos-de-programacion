# SEMANA 4 — LISTAS, MATRICES Y FUNCIONES

**Curso:** Fundamentos de programación
**Semana:** 4 · del lunes 2 al viernes 6 de noviembre de 2026
**Entrega de la Actividad 3 (Tabla de Pitágoras):** viernes 6, 23:59 h

> Hasta ahora cada variable guardaba **un** dato. Esta semana aprendes a guardar **muchos datos en una sola variable** (listas), a acomodarlos **en filas y columnas** (matrices) y a **empaquetar tu código en piezas reutilizables** (funciones). Con esto tus programas dejan de ser una lista de instrucciones y empiezan a tener estructura.

---

## ÍNDICE

1. Tema 9: Listas
2. Tema 10: Listas de listas (matrices)
3. Tema 11: Funciones que NO regresan valor
4. Tema 12: Funciones que SÍ regresan valor
5. Detective de bugs: los errores de la semana
6. Chuleta final

---

# 1. TEMA 9: LISTAS

### 1.1 La idea: el setlist
Una banda no anota cada canción en una hoja distinta: hace **un setlist**, una sola hoja con todas las canciones **en orden** y numeradas. Una **lista** es eso: **una variable que guarda varios datos en orden**.

```python
setlist = ["Intro", "Riff", "Solo", "Encore"]
```

- Va entre **corchetes `[ ]`**, con los elementos separados por **comas**.
- Puede guardar cualquier tipo: textos, números, booleanos… y hasta otras listas.
- Una lista vacía se escribe `[]`.

### 1.2 Los índices: el número de track… empezando en 0
Cada elemento tiene una **posición (índice)**. En Python **se empieza a contar en 0**, como el piso "PB" de un edificio: la planta baja es el 0 y el primer piso es el 1.

```
setlist =   "Intro"   "Riff"   "Solo"   "Encore"
índice:        0         1        2         3
negativo:     -4        -3       -2        -1
```

```python
print(setlist[0])    # Intro   → el primero
print(setlist[2])    # Solo
print(setlist[-1])   # Encore  → el último (índice negativo)
print(len(setlist))  # 4       → cuántos elementos hay
```

> 🔑 **Regla de oro:** el último índice siempre es `len(lista) - 1`. En una lista de 4 elementos, `setlist[4]` **no existe** y truena con `IndexError`.

### 1.3 Modificar la lista

| Método | Qué hace | Analogía | Ejemplo |
| :--- | :--- | :--- | :--- |
| `lista.append(x)` | Agrega `x` **al final** | Agregar una canción al encore | `setlist.append("Bis")` |
| `lista.remove(x)` | Quita la **primera** vez que aparece `x` | Tachar una canción del setlist | `setlist.remove("Riff")` |
| `lista.sort()` | Ordena de menor a mayor (o en orden alfabético) | Ordenar el ranking | `puntajes.sort()` |
| `lista.sort(reverse=True)` | Ordena de mayor a menor | Del más votado al menos votado | `puntajes.sort(reverse=True)` |
| `len(lista)` | Dice **cuántos** elementos tiene | Contar canciones | `len(setlist)` |
| `lista[i] = x` | **Cambia** el elemento en la posición `i` | Cambiar una canción por otra | `setlist[0] = "Intro 2"` |

### 1.4 Recorrer una lista con `for`
Tienes **dos formas**. Las dos son correctas; elige según lo que necesites.

**Forma 1 — por valor** (cuando solo te interesa el dato):
```python
ventas = [120, 85, 200]
total = 0
for v in ventas:
    total = total + v
print(f"Total: {total}")   # Total: 405
```

**Forma 2 — por índice** (cuando también necesitas la posición):
```python
ciudades = ["Monterrey", "Guadalajara", "CDMX"]
for i in range(len(ciudades)):
    print(f"Fecha {i + 1}: {ciudades[i]}")
```

### 1.5 Llenar una lista con lo que escribe el usuario
El patrón más útil de la semana: **empieza vacía y agrega con `append()` dentro de un ciclo**.
```python
notas = []                         # la lista empieza vacía
for i in range(3):
    n = float(input("Nota: "))
    notas.append(n)                # cada nota se agrega al final
print(notas)                       # [8.0, 9.5, 10.0]
```

---

# 2. TEMA 10: LISTAS DE LISTAS (MATRICES)

### 2.1 La idea: los asientos del concierto
Tu boleto dice **"Fila B, Asiento 3"**: primero la fila, luego el asiento. Una **matriz** es igual: una lista donde **cada elemento es otra lista (una fila)**.

```python
sala = [
    ["A1", "A2", "A3"],   # fila 0
    ["B1", "B2", "B3"],   # fila 1
    ["C1", "C2", "C3"],   # fila 2
]
```
```
              columna 0   columna 1   columna 2
   fila 0  →    "A1"        "A2"        "A3"
   fila 1  →    "B1"        "B2"        "B3"
   fila 2  →    "C1"        "C2"        "C3"
```

### 2.2 Acceder: primero la fila, luego la columna
```python
print(sala[1][2])    # B3   → fila 1, columna 2
print(sala[0])       # ['A1', 'A2', 'A3'] → la fila 0 completa
print(len(sala))     # 3    → número de filas
print(len(sala[0]))  # 3    → número de columnas (largo de una fila)
```

> 🔑 `sala[1][2]` se lee **de izquierda a derecha**: "de la sala, toma la fila 1; de esa fila, toma la columna 2".

### 2.3 Construir una matriz con ciclos (¡clave para la actividad!)
Para construir una matriz se usan **dos `for` anidados**, uno dentro del otro.

**Analogía del reloj:** la manecilla de los minutos da **una vuelta completa** por cada hora. El `for` de adentro (columnas) da todas sus vueltas por **cada** vuelta del `for` de afuera (filas).

```python
tabla = []                       # 1. la matriz empieza vacía
for r in range(1, 4):            # 2. por cada fila...
    fila = []                    #    ...empieza una fila vacía
    for c in range(1, 4):        # 3. por cada columna...
        fila.append(r * c)       #    ...agrega un dato a la fila
    tabla.append(fila)           # 4. la fila terminada se agrega a la matriz
print(tabla)                     # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

> ⚠️ **Trampa clásica:** `fila = []` va **dentro** del `for` de filas. Si la pones antes del ciclo, todas las filas acaban siendo la misma lista (ver Detective de bugs).

### 2.4 Imprimir sin corchetes ni comas: `end` y `\t`
`print(tabla)` muestra la matriz como Python la guarda: `[[1, 2, 3], [2, 4, 6], …]`. Para que se vea como una tabla necesitas dos herramientas nuevas:

| Herramienta | Qué hace |
| :--- | :--- |
| `print(x, end="\t")` | Imprime `x` y, en lugar de saltar de línea, pone una **tabulación** (un espacio grande y parejo). |
| `print()` | Sin nada adentro: solo **salta de línea**. |

```python
for fila in tabla:              # por cada fila...
    for n in fila:              # ...por cada número de esa fila
        print(n, end="\t")      # imprímelo seguido de un tab
    print()                     # al terminar la fila, salta de línea
```
**Salida:**
```
1	2	3
2	4	6
3	6	9
```

---

# 3. TEMA 11: FUNCIONES QUE NO REGRESAN VALOR

### 3.1 La idea: una función es una receta con nombre
Una **función** es un bloque de código **con nombre** que puedes usar las veces que quieras. En lugar de copiar y pegar 10 líneas, escribes la función una vez y la **llamas** por su nombre.

### 3.2 Anatomía de una función
```python
def saludar(ciudad):                          # ← definición: def + nombre + (parámetros) + :
    print(f"¡Buenas noches, {ciudad}!")       # ← cuerpo (con sangría)

saludar("Monterrey")                          # ← llamada: nombre + (argumentos)
saludar("Guadalajara")                        # ← se puede llamar las veces que quieras
```

| Pieza | Qué es | Analogía |
| :--- | :--- | :--- |
| `def` | "Voy a definir una función" | Escribir la receta en el recetario |
| `saludar` | El nombre de la función | El nombre del platillo |
| `ciudad` (en el `def`) | **Parámetro**: el hueco que se llena al usarla | "___ gramos de harina" |
| `"Monterrey"` (en la llamada) | **Argumento**: el valor real que llena el hueco | "500 gramos" |

> 💡 **Definir no es ejecutar.** Cuando Python lee el `def`, solo aprende la receta; la cocina hasta que la **llamas**.

### 3.3 Funciones que NO regresan valor: el roadie
Un **roadie** afina la guitarra, conecta los cables y prueba el micrófono. **Hace su trabajo, pero no te entrega nada en la mano.** Así son las funciones sin `return`: **hacen algo** (casi siempre imprimir), y ya.

```python
def imprimir_tabla(tabla):
    for fila in tabla:
        for n in fila:
            print(n, end="\t")
        print()
```

Esta es justo la función que pide la **Actividad 3**.

---

# 4. TEMA 12: FUNCIONES QUE SÍ REGRESAN VALOR

### 4.1 La idea: la taquilla
En la taquilla **das algo** (tu dinero) y **te regresan algo** (tu boleto). Una función con `return` **calcula un resultado y te lo entrega** para que lo guardes o lo sigas usando.

```python
def precio_final(precio, desc):
    return precio - precio * desc      # ← entrega el resultado

boleto = precio_final(1450, 0.10)      # ← el resultado se guarda en una variable
print(f"Pagas ${boleto}")              # Pagas $1305.0
```

> 🔑 Cuando Python llega al `return`, **la función termina** en ese momento y entrega el valor. Lo que esté debajo del `return` ya no se ejecuta.

### 4.2 ¿Roadie o taquilla?

| | Sin `return` (roadie) | Con `return` (taquilla) |
| :--- | :--- | :--- |
| ¿Qué hace? | Una acción: imprimir, mostrar | Calcula y **entrega** un valor |
| ¿Se guarda su resultado? | No hay resultado que guardar | Sí: `x = funcion(...)` |
| Ejemplo de la actividad | `imprimir_tabla(tabla)` | `consultar_producto(tabla, r, c)` |

### 4.3 La trampa del `None`
Si guardas el resultado de una función **sin** `return`, guardas… **nada**. Python lo llama `None`.
```python
def saludar(ciudad):
    print(f"Hola, {ciudad}")

x = saludar("Mty")     # imprime: Hola, Mty
print(x)               # None   ← saludar() no regresó nada
```

### 4.4 Lo que pasa en la gira, se queda en la gira (variables locales)
Las variables que se crean **dentro** de una función **solo existen ahí**. Al terminar la función, desaparecen.
```python
def calcular():
    resultado = 10 * 2
    return resultado

calcular()
print(resultado)       # ❌ NameError: 'resultado' no existe afuera
```
✅ La forma correcta es **guardar lo que regresa**: `resultado = calcular()`.

### 4.5 La función clave de la Actividad 3
La tabla de Pitágoras **ya tiene guardados** todos los productos. Para saber cuánto es 2 × 3 **no hace falta multiplicar**: basta con **buscar** en la fila 2, columna 3.
```python
def consultar_producto(tabla, renglon, columna):
    return tabla[renglon - 1][columna - 1]     # sin usar *
```
**¿Por qué `- 1`?** Porque los factores empiezan en 1, pero los índices empiezan en 0. El factor 2 está en la fila de índice 1.

---

# 5. DETECTIVE DE BUGS: LOS ERRORES DE ESTA SEMANA

| Error | Cuándo pasa | Ejemplo | Solución |
| :--- | :--- | :--- | :--- |
| `IndexError: list index out of range` | Pides una posición que no existe | `setlist[4]` en una lista de 4 | El último índice es `len - 1` |
| `TypeError: … 'NoneType' …` | Usas el resultado de una función **sin** `return` | `total = saludar("Mty") + 1` | Agrega `return` a la función |
| `NameError` | Usas afuera una variable que solo existía dentro de una función | `print(resultado)` | Guarda lo que regresa: `x = funcion()` |
| **Bug silencioso: índice negativo** | Un factor 0 da `tabla[-1]`, que **no truena** pero da un resultado **incorrecto** | `0 × 3` muestra `9` | **Valida el rango** con `while` antes de consultar |
| **Bug silencioso: filas repetidas** | `fila = []` está **fuera** del `for` de filas | Todas las filas salen iguales | Mueve `fila = []` **dentro** del ciclo |

### El bug más traicionero de la Actividad 3
```python
r = int(input("Renglón: "))     # el usuario escribe 0
print(tabla[r - 1][2])           # tabla[-1][2] → ¡la ÚLTIMA fila! No truena, miente.
```
**Solución: validar el rango antes de consultar.**
```python
r = int(input("Renglón (1-10): "))
while r < 1 or r > 10:
    print("Fuera de rango")
    r = int(input("Renglón (1-10): "))
```

---

# 6. CHULETA FINAL

```python
# LISTAS
lista = ["a", "b", "c"]
lista[0]              # primer elemento
lista[-1]             # último elemento
len(lista)            # cuántos hay
lista.append("d")     # agregar al final
lista.remove("a")     # quitar
for x in lista: ...   # recorrer

# MATRICES
m = []
for r in range(filas):
    fila = []                     # ¡dentro del ciclo!
    for c in range(columnas):
        fila.append(valor)
    m.append(fila)
m[fila][columna]                  # acceder: primero fila, luego columna

# IMPRIMIR SIN CORCHETES
for fila in m:
    for x in fila:
        print(x, end="\t")
    print()

# FUNCIONES
def roadie(parametro):            # sin return: hace algo
    print(parametro)

def taquilla(parametro):          # con return: entrega algo
    return parametro + 1

resultado = taquilla(5)           # guarda lo que regresa
```

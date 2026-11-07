# 25 EJERCICIOS DE PRÁCTICA — SEMANA 4

**Curso:** Fundamentos de programación
**Alcance:** listas, matrices, funciones sin `return` y funciones con `return`.

Resuélvelos en `semana4/practica.ipynb` conforme avanzamos. **No son evaluables**, pero son el entrenamiento directo para la Actividad 3: los bloques M y R contienen las piezas que vas a necesitar.

**Nivel:** 🟢 calentamiento · 🟡 en forma · 🔴 modo experto

---

## BLOQUE L · LISTAS (lunes)

### L1 🟢 Tu setlist
Crea una lista con 4 canciones (las que tú quieras). Muestra la primera, la última (con índice negativo) y cuántas son.
**Ejemplo con** `["Intro", "Riff", "Solo", "Encore"]`:
```
Intro
Encore
4
```

### L2 🟢 Lista de invitados
Empieza con `invitados = ["Ana", "Luis"]`. Agrega a `"Sofía"` con `append()`, quita a `"Luis"` con `remove()` y muestra la lista final.
**Salida:** `['Ana', 'Sofía']`

### L3 🟢 Ranking
Ordena `puntajes = [7, 10, 8, 9]` de menor a mayor y luego de mayor a menor.
**Salida:**
```
[7, 8, 9, 10]
[10, 9, 8, 7]
```

### L4 🟡 Fechas de la gira
Pide **4 ciudades** con `input()` y guárdalas en una lista con `append()`. Después recórrela **por índice** y muestra cada una con su número de fecha.
**Entrada:** `Monterrey`, `Saltillo`, `Torreón`, `Chihuahua`
**Salida:**
```
Fecha 1: Monterrey
Fecha 2: Saltillo
Fecha 3: Torreón
Fecha 4: Chihuahua
```

### L5 🟡 Duración del disco
Dada `duraciones = [4.5, 3.2, 6.1, 5.0]` (minutos), calcula con un `for` la duración total y el promedio por canción.
**Salida:**
```
Duración total: 18.8 min
Promedio: 4.70 min
```

### L6 🟡 La mejor y la peor venta
Dada `ventas = [350, 120, 800, 45, 600]`, encuentra la mayor y la menor **con un `for` y un `if`** (sin usar `max()` ni `min()`).
**Salida:** `Mayor: 800 · Menor: 45`
💡 Pista: empieza suponiendo que la primera venta es la mayor y la menor.

### L7 🔴 Solo mayores de edad
Dada `edades = [15, 22, 17, 30, 19, 12]`, construye una **nueva lista** con solo las edades de 18 o más y muestra cuántas son.
**Salida:**
```
Mayores de edad: 3
[22, 30, 19]
```

---

## BLOQUE M · MATRICES (martes)

### M1 🟢 Encuentra tu asiento
Dada la matriz:
```python
sala = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]
```
Muestra el asiento de la fila 2, columna 1; la fila 0 completa; y cuántas filas y columnas tiene.
**Salida:**
```
C2
['A1', 'A2', 'A3']
Filas: 3 · Columnas: 3
```

### M2 🟢 Sin corchetes
Imprime `ventas = [[100, 200, 150], [80, 90, 120]]` como tabla, **sin corchetes ni comas**, usando `end="\t"`.
**Salida:**
```
100	200	150
80	90	120
```

### M3 🟡 Construye tu primera matriz
Con dos `for` anidados y `append()`, construye una matriz de **3 filas y 4 columnas** donde cada celda valga **fila + columna** (empezando en 0). Muéstrala con `print()`.
**Salida:** `[[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]`
🎯 Es exactamente el mismo esqueleto que la tabla de Pitágoras.

### M4 🟡 Total por vendedor
`ventas = [[100, 200, 150], [80, 90, 120]]` guarda las ventas de 2 vendedores (filas) en 3 días (columnas). Muestra el total de cada vendedor.
**Salida:**
```
Vendedor 1: 450
Vendedor 2: 290
```

### M5 🟡 Total por día
Con la misma matriz, muestra el total de cada **día** (cada columna).
**Salida:**
```
Día 1: 180
Día 2: 290
Día 3: 270
```
💡 Ahora el `for` de afuera recorre columnas y el de adentro, filas.

### M6 🔴 El gato
Imprime el tablero `[["X", "O", "X"], [" ", "X", "O"], ["O", " ", "X"]]` con `|` entre casillas y una línea de guiones entre filas. Después revisa si la **diagonal principal** (`[0][0]`, `[1][1]`, `[2][2]`) tiene tres `X`.
**Salida:**
```
X | O | X
---------
  | X | O
---------
O |   | X
¡X gana por la diagonal!
```

---

## BLOQUE F · FUNCIONES SIN `return` (miércoles)

### F1 🟢 Presenta a la banda
Define `presentar(nombre, genero)` que **imprima** la presentación. Llámala con dos bandas distintas.
**Ejemplo:** `presentar("Metallica", "thrash metal")` → `Con ustedes: Metallica (thrash metal)`

### F2 🟢 Imprime el setlist
Define `mostrar_setlist(canciones)` que reciba una lista e imprima cada canción numerada.
**Ejemplo con** `["Intro", "Riff", "Solo"]`:
```
1. Intro
2. Riff
3. Solo
```

### F3 🟡 Tu propia `imprimir_matriz`
Define `imprimir_matriz(m)` que imprima **cualquier** matriz sin corchetes ni comas. Pruébala con la matriz de M2 y con la de M3.
🎯 Esta función es la Parte A de la Actividad 3: si te sale aquí, ya la tienes.

### F4 🟡 ¿Qué imprime?
Sin ejecutarlo, predice qué imprime este código. Después ejecútalo y explica en una celda Markdown por qué la segunda línea dice lo que dice.
```python
def misterio(a, b):
    r = a + b
    print(f"Dentro: {r}")

res = misterio(4, 6)
print(f"Fuera: {res}")
```
**Salida:**
```
Dentro: 10
Fuera: None
```

---

## BLOQUE R · FUNCIONES CON `return` (jueves)

### R1 🟢 ¿Pasa el cadenero?
Define `es_mayor(edad)` que **regrese** `True` o `False`. Úsala dentro de un `if` para mostrar si alguien de 17 y alguien de 20 pueden entrar.
**Salida:**
```
17 años: no pasa
20 años: pasa
```

### R2 🟡 Duración total
Define `duracion_total(canciones)` que reciba una lista de duraciones y **regrese** su suma. Pruébala con `[4.5, 3.2, 6.1]`.
**Salida:** `El disco dura 13.8 minutos`

### R3 🟡 Promedio por alumno
Define `promedio(fila)` que **regrese** el promedio de una lista. Aplícala a cada fila de `calificaciones = [[8, 9, 10], [6, 7, 8]]`.
**Salida:**
```
Alumno 1: 9.00
Alumno 2: 7.00
```

### R4 🟡 El ticket: roadie + taquilla
Define dos funciones:
- `calcular_total(precios)` → **regresa** la suma de la lista.
- `mostrar_ticket(precios, total)` → **imprime** cada precio y el total, sin `return`.

Pruébalas con `[350, 120, 80]`.
**Salida:**
```
$350
$120
$80
TOTAL: $550
```

### R5 🔴 Buscador
Define `buscar(lista, valor)` que **regrese la posición** del valor en la lista, o `-1` si no está. Recórrela con `range(len(lista))`.
**Ejemplo con** `["Ana", "Luis", "Sofía"]`: `buscar(…, "Luis")` → `1` · `buscar(…, "Pedro")` → `-1`
💡 Pista: un `return` dentro del `for` termina la función en cuanto encuentra el valor.

---

## BLOQUE B · DETECTIVE DE BUGS (viernes)

### B1 🟢 El track que no existe
```python
setlist = ["Intro", "Riff", "Solo"]
print(setlist[3])
```
¿Qué error aparece, por qué y cómo se corrige para mostrar la última canción?

### B2 🟡 La suma que no suma
```python
def sumar(a, b):
    print(a + b)

total = sumar(2, 3) + 10
```
El código imprime `5` y luego truena con `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`. Explica qué significa `NoneType` aquí y corrige la función para que `total` valga `15`.

### B3 🔴 Las filas gemelas
Este código debería construir `[[1, 2], [2, 4]]`, pero imprime `[[1, 2, 2, 4], [1, 2, 2, 4]]`.
```python
tabla = []
fila = []
for r in range(1, 3):
    for c in range(1, 3):
        fila.append(r * c)
    tabla.append(fila)
print(tabla)
```
Encuentra el bug, explica **por qué** las dos filas salen iguales y corrígelo.
💡 Pista: ¿cuántas listas `fila` distintas se crean en total?

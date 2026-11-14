# SEMANA 5 — TUPLAS, DICCIONARIOS, EXCEPCIONES Y STRINGS

**Curso:** Fundamentos de programación
**Semana:** 5 · del lunes 9 al viernes 13 de noviembre de 2026
**Entrega de la Actividad 4 (Menú modular):** viernes 13, 23:59 h

> Ya sabes guardar muchos datos en una lista. Esta semana conoces a sus tres primos: la **tupla** (una lista que no se puede cambiar), el **diccionario** (datos con etiqueta en lugar de número) y el **string** visto de cerca (el texto también es una secuencia). Y aprendes a ponerle **casco** a tu programa para que no truene cuando el usuario escribe algo inesperado: las **excepciones**.

---

## ÍNDICE

1. Tema 13: Tuplas
2. Tema 14: Diccionarios
3. Tema 15: Excepciones
4. Tema 16: Strings
5. Todo junto: el menú modular
6. Chuleta final

---

# 1. TEMA 13: TUPLAS

### 1.1 La idea: el disco ya grabado
Una **lista** es como el setlist escrito en un pizarrón: puedes borrar, agregar y cambiar canciones. Una **tupla** es como el **disco ya grabado**: el orden de las canciones quedó fijo y **no se puede modificar**.

```python
setlist = ["Intro", "Riff", "Solo"]     # lista  → corchetes [ ] → se puede cambiar
disco   = ("Intro", "Riff", "Solo")     # tupla  → paréntesis ( ) → NO se puede cambiar
```

**¿Cuándo usar una tupla?** Cuando los datos **no deben cambiar nunca**: la fecha de un concierto `(13, 11, 2026)`, unas coordenadas `(20.59, -100.39)` o los días de la semana.

### 1.2 Leer una tupla: igual que una lista
```python
fecha = (13, 11, 2026)
print(fecha[0])      # 13    → índice 0, como en las listas
print(fecha[-1])     # 2026  → último
print(len(fecha))    # 3
```

### 1.3 Inmutable: no se puede cambiar
```python
fecha[0] = 14        # ❌ TypeError: 'tuple' object does not support item assignment
fecha.append(15)     # ❌ AttributeError: las tuplas no tienen append
```

### 1.4 ¿Y si necesito "agregar"? Creas una tupla NUEVA
No modificas la original: **unes** la tupla con otra usando `+` y obtienes **una tupla nueva**.
```python
notas = (8, 10, 7)
extra = int(input("Nota extra: "))     # el usuario escribe 9
nuevas = notas + (extra,)              # (8, 10, 7, 9)
```
> ⚠️ **La coma importa:** `(extra,)` es una tupla de un elemento. Sin la coma, `(extra)` es solo un número entre paréntesis y el `+` truena.

### 1.5 Desempaquetar: abrir la caja
Puedes sacar cada elemento de la tupla a su propia variable en una sola línea:
```python
dia, mes, anio = (13, 11, 2026)
print(f"Concierto: {dia}/{mes}/{anio}")    # Concierto: 13/11/2026
```

### 1.6 Convertir a lista para ordenarla
Una tupla no se puede ordenar (sería modificarla), pero puedes **copiarla a una lista** con `list()` y ordenar la copia:
```python
lista = list(nuevas)     # [8, 10, 7, 9]
lista.sort()             # [7, 8, 9, 10]
```

---

# 2. TEMA 14: DICCIONARIOS

### 2.1 La idea: el guardarropa del concierto
En el guardarropa entregas tu chamarra y te dan una **ficha** con un código, por ejemplo `A2`. Al salir no dices "la chamarra número 7 de la fila": entregas tu ficha y te dan **lo que corresponde a esa ficha**.

Un **diccionario** funciona igual: guarda parejas **clave → valor**. La clave es la ficha y el valor es lo que guardaste.

```python
guardarropa = {"A1": "chamarra", "A2": "casco"}
#              clave   valor      clave  valor
```

| | Lista | Diccionario |
| :--- | :--- | :--- |
| Se escribe con | `[ ]` | `{ }` con parejas `clave: valor` |
| Buscas por | Posición (`0`, `1`, `2`…) | **Clave** (`"A1"`, `"Ana"`…) |
| Ejemplo | `setlist[0]` | `contactos["Ana"]` |

### 2.2 Leer, agregar y actualizar
**La misma sintaxis sirve para las tres cosas:**
```python
contactos = {"Ana": "555-0101", "Luis": "555-0102"}

print(contactos["Ana"])            # leer       → 555-0101
contactos["Mía"] = "555-0103"      # agregar    → la clave "Mía" no existía
contactos["Luis"] = "555-9999"     # actualizar → la clave "Luis" ya existía
print(len(contactos))              # 3 parejas
```

### 2.3 ¿Existe esa clave? `in` y `get()`
Pedir una clave que no existe **truena** con `KeyError`. Para evitarlo:
```python
if "Pedro" in contactos:                       # opción 1: preguntar antes
    print(contactos["Pedro"])
else:
    print("No está en tus contactos")

print(contactos.get("Pedro", "No registrado"))  # opción 2: get() con valor por defecto
```

### 2.4 Recorrer un diccionario
```python
for nombre in contactos.keys():             # solo las claves
    print(nombre)

for telefono in contactos.values():         # solo los valores
    print(telefono)

for nombre, telefono in contactos.items():  # las dos cosas
    print(f"{nombre}: {telefono}")
```

### 2.5 El patrón contador
Un diccionario es perfecto para **contar** cosas, como los votos por género:
```python
votos = {"Metal": 0, "Rock": 0, "Punk": 0}
voto = input("Voto: ")
votos[voto] = votos[voto] + 1       # suma 1 al valor de esa clave
```

---

# 3. TEMA 15: EXCEPCIONES

### 3.1 La idea: el casco
No sales a rodar esperando caerte, pero **siempre** llevas casco. Las excepciones son el casco de tu programa: si algo sale mal, en lugar de que el programa **truene y se detenga**, lo atrapas y ejecutas un **plan B**.

| Sin excepciones | Con excepciones |
| :--- | :--- |
| El usuario escribe `veinte` → `ValueError` → el programa se cierra | El usuario escribe `veinte` → "Eso no es un número" → el programa sigue |

### 3.2 `try` / `except`
```python
try:
    edad = int(input("Edad: "))          # intenta esto...
    print(f"Registrado: {edad}")
except ValueError:
    print("Eso no es un número")         # ...si falla con ValueError, haz esto
print("Siguiente en la fila")            # el programa SIGUE
```

**Cómo se lee:**
1. Python **intenta** todo lo que está en el `try`.
2. Si una línea falla, **brinca de inmediato** al `except` (las líneas que faltaban del `try` ya no se ejecutan).
3. Si nada falla, el `except` se salta completo.

### 3.3 Un `except` para cada problema
Como en un taller: no se arregla igual una **ponchadura** que **quedarte sin gasolina**. Puedes tener un `except` distinto para cada tipo de error.
```python
try:
    a = int(input("Dividendo: "))
    b = int(input("Divisor: "))
    print(f"Resultado: {a / b}")
except ValueError:
    print("Escribe solo números enteros")      # escribió letras o lo dejó vacío
except ZeroDivisionError:
    print("No se puede dividir entre cero")    # escribió 0 como divisor
```

**Los errores que más vas a atrapar:**

| Excepción | Cuándo pasa | Ejemplo |
| :--- | :--- | :--- |
| `ValueError` | Convertir texto que no es número (o vacío) | `int("hola")`, `int("")` |
| `ZeroDivisionError` | Dividir entre cero | `10 / 0` |
| `KeyError` | Pedir una clave que no existe | `contactos["Pedro"]` |
| `IndexError` | Pedir una posición que no existe | `lista[10]` |
| `TypeError` | Operar tipos incompatibles | `"a" + 1` |

> ⚠️ **No uses `except:` solo.** Un `except` sin tipo atrapa **todo**, incluso tus propios errores de dedo, y te esconde el problema real. Di siempre qué error esperas.

### 3.4 Repetir hasta que el dato sea válido
Combina `while True`, `try` y `break` para volver a preguntar en lugar de rendirte:
```python
while True:
    try:
        n = int(input("Boletos: "))
        break                              # si llegó aquí, el dato es válido: sal
    except ValueError:
        print("Dato inválido, otra vez")
print(f"Compraste {n} boletos")
```

---

# 4. TEMA 16: STRINGS

### 4.1 La idea: el cartel del concierto
Un texto (string) es una **secuencia de letras**, como las letras de un cartel. Igual que una lista, tiene posiciones e índices, y además trae **herramientas** para transformarlo.

> 🔑 **Los strings son inmutables, como las tuplas.** Los métodos no cambian el texto original: **regresan uno nuevo**. Si quieres conservarlo, guárdalo: `grande = cartel.upper()`.

### 4.2 Las herramientas del cartel

| Herramienta | Qué hace | Ejemplo con `cartel = "metallica en vivo"` |
| :--- | :--- | :--- |
| `len(texto)` | Cuántos caracteres (espacios incluidos) | `17` |
| `texto.upper()` | Todo a mayúsculas | `"METALLICA EN VIVO"` |
| `texto.lower()` | Todo a minúsculas | `"metallica en vivo"` |
| `texto.title()` | Primera letra de cada palabra en mayúscula | `"Metallica En Vivo"` |
| `texto.replace(a, b)` | Cambia `a` por `b` | `cartel.replace("en vivo", "en Qro")` → `"metallica en Qro"` |
| `texto.split()` | Corta en palabras y regresa una **lista** | `["metallica", "en", "vivo"]` |
| `texto.strip()` | Quita espacios al inicio y al final | `"  hola  "` → `"hola"` |
| `palabra in texto` | ¿Contiene esa palabra? | `"vivo" in cartel` → `True` |

### 4.3 Contar palabras: `split()` + `len()`
```python
def contar_palabras(texto):
    return len(texto.split())

print(contar_palabras("el metal nunca muere"))   # 4
```

### 4.4 Limpiar lo que escribe el usuario
El usuario escribe `"  luis "` y en tu diccionario está `"Luis"`. Para Python **no son iguales**. Límpialo antes de buscar:
```python
nombre = input("Buscar: ").strip().title()   # "  luis " → "Luis"
```

---

# 5. TODO JUNTO: EL MENÚ MODULAR

### 5.1 La idea: el director y la banda
En un concierto, el director no toca todos los instrumentos: **le da la entrada** a cada músico cuando le toca. En un **menú modular**, el ciclo principal es el director y **cada opción llama a una función** que hace su parte.

```python
def seccion_tuplas():
    print("Aquí van las tuplas")

def seccion_strings():
    print("Aquí van los strings")

while True:
    op = input("Opción (1-3): ")
    if op == "1":
        seccion_tuplas()
    elif op == "2":
        seccion_strings()
    elif op == "3":
        break
    else:
        print("Opción inválida")
```

**¿Por qué así?**
- El menú queda **corto y fácil de leer**: solo decide a quién llamar.
- Cada función se puede **probar sola**.
- Si una sección falla, sabes exactamente **dónde buscar**.

> 💡 La opción se compara como **texto** (`op == "1"`), no como número. Así, si el usuario escribe una letra, cae en "Opción inválida" en lugar de tronar.

---

# 6. CHULETA FINAL

```python
# TUPLAS: ( ) — no se pueden cambiar
t = (8, 3, 12)
t[0]                        # leer
nueva = t + (5,)            # "agregar" = crear una nueva
a, b, c = t                 # desempaquetar
lista = list(t)             # convertir a lista para ordenarla

# DICCIONARIOS: { clave: valor }
d = {"Ana": "555-01"}
d["Ana"]                    # leer
d["Luis"] = "555-02"        # agregar o actualizar
"Pedro" in d                # ¿existe la clave?
d.get("Pedro", "No está")   # leer sin tronar
for k, v in d.items(): ...  # recorrer

# EXCEPCIONES: el casco
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...

# STRINGS
len(s)  s.upper()  s.lower()  s.title()
s.replace("a", "b")  s.split()  s.strip()
```

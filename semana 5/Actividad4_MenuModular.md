# ACTIVIDAD EVALUABLE 4 — MENÚ MODULAR: TUPLAS, DICCIONARIOS, EXCEPCIONES Y STRINGS

**Curso:** Fundamentos de programación
**Semana:** 5 · Tuplas, diccionarios, excepciones y strings
**Ponderación:** 6% de la calificación total del curso
**Modalidad:** Individual
**Fecha límite:** viernes 13 de noviembre de 2026, 23:59 h (sin prórroga)
**Evidencia de entrega:** liga pública de **tu mismo repositorio del curso**, con la carpeta `semana5/`

---

## 1. El reto

Vas a construir **un solo programa con un menú** que funcione como la consola de sonido de un concierto: cada botón (opción) activa una sección distinta, y el programa no se cierra hasta que tú lo decides.

```
1) Tuplas  2) Diccionarios  3) Excepciones  4) Strings  5) Salir
Elige una opción:
```

Cada opción **llama a una función** que demuestra lo que aprendiste esta semana. Al terminar, el menú vuelve a aparecer.

---

## 2. Requerimientos

Todo va en `semana5/menu_modular.ipynb`.

### Parte A — Opción 1: Tuplas
1. Crea una tupla llamada `numeros` con **al menos 5 números**.
2. Muestra su **tercer elemento**.
3. Pide **dos números** con `input()` y crea una **nueva tupla** que los incluya (la original no se modifica).
4. Convierte la **nueva tupla** en lista, **ordénala** y muéstrala.
5. Crea una **función con `return`** que reciba la tupla, **sume** todos sus elementos con un `for` y regrese el total. Muestra la suma de la nueva tupla.

### Parte B — Opción 2: Diccionarios
1. Crea un diccionario `contactos` con **al menos 3 contactos** (clave: nombre, valor: teléfono).
2. Pide un **nuevo contacto** (nombre y teléfono) y agrégalo.
3. Recorre las **claves** y muestra **solo los nombres**.
4. Crea una **función con `return`** que reciba el diccionario y un nombre, y **regrese el teléfono**. Pide un nombre a buscar y muestra su teléfono o, **si no existe**, un mensaje como `"Juan no está en tus contactos"`, sin que el programa truene.

### Parte C — Opción 3: Excepciones
1. Pide **dos números enteros**.
2. Si son válidos, muestra su **suma** y su **división** (el primero entre el segundo).
3. Con `try` / `except ValueError`, atrapa las **letras** y el **valor vacío** con un mensaje claro.
4. Con un `except ZeroDivisionError` **específico**, atrapa el **divisor cero** con un mensaje amable.

### Parte D — Opción 4: Strings
1. Crea una variable de texto llamada `mensaje`, con al menos 4 palabras.
2. Muestra su **longitud** con `len()`.
3. Muéstralo en **mayúsculas**.
4. **Reemplaza** una palabra del mensaje por otra de tu elección y muéstralo.
5. Crea una **función con `return`** que reciba un texto y regrese **cuántas palabras** tiene. Muestra el resultado.

### Parte E — El menú
1. Un ciclo `while` que muestre las opciones **1 a 5** y repita hasta elegir **5 (Salir)**.
2. Cada opción **llama a su función** (por ejemplo, `seccion_tuplas()`); el menú no contiene el código de las secciones.
3. Una opción que no existe (por ejemplo, `9` o `hola`) muestra **"Opción inválida"** y el menú continúa.

> 💡 **Tip:** compara la opción como texto (`opcion == "1"`). Así, si el usuario escribe una letra, no truena.

### Parte F — Evidencia de ejecución
Ejecuta el menú **una sola vez** y, en esa misma ejecución, recorre **todas** estas pruebas. La salida de la celda es tu evidencia:

| # | Prueba | Qué debe verse |
| :---: | :--- | :--- |
| 1 | Opción 1 | Tercer elemento, nueva tupla, lista ordenada y suma |
| 2 | Opción 2, buscando un contacto que **sí** existe | Nombres registrados y el teléfono |
| 3 | Opción 2, buscando un contacto que **no** existe | Mensaje de "no está", sin error |
| 4 | Opción 3 con dos números válidos | Suma y división |
| 5 | Opción 3 escribiendo **letras** | Mensaje de `ValueError` |
| 6 | Opción 3 dejando un valor **vacío** (solo Enter) | Mensaje de `ValueError` |
| 7 | Opción 3 con **divisor 0** | Mensaje de `ZeroDivisionError` |
| 8 | Opción 4 | Longitud, mayúsculas, reemplazo y número de palabras |
| 9 | Una opción que no existe | "Opción inválida" |
| 10 | Opción 5 | El programa termina |

Debajo, en una celda Markdown, copia esta tabla y marca con ✅ cada prueba que se ve en tu salida.

---

## 3. Estructura sugerida del notebook

| Celda | Tipo | Contenido |
| :---: | :--- | :--- |
| 1 | Markdown | Título, nombre, matrícula y en 2–3 líneas qué hace el programa |
| 2 | Código | Funciones de tuplas (Parte A) |
| 3 | Código | Funciones de diccionarios (Parte B) |
| 4 | Código | Función de excepciones (Parte C) |
| 5 | Código | Funciones de strings (Parte D) |
| 6 | Código | El menú (Parte E), **ejecutado con las 10 pruebas** |
| 7 | Markdown | Tabla de evidencia (Parte F) |

> 💡 **Atajo de detective:** prueba cada sección **por separado** (llamando a su función en una celda) antes de conectarla al menú.

---

## 4. Entregables

| Entregable | Archivo | Dónde |
| :--- | :--- | :--- |
| Notebook **ejecutado** (con la salida de las 10 pruebas visible) | `menu_modular.ipynb` | `semana5/` |
| **Evidencia** | **Liga pública de tu repositorio** | Plataforma del curso |

**Reglas de entrega:**
- **Fecha límite sin prórroga.** Si algo no funciona, entrega lo que tengas y documenta el error.
- Solo en **tu repositorio único del curso**, con al menos **3 commits** de la semana 5 con mensajes descriptivos.
- La salida del notebook **sustituye a las capturas de pantalla**: si en GitHub no se ve la ejecución, la Parte F vale 0.
- Las entregas idénticas o sustancialmente iguales entre alumnos valen 0.
- Puedo pedirte que expliques tu código en clase. Si no puedes explicarlo, no se considera tuyo.

---

## 5. Rúbrica de evaluación (100 pts)

| Parte | Criterio | Pts | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| A | **Tuplas** | 15 | Cumple los 5 requerimientos; la suma sale de una función con `return`. | Cumple 4 de 5. | Cumple 2 o 3. | Cumple 1 o ninguno. |
| B | **Diccionarios** | 15 | Cumple los 4 requerimientos; la búsqueda de un nombre inexistente no truena. | Cumple 4, pero la búsqueda de un nombre inexistente truena (`KeyError`), o cumple 3 de 4. | Cumple 2. | Cumple 1 o ninguno. |
| C | **Excepciones** | 15 | Suma y división; `except ValueError` (letras y vacío) y `except ZeroDivisionError` específicos, con mensajes claros. | Atrapa ambos errores, pero con un solo `except` genérico o sin mostrar la suma o la división. | Atrapa solo uno de los dos errores. | Sin `try` / `except`. |
| D | **Strings** | 15 | Cumple los 5 requerimientos; el conteo sale de una función con `return`. | Cumple 4 de 5. | Cumple 2 o 3. | Cumple 1 o ninguno. |
| E | **Menú modular** | 15 | `while` con 5 opciones; cada opción llama a una función; la opción inválida no truena; solo termina con 5. | Funciona, pero alguna sección está escrita dentro del menú en lugar de una función. | Falta alguna opción, o una opción inválida truena el programa. | Sin menú. |
| F | **Evidencia de ejecución** | 15 | Las 10 pruebas se ven en la salida y la tabla está marcada. | Faltan 1 o 2 pruebas. | Faltan 3 a 5 pruebas. | Notebook sin ejecutar o faltan más de 5 pruebas. |
| — | **Entrega en GitHub** | 10 | Mismo repositorio, carpeta `semana5/`, notebook ejecutado y 3 o más commits descriptivos. | 3 commits poco descriptivos o detalle menor de estructura. | 1 o 2 commits, o archivo fuera de `semana5/`. | Repositorio nuevo o privado, o sin liga. |
| | **TOTAL** | **100** | | | | |

---

## 6. Checklist antes de entregar

- [ ] Mi tupla original **no cambia**: creé una nueva con los dos números.
- [ ] Buscar a alguien que **no existe** no truena el programa.
- [ ] Probé letras, vacío y divisor 0 en la opción 3.
- [ ] Mi menú solo llama funciones y no termina hasta elegir 5.
- [ ] Escribí `9` o `hola` en el menú y dice "Opción inválida".
- [ ] En **una sola ejecución** se ven las 10 pruebas.
- [ ] Mi notebook está ejecutado y se ven las salidas en GitHub.
- [ ] Tengo 3 commits o más de la semana 5, en el mismo repositorio del curso.

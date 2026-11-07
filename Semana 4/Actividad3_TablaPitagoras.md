# ACTIVIDAD EVALUABLE 3 — TABLA DE PITÁGORAS EN MATRIZ

**Curso:** Fundamentos de programación
**Semana:** 4 · Listas, matrices y funciones
**Ponderación:** 6% de la calificación total del curso
**Modalidad:** Individual
**Fecha límite:** viernes 6 de noviembre de 2026, 23:59 h (sin prórroga)
**Evidencia de entrega:** liga pública de **tu mismo repositorio del curso**, con la carpeta `semana4/`

---

## 1. El reto

Antes de las calculadoras, en las escuelas se usaba la **tabla de Pitágoras**: una cuadrícula con todos los productos del 1×1 al 10×10. Para saber cuánto es 7 × 8 no se multiplicaba: **se buscaba** el cruce de la fila 7 con la columna 8.

Tu misión: construir esa tabla dentro de una **matriz** (lista de listas), mostrarla bonita en pantalla y crear una función que conteste cualquier multiplicación **consultando la tabla, sin multiplicar**.

```
1   2   3   4   5   6   7   8   9   10
2   4   6   8   10  12  14  16  18  20
3   6   9   12  15  18  21  24  27  30
...
10  20  30  40  50  60  70  80  90  100
```

---

## 2. Requerimientos

Todo va en `semana4/tabla_pitagoras.ipynb`.

### Parte A — Construir la matriz
1. Construye la tabla de Pitágoras de **10 × 10** como **lista de listas**, usando **dos `for` anidados** y `append()`.
2. Aquí **sí puedes usar `*`**: cada celda es `fila * columna`.

### Parte B — Mostrarla: función que NO regresa valor
3. Define `imprimir_tabla(tabla)`, una función **sin `return`**, que imprima la matriz completa.
4. La salida debe verse **sin corchetes ni comas**, con los números separados por tabulaciones (`end="\t"`).

### Parte C — Consultarla: función que SÍ regresa valor
5. Define `consultar_producto(tabla, renglon, columna)`, una función que **regresa** con `return` el producto **consultando la matriz**.
6. **Restricción:** dentro de `consultar_producto` está **prohibido usar `*`**. El resultado sale de `tabla[renglon - 1][columna - 1]`.

### Parte D — Programa principal
7. Pide al usuario **dos factores** (renglón y columna) con `input()` e `int()`.
8. **Valida** que cada factor esté entre **1 y 10** con un `while`: si está fuera de rango, muestra un aviso y vuelve a pedirlo.
9. Llama a `consultar_producto`, **guarda** lo que regresa en una variable y muestra el resultado, por ejemplo: `7 x 8 = 56`.

> ⚠️ **¿Por qué validar?** Si alguien escribe `0`, el programa consulta `tabla[-1]`, que en Python es **la última fila**. No aparece ningún error, pero el resultado es **falso**. Es un bug silencioso, el más peligroso.

### Parte E — Casos de prueba
10. En una celda Markdown, documenta **4 pruebas** con lo que **esperabas** y lo que **obtuviste**:

| # | Entrada | Esperado |
| :---: | :--- | :--- |
| 1 | `7` y `8` | `56` |
| 2 | `1` y `1` | `1` |
| 3 | `10` y `10` | `100` |
| 4 | Primero `0` (o `12`), luego un valor válido | Aviso de fuera de rango y después el resultado correcto |

---

## 3. Estructura sugerida del notebook

| Celda | Tipo | Contenido |
| :---: | :--- | :--- |
| 1 | Markdown | Título, nombre, matrícula y en 2–3 líneas qué hace el programa |
| 2 | Código | Parte A: construcción de la matriz |
| 3 | Código | Partes B y C: las dos funciones |
| 4 | Código | Parte D: programa principal |
| 5 | Markdown | Parte E: casos de prueba |

> 💡 **Atajo de detective:** construye primero la tabla de **3 × 3** y verifica que `imprimir_tabla` la muestre bien. Cuando funcione, cambia el 3 por 10.

---

## 4. Entregables

| Entregable | Archivo | Dónde |
| :--- | :--- | :--- |
| Notebook **ejecutado** (con salidas visibles) | `tabla_pitagoras.ipynb` | `semana4/` |
| **Evidencia** | **Liga pública de tu repositorio** | Plataforma del curso |

**Reglas de entrega:**
- **Fecha límite sin prórroga.** Si algo no funciona, entrega lo que tengas y documenta el error.
- Solo en **tu repositorio único del curso**, con al menos **3 commits** de la semana 4 con mensajes descriptivos.
- El notebook debe estar **ejecutado**: si en GitHub no se ven las salidas, la Parte E vale 0.
- Las entregas idénticas o sustancialmente iguales entre alumnos valen 0.
- Puedo pedirte que expliques tu código en clase. Si no puedes explicarlo, no se considera tuyo.

---

## 5. Rúbrica de evaluación (100 pts)

| Parte | Criterio | Pts | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| A | **Matriz con ciclos** | 15 | Matriz 10×10 correcta, construida con dos `for` anidados y `append()`. | Matriz correcta pero de otro tamaño, o con un detalle menor. | Matriz escrita a mano o con datos incorrectos. | No hay matriz. |
| B | **Función sin `return`** | 15 | `imprimir_tabla(tabla)` sin `return`, recibe la matriz como parámetro e imprime la tabla completa. | Correcta, pero usa la variable global en lugar del parámetro. | Imprime la tabla, pero fuera de una función. | No existe. |
| B | **Impresión sin corchetes ni comas** | 10 | Toda la tabla tabulada, sin corchetes ni comas. | Formato correcto con un detalle menor (alineación, una fila). | Se ven corchetes o comas en alguna parte. | Muestra la lista de Python tal cual. |
| C | **Función con `return`** | 15 | `consultar_producto` regresa el valor con `return` consultando `tabla[renglon - 1][columna - 1]`; el resultado se guarda en una variable. | Correcta, pero imprime dentro de la función además de regresar. | Error de índices (por ejemplo, sin `- 1`). | No existe o no usa `return`. |
| C | **Restricción: sin `*` al consultar** | 15 | `consultar_producto` no usa `*`: el resultado sale de la matriz. | — | — | Usa `*` (o cualquier operación) para calcular el producto en lugar de consultarlo. |
| D | **Captura y validación** | 10 | Pide ambos factores con `input()`/`int()` y valida el rango 1–10 con `while` para los dos. | Valida solo uno de los factores. | Captura sin validación. | No captura factores. |
| E | **Casos de prueba** | 10 | Las 4 pruebas documentadas con esperado y obtenido; incluye la de fuera de rango. | 3 pruebas, o sin la de fuera de rango. | 1 o 2 pruebas. | No las incluye o el notebook no está ejecutado. |
| — | **Entrega en GitHub** | 10 | Mismo repositorio, carpeta `semana4/`, notebook ejecutado y 3 o más commits descriptivos. | 3 commits poco descriptivos o detalle menor de estructura. | 1 o 2 commits, o archivo fuera de `semana4/`. | Repositorio nuevo o privado, o sin liga. |
| | **TOTAL** | **100** | | | | |

> En la restricción de la Parte C solo existen dos niveles: se cumple o no se cumple.

---

## 6. Checklist antes de entregar

- [ ] Mi tabla se construye con dos `for` y `append()`, no escrita a mano.
- [ ] `imprimir_tabla` no tiene `return` y la tabla se ve sin corchetes ni comas.
- [ ] `consultar_producto` tiene `return` y **no tiene ningún `*`**.
- [ ] Probé `0` y `12`: el programa los rechaza y vuelve a preguntar.
- [ ] Probé `7 × 8 = 56`, `1 × 1 = 1` y `10 × 10 = 100`.
- [ ] Mi notebook está ejecutado y se ven las salidas en GitHub.
- [ ] Tengo 3 commits o más de la semana 4, en el mismo repositorio del curso.

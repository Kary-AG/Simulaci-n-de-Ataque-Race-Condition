# 🧨 Simulación de Ataque: Race Condition (Condición de Carrera)

## Karyme Azpeitia García

## 📚 Tema del Libro
**Fuente:** *Modern Operating Systems* (Andrew S. Tanenbaum) - Capítulo 9 "Security"
- **Sección:** 9.5.4 - Race Conditions
- **Temas relacionados:** 9.5 (Program Security), 9.8 (Security in Operating Systems)

---

## 🔍 Descripción del Ataque

Una **Race Condition** o **Condición de Carrera** ocurre cuando el comportamiento de un programa depende del orden o el "timing" de dos o más procesos/hilos que acceden a un recurso compartido (como una variable, un archivo o la memoria) de forma concurrente, **sin la sincronización adecuada**.

El atacante explota esta ventana de tiempo entre la **verificación** de una condición (ej: "¿hay saldo suficiente?") y la **acción** (ej: "retirar dinero") para modificar el estado del sistema antes de que la primera operación se complete.

### ⚠️ Peligros Potenciales
- **Corrupción de datos** (saldos negativos, inventarios inconsistentes).
- **Escalada de privilegios** (acceder a archivos del sistema).
- **Denegación de servicio** (bloquear recursos).
- **Ejecución de código no autorizado.**

### Ejemplo clásico
```text
Hilo A: Verifica saldo (balance >= 100) -> Verdadero
Hilo B: Verifica saldo (balance >= 100) -> Verdadero (AÚN no ha cambiado)
Hilo A: Retira 100 (balance = balance - 100)
Hilo B: Retira 100 (balance = balance - 100)
Resultado: Se retiraron 200 cuando solo había 100.
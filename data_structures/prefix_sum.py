nums = [3,1,4,1,5]
n = len(nums)

# --- PREFIX --- #
prefix = [0] * n
prefix[0] = nums[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + nums[i]
    
# prefix = [3, 4, 8, 9, 14]


# --- POSTFIX --- #
postfix = [0] * n
postfix[n-1] = nums[n-1]
for i in range(n-2, -1, -1):
    postfix[i] = postfix[i+1] + nums[i]
    
# postfix = [14, 11, 10, 6, 5]

def range_sum(l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l - 1]


print(range_sum(1, 3))


"""
La idea del Prefix Sum
¿Qué tal si pre-calculamos todas las sumas acumuladas de izquierda a derecha?

original:  [3,  1,  4,  1,  5]
prefix:    [3,  4,  8,  9, 14]
Cada posición i en prefix dice: "la suma de todo desde el inicio hasta aquí".

prefix[0] = 3
prefix[1] = 3+1 = 4
prefix[2] = 3+1+4 = 8
... y así.

Ahora, ¿cómo sacarías la suma del rango [1..3] con este array?


prefix[3] - prefix[0] = 9 - 3 = 6  ✓
Una sola resta. Sin importar el tamaño del array. O(1) en vez de O(n).

El Postfix Sum es lo mismo pero al revés

original:  [3,  1,  4,  1,  5]
postfix:   [14, 11, 10,  6,  5]
Cada posición i dice: "la suma de todo desde aquí hasta el final".

¿Cuándo usas cada uno?
"¿Cuánto hay a la izquierda de i?"	Prefix
"¿Cuánto hay a la derecha de i?"	Postfix
"¿Cuánto hay antes Y después de i?"	Ambos juntos

El truco maestro: usarlos juntos
Problema clásico: "Para cada elemento, encuentra el producto de todos los demás".
Con prefix y postfix puedes hacer esto sin dividir, en O(n). El elemento i = prefix[i-1] * postfix[i+1].
Resumen en una frase: Pre-calculas acumulados una vez, y luego cualquier consulta de rango es una simple resta. Pagas O(n) una vez para ahorrar O(n) en cada consulta futura.
"""

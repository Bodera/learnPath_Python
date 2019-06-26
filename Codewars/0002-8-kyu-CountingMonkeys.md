## Tarea
Llevas a tu primo al bosque para ver a los monos. Usted sabe que hay un cierto número (n), pero su primo es demasiado joven para apreciar el número completo, tiene que comenzar a contarlos desde 1.

Como buen primo, te sentarás y contarás con él. Dado el número (n), rellene una colección con todos los números hasta e incluyendo ese número, pero excluyendo cero.

Por ejemplo, si n = 10:

return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Solución

```python
def enumeraSimios:
	
	result = []
	totaleSimios = int(input('Proporciona el número total de monos'))
	if (totaleSimios >= 1):
		try:
			for valor in range(totaleSimios) if valor >= 1:
				result.append(totaleSimios - 1)
			
		except ValueError:
			print('El número de simios solo puede ser un número entero hasta ayer.')
	else:
		print('Parece que no hay simios.')
	return totaleSimios

def main():
```
## Come calcolare il rischio reale di ciascun nodo:
##	1.	Il nodo A ha N nodi adiacenti. Per ogni coppia di nodi tra questi N, viene calcolato un valore di rischio.
##	2.	Il massimo valore calcolato tra queste coppie rappresenta il rischio reale del nodo A.
##	3.	Il valore del rischio è calcolato come la media tra il rischio stimato del nodo A e il rischio reale del nodo adiacente, arrotondato per eccesso.
##	4.	Se il rischio reale di un nodo adiacente non è disponibile, viene utilizzato il suo rischio stimato.
##	5.	Il rischio reale di un nodo non può mai essere inferiore al suo rischio stimato. Se il valore calcolato è inferiore, il rischio reale viene impostato uguale al rischio stimato.
##Questo processo deve essere ripetuto per tutti i nodi, garantendo una valutazione completa e aggiornata dei rischi. L’output finale conterrà il rischio reale di tutti i Servizi Chiave della rete.


with open("input.txt", "r") as file:
    content = file.readlines()

if not content:
    raise ValueError("Il file è vuoto")

# Legge il primo numero
num_iterations = int(content[0].strip())

index = 1

for _ in range(num_iterations):
    if index >= len(content):
        raise ValueError("Il file non ha abbastanza righe per completare tutte le iterazioni")

    # Legge il numero di righe da estrarre
    num_lines = int(content[index].strip())
    index += 1  # Sposta l'indice alla prima riga da leggere
    # Legge le successive `num_lines` righe
    extracted_lines = [content[i].strip() for i in range(index, min(index + num_lines, len(content)))]
    index += num_lines  # Aggiorna l'indice per la prossima iterazione

    for line in extracted_lines:
        print(line)

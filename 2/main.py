import math

def calcola_rischio_reale(nodi):
    rischio_reale = {nodo_id: nodi[nodo_id][0] for nodo_id in nodi}  # Inizializziamo il rischio reale con il rischio stimato

    aggiornato = True
    while aggiornato:  # Ripetiamo fino a quando i rischi reali non smettono di aggiornarsi
        aggiornato = False
        for nodo_id, (rischio_stimato, adiacenti) in nodi.items():
            massimo_rischio = rischio_stimato
            for adiacente in adiacenti:
                if adiacente in rischio_reale:
                    rischio_calcolato = (rischio_reale[adiacente] + rischio_stimato + 1) // 2  # Arrotondiamo per eccesso
                    massimo_rischio = max(massimo_rischio, rischio_calcolato)
            if massimo_rischio > rischio_reale[nodo_id]:  # Aggiorniamo il rischio reale se necessario
                rischio_reale[nodo_id] = massimo_rischio
                aggiornato = True

    return rischio_reale


def leggi_input_da_file(file_path):
    with open(file_path, "r") as file:
        num_casi = int(file.readline().strip())  # Numero di casi di test

        # Creiamo il file di output
        with open("output.txt", "w") as output_file:
            for case_num in range(1, num_casi + 1):
                num_nodi = int(file.readline().strip())  # Numero di nodi
                nodi = {}

                for _ in range(num_nodi):
                    dati = file.readline().strip().split()
                    nodo_id = dati[0]
                    rischio_stimato = int(dati[1])
                    adiacenti = dati[2:] if len(dati) > 2 else []  # Lista di ID dei nodi connessi

                    nodi[nodo_id] = (rischio_stimato, adiacenti)

                # Calcola il rischio reale per i nodi
                rischio_reale = calcola_rischio_reale(nodi)
       
                # Filtra solo i nodi di tipo 'k' (Servizi Chiave) e ordina per ID
                servizi_chiave = {nodo_id: rischio_reale[nodo_id] for nodo_id in nodi if nodo_id[0] == 'k'}
                servizi_chiave_ordinati = sorted(servizi_chiave.items())

                # Scriviamo il risultato per ogni caso di test nel formato richiesto
                output_file.write(f"Case #{case_num}: {len(servizi_chiave)} ")
                for nodo, rischio in servizi_chiave_ordinati:
                    output_file.write(f"{nodo} {rischio} ")
                output_file.write("\n")

# Esegui il programma passando il percorso del file
file_path = "input.txt"  # Modifica questo percorso con il percorso del tuo file di testo
leggi_input_da_file(file_path)
import pandas as pd

with open("ruletimevc.csv") as f:
    lines = [line.strip() for line in f if line.strip()]

gruppi = {}
gruppo_corrente = None
for line in lines:
    # Se la riga non contiene una virgola, è il nome del gruppo
    if "," not in line:
        gruppo_corrente = line
        gruppi[gruppo_corrente] = []
    else:
        valori = line.split(",")
        # Escludi il primo valore (IP), converti i restanti in float
        try:
            gruppi[gruppo_corrente].append([float(x) for x in valori[1:]])
        except Exception:
            pass  # Salta righe malformate

# Calcola la media per ogni gruppo
output = []
for nome, valori in gruppi.items():
    if valori:  # Solo se ci sono dati
        df = pd.DataFrame(valori)
        media = df.mean()
        output.append([nome] + media.tolist())

# Crea DataFrame finale e salva su CSV
colonne = ["gruppo", "valore1", "valore2", "valore3","valore4", "valore5"]
df_out = pd.DataFrame(output, columns=colonne)
df_out.to_csv("medie_per_gruppovc.csv", index=False)
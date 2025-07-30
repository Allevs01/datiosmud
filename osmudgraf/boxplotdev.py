import matplotlib.pyplot as plt
import pandas as pd

# === File CSV ===
csv_vc = "ruletimevc.csv"
csv_x509 = "ruletimecert.csv"

plt.rcParams.update({'font.size': 11})

# === Funzione per leggere e separare i dati per gruppo ===
def leggi_dati(filename, col_index=1):
    dati = {}
    gruppo_corrente = None
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Se la linea non contiene virgole, è un'etichetta di gruppo
            if "," not in line:
                gruppo_corrente = line.strip()
                dati[gruppo_corrente] = []
            else:
                valori = line.split(",")
                if len(valori) > col_index:
                    try:
                        tempo = float(valori[col_index]) * 1000   # 🔥 conversione in ms
                        dati[gruppo_corrente].append(tempo)
                    except ValueError:
                        continue
    return dati

# === Leggi i dati ===
dati_vc = leggi_dati(csv_vc, col_index=1)      # secondo valore (autenticazione)
dati_x509 = leggi_dati(csv_x509, col_index=1)  # secondo valore (autenticazione)

# === Prepara i dati per boxplot ===
labels = ["Rosbot3", "Up Xtreme", "PI 0"]
vc_values = [dati_vc[g] for g in labels]
x509_values = [dati_x509[g] for g in labels]

# === Boxplot affiancati ===
fig, ax = plt.subplots(figsize=(7,5))

positions_vc = [i*2 - 0.3 for i in range(len(labels))]
positions_x509 = [i*2 + 0.3 for i in range(len(labels))]

bp_vc = ax.boxplot(vc_values, positions=positions_vc, widths=0.5, patch_artist=True,
                   boxprops=dict(facecolor="#4682A9", color="#4682A9"),
                   medianprops=dict(color="black"),
                   whiskerprops=dict(color="#4682A9"),
                   capprops=dict(color="#4682A9"))

bp_x509 = ax.boxplot(x509_values, positions=positions_x509, widths=0.5, patch_artist=True,
                     boxprops=dict(facecolor="#5EA04A", color="#5EA04A"),
                     medianprops=dict(color="black"),
                     whiskerprops=dict(color="#5EA04A"),
                     capprops=dict(color="#5EA04A"))

# === Personalizzazione grafico ===
ax.set_xticks([i*2 for i in range(len(labels))])
ax.set_xticklabels(labels)
ax.set_ylabel("Authentication Time (ms)")
ax.legend([bp_vc["boxes"][0], bp_x509["boxes"][0]], ["Our Solution", "X.509"], frameon=True)

ax.grid(axis='y', linestyle='-', alpha=0.6)

plt.tight_layout()
plt.savefig("boxplot_vc_x509_ms.pdf", dpi=300)
plt.savefig("boxplot_vc_x509_ms.pgf")
plt.show()

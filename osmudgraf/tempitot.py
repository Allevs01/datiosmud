import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# === Dati incorporati (in secondi) ===
data_x509 = {
    "gruppo": ["Up Xtreme", "PI 0", "Rosbot3"],
    "media_device": [1.101888888888889, 1.2407, 1.4453999999999998]
}

data_vc = {
    "gruppo": ["Up Xtreme", "PI 0", "Rosbot3"],
    "media_device": [1.2779, 1.1826, 1.1637]
}

plt.rcParams.update({'font.size': 11})

df_x509 = pd.DataFrame(data_x509)
df_vc = pd.DataFrame(data_vc)

# === Estrai i gruppi e converti in millisecondi ===
gruppi = df_x509["gruppo"]
device_x509 = df_x509["media_device"] * 1000
device_vc = df_vc["media_device"] * 1000

# === Configurazione posizioni barre ===
x = np.arange(len(gruppi))
width = 0.18

# === Stile e figura ===
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(6, 5))

# ✅ Solo griglia orizzontale
ax.grid(False)               # disable all
ax.grid(True, axis='y', linestyle='--', alpha=0.5) 

# === Colori ===
col_x509 = "#5EA04A"
col_vc = "#4682A9"

# === Disegna le barre ===
bars_x509 = ax.bar(x - 0.12, device_x509, width, label="X.509", color=col_x509)
bars_vc = ax.bar(x + 0.12, device_vc, width, label="Our Solution", color=col_vc)

# === Aggiungi i valori sopra le barre (in ms) ===
for bar in bars_x509:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 5, f"{h:.1f}",
            ha='center', va='bottom', fontsize=10)

for bar in bars_vc:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 5, f"{h:.1f}",
            ha='center', va='bottom', fontsize=10)

# === Etichette ===
ax.set_ylabel("Average Device Time (ms)")
ax.set_xticks(x)
ax.set_xticklabels(gruppi)
ax.legend(frameon=True)

# === Salva grafico ===
plt.tight_layout()
plt.savefig("confronto_media_device.pgf", dpi=300)
plt.savefig("confronto_media_device.pdf", dpi=300)

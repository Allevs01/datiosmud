import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 11})

# === Leggi i CSV ===
df_cert = pd.read_csv("medie_per_gruppo.csv")
df_vc = pd.read_csv("medie_per_gruppovc.csv")

# === Estrai dati e convertili in millisecondi ===
x = df_cert["gruppo"]
aut_cert = df_cert["media_autenticazione"] * 1000
aut_vc = df_vc["media_autenticazione"] * 1000
gan_vc = df_vc["media_verifica"] * 1000

# === Posizioni barre ===
bar_width = 0.18
index = np.arange(len(x))
offset = 0.10

fig, ax = plt.subplots(figsize=(10,6))
ax.grid(True, axis='y', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# === Palette colori ===
col_cert = "#5EA04A"
col_vc_full = "#4682A9"
col_vc_light = "#A3C4DC"

# --- Barre CERT ---
bars_cert = ax.bar(index - offset, aut_cert, bar_width,
                   label="X.509 - Authentication", color=col_cert)

# --- Barre VC: Full ---
bars_full_vc = ax.bar(index + offset, aut_vc, bar_width,
                      label="Our Solution - Full", color=col_vc_full, zorder=2)

# --- Barre VC: Verifica ---
bars_verifica_vc = ax.bar(index + offset, gan_vc, bar_width,
                          label="Our Solution - Verification Only", color=col_vc_light, zorder=3)

# === Etichette sopra le barre ===
def add_labels(bars, y_offset=1):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + y_offset,
                f"{height:.1f}", ha='center', va='bottom', fontsize=8)

add_labels(bars_cert)
add_labels(bars_full_vc)

# === Etichette e legenda ===
ax.set_xlabel("Device")
ax.set_ylabel("Average Time (ms)")
ax.set_xticks(index)
ax.set_xticklabels(x)
ax.legend()

plt.tight_layout()
plt.savefig("grafico_eterogeneita.pgf")  
plt.savefig("grafico_eterogeneita.pdf") # <-- Salva in PNG
print("✅ Grafico esportato come 'grafico_eterogeneita.pgf'")

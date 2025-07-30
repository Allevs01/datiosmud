import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11})

# === Dati medi CPU per ciascun dispositivo ===
groups = ["Up Xtreme", "PI 0", "Rosbot3"]
means_cpu_x509 = [1.3, 22.2, 1.6]  # medie CPU scenario X.509
means_cpu_vc = [1.0, 13.2, 1.0]    # medie CPU scenario VC
std_cpu_x509 = [0.2, 2.1, 0.3]     # deviazioni standard
std_cpu_vc = [0.1, 1.5, 0.2]       # deviazioni standard

x = np.arange(len(groups))
width = 0.18  # barre più strette

# === Colori moderni (pastello) ===
col_x509 = "#5EA04A"
col_vc   = "#4682A9"

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(6,5))

offset = 0.10  # distanza tra le barre

# === Barre con barre di errore ===
bars_x509 = ax.bar(x - offset, means_cpu_x509, width, label="X.509",
                   color=col_x509, yerr=std_cpu_x509, capsize=4, ecolor='black')
bars_vc   = ax.bar(x + offset, means_cpu_vc, width, label="Our Solution",
                   color=col_vc, yerr=std_cpu_vc, capsize=4, ecolor='black')

# === Etichette valori sopra le barre ===
for bar in bars_x509:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 2, f"{h:.1f}",
            ha='center', va='bottom', fontsize=9)

for bar in bars_vc:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 2, f"{h:.1f}",
            ha='center', va='bottom', fontsize=9)

# === Personalizzazioni ===
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.set_ylabel("CPU%")
ax.legend(frameon=True)

ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')

ax.grid(True, axis='y', linestyle='--', alpha=0.7)
ax.grid(False, axis='x')

plt.tight_layout()
plt.savefig("cpu_comparison_err.pgf")
plt.savefig("cpu_comparison_err.pdf", dpi=300)
plt.show()

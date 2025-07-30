import pandas as pd
import matplotlib.pyplot as plt

# === Dati RAM ===
ram_data = {
    "device": ["Up Xtreme"]*10 + ["PI 0"]*10 + ["Rosbot3"]*10 +
              ["Up Xtreme_vc"]*10 + ["PI 0_vc"]*10 + ["Rosbot3_vc"]*10,
    "ram": [10240,10240,10240,10240,10368,10112,10240,10240,10368,10240,    
            8960,8960,8960,8960,8968,8960,8960,8960,8960,8968,              
            10112,10112,10240,10112,10112,10240,10112,10112,10240,10112,    
            17792,17792,17664,17664,17792,17920,17792,17792,17792,17792,    
            14272,14272,14272,14272,14272,14272,14272,14272,14272,14272,    
            16896,16768,16896,16768,16768,16896,16768,16896,16896,16896]    
}
df_ram = pd.DataFrame(ram_data)

# === Gruppi ===
groups = ["Up Xtreme", "PI 0", "Rosbot3"]
ram_normal = [df_ram[df_ram["device"] == d]["ram"] for d in groups]
ram_vc = [df_ram[df_ram["device"] == f"{d}_vc"]["ram"] for d in groups]

# === Posizioni: 3 gruppi con due box affiancati ===
positions_normal = [1, 3, 5]      # X.509
positions_vc = [p + 0.4 for p in positions_normal]  # VC leggermente spostato
width = 0.35

# === Colori ===
col_x509_face = "#5EA04A"  # blu
col_x509_edge = "#5EA04A"
col_vc_face   = "#4682A9"  # arancione
col_vc_edge   = "#4682A9"

fig, ax = plt.subplots(figsize=(8,5))

# Funzione per colorare
def color_boxplot(bp, face, edge):
    for patch in bp['boxes']:
        patch.set(facecolor=face, edgecolor=edge)
    for element in ['whiskers', 'caps', 'medians']:
        for line in bp[element]:
            line.set(color=edge, linewidth=1.5)
    for flier in bp['fliers']:
        flier.set(marker='o', color=edge, alpha=0.6)

# === Disegno dei due set di boxplot ===
bp1 = ax.boxplot(ram_normal, positions=positions_normal, widths=width, patch_artist=True)
bp2 = ax.boxplot(ram_vc, positions=positions_vc, widths=width, patch_artist=True)

color_boxplot(bp1, col_x509_face, col_x509_edge)
color_boxplot(bp2, col_vc_face, col_vc_edge)

# === Asse X con SOLO 3 etichette (centro dei due box) ===
centers = [p + 0.2 for p in positions_normal]
ax.set_xticks(centers)
ax.set_xticklabels(groups)

ax.grid(axis='y', linestyle='--', alpha=0.6)  # ✅ solo griglia orizzontale
ax.grid(False, axis='x') 

ax.set_ylabel("RAM (Kb)")
ax.legend([bp1["boxes"][0], bp2["boxes"][0]], ["X.509", "Our Solution"], frameon=True)

plt.tight_layout()
plt.savefig("ram_boxplot_3x_affiancato.pdf", dpi=300)
plt.savefig("ram_boxplot_3x_affiancato.pgf", dpi=300)
plt.show()

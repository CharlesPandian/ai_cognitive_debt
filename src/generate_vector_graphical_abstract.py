#!/usr/bin/env python3
"""
Publication-Grade Vector Graphical Abstract Generator
Elsevier Computers & Education Standards
Creates 100% pure vector PDF and 300 DPI PNG:
- Title Banner
- Column 1: Theoretical Cognitive Pathways & Working Memory Architecture
- Column 2: Empirical Crossover & Behavioral Dynamics (Dual Subplots)
- Column 3: Multi-Agent Audit & Architectural Safeguards (BOFR Bar + 4 Tiles)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

# Colorblind-safe Okabe-Ito & Elsevier academic palette
PALETTE = {
    "black": "#111111",
    "dark_text": "#555555",
    "dark_grey": "#555555",
    "grey": "#555555",
    "light_grey": "#CFD8DC",
    "border_grey": "#90A4AE",
    "panel_bg": "#F5F7FA",
    "card_bg": "#FFFFFF",
    
    # Pathway A (Green)
    "green": "#009E73",
    "green_bg": "#E8F5E9",
    "green_border": "#2E7D32",
    
    # Pathway B (Vermilion / Red)
    "vermilion": "#D55E00",
    "vermilion_bg": "#FBE9E7",
    "vermilion_border": "#C62828",
    
    # Accent colors
    "blue": "#0072B2",
    "blue_bg": "#E3F2FD",
    "blue_border": "#1565C0",
    "orange": "#E69F00",
    "orange_bg": "#FFF8E1",
    "orange_border": "#EF6C00",
    "purple": "#7B1FA2",
    "purple_bg": "#F3E5F5",
    "purple_border": "#6A1B9A",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11.0,
    "axes.edgecolor": "#546E7A",
    "axes.linewidth": 1.0,
    "xtick.color": "#555555",
    "ytick.color": "#555555",
    "xtick.labelsize": 10.0,
    "ytick.labelsize": 10.0,
    "figure.autolayout": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42
})

def draw_network_graph(ax, cx, cy, radius=3.2, is_active=True):
    """Draws a vector schema node network (brain conceptual integration)."""
    np.random.seed(42)
    angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
    r_nodes = [radius * 0.95, radius * 0.65, radius * 1.0, radius * 0.7, 
               radius * 0.9, radius * 0.6, radius * 0.95, radius * 0.65]
    xs = [cx + r * np.cos(a) for r, a in zip(r_nodes, angles)]
    ys = [cy + r * np.sin(a) for r, a in zip(r_nodes, angles)]
    xs.append(cx)
    ys.append(cy) # center node
    
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0),
        (8, 0), (8, 2), (8, 4), (8, 6), (1, 5), (3, 7)
    ]
    
    if is_active:
        for i, j in edges:
            ax.plot([xs[i], xs[j]], [ys[i], ys[j]], color=PALETTE["green"], 
                    lw=1.4, alpha=0.75, zorder=3)
        for i in range(len(xs)):
            c = PALETTE["green"] if i != 8 else PALETTE["blue"]
            circle = plt.Circle((xs[i], ys[i]), 0.48, fc=c, ec="#FFFFFF", lw=1.2, zorder=4)
            ax.add_patch(circle)
    else:
        for idx, (i, j) in enumerate(edges):
            if idx % 2 == 0:
                ax.plot([xs[i], xs[j]], [ys[i], ys[j]], color="#B0BEC5", 
                        lw=1.0, linestyle="--", alpha=0.6, zorder=3)
        for i in range(len(xs)):
            circle = plt.Circle((xs[i], ys[i]), 0.42, fc="#ECEFF1", ec="#90A4AE", 
                                lw=1.0, linestyle="--", zorder=4)
            ax.add_patch(circle)

def draw_tutor_icon(ax, cx, cy):
    """Draws a stylized Socratic tutor avatar."""
    # Head
    head = plt.Circle((cx, cy + 1.2), 1.1, fc="#FFFFFF", ec=PALETTE["green_border"], lw=1.5, zorder=4)
    ax.add_patch(head)
    # Laurel wreath
    laurel = patches.Arc((cx, cy + 1.7), 1.8, 1.0, theta1=20, theta2=160, 
                         color=PALETTE["green"], lw=1.6, zorder=5)
    ax.add_patch(laurel)
    # Shoulders
    toga = patches.Polygon([[cx - 2.2, cy - 1.5], [cx + 2.2, cy - 1.5], 
                           [cx + 1.5, cy + 0.1], [cx - 1.5, cy + 0.1]], 
                           closed=True, fc=PALETTE["green_bg"], ec=PALETTE["green_border"], lw=1.5, zorder=4)
    ax.add_patch(toga)

def draw_robot_icon(ax, cx, cy):
    """Draws a stylized AI chatbot tablet."""
    tablet = patches.FancyBboxPatch((cx - 1.9, cy - 1.8), 3.8, 3.6, boxstyle="round,pad=0.2",
                                   fc="#FFFFFF", ec=PALETTE["vermilion_border"], lw=1.5, zorder=4)
    ax.add_patch(tablet)
    screen = patches.Rectangle((cx - 1.5, cy - 1.0), 3.0, 2.4, fc=PALETTE["vermilion_bg"], ec="#CFD8DC", lw=0.8, zorder=5)
    ax.add_patch(screen)
    # Robot face
    eye1 = plt.Circle((cx - 0.7, cy + 0.4), 0.28, fc=PALETTE["vermilion"], zorder=6)
    eye2 = plt.Circle((cx + 0.7, cy + 0.4), 0.28, fc=PALETTE["vermilion"], zorder=6)
    ax.add_patch(eye1)
    ax.add_patch(eye2)
    smile = patches.Arc((cx, cy - 0.1), 1.1, 0.6, theta1=200, theta2=340, color=PALETTE["vermilion"], lw=1.6, zorder=6)
    ax.add_patch(smile)
    # Home button
    btn = plt.Circle((cx, cy - 1.4), 0.2, fc="#90A4AE", zorder=5)
    ax.add_patch(btn)

# Vector Safeguard Icons
def draw_lock_icon(ax, cx, cy, s=1.0):
    """Pure vector padlock icon."""
    shackle = patches.Arc((cx, cy + 0.65*s), 0.85*s, 1.0*s, theta1=0, theta2=180, 
                          color=PALETTE["blue_border"], lw=2.0*s, zorder=5)
    ax.add_patch(shackle)
    body = patches.FancyBboxPatch((cx - 0.65*s, cy - 0.6*s), 1.3*s, 1.0*s, boxstyle="round,pad=0.1",
                                  fc=PALETTE["blue"], ec=PALETTE["blue_border"], lw=1.2, zorder=5)
    ax.add_patch(body)
    hole = plt.Circle((cx, cy - 0.1*s), 0.18*s, fc="#FFFFFF", zorder=6)
    ax.add_patch(hole)

def draw_clock_icon(ax, cx, cy, s=1.0):
    """Pure vector stopwatch icon."""
    circle = plt.Circle((cx, cy), 0.75*s, fc="#FFFFFF", ec=PALETTE["orange_border"], lw=1.8*s, zorder=5)
    ax.add_patch(circle)
    # Button
    btn = patches.Rectangle((cx - 0.18*s, cy + 0.72*s), 0.36*s, 0.22*s, 
                            fc=PALETTE["orange_border"], ec=PALETTE["orange_border"], zorder=5)
    ax.add_patch(btn)
    # Hands
    ax.plot([cx, cx], [cy, cy + 0.42*s], color=PALETTE["orange_border"], lw=1.8*s, zorder=6)
    ax.plot([cx, cx + 0.32*s], [cy, cy], color=PALETTE["orange_border"], lw=1.8*s, zorder=6)

def draw_shield_icon(ax, cx, cy, s=1.0):
    """Pure vector shield icon."""
    pts = [
        [cx - 0.7*s, cy + 0.75*s],
        [cx + 0.7*s, cy + 0.75*s],
        [cx + 0.7*s, cy + 0.1*s],
        [cx, cy - 0.85*s],
        [cx - 0.7*s, cy + 0.1*s]
    ]
    shield = patches.Polygon(pts, closed=True, fc=PALETTE["purple"], 
                             ec=PALETTE["purple_border"], lw=1.4*s, zorder=5)
    ax.add_patch(shield)
    # Star / emblem
    star = plt.Circle((cx, cy + 0.1*s), 0.25*s, fc="#FFFFFF", zorder=6)
    ax.add_patch(star)

def draw_dashboard_icon(ax, cx, cy, s=1.0):
    """Pure vector dashboard monitor icon."""
    mon = patches.FancyBboxPatch((cx - 0.85*s, cy - 0.4*s), 1.7*s, 1.15*s, boxstyle="round,pad=0.08",
                                 fc="#FFFFFF", ec=PALETTE["green_border"], lw=1.6*s, zorder=5)
    ax.add_patch(mon)
    # Stand
    stand = patches.Rectangle((cx - 0.2*s, cy - 0.75*s), 0.4*s, 0.35*s, fc=PALETTE["green_border"], zorder=4)
    base = patches.Rectangle((cx - 0.5*s, cy - 0.82*s), 1.0*s, 0.12*s, fc=PALETTE["green_border"], zorder=4)
    ax.add_patch(stand)
    ax.add_patch(base)
    # Telemetry bars on screen
    ax.plot([cx - 0.5*s, cx - 0.5*s], [cy - 0.15*s, cy + 0.4*s], color=PALETTE["green"], lw=2.2*s, zorder=6)
    ax.plot([cx - 0.1*s, cx - 0.1*s], [cy - 0.15*s, cy + 0.15*s], color=PALETTE["orange"], lw=2.2*s, zorder=6)
    ax.plot([cx + 0.3*s, cx + 0.3*s], [cy - 0.15*s, cy + 0.55*s], color=PALETTE["blue"], lw=2.2*s, zorder=6)

def generate_vector_graphical_abstract():
    fig = plt.figure(figsize=(16.8, 8.2), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    
    # Base layout axes [0, 100] x [0, 100]
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    
    # -------------------------------------------------------------
    # Title Banner (Clean, bold, professional Elsevier style)
    # -------------------------------------------------------------
    ax.text(50, 96.5, "ALGORITHMIC OFFLOADING AND COGNITIVE DEBT IN PRIMARY MATHEMATICS",
            ha="center", va="center", fontsize=19.5, weight="bold", color=PALETTE["black"])
    ax.text(50, 93.3, "Empirical Telemetry & Multi-Agent Audits of Generative AI Tutoring in Elementary Education",
            ha="center", va="center", fontsize=13.0, style="italic", color=PALETTE["grey"])
    
    ax.plot([2.5, 97.5], [91.5, 91.5], color=PALETTE["light_grey"], lw=1.2)
    
    # -------------------------------------------------------------
    # 3 Outer Container Panels
    # -------------------------------------------------------------
    col_w = 30.6
    gap = 1.6
    c1_x = 2.5
    c2_x = c1_x + col_w + gap
    c3_x = c2_x + col_w + gap
    col_y = 2.5
    col_h = 86.5
    
    for cx_pos, title_lines in [
        (c1_x, ["THEORETICAL COGNITIVE PATHWAYS", "& WORKING MEMORY ARCHITECTURE"]),
        (c2_x, ["EMPIRICAL CROSSOVER &", "BEHAVIORAL DYNAMICS"]),
        (c3_x, ["MULTI-AGENT AUDIT &", "ARCHITECTURAL SAFEGUARDS"])
    ]:
        panel_box = patches.FancyBboxPatch((cx_pos, col_y), col_w, col_h, boxstyle="round,pad=0.8",
                                           fc=PALETTE["panel_bg"], ec=PALETTE["border_grey"], lw=1.2, zorder=1)
        ax.add_patch(panel_box)
        # Header banner inside panel
        h_box = patches.FancyBboxPatch((cx_pos + 1.0, col_y + col_h - 6.2), col_w - 2.0, 5.2, boxstyle="round,pad=0.4",
                                       fc="#FFFFFF", ec=PALETTE["border_grey"], lw=0.9, zorder=2)
        ax.add_patch(h_box)
        if len(title_lines) == 1:
            ax.text(cx_pos + col_w/2, col_y + col_h - 3.6, title_lines[0], ha="center", va="center",
                    fontsize=12.2, weight="bold", color="#0D47A1", zorder=3)
        else:
            ax.text(cx_pos + col_w/2, col_y + col_h - 2.5, title_lines[0], ha="center", va="center",
                    fontsize=11.4, weight="bold", color="#0D47A1", zorder=3)
            ax.text(cx_pos + col_w/2, col_y + col_h - 4.7, title_lines[1], ha="center", va="center",
                    fontsize=11.4, weight="bold", color="#0D47A1", zorder=3)

    # =============================================================
    # COLUMN 1: THEORETICAL PATHWAYS
    # =============================================================
    card_w = col_w - 2.4
    card_x = c1_x + 1.2
    card_h = 35.5
    
    # 1.1 Pathway A (Top)
    pA_y = 44.5
    box_A = patches.FancyBboxPatch((card_x, pA_y), card_w, card_h, boxstyle="round,pad=0.6",
                                  fc=PALETTE["green_bg"], ec=PALETTE["green_border"], lw=1.4, zorder=2)
    ax.add_patch(box_A)
    ax.text(card_x + card_w/2, pA_y + card_h - 2.8, "PATHWAY A: PEDAGOGICAL SCAFFOLDING\n& PRODUCTIVE STRUGGLE",
            ha="center", va="center", fontsize=11.4, weight="bold", color=PALETTE["green_border"], linespacing=1.1)
            
    # Dialogue bubble
    bubble_a = patches.FancyBboxPatch((card_x + 1.0, pA_y + 17.5), 12.2, 11.2, boxstyle="round,pad=0.5",
                                     fc="#FFFFFF", ec=PALETTE["green"], lw=1.1, zorder=3)
    ax.add_patch(bubble_a)
    ax.text(card_x + 7.1, pA_y + 25.0, "12 ÷ 3 = ?", ha="center", va="center", fontsize=12.0, weight="bold", color="#2E7D32")
    ax.text(card_x + 7.1, pA_y + 20.8, "How can we think\nabout sharing equally?", ha="center", va="center", 
            fontsize=9.5, style="italic", color=PALETTE["dark_text"])
    draw_tutor_icon(ax, card_x + 7.1, pA_y + 11.2)
    ax.text(card_x + 7.1, pA_y + 7.2, "Socratic Dialogue\n& Guided Struggle", ha="center", va="center", fontsize=9.8, weight="bold", color=PALETTE["dark_text"])

    # Arrow
    ax.annotate("", xy=(card_x + 17.8, pA_y + 17.8), xytext=(card_x + 14.2, pA_y + 17.8),
                arrowprops=dict(arrowstyle="->", color=PALETTE["green"], lw=2.4))

    # Schema Network
    draw_network_graph(ax, card_x + 22.2, pA_y + 17.8, radius=3.1, is_active=True)
    ax.text(card_x + 22.2, pA_y + 11.2, "ACTIVE SCHEMA\nCONSOLIDATION", ha="center", va="center", 
            fontsize=10.4, weight="bold", color=PALETTE["green_border"])
    ax.text(card_x + 22.2, pA_y + 7.2, "Germane Load Promoted\n(Durable Long-Term Memory)", ha="center", va="center", 
            fontsize=9.0, color=PALETTE["dark_text"])

    # Banner A
    b_banner_a = patches.Rectangle((card_x + 0.4, pA_y + 0.4), card_w - 0.8, 3.6, fc="#FFFFFF", ec=PALETTE["green"], lw=0.9, zorder=3)
    ax.add_patch(b_banner_a)
    ax.text(card_x + card_w/2, pA_y + 2.2, "Desirable Difficulties & Stable Schema Formation", 
            ha="center", va="center", fontsize=10.2, weight="bold", color=PALETTE["green"])

    # VS Divider
    vs_circle = plt.Circle((card_x + card_w/2, 41.5), 2.3, fc="#FFFFFF", ec=PALETTE["dark_text"], lw=1.3, zorder=5)
    ax.add_patch(vs_circle)
    ax.text(card_x + card_w/2, 41.5, "VS", ha="center", va="center", fontsize=11.2, weight="bold", color=PALETTE["dark_text"], zorder=6)

    # 1.2 Pathway B (Bottom)
    pB_y = 4.2
    box_B = patches.FancyBboxPatch((card_x, pB_y), card_w, card_h, boxstyle="round,pad=0.6",
                                  fc=PALETTE["vermilion_bg"], ec=PALETTE["vermilion_border"], lw=1.4, zorder=2)
    ax.add_patch(box_B)
    ax.text(card_x + card_w/2, pB_y + card_h - 2.8, "PATHWAY B: AUTOMATED AI OFFLOADING\n& COGNITIVE DEBT",
            ha="center", va="center", fontsize=11.4, weight="bold", color=PALETTE["vermilion_border"], linespacing=1.1)

    bubble_b = patches.FancyBboxPatch((card_x + 1.0, pB_y + 17.5), 12.2, 11.2, boxstyle="round,pad=0.5",
                                     fc="#FFFFFF", ec=PALETTE["vermilion"], lw=1.1, zorder=3)
    ax.add_patch(bubble_b)
    ax.text(card_x + 7.1, pB_y + 25.0, "12 ÷ 3 = 4!", ha="center", va="center", fontsize=12.0, weight="bold", color="#C62828")
    ax.text(card_x + 7.1, pB_y + 21.0, "The answer is 4.\nHere is full solution!", ha="center", va="center", 
            fontsize=9.5, style="italic", color=PALETTE["dark_text"])
    draw_robot_icon(ax, card_x + 7.1, pB_y + 11.2)
    ax.text(card_x + 7.1, pB_y + 7.2, "Unconstrained Chatbot\n(Instant Bottom-Out)", ha="center", va="center", fontsize=9.8, weight="bold", color=PALETTE["dark_text"])

    # Arrow
    ax.annotate("", xy=(card_x + 17.8, pB_y + 17.8), xytext=(card_x + 14.2, pB_y + 17.8),
                arrowprops=dict(arrowstyle="->", color=PALETTE["vermilion"], lw=2.4))

    # Faded Schema Network
    draw_network_graph(ax, card_x + 22.2, pB_y + 17.8, radius=3.1, is_active=False)
    ax.text(card_x + 22.2, pB_y + 11.2, "COGNITIVE DEBT\nACCRUAL", ha="center", va="center", 
            fontsize=10.4, weight="bold", color=PALETTE["vermilion_border"])
    ax.text(card_x + 22.2, pB_y + 7.2, "Germane Load Bypassed\n(Zero Long-Term Integration)", ha="center", va="center", 
            fontsize=9.0, color=PALETTE["dark_text"])

    # Banner B
    b_banner_b = patches.Rectangle((card_x + 0.4, pB_y + 0.4), card_w - 0.8, 3.6, fc="#FFFFFF", ec=PALETTE["vermilion"], lw=0.9, zorder=3)
    ax.add_patch(b_banner_b)
    ax.text(card_x + card_w/2, pB_y + 2.2, "Algorithmic Sycophancy & Superficial Performance", 
            ha="center", va="center", fontsize=10.2, weight="bold", color=PALETTE["vermilion"])

    # =============================================================
    # COLUMN 2: EMPIRICAL CROSSOVER & BEHAVIORAL DYNAMICS
    # =============================================================
    sub_left = (c2_x + 3.2) / 100.0
    sub_w = (col_w - 5.0) / 100.0
    
    # 2.1 Crossover Plot (Top Subplot)
    ax_cross = fig.add_axes([sub_left, 0.485, sub_w, 0.285])
    
    phases = [0, 1]
    phase_labels = ["Assisted Practice\n(In-Session)", "Unassisted Transfer\n(Delayed Post-Test)"]
    high_y = [94.1, 34.2]
    scaff_y = [76.1, 63.0]
    
    ax_cross.plot(phases, high_y, color=PALETTE["vermilion"], marker="^", markersize=7.5, 
                  linewidth=2.6, linestyle="--", label="High AI-Offload (Consumer)", zorder=4)
    ax_cross.plot(phases, scaff_y, color=PALETTE["green"], marker="o", markersize=7.5, 
                  linewidth=2.6, linestyle="-", label="Scaffolded (Low Offload)", zorder=4)
                  
    ax_cross.fill_between(phases, high_y, scaff_y, where=np.array(high_y) >= np.array(scaff_y),
                          interpolate=True, color=PALETTE["vermilion"], alpha=0.12)
    ax_cross.fill_between(phases, high_y, scaff_y, where=np.array(high_y) < np.array(scaff_y),
                          interpolate=True, color=PALETTE["green"], alpha=0.12)
                          
    ax_cross.set_xticks(phases)
    ax_cross.set_xticklabels(phase_labels, fontsize=10.0, weight="bold")
    ax_cross.set_ylabel("Accuracy (%)", fontsize=10.8, weight="bold")
    ax_cross.tick_params(axis="y", labelsize=10.0)
    ax_cross.set_ylim(20, 114)
    ax_cross.set_xlim(-0.25, 1.25)
    ax_cross.grid(True, linestyle=":", alpha=0.6)
    ax_cross.set_title("The Performance–Learning Paradox\n(In-Session vs. Delayed Unassisted Accuracy)", 
                       fontsize=11.2, weight="bold", pad=5)
    ax_cross.legend(loc="lower left", fontsize=9.2, frameon=True, facecolor="#FAFAFA", edgecolor="#E0E0E0")
    
    ax_cross.annotate("Illusion of Competence\n(94.1% In-Session)", xy=(0, 94.1), xytext=(0.02, 98),
                      fontsize=10.0, color=PALETTE["vermilion"], weight="bold")
    ax_cross.annotate("Skill Collapse\n(34.2% Delayed)", xy=(1, 34.2), xytext=(0.55, 41),
                      fontsize=10.0, color=PALETTE["vermilion"], weight="bold",
                      arrowprops=dict(arrowstyle="->", color=PALETTE["vermilion"], lw=1.4))
    ax_cross.annotate("High Retention\n(83.4% Ratio)", xy=(1, 63.0), xytext=(0.58, 69),
                      fontsize=10.0, color=PALETTE["green"], weight="bold")

    # 2.2 Response Latency Collapse (Bottom Subplot)
    ax_lat = fig.add_axes([sub_left, 0.082, sub_w, 0.285])
    
    trials = [1, 2, 3, 4, 5]
    lat_scaff = [10.2, 11.0, 11.4, 11.5, 11.8]
    lat_offload = [9.8, 5.2, 3.8, 3.0, 2.7]
    
    ax_lat.plot(trials, lat_scaff, color=PALETTE["green"], marker="s", markersize=6.5, 
                linewidth=2.2, label="Scaffolded (Deliberate)", zorder=4)
    ax_lat.plot(trials, lat_offload, color=PALETTE["vermilion"], marker="v", markersize=6.5, 
                linewidth=2.2, linestyle="--", label="High AI-Offload (Impulsive)", zorder=4)
                
    ax_lat.axhspan(0, 3.0, color="#FFEBEE", alpha=0.5, label="Impulsive Guessing (<3s)")
    ax_lat.set_xticks(trials)
    ax_lat.set_xticklabels([f"Trial {t}" for t in trials], fontsize=10.0)
    ax_lat.tick_params(axis="y", labelsize=10.0)
    ax_lat.set_xlabel("Consecutive Unassisted Transfer Trials", fontsize=10.4, weight="bold")
    ax_lat.set_ylabel("Response Latency (s)", fontsize=10.8, weight="bold")
    ax_lat.set_ylim(0, 14.5)
    ax_lat.grid(True, linestyle=":", alpha=0.6)
    ax_lat.set_title("Response Latency Collapse\n(Erosion of Productive Struggle & Metacognition)", 
                     fontsize=11.2, weight="bold", pad=5)
    ax_lat.legend(loc="upper right", fontsize=9.0, frameon=True, facecolor="#FAFAFA", edgecolor="#E0E0E0")
    
    ax_lat.annotate("Impulsivity Acceleration\n(β = -0.173, p < 0.001)", xy=(4, 3.0), xytext=(1.6, 1.2),
                    fontsize=10.0, color=PALETTE["vermilion"], weight="bold",
                    arrowprops=dict(arrowstyle="->", color=PALETTE["vermilion"], lw=1.4))

    # =============================================================
    # COLUMN 3: MULTI-AGENT AUDIT & ARCHITECTURAL SAFEGUARDS
    # =============================================================
    sub_c3_left = (c3_x + 3.2) / 100.0
    
    # 3.1 BOFR Bar Plot (Top Subplot)
    ax_bofr = fig.add_axes([sub_c3_left, 0.485, sub_w, 0.285])
    
    models = ["Consumer\nDefault", "Naive\nHelpful", "Guardrailed\nSocratic"]
    bofr_rates = [100.0, 100.0, 49.3]
    bar_colors = [PALETTE["vermilion"], PALETTE["orange"], PALETTE["green"]]
    
    bars = ax_bofr.bar([0, 1, 2], bofr_rates, width=0.55, color=bar_colors, 
                       edgecolor="#333333", linewidth=1.0, zorder=3)
                       
    ax_bofr.set_xticks([0, 1, 2])
    ax_bofr.set_xticklabels(models, fontsize=10.2, weight="bold")
    ax_bofr.tick_params(axis="y", labelsize=10.0)
    ax_bofr.set_ylabel("Bottom-Out Failure (%)", fontsize=10.8, weight="bold")
    ax_bofr.set_ylim(0, 134)
    ax_bofr.grid(True, linestyle=":", alpha=0.6, axis="y")
    ax_bofr.set_title("Multi-Agent Pedagogical Audit\n(Bottom-Out Failure Rate on gemini-3.8-flash)", 
                      fontsize=11.2, weight="bold", pad=5)
                      
    ax_bofr.text(0, 103, "100.0%\n(Turn 1)", ha="center", va="bottom", fontsize=10.2, weight="bold", color=PALETTE["vermilion"])
    ax_bofr.text(1, 103, "100.0%\n(Turn 2)", ha="center", va="bottom", fontsize=10.2, weight="bold", color=PALETTE["orange"])
    ax_bofr.text(2, 52.5, "49.3%\n(Turn 4)", ha="center", va="bottom", fontsize=10.2, weight="bold", color=PALETTE["green"])
    
    ax_bofr.annotate("Conversational Wear-Down\nunder child pressure", xy=(2.0, 68), xytext=(2.0, 98),
                     ha="center", fontsize=9.2, color=PALETTE["dark_text"], style="italic",
                     arrowprops=dict(arrowstyle="->", color=PALETTE["dark_text"], lw=1.4))

    # 3.2 Four Modular Architectural Safeguards (Bottom Grid)
    grid_w = col_w - 2.4
    grid_x = c3_x + 1.2
    grid_y = 4.2
    grid_h = 35.5
    
    sg_box = patches.FancyBboxPatch((grid_x, grid_y), grid_w, grid_h, boxstyle="round,pad=0.6",
                                   fc="#FFFFFF", ec=PALETTE["blue_border"], lw=1.4, zorder=2)
    ax.add_patch(sg_box)
    ax.text(grid_x + grid_w/2, grid_y + grid_h - 2.8, "FOUR MODULAR ARCHITECTURAL SAFEGUARDS",
            ha="center", va="center", fontsize=11.4, weight="bold", color="#0D47A1")

    # 4 Sub-Tiles (2x2 grid)
    tile_w = (grid_w - 1.8) / 2.0
    tile_h = 13.6
    t1_x = grid_x + 0.6
    t2_x = t1_x + tile_w + 0.6
    t_top_y = grid_y + 16.2
    t_bot_y = grid_y + 1.2
    
    # Tile 1: Hard Answer-Gating
    b1 = patches.FancyBboxPatch((t1_x, t_top_y), tile_w, tile_h, boxstyle="round,pad=0.4",
                               fc=PALETTE["blue_bg"], ec=PALETTE["blue_border"], lw=1.1, zorder=3)
    ax.add_patch(b1)
    draw_lock_icon(ax, t1_x + tile_w/2, t_top_y + tile_h - 4.4, s=1.15)
    ax.text(t1_x + tile_w/2, t_top_y + tile_h - 1.8, "1. Hard Answer-Gating", ha="center", va="center",
            fontsize=10.4, weight="bold", color=PALETTE["blue_border"], zorder=4)
    ax.text(t1_x + tile_w/2, t_top_y + 3.8, "Logit & CAS Decoupling;\ncryptographically blocks\ntarget solution tokens.",
            ha="center", va="center", fontsize=9.0, color=PALETTE["dark_text"], linespacing=1.18, zorder=4)

    # Tile 2: Latency Windows
    b2 = patches.FancyBboxPatch((t2_x, t_top_y), tile_w, tile_h, boxstyle="round,pad=0.4",
                               fc=PALETTE["orange_bg"], ec=PALETTE["orange_border"], lw=1.1, zorder=3)
    ax.add_patch(b2)
    draw_clock_icon(ax, t2_x + tile_w/2, t_top_y + tile_h - 4.4, s=1.15)
    ax.text(t2_x + tile_w/2, t_top_y + tile_h - 1.8, "2. Latency Windows", ha="center", va="center",
            fontsize=10.4, weight="bold", color=PALETTE["orange_border"], zorder=4)
    ax.text(t2_x + tile_w/2, t_top_y + 3.8, "15–30s Enforced Pause;\nmitigates impulsivity &\npreserves reflection time.",
            ha="center", va="center", fontsize=9.0, color=PALETTE["dark_text"], linespacing=1.18, zorder=4)

    # Tile 3: Pedagogical Alignment (RLPF)
    b3 = patches.FancyBboxPatch((t1_x, t_bot_y), tile_w, tile_h, boxstyle="round,pad=0.4",
                               fc=PALETTE["purple_bg"], ec=PALETTE["purple_border"], lw=1.1, zorder=3)
    ax.add_patch(b3)
    draw_shield_icon(ax, t1_x + tile_w/2, t_bot_y + tile_h - 4.4, s=1.15)
    ax.text(t1_x + tile_w/2, t_bot_y + tile_h - 1.8, "3. Pedagogical RLPF", ha="center", va="center",
            fontsize=10.4, weight="bold", color=PALETTE["purple_border"], zorder=4)
    ax.text(t1_x + tile_w/2, t_bot_y + 3.8, "Align reward models\nto productive struggle;\npenalize sycophancy.",
            ha="center", va="center", fontsize=9.0, color=PALETTE["dark_text"], linespacing=1.18, zorder=4)

    # Tile 4: Teacher Dashboards
    b4 = patches.FancyBboxPatch((t2_x, t_bot_y), tile_w, tile_h, boxstyle="round,pad=0.4",
                               fc=PALETTE["green_bg"], ec=PALETTE["green_border"], lw=1.1, zorder=3)
    ax.add_patch(b4)
    draw_dashboard_icon(ax, t2_x + tile_w/2, t_bot_y + tile_h - 4.4, s=1.15)
    ax.text(t2_x + tile_w/2, t_bot_y + tile_h - 1.8, "4. Teacher Dashboards", ha="center", va="center",
            fontsize=10.4, weight="bold", color=PALETTE["green_border"], zorder=4)
    ax.text(t2_x + tile_w/2, t_bot_y + 3.8, "Real-time classroom\ntelemetry alerts when\noffloading spikes.",
            ha="center", va="center", fontsize=9.0, color=PALETTE["dark_text"], linespacing=1.18, zorder=4)

    # -------------------------------------------------------------
    # Save 100% Vector PDF and High-Resolution 300 DPI PNG
    # -------------------------------------------------------------
    out_dir = Path("/home/jason/EdTechPaper1/project_ai_cognitive_debt/figures")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_out = out_dir / "graphical_abstract.pdf"
    png_out = out_dir / "graphical_abstract.png"
    
    plt.savefig(pdf_out, format="pdf", bbox_inches="tight", dpi=300)
    plt.savefig(png_out, format="png", bbox_inches="tight", dpi=300)
    
    plt.close()
    print(f"Vector Graphical Abstract successfully saved to:\n- {pdf_out}\n- {png_out}")

if __name__ == "__main__":
    generate_vector_graphical_abstract()

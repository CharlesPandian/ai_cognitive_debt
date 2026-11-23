#!/usr/bin/env python3
"""
Publication Figure Generator: Computers & Education (Elsevier) Standards
Generates publication-grade figures (300 DPI PNG + vector PDF) with Okabe-Ito colorblind-safe palettes:
- graphical_abstract: Dedicated 3-column vector visual for Elsevier submission
1. fig1_dual_developmental_pathways: Dual developmental pathways (Productive Struggle vs AI Cognitive Offloading)
2. fig2_theoretical_framework: Multi-layer conceptual architecture (CLT, Desirable Difficulties, Sycophancy)
3. fig3_dual_study_pipeline: Methodological flow (Study 1 Telemetry -> Study 2 In-Silico Audit)
4. fig4_performance_learning_paradox: Crossover interaction & latency acceleration (Study 1)
5. fig5_bkt_retention_curves: Longitudinal mastery & post-removal cognitive decay (Study 1)
6. fig6_llm_audit_heatmap_survival: Multi-agent BOFR & Kaplan-Meier survival curves (Study 2)
7. fig7_domain_misconceptions_and_remediation: Mathematical domain vulnerability & misconception remediation (Study 2)
8. fig8_cognitive_debt_entropy_dynamics: Discrete hazard rates, cumulative cognitive debt, and entropy dynamics (Study 2)
"""

import json
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path as MPath
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PROCESSED = PROJECT_DIR / "data" / "processed"
FIGURES_DIR = PROJECT_DIR / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# Global Aesthetic Styling (Elsevier / Computers & Education)
# -------------------------------------------------------------
plt.rcParams.update({
    "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
    "font.family": "sans-serif",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10.5,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
    "legend.fontsize": 9,
    "figure.titlesize": 12,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.8,
    "grid.color": "#E5E5E5",
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
    "figure.autolayout": False
})

# Okabe-Ito Colorblind-Safe Palette
PALETTE = {
    "orange": "#E69F00",
    "sky_blue": "#56B4E9",
    "green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermilion": "#D55E00",
    "purple": "#CC79A7",
    "black": "#222222",
    "grey": "#7F7F7F",
    "light_bg_green": "#E8F5E9",
    "light_bg_red": "#FFEBEE",
    "card_border": "#CCCCCC"
}

def save_fig(fig, base_name):
    """Saves figure in both 300 DPI PNG and vector PDF."""
    if isinstance(base_name, str):
        base_names = [base_name]
    else:
        base_names = list(base_name)
    for b_name in base_names:
        pdf_path = FIGURES_DIR / f"{b_name}.pdf"
        png_path = FIGURES_DIR / f"{b_name}.png"
        fig.savefig(pdf_path, format="pdf", bbox_inches="tight", dpi=300)
        fig.savefig(png_path, format="png", bbox_inches="tight", dpi=300)
        print(f"Saved: {pdf_path.name} and {png_path.name}")
    plt.close(fig)

# -------------------------------------------------------------
# Graphical Abstract (Dedicated Vector Visual for Elsevier Submission)
# -------------------------------------------------------------
def ensure_graphical_abstract_file():
    """Generates 100% vector graphical_abstract.pdf and .png."""
    from generate_vector_graphical_abstract import generate_vector_graphical_abstract
    generate_vector_graphical_abstract()

# -------------------------------------------------------------
# Figure 1: Dual Developmental Pathways
# -------------------------------------------------------------
def generate_fig1_dual_developmental_pathways():
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    
    # Panel Left: Productive Struggle (Desirable Difficulties)
    rect_left = patches.FancyBboxPatch((3, 3), 45, 93, boxstyle="round,pad=1.2",
                                       fc=PALETTE["light_bg_green"], ec=PALETTE["green"], lw=2.2)
    ax.add_patch(rect_left)
    ax.text(25.5, 90.5, "PATHWAY A: PEDAGOGICAL SCAFFOLDING\n(Productive Struggle & Schema Construction)",
            ha="center", va="center", fontsize=11, weight="bold", color=PALETTE["green"])
    
    left_boxes = [
        ("1. Cognitive Challenge & Socio-Cognitive Conflict",
         "Learner encounters authentic non-routine math problem;\nworking memory load is actively managed.", 77),
        ("2. Socratic Fading & Metacognitive Prompting",
         "Tutor provides minimal directive cues;\nstudent executes calculations and schema mapping.", 56),
        ("3. Durable Schema Formation & Long-Term Memory",
         "Working memory consolidation creates robust retrieval routes;\nunassisted transfer accuracy exceeds 75–82%.", 35),
        ("Outcome: High Delayed Retention & Self-Regulation",
         "Retention Ratio: 83.4% | Sustained Response Latencies (6–8s)", 14)
    ]
    for title, desc, y_pos in left_boxes:
        box = patches.FancyBboxPatch((5.5, y_pos - 6.5), 40, 13.5, boxstyle="round,pad=0.8",
                                     fc="#FFFFFF", ec=PALETTE["green"], lw=1.3)
        ax.add_patch(box)
        ax.text(7.5, y_pos + 3.2, title, fontsize=9.4, weight="bold", color=PALETTE["black"])
        ax.text(7.5, y_pos - 3.0, desc, fontsize=8.2, color="#222222", linespacing=1.2)
        
    # Arrows Left
    for y_a in [68, 47, 26]:
        ax.annotate("", xy=(25.5, y_a - 4), xytext=(25.5, y_a),
                    arrowprops=dict(arrowstyle="->", color=PALETTE["green"], lw=2.2))

    # Panel Right: Automated Answer Offloading (Cognitive Debt)
    rect_right = patches.FancyBboxPatch((52, 3), 45, 93, boxstyle="round,pad=1.2",
                                        fc=PALETTE["light_bg_red"], ec=PALETTE["vermilion"], lw=2.2)
    ax.add_patch(rect_right)
    ax.text(74.5, 90.5, "PATHWAY B: AUTOMATED AI OFFLOADING\n(Illusion of Competence & Cognitive Debt)",
            ha="center", va="center", fontsize=11, weight="bold", color=PALETTE["vermilion"])
    
    right_boxes = [
        ("1. Prompt Impulsivity & Help-Seeking Abuse",
         "Learner seeks immediate answer within < 3 seconds;\navoids mental representation and executive struggle.", 77),
        ("2. Algorithmic Sycophancy & Answer Leakage",
         "Unconstrained or naive AI tutors provide direct answers;\nreplaces child's cognitive operations.", 56),
        ("3. Illusion of Competence (In-Session Spike)",
         "In-session accuracy artificially reaches 90–95%;\nzero mental schema constructed in long-term memory.", 35),
        ("Outcome: Delayed Skill Collapse & High Forgetting",
         "Post-removal accuracy drops to 34–45% | Retention Ratio: 13.7%", 14)
    ]
    for title, desc, y_pos in right_boxes:
        box = patches.FancyBboxPatch((54.5, y_pos - 6.5), 40, 13.5, boxstyle="round,pad=0.8",
                                     fc="#FFFFFF", ec=PALETTE["vermilion"], lw=1.3)
        ax.add_patch(box)
        ax.text(56.5, y_pos + 3.2, title, fontsize=9.4, weight="bold", color=PALETTE["black"])
        ax.text(56.5, y_pos - 3.0, desc, fontsize=8.2, color="#222222", linespacing=1.2)
        
    # Arrows Right
    for y_b in [68, 47, 26]:
        ax.annotate("", xy=(74.5, y_b - 4), xytext=(74.5, y_b),
                    arrowprops=dict(arrowstyle="->", color=PALETTE["vermilion"], lw=2.2))

    # Center Contrast Divider
    ax.text(50, 48.5, "VS", ha="center", va="center", fontsize=15, weight="bold",
            bbox=dict(boxstyle="circle,pad=0.45", fc="#FFFFFF", ec=PALETTE["grey"], lw=1.8))
            
    save_fig(fig, ["fig1_dual_developmental_pathways", "fig1_dual_developmental_pathway", "fig1_graphical_abstract"])

# Backward compatibility alias
generate_fig1_graphical_abstract = generate_fig1_dual_developmental_pathways

# -------------------------------------------------------------
# Figure 2: Theoretical Framework Diagram
# -------------------------------------------------------------
def generate_fig2_theoretical_framework():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Column Headers at Top
    col_headers = [
        ("COGNITIVE LOAD & MEMORY", 34.5),
        ("EXECUTIVE FUNCTION & SCAFFOLDING", 60.5),
        ("STRUGGLE & COGNITIVE DEBT", 86.5)
    ]
    for ch_text, ch_x in col_headers:
        ch_box = patches.FancyBboxPatch((ch_x - 11.8, 94.2), 23.6, 4.4, boxstyle="round,pad=0.3",
                                        fc="#F0F4F8", ec="#90A4AE", lw=1.1, zorder=2)
        ax.add_patch(ch_box)
        ax.text(ch_x, 96.4, ch_text, ha="center", va="center", fontsize=7.6, weight="bold", color="#1A237E")

    layers_data = [
        {
            "num": "LAYER 1",
            "title": "DEVELOPMENTAL\nCOGNITIVE\nARCHITECTURE",
            "subtitle": "(Ages 9–11 / Grades 4–5)",
            "color": "#0D47A1",
            "bg_color": "#E8EAF6",
            "y_top": 92.2, "y_bot": 66.2,
            "cards": [
                ("Working Memory Constraints", "Limited capacity (Sweller, 1988);\neasily overwhelmed or bypassed.", PALETTE["blue"]),
                ("Emergent Executive Function", "Impulse control & perseverance in\npre-frontal cortex development.", PALETTE["purple"]),
                ("Socio-Cognitive Conflict", "Piagetian equilibration triggered by\nproductive struggle (Piaget, 1977).", PALETTE["green"])
            ]
        },
        {
            "num": "LAYER 2",
            "title": "PEDAGOGICAL\nINTERACTION\nDYNAMICS",
            "subtitle": "(The Assistance Dilemma)",
            "color": "#E65100",
            "bg_color": "#FFF3E0",
            "y_top": 60.2, "y_bot": 34.2,
            "cards": [
                ("Desirable Difficulties", "Spacing & generation effects enhance\ndurable knowledge storage\n(Bjork & Bjork, 2011).", PALETTE["orange"]),
                ("Zone of Proximal Development", "Contingent scaffolding & fading\n(Vygotsky, 1978; Wood et al., 1976).", PALETTE["blue"]),
                ("Cognitive Offloading", "Substitutive offloading trades\neffort for long-term schema loss\n(Risko & Gilbert, 2016).", PALETTE["vermilion"])
            ]
        },
        {
            "num": "LAYER 3",
            "title": "GENERATIVE AI\nINTERFACE\nDYNAMICS",
            "subtitle": "(The Sycophancy Trap)",
            "color": "#B71C1C",
            "bg_color": "#FFEBEE",
            "y_top": 28.2, "y_bot": 2.2,
            "cards": [
                ("RLHF Algorithmic Sycophancy", "LLMs align to user compliance;\nprematurely leak answers under begging.", PALETTE["vermilion"]),
                ("Performance–Learning Paradox", "Flawless assisted execution masks\nzero latent schema integration.", PALETTE["orange"]),
                ("Accumulation of Cognitive Debt", "Impulsivity compounds, eroding\nunassisted problem-solving self-efficacy.", PALETTE["black"])
            ]
        }
    ]

    # Draw Layers
    for l_idx, l in enumerate(layers_data):
        y_h = l["y_top"] - l["y_bot"]
        
        # Layer Background band spanning full width
        l_band = patches.FancyBboxPatch((2.0, l["y_bot"]), 96.0, y_h, boxstyle="round,pad=0.8",
                                       fc="#FAFAFA", ec="#CFD8DC", lw=1.2, zorder=1)
        ax.add_patch(l_band)
        
        # Left Header Pillar Card
        p_box = patches.FancyBboxPatch((3.2, l["y_bot"] + 0.8), 17.5, y_h - 1.6, boxstyle="round,pad=0.5",
                                       fc=l["bg_color"], ec=l["color"], lw=1.6, zorder=2)
        ax.add_patch(p_box)
        ax.text(11.95, l["y_bot"] + y_h - 3.2, l["num"], ha="center", va="center", fontsize=9.2, weight="bold", color=l["color"], zorder=3)
        ax.text(11.95, l["y_bot"] + y_h/2 + 0.2, l["title"], ha="center", va="center", fontsize=8.6, weight="bold", color="#212121", linespacing=1.15, zorder=3)
        ax.text(11.95, l["y_bot"] + 3.0, l["subtitle"], ha="center", va="center", fontsize=7.2, style="italic", color="#555555", zorder=3)
        
        # 3 Content Cards
        x_centers = [34.5, 60.5, 86.5]
        card_w = 23.6
        for c_idx, (c_title, c_desc, c_col) in enumerate(l["cards"]):
            cx = x_centers[c_idx]
            c_box = patches.FancyBboxPatch((cx - card_w/2, l["y_bot"] + 1.2), card_w, y_h - 2.4, boxstyle="round,pad=0.5",
                                           fc="#FFFFFF", ec=c_col, lw=1.5, zorder=2)
            ax.add_patch(c_box)
            ax.text(cx, l["y_bot"] + y_h - 3.8, c_title, ha="center", va="center", fontsize=8.6, weight="bold", color=c_col, zorder=3)
            ax.plot([cx - card_w/2 + 1.5, cx + card_w/2 - 1.5], [l["y_bot"] + y_h - 6.5, l["y_bot"] + y_h - 6.5],
                    color=c_col, lw=0.6, alpha=0.4, zorder=3)
            ax.text(cx, l["y_bot"] + (y_h - 6.5)/2, c_desc, ha="center", va="center", fontsize=7.4, color="#263238", linespacing=1.22, zorder=3)

    # Downward Connecting Arrows between layers
    # Layer 1 -> Layer 2
    y1_bottom = layers_data[0]["y_bot"] + 1.2  # 67.4
    y2_top = layers_data[1]["y_top"] - 1.2     # 59.0

    labels_1_2 = ["Demands", "Cultivated via", "Provokes"]
    labels_2_3 = ["Subverted by", "Masked by", "Compounds into"]

    for c_idx, cx in enumerate([34.5, 60.5, 86.5]):
        # Arrow 1->2
        ax.annotate("", xy=(cx, y2_top + 0.3), xytext=(cx, y1_bottom - 0.3),
                    arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=2.0, mutation_scale=14), zorder=4)
        # Connector label badge
        ax.text(cx, (y1_bottom + y2_top)/2, labels_1_2[c_idx], ha="center", va="center",
                fontsize=7.2, weight="bold", color="#1A237E",
                bbox=dict(boxstyle="round,pad=0.25", fc="#FFFFFF", ec="#90A4AE", lw=0.8), zorder=5)

    # Layer 2 -> Layer 3
    y2_bottom = layers_data[1]["y_bot"] + 1.2  # 35.4
    y3_top = layers_data[2]["y_top"] - 1.2     # 27.0

    for c_idx, cx in enumerate([34.5, 60.5, 86.5]):
        # Arrow 2->3
        ax.annotate("", xy=(cx, y3_top + 0.3), xytext=(cx, y2_bottom - 0.3),
                    arrowprops=dict(arrowstyle="-|>", color="#C62828", lw=2.0, mutation_scale=14), zorder=4)
        # Connector label badge
        ax.text(cx, (y2_bottom + y3_top)/2, labels_2_3[c_idx], ha="center", va="center",
                fontsize=7.2, weight="bold", color="#C62828",
                bbox=dict(boxstyle="round,pad=0.25", fc="#FFFFFF", ec="#EF9A9A", lw=0.8), zorder=5)

    save_fig(fig, "fig2_theoretical_framework")

# -------------------------------------------------------------
# Figure 3: Dual-Study Methodological Pipeline Diagram
# -------------------------------------------------------------
def generate_fig3_dual_study_pipeline():
    fig, ax = plt.subplots(figsize=(11.5, 6.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    
    # Study 1 Container
    s1_box = patches.FancyBboxPatch((3, 3), 40.5, 93, boxstyle="round,pad=1.2",
                                    fc="#F3F6FB", ec=PALETTE["blue"], lw=2.2)
    ax.add_patch(s1_box)
    ax.text(23.25, 90.5, "STUDY 1: CAUSAL & LONGITUDINAL\nTELEMETRY ANALYSIS",
            ha="center", va="center", fontsize=10.5, weight="bold", color=PALETTE["blue"])
    
    s1_steps = [
        ("ASSISTments Ecosystem Datasets", "88 RCTs & 2012-2013 Clickstream\nN = 4,200 learners, 24 Math KCs", 78),
        ("Cognitive Offloading Index (COI)", "Classified into Low (<0.15), Moderate\n(0.15-0.45), & High (>=0.45) Cohorts", 58),
        ("Causal & Longitudinal Modeling", "Crossover ANOVA (F=4,613.27, p<0.001)\nMixedLM Latency Acceleration Slope", 32),
        ("Cognitive Debt BKT Modeling", "Post-scaffold removal retention decay\nDelta BIC = -24,740.7 vs Standard BKT", 12)
    ]
    for st, sd, yp in s1_steps:
        sb = patches.FancyBboxPatch((4.5, yp - 6.5), 37.5, 13.0, boxstyle="round,pad=0.6",
                                    fc="#FFFFFF", ec=PALETTE["blue"], lw=1.3)
        ax.add_patch(sb)
        ax.text(6.0, yp + 3.0, st, fontsize=8.8, weight="bold", color=PALETTE["black"])
        ax.text(6.0, yp - 3.0, sd, fontsize=7.6, color="#333333", linespacing=1.2)
        
    for ya in [68, 22]:
        ax.annotate("", xy=(23.25, ya - 3.5), xytext=(23.25, ya + 0.5),
                    arrowprops=dict(arrowstyle="->", color=PALETTE["blue"], lw=1.8))
    # Arrow between Step 2 and Step 3
    ax.annotate("", xy=(23.25, 41.5), xytext=(23.25, 48.5),
                    arrowprops=dict(arrowstyle="->", color=PALETTE["blue"], lw=1.8))

    # Study 2 Container
    s2_box = patches.FancyBboxPatch((56.5, 3), 40.5, 93, boxstyle="round,pad=1.2",
                                    fc="#FFF8F3", ec=PALETTE["orange"], lw=2.2)
    ax.add_patch(s2_box)
    ax.text(76.75, 90.5, "STUDY 2: IN-SILICO MULTI-AGENT\nPEDAGOGICAL AUDIT",
            ha="center", va="center", fontsize=10.5, weight="bold", color=PALETTE["orange"])
    
    s2_steps = [
        ("100 Stratified Benchmark Items", "Grade 4-5 Math (25 Arith, 25 Frac,\n25 Ratio, 25 Geom) with Distractors", 78),
        ("3 x 3 Factorial Audit Architecture", "3 Tutor Configs x 3 Student Personas\n900 Trajectories (3,600 Turns)", 58),
        ("gemini-3.8-flash API / Simulation", "ThinkingConfig(MEDIUM), 6.5s pacing\nRobust JSONL Checkpointing", 32),
        ("0-3 Rubric Scoring & Statistics", "BOFR %, Kaplan-Meier Survival, TTO\nDual-Rater Kappa = 0.886", 12)
    ]
    for st, sd, yp in s2_steps:
        sb = patches.FancyBboxPatch((58.0, yp - 6.5), 37.5, 13.0, boxstyle="round,pad=0.6",
                                    fc="#FFFFFF", ec=PALETTE["orange"], lw=1.3)
        ax.add_patch(sb)
        ax.text(59.5, yp + 3.0, st, fontsize=8.8, weight="bold", color=PALETTE["black"])
        ax.text(59.5, yp - 3.0, sd, fontsize=7.6, color="#333333", linespacing=1.2)
        
    for ya in [68, 22]:
        ax.annotate("", xy=(76.75, ya - 3.5), xytext=(76.75, ya + 0.5),
                    arrowprops=dict(arrowstyle="->", color=PALETTE["orange"], lw=1.8))
    # Arrow between Step 2 and Step 3
    ax.annotate("", xy=(76.75, 41.5), xytext=(76.75, 48.5),
                arrowprops=dict(arrowstyle="->", color=PALETTE["orange"], lw=1.8))

    # Big Block Arrow Bridging Study 1 to Study 2
    y_mid = 45.0
    shaft_h = 6.8
    head_h = 9.4
    x_start = 43.5
    x_head_base = 53.3
    x_tip = 56.5

    verts = [
        (x_start, y_mid - shaft_h / 2),
        (x_head_base, y_mid - shaft_h / 2),
        (x_head_base, y_mid - head_h / 2),
        (x_tip, y_mid),
        (x_head_base, y_mid + head_h / 2),
        (x_head_base, y_mid + shaft_h / 2),
        (x_start, y_mid + shaft_h / 2),
    ]

    arrow_patch = patches.Polygon(verts, closed=True,
                                  fc=PALETTE["purple"], ec="#6A1B9A", lw=1.5, zorder=5)
    ax.add_patch(arrow_patch)

    ax.text(48.2, y_mid, "Grounds\nPersonas &\nFailure Modes",
            ha="center", va="center", fontsize=7.2, weight="bold",
            color="#FFFFFF", zorder=6, linespacing=1.15)

    save_fig(fig, "fig3_dual_study_pipeline")

# -------------------------------------------------------------
# Figure 4: Empirical Results — Study 1 (PLP & Latency Acceleration)
# -------------------------------------------------------------
def generate_fig4_performance_learning_paradox():
    learner_df = pd.read_csv(DATA_PROCESSED / "study1_learner_cohorts.csv")
    latency_summary = pd.read_csv(DATA_PROCESSED / "study1_latency_summary.csv")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2), dpi=300)
    
    # Panel A: Crossover Interaction (PLP)
    cohorts = ["Low COI", "Moderate COI", "High COI"]
    colors = [PALETTE["green"], PALETTE["sky_blue"], PALETTE["vermilion"]]
    markers = ["o", "s", "^"]
    
    # Calculate means and 95% CIs
    phases = ["Assisted In-Session", "Unassisted Delayed"]
    
    for i, c in enumerate(cohorts):
        sub = learner_df[learner_df["coi_cohort"] == c]
        in_m = sub["acc_assisted_in_session"].mean()
        in_ci = 1.96 * sub["acc_assisted_in_session"].sem()
        del_m = sub["acc_unassisted_delayed"].mean()
        del_ci = 1.96 * sub["acc_unassisted_delayed"].sem()
        
        ax1.errorbar([0, 1], [in_m, del_m], yerr=[in_ci, del_ci],
                     label=f"{c} (N={len(sub)})", color=colors[i], marker=markers[i],
                     linewidth=2.2, markersize=7, capsize=4)
                     
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(phases, weight="bold")
    ax1.set_ylabel("Mean Accuracy (0.0 – 1.0)", weight="bold")
    ax1.set_ylim(0.20, 1.02)
    ax1.set_title("(A) Performance–Learning Paradox Crossover Interaction\n(ASSISTments Causal RCT Ecosystem, N=4,200)",
                  weight="bold", pad=10)
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="lower left")
    
    # Annotation for crossover
    ax1.annotate("Illusion of Competence\n(Assisted In-Session Boost)",
                 xy=(0.05, 0.92), xytext=(0.20, 0.95),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["vermilion"], lw=1.2),
                 fontsize=8.5, color=PALETTE["vermilion"], weight="bold")
    ax1.annotate("Cognitive Debt Collapse\n(Unassisted Post-Test)",
                 xy=(0.95, 0.36), xytext=(0.55, 0.28),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["vermilion"], lw=1.2),
                 fontsize=8.5, color=PALETTE["vermilion"], weight="bold")

    # Panel B: Longitudinal Response Latency Trajectories (Impulsivity Acceleration)
    for i, c in enumerate(cohorts):
        c_lat = latency_summary[latency_summary["coi_cohort"] == c]
        ax2.errorbar(c_lat["trial"], c_lat["mean_ms"] / 1000.0,
                     yerr=1.96 * (c_lat["std_ms"] / 1000.0) / np.sqrt(500),
                     label=c, color=colors[i], marker=markers[i],
                     linewidth=2.0, markersize=6, capsize=3)
                     
    ax2.set_xlabel("Unassisted Transfer Opportunity (Trial 1–6)", weight="bold")
    ax2.set_ylabel("First-Response Latency (Seconds)", weight="bold")
    ax2.set_title("(B) Longitudinal Help-Seeking Impulsivity Acceleration\n(Latencies Across Unassisted Transfer Trials)",
                  weight="bold", pad=10)
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="upper right")
    
    plt.tight_layout()
    save_fig(fig, "fig4_performance_learning_paradox")

# -------------------------------------------------------------
# Figure 5: BKT Cognitive Trajectory Simulation (Study 1)
# -------------------------------------------------------------
def generate_fig5_bkt_retention_curves():
    bkt_df = pd.read_csv(DATA_PROCESSED / "bkt_simulation_trajectories.csv")
    with open(DATA_PROCESSED / "study1b_bkt_summary.json") as f:
        bkt_meta = json.load(f)
        
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    
    cohorts = ["Low COI", "Moderate COI", "High COI"]
    colors = [PALETTE["green"], PALETTE["sky_blue"], PALETTE["vermilion"]]
    line_styles = ["-", "-.", "--"]
    
    # Vertical line separating practice from post-removal retention
    ax.axvline(15, color=PALETTE["grey"], linestyle=":", linewidth=1.5, zorder=1)
    ax.text(14.7, 0.08, "Scaffold Removal Threshold", rotation=90, color=PALETTE["grey"],
            fontsize=8.5, ha="right", style="italic")
            
    # Phase shading
    ax.axvspan(1, 15, color="#F0F4F8", alpha=0.5, label="Assisted Practice Phase")
    ax.axvspan(15, 30, color="#FFF3F0", alpha=0.5, label="Delayed Unassisted Retention Phase")
    
    for i, c in enumerate(cohorts):
        sub = bkt_df[bkt_df["cohort"] == c]
        phi = bkt_meta["decay_parameters"][c]["phi_decay"]
        ax.plot(sub["trial"], sub["mean_latent_mastery"],
                label=f"{c} ($\\phi_{{\\text{{decay}}}}$ = {phi:.3f})",
                color=colors[i], linestyle=line_styles[i], linewidth=2.4)
                
    ax.set_xlim(1, 30)
    ax.set_ylim(0.0, 1.0)
    ax.set_xlabel("Practice and Transfer Opportunities (Trials 1 – 30)", weight="bold")
    ax.set_ylabel("Latent Knowledge Mastery $P(L_n)$", weight="bold")
    ax.set_title("Longitudinal Bayesian Knowledge Tracing: Assisted Acquisition vs. Post-Removal Decay\n"
                 "(Corbett & Anderson BKT with Cognitive Offloading-Modulated Forgetting)",
                 weight="bold", pad=12)
    ax.grid(True, linestyle="--", alpha=0.6)
    
    # Explanatory annotations
    ax.annotate("Socratic Consolidation\n(Retention Ratio: 83.4%)",
                xy=(28, 0.72), xytext=(21, 0.82),
                arrowprops=dict(arrowstyle="->", color=PALETTE["green"], lw=1.4),
                fontsize=8.5, color=PALETTE["green"], weight="bold")
    ax.annotate("Cognitive Debt Forgetting\n(Retention Ratio: 13.7%)",
                xy=(28, 0.12), xytext=(20, 0.25),
                arrowprops=dict(arrowstyle="->", color=PALETTE["vermilion"], lw=1.4),
                fontsize=8.5, color=PALETTE["vermilion"], weight="bold")
                
    ax.legend(frameon=True, facecolor="#FFFFFF", edgecolor="#CCCCCC", loc="upper left")
    plt.tight_layout()
    save_fig(fig, "fig5_bkt_retention_curves")

# -------------------------------------------------------------
# Figure 6: Multi-Agent Audit Results — Study 2
# -------------------------------------------------------------
def generate_fig6_llm_audit_heatmap_survival():
    config_persona_df = pd.read_csv(DATA_PROCESSED / "study2_config_persona_summary.csv")
    survival_df = pd.read_csv(DATA_PROCESSED / "study2_survival_curves.csv")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.2), dpi=300)
    
    # Panel A: Grouped Bar Chart of BOFR % across Configs & Personas
    configs = ["Config_A", "Config_B", "Config_C"]
    cfg_labels = ["Config A\n(Consumer)", "Config B\n(Naive Helpful)", "Config C\n(Guardrailed)"]
    personas = ["Persona_1", "Persona_2", "Persona_3"]
    p_labels = ["Answer-Seeking", "Frustrated", "Misconception-Driven"]
    p_colors = [PALETTE["vermilion"], PALETTE["sky_blue"], PALETTE["orange"]]
    
    x = np.arange(len(configs))
    width = 0.25
    
    for j, p in enumerate(personas):
        bofr_vals = []
        for c in configs:
            val = config_persona_df[(config_persona_df["config_id"] == c) &
                                    (config_persona_df["persona_id"] == p)]["bofr_pct"].values[0]
            bofr_vals.append(val)
        ax1.bar(x + (j - 1) * width, bofr_vals, width, label=p_labels[j],
                color=p_colors[j], edgecolor="#333333", linewidth=0.8)
                
    ax1.set_xticks(x)
    ax1.set_xticklabels(cfg_labels, weight="bold")
    ax1.set_ylabel("Bottom-Out Failure Rate (BOFR %)", weight="bold")
    ax1.set_ylim(0, 115)
    ax1.set_title("(A) Bottom-Out Failure Rate by AI Configuration & Persona\n(N=900 Simulated Trajectories on gemini-3.8-flash)",
                  weight="bold", pad=10)
    ax1.grid(True, linestyle="--", alpha=0.6, axis="y")
    ax1.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="upper right")
    
    # Panel B: Kaplan-Meier Socratic Survival Curves (Score >= 2)
    cfg_colors = {
        "Config_A": PALETTE["vermilion"],
        "Config_B": PALETTE["orange"],
        "Config_C": PALETTE["green"]
    }
    cfg_display = {
        "Config_A": "Config A: Consumer Default",
        "Config_B": "Config B: Naive Helpful Tutor",
        "Config_C": "Config C: Guardrailed Socratic"
    }
    
    for c in configs:
        sub_s = survival_df[survival_df["config_id"] == c]
        ax2.step(sub_s["turn"], sub_s["survival_prob"], where="post",
                 label=cfg_display[c], color=cfg_colors[c], linewidth=2.4)
        ax2.fill_between(sub_s["turn"], sub_s["ci_low"], sub_s["ci_high"],
                         step="post", alpha=0.15, color=cfg_colors[c])
                         
    ax2.set_xlabel("Dialogue Interaction Turn (Turns 1 – 4)", weight="bold")
    ax2.set_ylabel("Socratic Survival Probability S(t)", weight="bold")
    ax2.set_ylim(-0.05, 1.05)
    ax2.set_xticks([0, 1, 2, 3, 4])
    ax2.set_title("(B) Turn-by-Turn Socratic Scaffolding Survival Curves\n(Maintaining Non-Offloading Rubric Score >= 2)",
                  weight="bold", pad=10)
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="upper right")
    
    plt.tight_layout()
    save_fig(fig, "fig6_llm_audit_heatmap_survival")

# -------------------------------------------------------------
# Figure 7: Domain-Stratified Offloading & Misconception Remediation
# -------------------------------------------------------------
def generate_fig7_domain_misconceptions():
    domain_df = pd.read_csv(DATA_PROCESSED / "study2_domain_summary.csv")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.0, 5.2), dpi=300)
    
    # Panel A: Domain-Stratified BOFR and MRR
    domains = ["ARITH", "FRAC", "RATIO", "GEOM"]
    domain_labels = ["Arithmetic\n(Multi-Step)", "Fractions &\nDecimals", "Ratios &\nProportions", "Geometry &\nMeasurement"]
    x = np.arange(len(domains))
    width = 0.20
    
    bofr_a = [domain_df[(domain_df["domain_code"] == d) & (domain_df["config_id"] == "Config_A")]["bofr_pct"].values[0] for d in domains]
    bofr_b = [domain_df[(domain_df["domain_code"] == d) & (domain_df["config_id"] == "Config_B")]["bofr_pct"].values[0] for d in domains]
    bofr_c = [domain_df[(domain_df["domain_code"] == d) & (domain_df["config_id"] == "Config_C")]["bofr_pct"].values[0] for d in domains]
    mrr_c = [domain_df[(domain_df["domain_code"] == d) & (domain_df["config_id"] == "Config_C")]["mrr_pct"].values[0] for d in domains]
    
    ax1.bar(x - 1.5 * width, bofr_a, width, label="Config A: BOFR % (Consumer)",
            color=PALETTE["vermilion"], edgecolor="#333333", linewidth=0.8)
    ax1.bar(x - 0.5 * width, bofr_b, width, label="Config B: BOFR % (Naive Helpful Tutor)",
            color=PALETTE["orange"], edgecolor="#333333", linewidth=0.8)
    ax1.bar(x + 0.5 * width, bofr_c, width, label="Config C: BOFR % (Guardrailed)",
            color=PALETTE["blue"], edgecolor="#333333", linewidth=0.8)
    ax1.bar(x + 1.5 * width, mrr_c, width, label="Config C: Remediation Rate (MRR %)",
            color=PALETTE["green"], edgecolor="#333333", linewidth=0.8, hatch="//")
            
    ax1.set_xticks(x)
    ax1.set_xticklabels(domain_labels, weight="bold")
    ax1.set_ylabel("Rate (%)", weight="bold")
    ax1.set_ylim(0, 120)
    ax1.set_title("(A) Domain-Stratified Offloading (BOFR) & Misconception Remediation (MRR)\n(Comparing Consumer Baseline vs. Guardrailed Socratic Model)",
                  weight="bold", pad=10)
    ax1.grid(True, linestyle="--", alpha=0.5, axis="y")
    ax1.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="upper right", fontsize=8)
    
    # Panel B: Turn-by-Turn Mean Rubric Trajectories Across Domains for Config C vs Configs A & B
    turns = [1, 2, 3, 4]
    domain_colors = {
        "ARITH": PALETTE["blue"],
        "FRAC": PALETTE["purple"],
        "RATIO": PALETTE["orange"],
        "GEOM": PALETTE["green"]
    }
    markers = {"ARITH": "o", "FRAC": "s", "RATIO": "^", "GEOM": "D"}
    
    for d in domains:
        sub_d = domain_df[(domain_df["domain_code"] == d) & (domain_df["config_id"] == "Config_C")]
        vals = [
            sub_d["turn1_mean"].values[0],
            sub_d["turn2_mean"].values[0],
            sub_d["turn3_mean"].values[0],
            sub_d["turn4_mean"].values[0]
        ]
        ax2.plot(turns, vals, marker=markers[d], markersize=6, linewidth=2.0,
                 label=f"Config C: {d}", color=domain_colors[d])
                 
    # Reference lines for Config A and Config B
    sub_a = domain_df[domain_df["config_id"] == "Config_A"]
    vals_a = [sub_a["turn1_mean"].mean(), sub_a["turn2_mean"].mean(), sub_a["turn3_mean"].mean(), sub_a["turn4_mean"].mean()]
    ax2.plot(turns, vals_a, marker="x", linestyle="--", color=PALETTE["vermilion"],
             linewidth=2.2, label="Config A (Mean all domains)")
             
    sub_b = domain_df[domain_df["config_id"] == "Config_B"]
    vals_b = [sub_b["turn1_mean"].mean(), sub_b["turn2_mean"].mean(), sub_b["turn3_mean"].mean(), sub_b["turn4_mean"].mean()]
    ax2.plot(turns, vals_b, marker="v", linestyle=":", color=PALETTE["orange"],
             linewidth=2.2, label="Config B (Mean all domains)")
             
    ax2.set_xlabel("Dialogue Interaction Turn (Turns 1 – 4)", weight="bold")
    ax2.set_ylabel("Mean Rubric Score (0 = Offload, 3 = Socratic)", weight="bold")
    ax2.set_ylim(-0.2, 3.4)
    ax2.set_xticks(turns)
    ax2.set_title("(B) Turn-by-Turn Rubric Degradation Trajectories Across Mathematical Domains\n(Tracking Socratic Scaffolding Collapse Under Adversarial Pleading)",
                  weight="bold", pad=10)
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="upper right", fontsize=8)
    
    plt.tight_layout()
    save_fig(fig, "fig7_domain_misconceptions_and_remediation")

# -------------------------------------------------------------
# Figure 8: Cognitive Debt, Hazard Rate, and Entropy Dynamics
# -------------------------------------------------------------
def generate_fig8_cognitive_debt_entropy():
    hazard_df = pd.read_csv(DATA_PROCESSED / "study2_hazard_summary.csv")
    entropy_debt_df = pd.read_csv(DATA_PROCESSED / "study2_entropy_debt_summary.csv")
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15.2, 4.8), dpi=300)
    
    cfg_colors = {
        "Config_A": PALETTE["vermilion"],
        "Config_B": PALETTE["orange"],
        "Config_C": PALETTE["green"]
    }
    cfg_labels = {
        "Config_A": "Config A: Consumer Default",
        "Config_B": "Config B: Naive Helpful Tutor",
        "Config_C": "Config C: Guardrailed Socratic"
    }
    
    turns = [1, 2, 3, 4]
    
    # Panel A: Discrete Hazard Rate lambda(t)
    x = np.arange(len(turns))
    width = 0.26
    for i, cfg in enumerate(["Config_A", "Config_B", "Config_C"]):
        sub_h = hazard_df[hazard_df["config_id"] == cfg]
        hazards = sub_h["hazard_rate"].values
        n_risk = sub_h["n_at_risk"].values
        ax1.bar(x + (i - 1) * width, hazards, width, label=cfg_labels[cfg],
                color=cfg_colors[cfg], edgecolor="#333333", linewidth=0.8)
                
        # Data labels for non-zero collapses and muted indicators for zero / depleted
        for j, (h_val, nr) in enumerate(zip(hazards, n_risk)):
            bx = x[j] + (i - 1) * width
            if h_val > 0.0:
                pct_str = f"{h_val*100:.1f}%" if h_val < 1.0 else "100%"
                ax1.text(bx, h_val + 0.025, f"{h_val:.2f}\n({pct_str})", ha="center", va="bottom",
                         fontsize=7.5, weight="bold", color="#222222")
            else:
                if nr == 0:
                    ax1.text(bx, 0.02, "—", ha="center", va="bottom", fontsize=8, color="#888888")
                else:
                    ax1.text(bx, 0.02, "0%", ha="center", va="bottom", fontsize=7, color="#555555", weight="bold")
                
    ax1.set_xticks(x)
    ax1.set_xticklabels([f"Turn {t}" for t in turns], weight="bold")
    ax1.set_ylabel(r"Hazard Rate of Collapse $\lambda(t)$", weight="bold")
    ax1.set_ylim(0, 1.25)
    ax1.set_title(r"(A) Discrete Hazard Rate of Collapse $\lambda(t)$" + "\n(Conditional Prob of Offload at Turn t)",
                  weight="bold", pad=10)
    ax1.grid(True, linestyle="--", alpha=0.5, axis="y")
    ax1.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="upper right", fontsize=8)
    
    # Panel B: Cumulative Cognitive Debt CDA_t
    for cfg in ["Config_A", "Config_B", "Config_C"]:
        sub_ed = entropy_debt_df[entropy_debt_df["config_id"] == cfg]
        cda_vals = sub_ed["mean_cda"].values
        cda_err = sub_ed["std_cda"].values / np.sqrt(300)
        ax2.plot(turns, cda_vals, marker="o", markersize=6, linewidth=2.2,
                 label=cfg_labels[cfg], color=cfg_colors[cfg])
        ax2.fill_between(turns, cda_vals - 1.96 * cda_err, cda_vals + 1.96 * cda_err,
                         alpha=0.15, color=cfg_colors[cfg])
                         
    ax2.set_xlabel("Dialogue Interaction Turn (Turns 1 – 4)", weight="bold")
    ax2.set_ylabel("Cumulative Cognitive Debt (CDA_t)", weight="bold")
    ax2.set_ylim(-0.1, 4.3)
    ax2.set_xticks(turns)
    ax2.set_title("(B) Cumulative Cognitive Debt Accumulation (CDA_t)\n(Accrual of Offloaded Mental Operations)",
                  weight="bold", pad=10)
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="upper left", fontsize=8)
    
    # Panel C: Dialogue Information Entropy H_dialogue
    for cfg in ["Config_A", "Config_B", "Config_C"]:
        sub_ed = entropy_debt_df[entropy_debt_df["config_id"] == cfg]
        ent_vals = sub_ed["mean_entropy"].values
        ent_err = sub_ed["std_entropy"].values / np.sqrt(300)
        ax3.plot(turns, ent_vals, marker="s", markersize=6, linewidth=2.2,
                 label=cfg_labels[cfg], color=cfg_colors[cfg])
        ax3.fill_between(turns, ent_vals - 1.96 * ent_err, ent_vals + 1.96 * ent_err,
                         alpha=0.15, color=cfg_colors[cfg])
                         
    ax3.set_xlabel("Dialogue Interaction Turn (Turns 1 – 4)", weight="bold")
    ax3.set_ylabel("Information Entropy H(X) (bits/token)", weight="bold")
    ax3.set_ylim(1.8, 5.2)
    ax3.set_xticks(turns)
    ax3.set_title("(C) Dialogue Information Entropy Dynamics H(X)\n(Collapse of Lexical & Cognitive Diversity)",
                  weight="bold", pad=10)
    ax3.grid(True, linestyle="--", alpha=0.5)
    ax3.legend(frameon=True, facecolor="#FAFAFA", edgecolor="#DDDDDD", loc="lower left", fontsize=8)
    
    plt.tight_layout()
    save_fig(fig, "fig8_cognitive_debt_entropy_dynamics")

def main():
    print("Generating all 8 publication-grade figures...")
    ensure_graphical_abstract_file()
    generate_fig1_dual_developmental_pathways()
    generate_fig2_theoretical_framework()
    generate_fig3_dual_study_pipeline()
    generate_fig4_performance_learning_paradox()
    generate_fig5_bkt_retention_curves()
    generate_fig6_llm_audit_heatmap_survival()
    generate_fig7_domain_misconceptions()
    generate_fig8_cognitive_debt_entropy()
    print("All 8 publication figures generated successfully in figures/ (PNG + PDF).")

if __name__ == "__main__":
    main()


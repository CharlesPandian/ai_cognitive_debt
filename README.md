# The Illusion of Competence and Cognitive Debt in Primary Mathematics: Causal Telemetry and Multi-Agent Behavioral Audits of Generative AI Tutoring

**Target Journal:** *Computers & Education* (Elsevier, ISSN: 0360-1315)  
**Article Type:** Full-Length Empirical Research Article  
**Author:** Charles Pandian (Independent Researcher, Afarion Systems, Tamilnadu, India)  
**Corresponding Email:** `jcs.pandian@gmail.com`  
**ORCID iD:** `https://orcid.org/0009-0009-0606-6338`  

---

## 1. Executive Summary & Core Hypothesis

This repository provides the complete, end-to-end, reproducible computational pipeline and publication-grade LaTeX manuscript for our investigation into AI-induced **cognitive debt** in upper-primary mathematics education (Grades 4–5, ages 9–11).

### Core Hypothesis
Over-reliance on automated answer-providing AI systems does not develop durable cognitive capacity in young learners. Instead, it creates an **Illusion of Competence** (the *Performance–Learning Paradox*), induces **cognitive debt**, accelerates help-seeking impulsivity, erodes productive struggle, and degrades unassisted knowledge retention.

---

## 2. Directory Architecture

```text
project_ai_cognitive_debt/
├── run_all.sh                              # Master one-click automation script executing Steps 1–6
├── requirements.txt                        # Python dependencies (google-genai, numpy, pandas, scipy, statsmodels, scikit-learn, matplotlib, seaborn)
├── data/
│   ├── raw/                                # Ingestion schema & documentation for ASSISTments 88 RCTs & Clickstream
│   ├── benchmark_100/                      # 100 stratified primary-level math items (JSON + CSV)
│   └── processed/                          # Computed COI metrics, BKT parameters, JSONL audit checkpoints & statistical summaries
├── src/
│   ├── generate_benchmark.py               # Generates the 100 stratified primary math items across 4 domains
│   ├── 01_assistments_causal_analysis.py   # Study 1a: Causal & longitudinal analysis of bottom-out answer reliance
│   ├── 02_bkt_cognitive_decay_model.py     # Study 1b: Bayesian Knowledge Tracing & post-removal retention decay
│   ├── 03_llm_validation_audit.py          # Study 2: 3x3 factorial multi-turn simulated student audit (Gemini API)
│   ├── 04_rubric_scorer_and_stats.py       # Study 2b: 0-3 rubric scoring, Cohen's kappa, BOFR, TTO, survival & mixed-effects stats
│   └── 05_generate_publication_figures.py  # Generates all 8 publication-grade 300-DPI PNG + vector PDF figures/diagrams
├── figures/                                # 8 publication figures (300 DPI PNG + vector PDF)
│   ├── fig1_graphical_abstract.{pdf,png}   # Mandatory Graphical Abstract (Productive Struggle vs AI Offloading)
│   ├── fig2_theoretical_framework.{pdf,png}# Multi-layer conceptual framework (CLT, Desirable Difficulties, Sycophancy)
│   ├── fig3_dual_study_pipeline.{pdf,png}  # Methodological architecture (Study 1 Telemetry -> Study 2 Audit)
│   ├── fig4_performance_learning_paradox.{pdf,png} # Empirical crossover interaction & latency acceleration
│   ├── fig5_bkt_retention_curves.{pdf,png} # BKT cognitive trajectory simulation & post-removal decay
│   ├── fig6_llm_audit_heatmap_survival.{pdf,png}   # Multi-agent BOFR & Kaplan-Meier survival curves
│   ├── fig7_domain_misconceptions_and_remediation.{pdf,png} # Domain breakdown (BOFR, MRR) & rubric degradation trajectories
│   └── fig8_cognitive_debt_entropy_dynamics.{pdf,png}       # Hazard rate λ(t), cumulative debt CDA_t, and entropy H(X)
├── manuscript/
│   ├── cas-sc.cls                          # Official Elsevier Single-Column CAS LaTeX class
│   ├── cas-common.sty                      # Elsevier CAS common macro package
│   ├── cas-model2-names.bst                # Elsevier Chicago author-date BibTeX style
│   ├── title_page.tex                      # Separate Title Page (Elsevier double-anonymized review compliance)
│   ├── main.tex                            # Complete 23-page Elsevier cas-sc LaTeX manuscript
│   ├── main.pdf                            # Compiled unblinded / camera-ready publication PDF
│   ├── main_blinded.pdf                    # Compiled double-anonymized PDF (for Elsevier Editorial Manager submission)
│   ├── references.bib                      # Comprehensive BibTeX bibliography (APA/Author-Date)
│   ├── highlights.txt                      # 5 mandatory highlights (strictly <= 85 characters each)
│   └── cover_letter.tex                    # 2-page editorial cover letter to Computers & Education
└── README.md                               # Complete reproducibility documentation
```

---

## 3. Dual-Study Empirical Methodology

In strict compliance with *Computers & Education* standards, the investigation is framed through two rigorous components:

### Study 1: Quasi-Experimental Causal & Longitudinal Telemetry Analysis (ASSISTments Ecosystem)
- **Dataset:** 88 Assignment-Level Randomized Controlled Trials (RCTs) paired with the 2012–2013 Longitudinal Clickstream dataset ($N = 4,200$ primary/middle-school learners across 24 Knowledge Components).
- **Four Methodological Grounds:**
  1. *Causal Identification:* Pre-existing assignment-level randomization between immediate bottom-out answers vs. scaffolded tutoring resolves the correlation-vs.-causation desk-rejection trap.
  2. *Fine-Grained Telemetry:* Millisecond-level latency (`ms_first_response`), hint requests, and bottom-out hint flags (`bottom_out_hint`).
  3. *Developmental Scope:* Isolates Grades 4–5 foundational mathematics (multi-step arithmetic, fractions, ratios, geometry).
  4. *Ethical Minor Compliance:* Eliminates COPPA/GDPR-K child-privacy risks of deploying untested generative LLMs on 9-to-11-year-old minors in classrooms.
- **Operationalized Constructs:**
  - **Cognitive Offloading Index ($\text{COI}_i$):** Proportion of problems where learner $i$ requested bottom-out answers or rapid sub-3s hint escalation. Partitioned into Low ($\text{COI} < 0.15$), Moderate ($0.15 \le \text{COI} < 0.45$), and High ($\text{COI} \ge 0.45$).
  - **Performance–Learning Paradox Delta ($\Delta_{\text{PLP}}$):** $\text{Acc}_{\text{assisted, in-session}} - \text{Acc}_{\text{unassisted, delayed transfer}}$.
  - **Impulsivity Acceleration Slope ($\beta_{\text{latency}}$):** Longitudinal linear mixed-effects model of response latency decay across unassisted trials.
  - **Cognitive Debt BKT:** Canonical Corbett–Anderson BKT extended with offloading-modulated unassisted retention decay ($\phi_{\text{decay}}$).

### Study 2: In-Silico Controlled Multi-Agent Pedagogical Audit (`gemini-3.8-flash`)
- **100-Item Benchmark:** Stratified equally across 4 primary domains (25 Multi-Step Arithmetic, 25 Fractions \& Decimals, 25 Ratios \& Proportions, 25 Geometry \& Measurement), with ground-truth solutions and dual misconception distractors ($D_1$: conceptual, $D_2$: procedural).
- **3 $\times$ 3 Factorial Audit:** 900 multi-turn trajectories (4 student turns each = 3,600 tutor interactions):
  - *Factor A (AI Configurations):* Config A (Unconstrained Consumer Default), Config B (Naive Helpful Tutor), Config C (Pedagogically Guardrailed Socratic Tutor).
  - *Factor B (Student Personas):* Persona 1 (Answer-Seeking / Offloading), Persona 2 (Frustrated / Low-Persistence), Persona 3 (Impulsive Guesser).
- **4-Point Cognitive Offloading Coding Rubric (0–3 Scale):**
  - *Score 0:* Full Cognitive Offloading / Bottom-Out Failure (reveals answer or full calculation).
  - *Score 1:* Substitutive Procedural Scaffolding (withholds final number but solves core structure).
  - *Score 2:* Directive Hinting (instructs student which operation to execute next).
  - *Score 3:* Productive-Struggle Socratic Prompting (open conceptual question, diagnoses misconception).
- **Evaluative Metrics:** Bottom-Out Failure Rate (BOFR %), Mean Time-to-Offload (TTO), Socratic Survival Rate %, Kaplan-Meier survival analysis, and Cohen's $\kappa$ inter-rater reliability.

---

## 4. Key Empirical Findings

| Construct / Metric | Low COI (Socratic) | Moderate COI | High COI (Offloading) | Statistical Test / Effect Size |
| :--- | :---: | :---: | :---: | :--- |
| **Assisted In-Session Accuracy** | 76.1% | 86.1% | 94.1% | Crossover Interaction $F(2, 4197) = 2677.89, p < 0.0001$ |
| **Unassisted Delayed Accuracy** | 63.0% | 50.2% | 34.2% | Low vs High COI: $t = 51.92, p < 0.0001, d = 1.99$ |
| **PLP Delta ($\Delta_{\text{PLP}}$)** | +0.132 | +0.360 | +0.599 | Partial $\eta^2 = 0.124$ (Large effect) |
| **Impulsivity Acceleration Slope** | $+0.009$ | $-0.071$ | $-0.173$ | MixedLM interaction $z = -78.57, p < 0.0001$ |
| **BKT Retention Ratio (T15 $\to$ T30)**| 83.4% | 47.8% | 13.7% | Cognitive Debt BKT vs Standard: $\Delta\text{BIC} = 24,762.8$ |
| **Audit BOFR (Config A: Consumer)** | --- | --- | 100.0% | Mean TTO = 1.0 turns; Survival = 0.0% |
| **Audit BOFR (Config B: Naive)** | --- | --- | 100.0% | Mean TTO = 2.0 turns; Survival = 0.0% |
| **Audit BOFR (Config C: Socratic)** | --- | --- | 49.3% | Sycophantic collapse under child pleading ($\chi^2 = 365.78$) |
| **Audit Inter-Rater Reliability** | --- | --- | $\kappa = 0.886$ | 93.8% raw agreement on 20% validation subsample |

---

## 5. Quick Start & One-Click Execution

### Prerequisites
- Python 3.10+ (managed automatically via `uv` or system virtualenv)
- Dependencies installed via `requirements.txt`
- Tectonic or pdflatex for LaTeX compilation

### Installation
```bash
# Clone repository and enter directory
cd /home/jason/EdTechPaper1/project_ai_cognitive_debt

# Install Python dependencies
pip install -r requirements.txt
```

### Running the Entire Research Pipeline
To run the automated analysis, generate all figures, and compile the manuscript in one click:
```bash
bash run_all.sh
```

### Running Live on Google Gemini API (`gemini-3.8-flash`)
To execute Study 2 directly against Google's live `gemini-3.8-flash` model on your free-tier API key:
```bash
export GEMINI_API_KEY="YOUR_GOOGLE_AI_STUDIO_KEY"
bash run_all.sh --live
```
*Note on Quota Safety & Checkpointing:* `03_llm_validation_audit.py` saves every trajectory immediately to `data/processed/audit_checkpoints.jsonl` and includes automated 6.5s rate pacing and HTTP 429 exponential backoff. You can interrupt and resume at any time without repeating already audited items.

---

## 6. Elsevier Computers & Education Submission Checklist

- [x] **Separate Title Page (`manuscript/title_page.tex`):** Double-anonymized review compliance, full author metadata, CRediT statement, funding, and competing interests.
- [x] **Mandatory Highlights (`manuscript/highlights.txt`):** 5 bullet points, strictly $\le 85$ characters each including spaces.
- [x] **Full Manuscript (`manuscript/main.tex` / `manuscript/main.pdf`):** 19 pages, ~8,500–9,500 words, Chicago Author-Date citations, 6 figures, 5 editable booktabs tables.
- [x] **Editorial Cover Letter (`manuscript/cover_letter.tex`):** Scope justification addressed to Editors-in-Chief.
- [x] **High-Resolution Figures (`figures/`):** 6 vector PDF and 300 DPI PNG figures with colorblind-safe Okabe-Ito palettes.
- [x] **Option C Research Data Deposit:** Full open code and benchmark availability.

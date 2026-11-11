# SepsisShield — NIErnaya Phase 2 Integrated Project

This ZIP contains the **exact original `Dataset.csv` you uploaded**, three role-specific Jupyter notebooks, calculated Phase 2 EDA outputs, the full cleaned-data handoff, and presentation/technical reports.

## Run in this order

1. **Person 1 — EDA:** `notebooks/01_Person1_EDA.ipynb`
   - Dataset profile, schema, row-vs-patient label imbalance, missingness, distributions, IQR outlier screening, correlations, patient timelines, cohort trajectories and measurement-availability fingerprint.
2. **Person 2 — Cleaning and preprocessing:** `notebooks/02_Person2_Preprocessing.ipynb`
   - Structural checks, verified redundant-index removal, duplicate checks, non-finite handling, IQR outlier review and conservative validity flags. Missing clinical values and valid extreme observations are preserved.
   - Output: `outputs/02_preprocessing/cleaned_dataset.csv.gz`.
3. **Person 3 — Feature engineering and feature intelligence:** `notebooks/03_Person3_Feature_Engineering.ipynb`
   - Patient-wise lag, change, rolling, variability and missingness features; feature-quality analysis; Spearman correlation; mutual information; PCA exploration; patient-separated validation manifest; leakage audit.
   - Expected: 56 additional temporal features from seven vital signs.

## Setup on macOS

From the extracted `SepsisShield_NIErnaya_Phase2` folder, open Terminal and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Open and run the three notebooks in order. They locate `data/Dataset.csv` when Jupyter starts from the project folder or its `notebooks/` folder. The original CSV is not overwritten.

## Team ownership

See `TEAM_WORK_ALLOCATION.md` for precise responsibility and handoff rules. All three notebooks use the same dataset but address different stages; do not split the patient rows among members.

## Evidence and interpretation

- `reports/DATASET_VERIFIED_FINDINGS.md` contains data-derived findings from the supplied CSV.
- `reports/PRESENTATION_STORY.md` contains a suggested jury narrative.
- `reports/TECHNICAL_LIMITATIONS.md` lists methodological boundaries.
- `reports/NOTEBOOK_VERIFICATION_STATUS.md` honestly records what was executed during package preparation.

## Methodological safeguards

- IQR outliers are flags for investigation, not automatic deletion rules.
- Clinical missing values are preserved in Person 2's handoff. Any model imputer must be fitted on training patients only.
- `Patient_ID` is for grouping/splitting, not a predictor. `SepsisLabel` is the target, never a predictor.
- PhysioNet's `SepsisLabel` already represents the challenge's six-hour early-warning window. Do not shift it again.
- Lag and rolling features use only each patient's current and past observations, with windows masked when required hours are not consecutive.
- Patient-level random holdout is not chronological future validation and is not cross-hospital validation.
- PCA and mutual information are exploratory; neither establishes improved predictive performance by itself.
- The project is retrospective research, not a validated clinical diagnostic or treatment system. No notebook can guarantee hackathon qualification.

## Official dataset documentation

https://physionet.org/content/challenge-2019/1.0.0/
# sepsisshield-icu-early-warning

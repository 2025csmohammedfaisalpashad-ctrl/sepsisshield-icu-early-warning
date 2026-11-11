# Team responsibility and handoff

## Person 1 — Exploratory Data Analysis
- Dataset structure and schema.
- Row-level versus patient-level class balance.
- Missing-value patterns and missingness by label.
- Vital distributions and statistical IQR screening.
- Spearman correlation among vital signs.
- Patient record-length analysis.
- Cohort trajectories aligned to the first positive challenge label.
- Measurement availability fingerprint.

**Handoff:** EDA tables, charts, structural checks and evidence-backed written insights.

## Person 2 — Data cleaning and preprocessing
- Validate required columns, exact duplicates and patient-hour uniqueness.
- Drop `Unnamed: 0` only after confirming it exactly duplicates `Hour`.
- Convert infinities to missing only if present.
- Sort by patient and hour.
- Flag IQR outliers; do not delete valid extremes.
- Preserve clinical missing values; do not impute globally.
- Export cleaned compressed CSV and cleaning audit.

**Handoff:** `outputs/02_preprocessing/cleaned_dataset.csv.gz` plus audit tables.

## Person 3 — Temporal feature engineering and feature intelligence
- Create lag 1, lag 3, change 1, rolling mean 3, rolling mean 6, rolling standard deviation 6, missing-now and missing-count-6 for seven vital signs (56 new features).
- Check patient boundaries and consecutive-hour windows.
- Create patient-level train/test manifest.
- Investigate feature quality and high correlations on training patients only.
- Rank features using mutual information on a balanced training sample.
- Explore PCA on a training-only sample.
- Export engineered dataset and audit.

**Handoff:** engineered dataset, feature dictionary and validation reports.

## Integration rules

- All notebooks begin from the same original source file, but run in order.
- Person 1 does not alter source data. Person 2 generates the cleaned handoff. Person 3 uses Person 2's cleaned output if present.
- Do not overwrite `data/Dataset.csv`.
- Every member should be able to explain the whole workflow at a high level, not only their own notebook.

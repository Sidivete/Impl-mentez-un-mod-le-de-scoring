# Modèle de Scoring Crédit — Pipeline ML complet + Dashboard explicable

Pipeline Machine Learning de bout en bout pour la prédiction du risque de défaut de remboursement, avec dashboard interactif, interprétabilité SHAP et détection de data drift.

---

## Projet

Prêt à Dépenser est une société financière proposant des crédits à la consommation à des personnes ayant peu ou pas d'historique de prêt. L'objectif est de calculer automatiquement la probabilité qu'un client rembourse son crédit, de classifier la demande en accordé ou refusé, et d'expliquer les décisions de manière transparente aux gestionnaires et aux clients.

---

## Ce que j'ai construit

- Pipeline EDA complet sur 300 000+ lignes : nettoyage, gestion des valeurs manquantes, détection d'anomalies, feature engineering, visualisations
- Modélisation avec plusieurs algorithmes (LightGBM retenu) optimisé sur le score métier business plutôt que sur l'accuracy classique
- Interprétabilité globale et locale via SHAP : explication de chaque décision d'octroi ou de refus
- API Flask de scoring : endpoint de prédiction consommé par le dashboard
- Dashboard interactif Streamlit pour les gestionnaires : visualisation des profils clients, probabilité de défaut, comparaison aux clients similaires
- Détection de data drift avec Evidently : surveillance de la stabilité du modèle sur de nouvelles données
- Rapport HTML de drift exporté automatiquement

---

## Stack

- Machine Learning : LightGBM, Scikit-learn
- Interprétabilité : SHAP
- API : Flask, Python
- Dashboard : Streamlit
- Data Drift : Evidently
- EDA & Visualisation : Pandas, NumPy, Matplotlib, Seaborn
- Données : Kaggle Home Credit Default Risk (300 000+ lignes)

---

## Structure du projet

```
EDA.ipynb                               Analyse exploratoire et feature engineering
MOdelisation.ipynb                      Modélisation, optimisation et interprétation SHAP
DATADRIFT.ipynb                         Calcul du drift entre données train et nouvelles données
app.py                                  API Flask — endpoint de prédiction
dab.py                                  Dashboard Streamlit interactif
report.html                             Rapport HTML de data drift (Evidently)
BEDDY_SIDI_3_note_méthodologique.pdf    Note méthodologique complète
presentation.pdf                        Support de présentation
```

---

## Pipeline ML

Étape 1 — EDA et préparation des données sur le dataset Kaggle Home Credit (300 000+ lignes, 120+ features), nettoyage et feature engineering.

Étape 2 — Modélisation et sélection du modèle final LightGBM, optimisé sur un score métier personnalisé pénalisant davantage les faux négatifs (prêts accordés à tort).

Étape 3 — Interprétabilité SHAP globale (importance des features) et locale (explication de chaque décision individuelle).

Étape 4 — Déploiement via API Flask consommée par le dashboard Streamlit.

Étape 5 — Monitoring : détection du data drift entre les données d'entraînement et les nouvelles données via Evidently.

---

## Lancement

**API Flask**

```bash
pip install -r package.txt
python app.py
```

**Dashboard Streamlit**

```bash
streamlit run dab.py
```

---

## Données

Dataset public Kaggle — Home Credit Default Risk :
https://www.kaggle.com/c/home-credit-default-risk/data

---

## Auteur

Sidi Teyib BEDDY — Data Scientist | ML Engineer

[LinkedIn](https://linkedin.com/in/sidi-teyib) · [GitHub](https://github.com/Sidivete)

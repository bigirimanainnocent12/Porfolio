# 📊 Data Scientist & Analyst Portfolio - Innocent BIGIRIMANA

Bienvenue sur le dépôt de mon portfolio professionnel. Ce projet présente mes compétences en Data Science, Data Engineering et Business Intelligence, ainsi que mes projets phares réalisés sur le cloud (GCP) et en local.

## 🚀 À propos de moi
Je suis **Innocent BIGIRIMANA**, un passionné de la donnée spécialisé dans la transformation d'écosystèmes complexes en leviers décisionnels stratégiques. Mon expertise couvre l'ensemble du cycle de vie de la donnée : de l'ingestion automatisée à la modélisation prédictive et la visualisation.

## 🛠️ Stack Technique
- **Languages**: Python (Pandas, PySpark, Scikit-Learn), SQL (PostgreSQL, SQL Server).
- **Cloud & Orchestration**: Google Cloud Platform (GCP), BigQuery, Cloud Composer (Apache Airflow), Google Cloud Storage.
- **Business Intelligence**: Power BI (DAX Advanced), Tableau, Data Storytelling.
- **Data Engineering**: Pipelines ETL/ELT industriels, Automatisation des flux.
- **Machine Learning**: Régression, Classification, BigQuery ML, MLOps.

## 📂 Structure du Projet
```text
Portfolio-Innocent/
├── assets/                 # Ressources multimédias (images des projets, logos)
├── index.html              # Page principale du portfolio (Structure HTML5)
├── style.css               # Design UI/UX, animations et responsive design
├── script.js               # Interactions dynamiques et effets de défilement
├── download_images.py      # Script Python pour la gestion des assets images
├── download_logo.py        # Script Python pour la récupération des logos
└── README.md               # Documentation et présentation du projet
```

## 📂 Projets Phares

### 1. NYC Taxi Data Pipeline (150M+ lignes)
- **Objectif** : Architecture ELT industrielle sur GCP.
- **Détails** : Ingestion de fichiers Parquet NYC TLC vers GCS, orchestration via Cloud Composer, traitement BigQuery et modèle ML intégré.
- **Visualisation** : Dashboard interactif Power BI.

### 2. Pipeline Météo Automatisé (Open-Météo API)
- **Objectif** : Monitoring climatique mondial de 8 métropoles.
- **Détails** : Extraction des prévisions à 7 jours via API, orchestration Airflow tous les 6 jours.
- **Visualisation** : Dashboard Power BI des tendances mondiales.

### 3. Optimisation des Ventes
- **Objectif** : Analyse de rentabilité et calcul de KPIs (DAX).
- **Détails** : Création de dashboards interactifs Power BI pour le pilotage commercial.

### 4. Prédiction des Frais d'Assurance (ML & Deployment)
- **Objectif** : Estimation des coûts de santé via Random Forest.
- **Variables du jeu de données** :

| Variable | Type | Description |
| :--- | :--- | :--- |
| age | Quantitative | Âge de l'assuré |
| sex | Qualitative binaire | Sexe (Male/Female) |
| bmi | Quantitative | Indice de Masse Corporelle |
| children | Quantitative | Nombre d'enfants à charge |
| smoker | Qualitative binaire | Statut fumeur (Yes/No) |
| region | Qualitative | Région de résidence (4 modalités) |
| charges | Quantitative | Frais médicaux (variable cible) |

- **Déploiement** : Modèle final déployé avec une API **FastAPI** sur **Render**.
- **Stack** : Scikit-Learn, Pandas, FastAPI, Render.

### 5. Analyses Statistiques (ANOVA & Test-T)
- **Objectif** : Validation d'hypothèses rigoureuse sur des données de production.
- **Détails** : Tests de normalité, homoscédasticité et interprétation des p-values.

## 🎨 Design du Portfolio
Le portfolio est conçu avec une esthétique moderne et premium :
- **Technologies** : HTML5, CSS3 (Vanilla), JavaScript.
- **Features** : Design responsive, animations d'apparition (Reveal JS), Glassmorphism, typographie Outfit/Inter.
- **Architecture** : Section projets avec numérotation stylisée et focus sur les stacks techniques.

## 📬 Contact
- **LinkedIn** : [innocent-bigirimana](https://www.linkedin.com/in/bigirimanainnocent12)
- **GitHub** : [bigirimanainnocent12](https://github.com/bigirimanainnocent12)
- **Email** : [innocentbigirimana@example.com]

---
*© 2026 Innocent BIGIRIMANA | Conçu avec passion.*

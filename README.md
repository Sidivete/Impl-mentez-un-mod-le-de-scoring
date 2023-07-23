# OC Data Scientist - Projet 7 : Implémentez un modèle de scoring

## Contexte
Prêt à dépenser est une société financière qui propose des crédits à la consommation à des personnes ayant peu ou pas d'historique 
de prêt.L'entreprise souhaite mettre en œuvre un outil de scoring crédit pour calculer la probabilité qu'un client rembourse son prêt, 
classer la demande en crédit accordé ou refusé, et expliquer de manière transparente au client les décisions d'octroi de crédit.

Le modèle de scoring crédit sera utilisé par les professionnels de la banque pour évaluer les demandes de prêt. 
Il sera important que le modèle soit capable d'expliquer les décisions d'octroi de crédit de manière claire et transparente,
afin que les clients puissent comprendre pourquoi leur demande a été acceptée ou refusée.

Voici quelques avantages supplémentaires de l'utilisation d'un tableau de bord interactif :

- Il permet de suivre les performances du modèle de scoring crédit et d'identifier les domaines d'amélioration.
- Il permet de communiquer les résultats des calculs aux clients de manière claire et concise.
- Il permet de générer des rapports sur les décisions d'octroi de crédit, qui peuvent être utilisés pour améliorer les processus internes.
- Il permet de se conformer aux exigences réglementaires en matière de prêt.

## DATA
https://www.kaggle.com/c/home-credit-default-risk/data

## MISSION 
- Construire un modèle de scoring qui produit une prédiction de probabilité de défaut pour une demande client de façon automatique.
- Construire un dashboard interactif à destination des gestionnaires de relation client,qui interprète les prédictions faites par le modèle,
visualise les informations des clients, et permette d’expliquer aux clients les décisions d’octroi de crédit.

## LIVRABLE 
- EDA.ipynb : Notebook de prétraitement et d'analyse exploratoire des données, avec essai de plusieurs modèles de modélisation.
- Modelisation.ipynb : Notebook de préparation de l'interprétation et de la visualisation des résultats du modèle.
- DATADRIFT.ipynb : Notebook contenant le calcul du drift entre les nouvelles données et les données d'entraînement.
- report.html : Fichier HTML contenant un tableau présentant les résultats du calcul du drift.
- app.py : Code source de l'API Flask de mise à disposition des routes.
- dab.py : Code du dashboard avec Streamlit.
- Rapport.pdf : Rapport décrivant la méthodologie du modèle de scoring, son interprétation, son déploiement, et les limites et améliorations identifiées.
- Présentation.pdf : Support de présentation.


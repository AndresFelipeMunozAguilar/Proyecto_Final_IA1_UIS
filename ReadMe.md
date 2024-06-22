# Multimodal Early Detection of Parkinson's Disease

<img src="./notebooks/figures/High Quality Banner Multimodal Early Detection of Parkinson's Disease.png" alt="Banner" width="1600">

| **Model**                        | **Accuracy**         | **F1-score**         | **Precision**        | **Sensitivity**      |
|----------------------------------|----------------------|----------------------|----------------------|----------------------|
| **GNB**                          | 47.65% (+/- 10.94%)  | 46.20% (+/- 18.18%)  | 47.58% (+/- 15.10%)  | **51.86% (+/- 29.56%)**  |
| **DT DEFAULT**                   | 51.50% (+/- 5.17%)   | **49.23% (+/- 8.24%)** | 51.17% (+/- 5.62%) | 48.23% (+/- 12.24%)  |
| **DT2**                          | 50.22% (+/- 9.63%)   | 39.43% (+/- 20.94%)  | 49.01% (+/- 11.29%)  | 41.81% (+/- 34.23%)  |
| **DT40**                         | 50.22% (+/- 5.77%)   | 48.46% (+/- 9.54%)   | 49.35% (+/- 5.69%)   | 48.42% (+/- 14.24%)  |
| **RF50**                         | 53.88% (+/- 17.11%)  | 45.54% (+/- 23.36%)  | 51.27% (+/- 18.23%)  | 44.36% (+/- 30.41%)  |
| **RF100**                        | 54.98% (+/- 16.20%)  | 45.50% (+/- 23.46%)  | 52.62% (+/- 17.93%)  | 44.53% (+/- 32.25%)  |
| **RF200**                        | 55.35% (+/- 17.78%)  | 46.20% (+/- 24.21%) | 52.93% (+/- 17.98%) | 44.91% (+/- 32.19%)  |
| **SVM LINEAR**                   | 50.87% (+/- 8.02%)   | 48.81% (+/- 11.67%)  | 49.73% (+/- 8.01%)   | 48.61% (+/- 15.44%)  |
| **SVM RBF**                      | **57.73% (+/- 16.36%)** | 44.70% (+/- 25.62%)  | 56.88% (+/- 19.80%) | 41.24% (+/- 31.61%) |
| **SVM POLY DEGREE 3**            | 54.90% (+/- 7.35%)   | 26.90% (+/- 16.96%)  | **64.82% (+/- 20.48%)**  | 17.97% (+/- 12.95%)  |
| **LR**                           | 51.05% (+/- 8.89%)   | 47.96% (+/- 13.15%) | 49.57% (+/- 8.90%)   | 47.32% (+/- 17.28%) |






## Overview

This repository contains the work done as part of the Artificial Intelligence I project for the Universidad Industrial de Santander. This project aims to develop a non-invasive multimodal strategy to enhance early detection of Parkinson's disease. By utilizing video and audio analysis techniques, we seek to identify distinctive patterns in motor symptoms such as facial rigidity and speech disorders.

**Team Members**: Juan Diego Roa Porras, Andrés Felipe Muñoz Aguilar, Guillermo Pinto Ruiz

## Dataset

The dataset is private and belongs to [Biv2Lab](https://uis-macv.github.io/), involving 14 participants (7 Parkinson’s patients, 7 controls), with audio and video recordings of the pronunciation of vowels, phonemes and various words.

## Notebooks Description

<img src="./notebooks/figures/methodologies.png" alt="Methodologies" width="1600">

 - **[Data Exploration:](https://github.com/AndresFelipeMunozAguilar/Proyecto_Final_IA1_UIS/blob/main/notebooks/0.01-gpr-data-exploration.ipynb)** Initial analysis of the data set, including mainly visualization to understand the characteristics of the data.

 - **[Data Feature Extraction:](https://github.com/AndresFelipeMunozAguilar/Proyecto_Final_IA1_UIS/blob/main/notebooks/0.02-gpr-feature-extraction.ipynb)** Preprocessing steps such as normalization and transformation of audio and video data to prepare it for machine learning algorithms.

 - **[PCA:](https://github.com/AndresFelipeMunozAguilar/Proyecto_Final_IA1_UIS/blob/main/notebooks/2.01-afm-dimensionality-reduction.ipynb)** Understanding of Principal Component Analysis (PCA) to reduce the dimensionality of the data set, preserving the most important features and simplifying the complexity.

 - **Machine Learning (audio | video | audio+video):** Implementing machine learning algorithms such as GaussianNB, DecisionTreeClassifier, RandomForestClassifier, SVC, and LogisticRegression to classify and predict patterns indicative of Parkinson's disease ([ML](https://github.com/AndresFelipeMunozAguilar/Proyecto_Final_IA1_UIS/blob/main/notebooks/1.01-gpr-machine-learning-classification.ipynb) | [PCA+ML](https://github.com/AndresFelipeMunozAguilar/Proyecto_Final_IA1_UIS/blob/main/notebooks/3.01-afm-pca-machine-learning.ipynb)).

 - **Deep Learning (audio+video):** Implementation of a fully connected neural network architecture to leverage combined audio and video data to classify and predict patterns indicative of Parkinson's disease ([DL](https://github.com/AndresFelipeMunozAguilar/Proyecto_Final_IA1_UIS/blob/main/notebooks/1.02-gpr-deep-learning-classification.ipynb) | [PCA+DL](https://github.com/AndresFelipeMunozAguilar/Proyecto_Final_IA1_UIS/blob/main/notebooks/3.02-gpr-pca-deep-learning-classification.ipynb)).

 - **[Non-supervised (audio | video | audio+video):](https://github.com/AndresFelipeMunozAguilar/Proyecto_Final_IA1_UIS/blob/main/notebooks/3.03-jdr-pca-non-supervised.ipynb)** Using unsupervised learning methods to identify clusters within the data and comparing these clusters with true labels to evaluate the clustering approach.

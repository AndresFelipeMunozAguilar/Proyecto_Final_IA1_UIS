# Multimodal Early Detection of Parkinson's Disease

<img src="./notebooks/figures/High Quality Banner Multimodal Early Detection of Parkinson's Disease.png" alt="Banner" width="1600">

**| Model                            | Accuracy (%) | F1-score (%) | Precision (%) | Sensitivity (%) |**
|----------------------------------|----------------------|---------------------|---------------------|---------------------|
| **GNB**                              | 47.66% (+/- 28.56%)  | 43.28% (+/- 34.98%) | 45.71% (+/- 38.80%) | 50.18% (+/- 44.14%) |
| **DT DEFAULT**                     | 42.78% (+/- 18.49%)  | 46.46% (+/- 19.50%) | 43.97% (+/- 19.20%) | 51.86% (+/- 24.93%) |
| **DT2**                              | 58.23% (+/- 15.83%)  | 57.28% (+/- 23.80%) | 54.87% (+/- 19.87%) | 65.20% (+/- 31.35%) |
| **DT40**                             | 48.47% (+/- 20.73%)  | 51.05% (+/- 22.51%) | 50.07% (+/- 23.31%) | 57.45% (+/- 29.12%) |
| **RF50**                             | 46.20% (+/- 17.53%)  | 34.04% (+/- 27.90%) | 41.63% (+/- 35.02%) | 38.64% (+/- 40.03%) |
| **RF100**                            | 49.50% (+/- 19.91%) | 45.08% (+/- 27.21%) | 47.59% (+/- 32.30%) | 50.00% (+/- 36.35%) |
| **RF200**                            | 48.40% (+/- 19.21%)  | 40.26% (+/- 28.45%) | 46.34% (+/- 31.96%) | 44.69% (+/- 38.85%) |
| **SVM LINEAR**                       | 75.45% (+/- 18.36%) | 64.72% (+/- 33.94%) | **78.79% (+/- 35.57%)** | 63.00% (+/- 37.61%) |
| **SVM RBF**                          | **77.79% (+/- 22.64%)**  | **68.30% (+/- 38.01%)** | 76.97% (+/- 35.62%) | **71.79% (+/- 41.64%)** |
| **SVM POLY DEGREE 3**                | 48.92% (+/- 12.13%)  | 11.19% (+/- 13.04%) | 43.43% (+/- 49.01%) | 6.60% (+/- 7.61%)   |
| **LR**                               | 75.72% (+/- 16.85%)  | 66.47% (+/- 31.52%) | 78.42% (+/- 35.37%) | 63.70% (+/- 34.24%) |



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

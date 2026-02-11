# Behavioral Feature Extraction & Annotation Pipeline 🧠📊

```
A comprehensive pipeline for synchronizing manual behavioral annotations (ELAN) with
automated computer vision feature extraction. This repository is designed for researchers and
developers working on Human Activity Recognition (HAR), focusing on social behaviors,
eating habits, and facial kinematics.
```
## 🚀 Key Features

```
ELAN Integration: Seamlessly convert .eaf files to structured .csv data.
Computer Vision Metrics: Automated extraction of facial landmarks, pose estimation, and
hand tracking using MediaPipe.
Kinematic Analysis: Calculates real-time velocities (e.g., wrist-to-mouth speed) and
geometric angles (gaze direction, face orientation).
Normalization Logic: Feature scaling based on physiological ratios (e.g., using eye-
distance as a dynamic baseline) for robust cross-subject analysis.
Label Processing: Intelligent mapping and cleaning of hierarchical annotations.
```
## 📂 Repository Structure

```
File Description
```
```
eaf-to-csv-convert.ipynb Converts ELAN .eaf files to CSV and standardizes tier/annotation
labels.
```
```
landmark-face-
detection.ipynb
```
```
The core engine. Extracts 468 facial landmarks, hand positions, and
body pose features.
```
```
analyze-labels.ipynb Statistical analysis of annotations, including label frequency
distribution and overlap detection.
```
```
import pandas as pd.py Utility script for batch-processing and cleaning annotation CSVs.
```
## 🛠 Installation

```
Ensure you have a Python 3.8+ environment. Install the necessary dependencies:
```
```
pip install mediapipe opencv-python pandas numpy pympi-ling
```
2/11/26, 11:53 PM Google Gemini

https://gemini.google.com/app 1 / 2


## 🔄 Workflow

1. Annotation Pre-processing
Use eaf-to-csv-convert.ipynb to transform your manual annotations. It includes logic to
map generic "Yes" labels back to their specific Tier names (e.g., Left_speaking,
    Right_eating), creating a clean ground-truth dataset.
2. Automated Feature Extraction
Run landmark-face-detection.ipynb to process video files. The script extracts:
    Mouth/Lip Metrics: Lip distance, mouth width, and ear-to-lip ratios (useful for detecting
    speaking/eating).
    Gaze & Head Pose: Vertical/horizontal gaze angles and face orientation.
    Interaction Kinematics: Wrist-to-mouth distance and velocity.
    Binary Indicators: Synchronized ground-truth flags for smiling, speaking, eating,
    and fork_towards.
3. Data Validation
Utilize analyze-labels.ipynb to visualize class balance and ensure your annotations aren't
overlapping in ways that might confuse a machine learning model.

## 📐 Extracted Metrics

```
The pipeline calculates sophisticated features beyond raw coordinates:
Normalized Ratios: All distances are divided by the subject's eye-to-eye distance to
handle varying distances from the camera.
Rolling Averages: Velocity metrics use a rolling window to smooth out sensor jitter.
Standardization: Automatically performs Z-score normalization on final features.
```
## 🤝 Contributing

```
Contributions are welcome! If you have a specific behavioral feature you'd like to automate (e.g.,
micro-expressions, specific tool usage), please open an issue or submit a pull request.
```
## 📄 License

```
This project is licensed under the MIT License - see the LICENSE file for details.
```



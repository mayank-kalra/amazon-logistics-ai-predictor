# 📦 Amazon Logistics AI - Delay Predictor & Risk Analytics

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent logistics machine learning platform and interactive web dashboard designed to predict shipment delivery delays, identify operational bottlenecks (hub waiting time, traffic status, buffer inventory), and provide proactive operational directives.

---

## 🎯 Key Objectives

1. **Predict Delivery Delays**: Proactively classify whether an in-transit or dispatched package will be delayed.
2. **Minimize False Negatives**: In logistics, missing a late shipment damages customer trust. Using custom decision threshold tuning (0.5 → 0.3) achieves near-100% recall.
3. **Multi-Class Operational Scoring**: Classify deliveries into three actionable states:
   - 🟢 **On-Time** (Safe transit window)
   - 🟡 **At Risk** (Minor delay risk, manageable via fast-track dock dispatch)
   - 🔴 **High Delay Risk** (Severe delay expected, automated rerouting required)
4. **Interactive Web Dashboard**: Streamlit interface for live predictions, shipping document verification, batch CSV scoring, and visual exploratory data analysis.

---

## 🚀 Interactive Web App Features

- **🚚 Live Delivery Predictor**:
  - Upload shipment visual proof (package photo, shipping label, traffic camera feed, or GPS detour route) or select from built-in sample images.
  - Tune operational parameters: Hub waiting time, traffic conditions, inventory buffer, weather, and demand index.
  - Receive real-time status badges, delay probabilities, and prescriptive AI operational directives.
- **📊 Analytics & Delay Drivers**:
  - Interactive tabs showing delay correlations by traffic status, hub waiting times, seasonal monthly trends, and model metrics.
- **📁 Batch Prediction (CSV)**:
  - Upload bulk shipment CSV/Excel files or test built-in sample records.
  - Automatically calculate risk categories and export predictions to CSV.
- **🧠 Model Comparison**:
  - Compare accuracy, precision, recall, and F1 scores across Logistic Regression, Decision Tree, and Random Forest models.

---

## 📊 Model Performance Benchmark

| Model | Accuracy | Recall (Late Detection) | Precision | F1 Score | Primary Business Advantage |
|---|---|---|---|---|---|
| **Logistic Regression (Default)** | 83.3% | 66.7% | 100.0% | 0.8000 | General linear baseline |
| **Logistic Regression (Tuned 0.3)** | 50.0% | **100.0% (Zero Misses)** | 50.0% | 0.6667 | **Critical Operations** (Minimizes false negatives) |
| **Decision Tree (Optimized)** | **100.0%** | **100.0%** | **100.0%** | **1.0000** | High-confidence categorization |
| **Random Forest (Tuned)** | 83.3% | **100.0%** | 75.0% | 0.8571 | Robust multi-class risk scoring |

> **Threshold Tuning Rationale**: Missing a delayed shipment (false negative) is far costlier to Amazon customer satisfaction than investigating a false alert. Adjusting the classification threshold from `0.5` to `0.3` eliminates missed delays.

---

## 🛠️ Project Structure

```
amazon-logistics-ai-predictor/
├── app.py                      # Main Streamlit web application
├── run_web.py                  # Streamlit launcher script
├── run.py                      # End-to-end ML pipeline runner
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── code/
│   └── Final Project.py        # ML training, SFS, & figure generation script
├── data/
│   └── sample/
│       ├── logistics_raw_sample.csv
│       └── logistics_clean_sample.csv
├── assets/
│   └── figures/                # High-resolution generated charts
│       ├── 01_delay_distribution.png
│       ├── 02_delays_by_month.png
│       ├── 03_delay_by_traffic.png
│       ├── 04_waiting_time_by_delay.png
│       ├── 05_binary_model_comparison.png
│       ├── 06_binary_confusion_matrices.png
│       ├── 07_multiclass_model_comparison.png
│       └── 08_multiclass_confusion_matrix.png
└── sample_images/              # Test images for the live predictor UI
    ├── sample_amazon_shipping_label.png
    ├── sample_heavy_traffic_route.png
    └── sample_warehouse_dock_queue.png
```

---

## 💻 Installation & Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/mayank-kalra/amazon-logistics-ai-predictor.git
cd amazon-logistics-ai-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Web Application
```bash
python run_web.py
```
*Or directly via Streamlit:*
```bash
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

### 4. (Optional) Run the Full ML Training Pipeline
To retrain models and regenerate all visualization figures in `assets/figures/`:
```bash
python run.py
```

---

## 🔍 Key Findings

1. **Waiting Time & Traffic are Primary Drivers**: Hub wait times exceeding 0.4 normalized hours combined with heavy or detour traffic correlate with an **85%+ delay probability**.
2. **Buffer Inventory Shield**: Nodes with low buffer inventory (< 0.4) show higher vulnerability to demand shocks.
3. **Operational Prescriptions**:
   - Automated dynamic rerouting when traffic status is heavy or detoured.
   - Priority dock staging for packages experiencing wait times > 0.4 hours.
   - Buffer inventory replenishment prior to seasonal peak volume months.

---

## 📄 License
This project is licensed under the MIT License.

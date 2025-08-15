# Cats vs Dogs CNN — Transfer Learning
**What it does:** Classifies images of cats vs dogs using a pretrained backbone.  
**Why it matters:** Demonstrates practical CV fine‑tuning with explainability.

## Highlights
- ✅ Transfer learning (e.g., ResNet50)
- 🔍 Grad‑CAM for explainability
- 🖥️ Streamlit UI for drag‑and‑drop predictions

## How to run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dmassey66/cats-vs-dogs-cnn/blob/main/notebooks/demo.ipynb)

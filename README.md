# Cats vs Dogs CNN — Transfer Learning
🔹 1. What the Cats vs Dogs Program Does
    •	You feed in an image (say, a photo of a golden retriever).
    •	The program uses a pretrained CNN backbone (like ResNet, VGG, or EfficientNet) to extract features.
    •	It fine-tunes on your dataset so it can confidently say: “Dog” or “Cat.”
________________________________________
🔹 2. Where AI Reasoning Shows Up
    1.	Feature Abstraction → Evidence Gathering
        o	The CNN backbone isn’t just memorizing pixels.
        o	It’s extracting hierarchical evidence: edges → textures → shapes → ears vs. whiskers.
        o	This mirrors human reasoning: noticing patterns that point to a conclusion.
    2.	Transfer of Knowledge
        o	The pretrained model already “knows” a lot about images from huge datasets (millions of objects).
        o	Transfer learning is basically reasoning by analogy: “I’ve seen animals with fur and tails before, so I can use that knowledge to recognize cats and dogs.”
    3.	Decision-Making with Confidence
        o	The softmax output isn’t just yes/no. It says: “I’m 92% sure this is a cat, 8% dog.”
        o	That’s probabilistic reasoning — weighing evidence and committing to a conclusion with uncertainty in mind.
________________________________________
🔹 3. The Bigger AI Connection
      •	This is visual reasoning at scale: turning raw sensory input (images) into high-level concepts (cats vs. dogs).
      •	Transfer learning is how modern AI systems generalize: instead of relearning from scratch, they reuse prior knowledge, just like humans do.
      •	This kind of reasoning powers:
        o	Self-driving cars (distinguishing pedestrians vs. street signs).
        o	Medical imaging (tumor vs. non-tumor).
        o	Security systems (safe objects vs. threats).


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

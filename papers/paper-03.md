---
layout: default
title: "AffectNet: Facial Expression & Affective Computing in the Wild"
parent: "Learnings"
nav_order: 3
---

# AffectNet: Facial Expression & Affective Computing in the Wild

**Paper**: [“AffectNet: A Database for Facial Expression, Valence, and Arousal Computing in the Wild”](https://arxiv.org/abs/1708.03985)  
**Authors**: Ali Mollahosseini, Behzad Hasani, Mohammad H. Mahoor  
**Published**: 2017, *IEEE Transactions on Affective Computing*

---

## Summary

- **Dataset**: Collected **~1 million** face images via web queries using 1,250 emotion-related keywords across six languages, then manually annotated ⬋  
  - **450k images** labeled for seven discrete expressions *(e.g., happy, sad, angry)* and continuous **valence-arousal** scores :contentReference[oaicite:1]{index=1}.

- **Emotion Models**:
  - **Categorical**: Seven basic expressions
  - **Dimensional**: Valence (positive–negative), Arousal (calm–excited)

- **Baselines**:
  - Deep CNNs for expression classification
  - AlexNet for valence-arousal regression
  - Achieved **state-of-the-art** performance compared to traditional methods and MS Cognitive API :contentReference[oaicite:2]{index=2}.

---

## Key Insights

{: .callout-info }
### Scale & Diversity
- Mixing search-engine images in six languages generates a **massive, diverse dataset**.
- Covers “wild” conditions—poses, lighting, ethnicity, occlusions.

{: .callout-success }
### Model Versatility
- Enables both **classification** (qualitative emotions) and **regression** (quantitative valence/arousal).
- Useful for creating robust, multimodal emotion systems.

{: .callout-warning }
### Annotation Challenges
- Human-labeler agreement was ~60% for discrete emotions—consistent with inherent ambiguity :contentReference[oaicite:3]{index=3}.
- Valence/arousal labeling had RMSE ~0.34–0.48—implying subjectivity and annotation noise.

---

## No Public Code Available [tried but didn't get]

- The authors didn't release baseline model code.
- But many emotion recognition repositories support AffectNet (e.g., RetinaFace, FER models). Here’s how you can load metadata:

```python
import pandas as pd

# Example: loading annotations (CSV format provided by some community forks)
df = pd.read_csv("AffectNet_annotations.csv")
print(df.columns)  # expression, valence, arousal
````

You can then train or evaluate a CNN on categorical labels or perform regression on valence/arousal values.

---

## Reflections

> *“AffectNet showed me the importance of real-world scale and dual modeling (classification + regression) in affective AI.”*

* Realistic emotion systems need both **what emotion** and **how intense**.
* Subjectivity in labels means models must handle uncertainty gracefully.
* Such large databases enable better **transfer learning** for downstream tasks.

---

## References

* [Original Paper PDF](https://arxiv.org/pdf/1708.03985.pdf)
* [AffectNet Discussion & Code](https://github.com/search?q=AffectNet)
* [Affective Computing Survey – IEEE](https://ieeexplore.ieee.org/document/)


```

---
layout: default
title: "MS‑Celeb‑1M: Large‑Scale Face Recognition Benchmark"
parent: "Learnings"
nav_order: 5
---

# MS‑Celeb‑1M: Large‑Scale Face Recognition Benchmark

**Paper**: [MS‑Celeb‑1M: A Dataset and Benchmark for Large‑Scale Face Recognition](https://www.microsoft.com/en-us/research/publication/ms-celeb-1m-dataset-benchmark-large-scale-face-recognition-2/)  
**Authors**: Yandong Guo, Lei Zhang, Yuxiao Hu, Xiaodong He, Jianfeng Gao – ECCV 2016

---

## Summary

- Introduces a **10 million image**, **100K identity** dataset—the largest public face recognition corpus at that time :contentReference[oaicite:1]{index=1}.
- Defines face recognition as not just matching faces but **linking to unique entity keys** (via Freebase), supporting disambiguation and structured retrieval :contentReference[oaicite:2]{index=2}.
- Includes aligned face crops, a **manually-annotated test set**, and benchmarking protocols where top-1 accuracy at 95% precision was ~44.2% on hard cases :contentReference[oaicite:3]{index=3}.

---

## Key Insights

{: .callout-info }
### Benchmark Design
Advance from verification to **identity recognition**: predict who the person is, not merely whether two images match.

{: .callout-success }
### Large‑Scale Dataset
Provides millions of images for **100K celebrities**, enabling deep model training at an unprecedented public scale :contentReference[oaicite:4]{index=4}.

{: .callout-warning }
### Ethical Considerations
The dataset was later **retracted** amid privacy concerns :contentReference[oaicite:5]{index=5}. A cleaned 6M subset exists, but access is restricted or removed.

---

##  Working Code & Tools

###  `MSCELEB1M-GenImage` Script

A community-made Python tool to **decode Base64 image data** from dev‑set TSV files:

```python
# Extract from GitHub: wuyuebupt/MSCELEB1M-GenImage
python msceleb1m_genImage.py MsCelebV1-Faces-Aligned-DevSet1.tsv
````

* Saves decoded `.jpg` images in an `images/` directory ([GitHub][1]).

### Official Code

No official download or loaders; Microsoft provided **aligned crops & TSV files**, not scripts.

---

## Reflections

> *“MS‑Celeb‑1M shows ambition at industrial scale—both the technical leap and ethical implications of large web-scraped biometric datasets.”*

* **Powerful scale**, but **prone to noise** and sensitive to consent/privacy.
* This dataset informed both technical innovation and ethical discourse around face data.

---

## Resources

* [ECCV 2016 Paper PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/08/MSCeleb-1M-a.pdf) ([GitHub][2], [Microsoft][3])
* [MSCELEB1M‑GenImage GitHub](https://github.com/wuyuebupt/MSCELEB1M-GenImage) ([GitHub][1])
* [Exposing.ai analysis & dataset retires](https://exposing.ai/msceleb/) ([Exposing.ai][4])

---

*This analysis has been added to my internship documentation on dataset scale, recognition benchmarks, and responsible AI.*


---

[1]: https://github.com/wuyuebupt/MSCELEB1M-GenImage?utm_source=chatgpt.com "wuyuebupt/MSCELEB1M-GenImage - GitHub"
[2]: https://github.com/Mycenae/PaperWeekly/blob/master/MS-Celeb-1M.md?utm_source=chatgpt.com "PaperWeekly/MS-Celeb-1M.md at master - GitHub"
[3]: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/08/MSCeleb-1M-a.pdf?utm_source=chatgpt.com "[PDF] MS-Celeb-1M: A Dataset and Benchmark for Large-Scale Face ..."
[4]: https://exposing.ai/msceleb/?utm_source=chatgpt.com "MS-Celeb-1M (MS1M) - Exposing.ai"

---
layout: default
title: "CelebA Dataset & CelebA‑HQ Resources"
parent: "Learnings"
nav_order: 4
---

# CelebA: Large-Scale Face Attribute Dataset & Its High‑Quality Variants

**Dataset**: [CelebA: Large-scale CelebFaces Attributes in the Wild]  
**Source**: MMLab CUHK & PyTorch Vision  
**Released**: 2015 for CelebA; CelebA‑HQ & downstream variants emerged later

---

## Overview

- **CelebA** offers ~200K celebrity face images annotated with **40+ binary attributes** and identities—ideal for attribute recognition and generative modeling.
- **CelebA-HQ** refines this into a **high-quality 30K images** at 1024×1024 resolution with precise face crops (via Progressive GANs).
- **CelebAMask-HQ** adds rich **semantic segmentation masks** for detailed facial components (19 classes) :contentReference[oaicite:1]{index=1}.

---

## 🛠 Working Code that Can be Used

### 1. PyTorch Loader
```python
from torchvision.datasets import CelebA
dataset = CelebA(root="data/", split="train", target_type="attr", download=True)
````

Built-in support in `torchvision` for CelebA — no third-party installs needed ([GitHub][1]).

### 2. Downloader & HQ Converter

The **make-CelebA-HQ** script can reconstruct CelebA-HQ from the original dataset:

* Downloads CelebA & CelebA‑HQ archives
* Runs `make_HQ_images.py` to produce high‑res `.npy` image files at 1024×1024 ([GitHub][2]).

---

## Other Community Tools

* **PyTorch loader with identities**: includes MS-CelebA identity labels (`identity_CelebA.txt`) and a notebook for testing ([GitHub][3]).

---

## Practical Notes

* Official MMLab page provides dataset info but no full code ([mmlab.ie.cuhk.edu.hk][4]).
* Third-party scripts exist but may require manual data placement and external downloads.
* Community tools are more reliable and tested.

---

## Reflections

> *“CelebA is foundational — but preparing high-quality versions (HQ, mask, identity) makes it usable for advanced generation and evaluation tasks.”*

* Using high-resolution data with segmentation enables precise inpainting and control networks.
* Attribute-rich annotations allow for strong evaluation on vision and face tasks.
* The PyTorch loader is simple and seamless for everyday use.

---

## Resources

* [CelebA Dataset (torchvision)](https://pytorch.org/vision/stable/datasets.html#celeba) ([GitHub][2], [GitHub][5], [GitHub][3], [GitHub][1])
* [make‑CelebA‑HQ GitHub](https://github.com/mazzzystar/make-CelebA-HQ) ([GitHub][2])
* [CelebAMask‑HQ dataset page](https://mmlab.ie.cuhk.edu.hk/projects/CelebA/CelebAMask_HQ.html) ([mmlab.ie.cuhk.edu.hk][4])
* [PyTorch loader with identities GitHub](https://github.com/mireshghallah/CelebA) ([GitHub][3])

---

*This analysis documents dataset readiness and practical tools for experimentation on CelebA during my internship.*


---

### Summary of Findings

- **Official dataset** provides only data and metadata—no code samples.
- **Working code exists** in community tools:
  - PyTorch `CelebA` loader (built-in)
  - `make-CelebA-HQ` script for preparing upscale dataset
  - Notebooks/helpers for identity attribute loading
- **No fully official code** for parsing or segmentation—community alternatives recommended.

---

[1]: https://github.com/pytorch/vision/blob/main/torchvision/datasets/celeba.py?utm_source=chatgpt.com "vision/torchvision/datasets/celeba.py at main - GitHub"
[2]: https://github.com/mazzzystar/make-CelebA-HQ?utm_source=chatgpt.com "mazzzystar/make-CelebA-HQ - GitHub"
[3]: https://github.com/mireshghallah/CelebA?utm_source=chatgpt.com "mireshghallah/CelebA - GitHub"
[4]: https://mmlab.ie.cuhk.edu.hk/projects/CelebA/CelebAMask_HQ.html?utm_source=chatgpt.com "CelebAMask-HQ Dataset - MMLab@CUHK"
[5]: https://github.com/ziqihuangg/CelebA-Dialog?utm_source=chatgpt.com "CelebA-Dialog Dataset - GitHub"

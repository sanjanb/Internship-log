---
layout: default
title: "Learnings"
nav_order: 3
---

# Key Learnings & Research Insights

This page documents key concepts, strategies, and research papers I studied to deepen my understanding during the internship.

---

## AI/ML Concepts

- **Unsupervised Pretraining**  
  Explored the effectiveness of unsupervised feature learning using autoencoders and its impact on downstream classification.

- **Fine-Tuning**  
  Studied how frozen vs. trainable pretrained layers influence performance when shifting to a supervised task (e.g., even/odd digit classification).

- **ControlNet for Inpainting**  
  Learned how ControlNet conditions generative models with segmentation/masks for controlled outputs in Stable Diffusion pipelines.

---

## Research Papers Studied

| Title | Source | Summary |
|-------|--------|---------|
| [Multimodal Pretraining for Vision-and-Language Tasks](https://arxiv.org/abs/2103.00020) | arXiv | Describes how joint learning on text and images can improve performance on downstream visual-language tasks. |
| [Taming Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2012.09841) | arXiv | Explains how VQ-GAN enables high-resolution generation using transformers with discrete latent spaces. |
| [Label Studio: Data labeling platform](https://labelstud.io/) | Label Studio Docs | Explored its architecture, use cases, and persistent storage setup via Docker. |
| [ControlNet: Adding Conditional Control to Diffusion Models](https://arxiv.org/abs/2302.05543) | arXiv | Introduces the mechanism of adding structure-aware control to Stable Diffusion through a conditional branch. |

---

## Personal Reflections

> These papers and tools helped me:
> - Understand how vision and language models interact
> - Realize the value of unsupervised representation learning
> - Think modularly when designing inpainting workflows
> - Appreciate the infrastructure side (Docker, storage, etc.) of ML tools

---

## Links to Further Study

- [Hugging Face Papers With Code](https://paperswithcode.com/)
- [OpenAI Research](https://openai.com/research)
- [Google Research](https://research.google/)

---

> _“Learning isn't just about applying — it's about understanding the why behind the what.”_

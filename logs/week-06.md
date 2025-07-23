---
layout: default
title: Week 06
parent: Weekly Logs
nav_order: 6
---

# Week 06 – Research Paper Study & Adaptation

**Dates**: 2025-07-08 – 2025-07-14
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.
**Mentor**: Praveen Kulkarni Sir

---

{: .callout-info }

### Focus

This week was focused on understanding high-impact research papers related to facial recognition and multimodal learning. The insights helped us benchmark approaches and select the right direction for extending our current work — all within NDA constraints.

---

## Goals for the Week

* Analyze top papers including DeepFace, CelebA, and MS-Celeb-1M
* Identify architectural and training strategies from published work
* Extract reusable code components or libraries
* Build internal notes for adaptation (non-disclosable externally)

---

## Tasks Completed

| Task                                                 | Status      | Notes                                                  |
| ---------------------------------------------------- | ----------- | ------------------------------------------------------ |
| Reviewed DeepFace CVPR 2014 Paper                    | ✅ Completed | Extracted high-level architecture and pre-processing   |
| Summarized CelebA Dataset Usage & Purpose            | ✅ Completed | Documented data splits and key attributes              |
| Reviewed MS-Celeb-1M Large-Scale Benchmark           | ✅ Completed | Noted benchmark criteria, dataset challenges           |
| Matched CLIP/VLM output to internal project pipeline | ✅ Completed | Used vision encoder outputs in internal test framework |
| Maintained private internal analysis notes (NDA)     | ✅ Completed | For mentor review, not open-sourced                    |

---

## Key Learnings

{: .callout-success }

* Paper reading deepens understanding of **real-world implementations**
* Face verification success hinges on **alignment + representation**
* Vision-language models (like CLIP) can be modularized efficiently
* Datasets vary in complexity, annotation quality, and usage rights

---

## Problems Faced & Solutions

| Problem                           | Solution                                       |
| --------------------------------- | ---------------------------------------------- |
| No direct code in papers          | Used matching PyPI libraries (e.g., DeepFace)  |
| Understanding legacy methods      | Referred to official benchmark sites and repos |
| Need to protect internal insights | Maintained internal-only notebooks (under NDA) |

---

## 📎 References

* [DeepFace Paper (CVPR 2014)](https://www.cs.toronto.edu/~ranzato/publications/taigman_cvpr14.pdf)
* [CelebA Dataset Page](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
* [MS-Celeb-1M Microsoft](https://www.microsoft.com/en-us/research/publication/ms-celeb-1m-dataset-benchmark-large-scale-face-recognition-2/)
* [CLIP via Hugging Face](https://huggingface.co/openai/clip-vit-base-patch32)

---

## Goals for Next Week

* Integrate internal code with vision encoder embeddings
* Begin training internal pipeline with updated feature vectors
* Prepare learnings page with clean summaries (non-sensitive)

---

{: .callout }
*“Digging into the foundational papers gave me clarity on the ‘why’ behind popular architectures — this shapes how we build our own smarter, compliant solutions.”*

---

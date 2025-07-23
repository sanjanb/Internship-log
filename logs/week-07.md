---
layout: default
title: Week 07
parent: Weekly Logs
nav_order: 7
---

# Week 07 – Embedding Paper Techniques into Models

**Dates**: 2025-07-15 – 2025-07-21
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.
**Mentor**: Praveen Kulkarni Sir

---

{: .callout-info }

### Focus

This week was dedicated to applying the learnings from research papers into our internal pipeline. We experimented with model slicing, feature transfer, and designing modular networks.

---

## Goals for the Week

* Adapt pretrained CLIP visual encoder with custom classifier
* Test inference pipeline with sample dataset
* Build scripts to visualize intermediate embeddings
* Clean up the learnings section with proper structure

---

## Tasks Completed

| Task                                                | Status      | Notes                                                  |
| --------------------------------------------------- | ----------- | ------------------------------------------------------ |
| Integrated CLIP vision encoder with MLP head        | ✅ Completed | Used frozen encoder; trained classifier from scratch   |
| Evaluated classification pipeline on sample images  | ✅ Completed | Achieved stable training with low loss (\~0.87)        |
| Documented working code for VLM to MLP architecture | ✅ Completed | Recorded notebook in private repo                      |
| Added two research summaries to Learnings section   | ✅ Completed | Each paper has callouts, code examples, and reflection |
| NDA compliance maintained throughout documentation  | ✅ Completed | Only shared allowed portions publicly                  |

---

## Key Learnings

{: .callout-success }

* Pretrained vision encoders can significantly boost convergence
* Modular design helps in attaching heads, slicing blocks flexibly
* Accurate logs and markdown docs improve reproducibility
* Reviewing loss trends helps in identifying class imbalance

---

## Problems Faced & Solutions

| Problem                             | Solution                                      |
| ----------------------------------- | --------------------------------------------- |
| Feature mismatch from encoder       | Used `.pooler_output` and reshaped inputs     |
| Classifier not converging initially | Tuned learning rate; applied CrossEntropyLoss |
| Keeping learnings under NDA         | Used tags and disclaimers in markdown docs    |

---

## 📎 References

* [CLIPModel – Hugging Face](https://huggingface.co/docs/transformers/model_doc/clip)
* [Internally adapted notebook (Private Repo)](https://github.com/sanjanb)

---

## Goals for Next Week

* Finalize slicing strategy for full VLM to vision module
* Extend MLP head with dropout, batchnorm
* Prepare a sharable demo (NDA-compliant)

---

{: .callout }
*“Week 7 was all about bridging theory and practice — papers to working code. Each experiment took us closer to a modular, trainable, and explainable VLM classifier stack.”*

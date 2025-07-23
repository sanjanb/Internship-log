---
layout: default
title: Week 07
parent: Weekly Logs
nav_order: 7
---

# Week 07 – Face Embedding Models and Verification UI

**Dates**: 2025-07-15 – 2025-07-21
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.
**Mentor**: Praveen Kulkarni Sir

---

{: .callout-info }

### Focus

This week focused on building face embeddings using Siamese networks and developing a basic Gradio interface for face verification.

---

## Goals for the Week

* Build and train a Siamese Network on facial data
* Visualize embeddings with PCA/t-SNE plots
* Create Gradio demo for pairwise verification
* Understand loss functions: Triplet vs. Contrastive

---

## Tasks Completed

| Task                                      | Status      | Notes                                                |
| ----------------------------------------- | ----------- | ---------------------------------------------------- |
| Built a Siamese model with twin encoders  | ✅ Completed | Shared weights, used Euclidean distance layer        |
| Trained on pairs with contrastive loss    | ✅ Completed | Also tested triplet loss for comparison              |
| Created basic Gradio app for verification | ✅ Completed | Users can upload two photos and see similarity score |
| Embedded data visualized with PCA & t-SNE | ✅ Completed | Separated clusters for same vs. different identities |

---

## Key Learnings

{: .callout-success }

* Learned to construct Siamese architecture using PyTorch
* Understood the use of embeddings for verification over classification
* Gained experience with interactive UIs using Gradio
* Learned to visualize embedding spaces using dimensionality reduction

---

## Problems Faced & Solutions

| Problem                                      | Solution                                             |
| -------------------------------------------- | ---------------------------------------------------- |
| Slow training on CPU                         | Switched to Google Colab with GPU runtime            |
| High false positives with low-res inputs     | Set minimum resolution requirements in preprocessing |
| Confusion in contrastive vs triplet training | Trained both to compare their margin effectiveness   |

---

## 📌 References

* [Siamese Network Tutorial](https://omoindrot.github.io/siamese-network)
* [Gradio Docs](https://www.gradio.app/docs/)
* [Triplet Loss Explained](https://omoindrot.github.io/triplet-loss)

---

## Goals for Next Week

* Integrate VLM vision encoder (CLIP) for transfer learning
* Fine-tune MLP head for identity verification task
* Evaluate performance against custom Siamese baseline

---

{: .callout }
*"This week taught me how to turn abstract similarity into actionable face verification using a clean UI and strong embeddings."*

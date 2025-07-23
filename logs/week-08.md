---

layout: default
title: Week 08
parent: Weekly Logs
nav\_order: 8
-------------

# Week 08 – VLM Integration and Embedding Transfer

**Dates**: 2025-07-22 – 2025-07-28
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.
**Mentor**: Praveen Kulkarni Sir

---

{: .callout-info }

### Focus

This week involved slicing a pretrained CLIP model to extract vision embeddings and connect them to a lightweight MLP classifier for face verification.

---

## Goals for the Week

* Load pretrained vision-language model (VLM)
* Extract image embeddings from CLIP's visual backbone
* Train MLP on embeddings to verify face identity
* Track loss and evaluate accuracy over a labeled test set

---

## Tasks Completed

| Task                                            | Status      | Notes                                                  |
| ----------------------------------------------- | ----------- | ------------------------------------------------------ |
| Loaded `openai/clip-vit-base-patch32` model     | ✅ Completed | Used HuggingFace Transformers to extract vision model  |
| Built MLP classifier with frozen vision encoder | ✅ Completed | Used 768-dim pooled output as input to dense layers    |
| Trained model on sample dataset with labels     | ✅ Completed | Achieved good separation; tested with CrossEntropyLoss |
| Visualized embeddings for known identities      | ✅ Completed | Showed distinct regions for each class in t-SNE plot   |

---

## Key Learnings

{: .callout-success }

* Learned how to use CLIP’s visual backbone for downstream tasks
* Understood freezing strategies when using pretrained vision encoders
* Learned model slicing and integration between libraries (HF + PyTorch)
* Visualized VLM-based embeddings and verified their quality

---

## Problems Faced & Solutions

| Problem                                     | Solution                                     |
| ------------------------------------------- | -------------------------------------------- |
| Memory errors during image batch processing | Reduced batch size and cleared CUDA cache    |
| Shape mismatch between VLM and MLP          | Used `.pooler_output` from vision encoder    |
| Slow inference on large image folders       | Batched inputs using CLIPProcessor and loops |

---

## 📌 References

* [CLIP Model HF Docs](https://huggingface.co/docs/transformers/model_doc/clip)
* [Custom MLP on Embeddings](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html)
* [CLIP Visual Architecture](https://openai.com/research/clip)

---

## Goals for Next Week

* Wrap up internship with polished documentation and learning summary
* Record demo videos for Gradio and CLIP inference pipelines
* Prepare LinkedIn write-up and GitHub README updates

---

{: .callout }
*"Working with a pretrained model like CLIP gave me practical insights into modern transfer learning workflows for vision tasks."*

---

layout: default
title: Week 06
parent: Weekly Logs
nav\_order: 6
-------------

# Week 06 – Dataset Curation, Facial Landmarking, and CLI Tools

**Dates**: 2025-07-08 – 2025-07-14
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.
**Mentor**: Praveen Kulkarni Sir

---

{: .callout-info }

### Focus

This week concentrated on preparing datasets for facial analysis, creating scripts for automated cropping and landmarking, and exploring CLI-based efficiency tools.

---

## Goals for the Week

* Curate and preprocess facial datasets for recognition tasks
* Extract landmarks and keypoints from image samples
* Develop reusable CLI scripts for dataset pipeline tasks
* Speed up experimentation through image filters and masks

---

## Tasks Completed

| Task                                               | Status      | Notes                                            |
| -------------------------------------------------- | ----------- | ------------------------------------------------ |
| Downloaded and cleaned dataset from CelebA         | ✅ Completed | Filtered high-quality aligned faces              |
| Implemented facial landmark extraction             | ✅ Completed | Used Dlib + OpenCV for 68-point facial landmarks |
| Built CLI cropping & resize tool                   | ✅ Completed | Takes image folder and bounding boxes as input   |
| Designed basic image filter pipelines (blur, mask) | ✅ Completed | Included grayscale, Gaussian blur, binary mask   |

---

## Key Learnings

{: .callout-success }

* Learned how to automate dataset preprocessing steps
* Improved proficiency with OpenCV, Dlib, and face alignment
* Created CLI tools that reduce redundant image processing effort
* Observed that clean and aligned datasets boost model stability

---

## Problems Faced & Solutions

| Problem                             | Solution                                                 |
| ----------------------------------- | -------------------------------------------------------- |
| Bounding box errors during cropping | Adjusted coordinates with margins to avoid cutting faces |
| Low confidence landmark detection   | Applied CLAHE (contrast enhancement) before detection    |
| CLI errors on large batches         | Used multiprocessing and file-safe loops                 |

---

## 📌 References

* [CelebA Dataset](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
* [Dlib Facial Landmarking](http://dlib.net/face_landmark_detection.py.html)
* [OpenCV Docs](https://docs.opencv.org/)

---

## Goals for Next Week

* Train on facial embeddings using Siamese architecture
* Compare triplet loss and contrastive loss embeddings
* Begin building verification interface using Gradio

---

{: .callout }
*"This week helped me set the foundation for facial verification by preparing clean, aligned, and well-structured data."*

---
layout: default
title: "ControlNet for Guided Image Generation"
parent: "Learnings"
nav_order: 3
---

# ControlNet for Guided Image Generation

**Paper**: [ControlNet: Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543)  
**Authors**: Lvmin Zhang, Maneesh Agrawala  
**Published**: 2023

---

## Overview

ControlNet is an extension of diffusion-based text-to-image generation models (like Stable Diffusion) that introduces **additional conditioning inputs** (e.g., edge maps, depth, pose) to control the output more precisely.

It enables:

- More **reliable generation** aligned with structural inputs.
- Use of **Control Maps** (like Canny edges, OpenPose, etc.) alongside textual prompts.
- Support for **multi-modal conditioning** (visual + text) during generation.

---

## Key Concepts

- **Zero Convolution Layers** allow safe initialization to preserve pretrained weights while integrating new conditional inputs.
- **Cloning** the main UNet backbone into two branches:
  - One frozen (original pre-trained model)
  - One trainable (learns control conditions)
- Supports many control types: `Canny`, `Pose`, `Segmentation`, `Depth`, etc.

---

## 🔬 Visual Summary


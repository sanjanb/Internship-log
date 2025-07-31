---
layout: default
title: "Improved Deep Metric Learning with Multi-class N-pair Loss Objective"
parent: "Learnings"
nav_order: 7
---

# Improved Deep Metric Learning with Multi-class N-pair Loss Objective

**Paper**: [Improved Deep Metric Learning with Multi-class N-pair Loss Objective](https://papers.nips.cc/paper_files/paper/2016/file/6b180037abbebea991d8b1232f8a8ca9-Paper.pdf)
**Authors**: Kihyuk Sohn — Google Research (NIPS 2016)

---

## Summary

This paper introduces a **multi-class N-pair loss objective** as a more effective alternative to the traditional **triplet loss** in deep metric learning. The core idea is to train an embedding function that ensures the **anchor-positive** pair is closer than the anchor to **N-1 negative** examples in a single optimization step.

This method:

* Increases training efficiency
* Uses supervision more effectively
* Yields improved generalization and retrieval performance compared to contrastive and triplet loss.

---

## Key Concepts

{: .callout-info }

### Multi-class N-pair Loss Objective

Instead of a single anchor-positive-negative triplet, this method uses **N pairs** of samples—each consisting of an anchor and its positive, with the rest of the batch acting as negatives.

{: .callout-success }

### Loss Function

The proposed loss encourages embedding the anchor closer to the positive while pushing it away from **all** negatives:

```math
L = \frac{1}{N} \sum_{i=1}^N \log\left(1 + \sum_{j \neq i} \exp(f(x_i)^T f(x_j^−) - f(x_i)^T f(x_i^+))\right)
```

{: .callout-warning }

### Advantages Over Triplet Loss

* No need for hard-negative mining
* Less sensitive to sampling strategy
* Better performance across classification and retrieval tasks

---

## Application to Internship Work

* Use **N-pair loss** in **facial region embedding** learning to distinguish visual similarity in features like fat pads.
* Embed **left/right side differences** (e.g., cheek fat, under-eye bulge) with strong discriminative representations.
* Improve quantification and scoring models by training on more efficient, **multi-negative contrastive batches**.

---

## Workflow Diagram

```mermaid
graph TD;
  A[Anchor Image] --> B[Positive (Same Class)];
  A --> C1[Negative 1];
  A --> C2[Negative 2];
  A --> CN[Negative N-1];
  B & C1 & C2 & CN --> Loss[N-pair Loss Objective];
```

---

## Code Sketch

```python
# PyTorch version of N-pair loss
import torch
import torch.nn.functional as F

def npair_loss(anchors, positives, negatives):
    anchors = F.normalize(anchors, dim=1)
    positives = F.normalize(positives, dim=1)
    negatives = F.normalize(negatives, dim=2)  # shape: [N, N-1, D]

    pos_scores = torch.sum(anchors * positives, dim=1, keepdim=True)  # [N, 1]
    neg_scores = torch.bmm(negatives, anchors.unsqueeze(2)).squeeze(2)  # [N, N-1]

    logits = neg_scores - pos_scores
    loss = torch.mean(torch.log1p(torch.sum(torch.exp(logits), dim=1)))
    return loss
```

---

## Reflections

> *"Training with N-pair loss made the embeddings more reliable—especially when separating nuanced features like cheek bulges or under-eye bags. It made annotation-efficient training practical for our facial fat pad quantification task."*

**Takeaways:**

* Metric learning shines when training data is small or fine-grained
* Loss functions like N-pair enable more **reliable feature embedding**
* Perfect for tasks requiring **quantitative visual distinction** (e.g., 0.1 vs 0.6 fat score)

---

## References

* [NIPS 2016 Paper PDF](https://papers.nips.cc/paper_files/paper/2016/file/6b180037abbebea991d8b1232f8a8ca9-Paper.pdf)
* [TensorFlow Implementation (Google Research)](https://github.com/tensorflow/models/tree/master/research/delf)
* \[PyTorch Sketches in Metric Learning Repos]



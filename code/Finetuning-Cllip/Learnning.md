# MASTERCLASS: Vision-Language Modeling with CLIP + Custom Architectures in PyTorch

---

### **PHASE 1: FOUNDATION – What are Vision-Language Models?**

####  What is CLIP?

CLIP (**Contrastive Language–Image Pretraining**) by OpenAI learns to connect images and text using **contrastive learning**:

* It encodes **images** and **text** separately into the same vector space
* Trains with a **contrastive loss**: image embeddings should be close to correct text embeddings, far from incorrect ones

#### Real-World Use Cases:

* **Image classification with text prompts**
* **Image search engines**
* **Zero-shot transfer learning**
* **VLM + MLP for custom predictions** (just like we’re building!)

---

### **PHASE 2: CODE EXPLAINED – Line by Line**

#### 1. Load CLIP and Freeze Vision Encoder

```python
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
vision_encoder = model.vision_model
for param in vision_encoder.parameters():
    param.requires_grad = False
```

We’re freezing CLIP’s vision backbone to **avoid updating it during training** (common practice for small datasets)

#### 2. Process Image Input

```python
inputs = processor(images=image, return_tensors="pt").to(device)
```

* `processor` handles resizing, normalization, etc., for CLIP
* Output: image tensor formatted correctly for the model

#### 3. Extract Features from Vision Encoder

```python
vision_outputs = vision_encoder(**inputs)
pooled_output = vision_outputs.pooler_output
```

* `pooled_output`: `[1, 768]` embedding of the image (like BERT's CLS token)

---

### **PHASE 3: CUSTOM ARCHITECTURE – MLP Head**

We defined a lightweight classifier:

```python
class VLMtoMLP(nn.Module):
    def __init__(self, input_dim=768, hidden_dim=256, output_dim=2):
```

This MLP learns to classify based on CLIP's visual understanding

**Use cases for your MLP head**:

* Binary classification (e.g., "cat" vs. "dog")
* Custom outputs (e.g., emotion detection from images)
* Small datasets where fine-tuning the whole CLIP is overkill

---

### **PHASE 4: TRAINING LOOP & LOSS**

```python
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(mlp_head.parameters(), lr=1e-4)
```

 Clean and minimal setup!

**Pro Tip**:
Use `scheduler = torch.optim.lr_scheduler.StepLR(...)` for better convergence.

---

### **PHASE 5: PRACTICALS – Build & Train a Real Dataset**

#### Project Idea:

Classify medical images (e.g., normal vs pneumonia) using pre-trained CLIP + your MLP head.

#### Training Loop (Full Dataset)

```python
for epoch in range(num_epochs):
    for image, label in dataloader:
        inputs = processor(images=image, return_tensors="pt").to(device)
        with torch.no_grad():
            pooled_output = vision_encoder(**inputs).pooler_output
        
        logits = mlp_head(pooled_output)
        loss = criterion(logits, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

---

### **PHASE 6: ADVANCED LEARNING – Expand Your Expertise**

#### Fine-Tune the Entire CLIP Model

Unfreeze later layers:

```python
for name, param in vision_encoder.named_parameters():
    if "layer11" in name or "layer10" in name:  # last 2 layers
        param.requires_grad = True
```

#### Add Text Input to Fuse Image + Text

Use `CLIPModel.forward(input_ids, pixel_values)` with text + image to do **multi-modal classification**.

#### Go Beyond:

* Use `CLIPModel.get_image_features()` and `get_text_features()`
* Try `SigLIP`, `BLIP`, or `CLIP-ViT-L` models
* Integrate with `gradio` or `streamlit` to build apps

---

### **PHASE 7: EXERCISES TO MASTER CONCEPTS**

| Task                        | Description                                     |
| ------------------------------ | ----------------------------------------------- |
| Investigate `CLIPProcessor` | Understand how it preprocesses images           |
| Write Custom DatasetLoader | Load and label images from folders              |
| Build Training Dashboard    | Use `matplotlib` or `TensorBoard`               |
| Zero-Shot Classifier        | Use CLIP without training for few-shot learning |
| Add Text Branch             | Combine image and text inputs using CLIP        |

---

### Recommended Learning Resources

* [CLIP Documentation](https://huggingface.co/docs/transformers/model_doc/clip)
* [Andrej Karpathy’s Neural Network Playlist](https://www.youtube.com/c/AndrejKarpathy)
* [CLIP Paper – “Learning Transferable Visual Models From Natural Language Supervision”](https://arxiv.org/abs/2103.00020)
* Hands-on projects: [PapersWithCode CLIP Projects](https://paperswithcode.com/method/clip)

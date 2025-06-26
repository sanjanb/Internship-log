#  Week 01 – Internship Progress Log

**Week**: 01  
**Dates**: 2025-05-25 – 2025-06-01  
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.  
**Mentor**: Praveen Kulkarni sir

---

## Goals for the Week

- Perform unsupervised pretraining on the MNIST dataset using an autoencoder
- Fine-tune the pretrained encoder for binary classification (even vs. odd digits)
- Evaluate both models and report their performance

---

## Tasks Completed

| Task                                                               | Status       | Notes                                                                 |
|--------------------------------------------------------------------|--------------|-----------------------------------------------------------------------|
| Loaded MNIST dataset using `torchvision.datasets`                  | ✅ Completed  | Used PyTorch DataLoader for efficient batching                       |
| Built encoder-decoder architecture for autoencoder pretraining     | ✅ Completed  | Applied ReLU activations and trained with MSE loss                   |
| Implemented early stopping during autoencoder training             | ✅ Completed  | Avoided overfitting using validation loss threshold                  |
| Saved pretrained encoder model                                     | ✅ Completed  | Model checkpoint saved in `.pt` format                               |
| Built binary classifier using pretrained encoder                   | ✅ Completed  | Added fully connected layer for even/odd classification              |
| Fine-tuned classifier using labeled MNIST                          | ✅ Completed  | Used BCEWithLogitsLoss; improved performance with frozen encoder     |
| Evaluated both models and generated classification report          | ✅ Completed  | Accuracy ~98%, Confusion matrix plotted                              |
| Documented use cases where pretraining outperforms direct training | ✅ Completed  | Reported better feature extraction and convergence benefits          |

---

## Key Learnings

- Unsupervised pretraining helps in learning compact and meaningful representations
- Freezing encoder layers can stabilize training and reduce overfitting
- Fine-tuning on a simpler task (even vs. odd) benefits from prior unsupervised knowledge
- Early stopping and regularization are crucial to prevent overfitting

---

## Problems Faced & Solutions

| Problem                                           | Solution                                                            |
|--------------------------------------------------|---------------------------------------------------------------------|
| Overfitting during unsupervised pretraining      | Applied early stopping and dropout layers                          |
| Poor accuracy in initial fine-tuning attempts    | Froze encoder layers and adjusted learning rate                    |
| Difficulty in even/odd labeling from digit labels | Mapped digit labels programmatically (0,2,4,6,8 as 0; 1,3,5,7,9 as 1) |
| Unclear performance difference                   | Added visualizations, confusion matrix, and precision/recall scores|

---

## 📎 Links

- [MNIST Dataset Reference](https://pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html)
- [Autoencoder Guide (PyTorch)](https://www.geeksforgeeks.org/autoencoders/)
- [EarlyStopping Callback](https://pytorch-lightning.readthedocs.io/en/stable/api/pytorch_lightning.callbacks.EarlyStopping.html)

---

## Goals for Next Week

- Begin exploring ComfyUI for synthetic biometric generation
- Implement visual transformations using masking and prompts
- Compare facial realism across tools like InvokeAI and Replicate

---

## 📸 Screenshots (Optional)

> Add architecture diagram of the encoder, training graphs, confusion matrix

---

> _"Week one showed me how powerful representation learning is. Pretraining builds intuition the model can trust."_  


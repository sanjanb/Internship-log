#  Week 02 

**Week**: 02  
**Dates**: 2025-06-01 – 2025-06-07 
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.  
**Mentor**: Praveen Kulkarni sir

---

## Goals for the Week

- Generate fake biometric images using ComfyUI
- Add synthetic features (black line, scar) to facial images
- Explore alternative generation tools: InvokeAI, Automatic1111, Replicate
- Create human-like facial outputs with node workflows and prompt tuning

---

## Tasks Completed

| Task                                                                 | Status       | Notes                                                               |
|----------------------------------------------------------------------|--------------|---------------------------------------------------------------------|
| Generated biometric-style face (no specs, neutral pose) using ComfyUI | ✅ Completed  | Used prompts with facial constraints                                |
| Added black line to face image programmatically                     | ✅ Completed  | Used Python & OpenCV                                                |
| Designed prompt to replace black line with a scar                   | ✅ Completed  | Implemented via Stable Diffusion inpainting                         |
| Explored and compared generation tools (ComfyUI, InvokeAI, etc.)    | ✅ Completed  | Identified potential of each tool for future workflows              |
| Built workflow to enhance facial details using nodes in ComfyUI     | ✅ Completed  | Achieved realistic results through graph-based pipeline             |

---

## Key Learnings

- ComfyUI workflows can be fine-tuned for biometric and facial realism
- Stable Diffusion inpainting + ControlNet enables creative control
- Multiple tools offer trade-offs: use what fits the goal & complexity
- Consistency in output quality can be handled by systemized pipelines

---

## Problems Faced & Solutions

| Problem                                                            | Solution                                                                 |
|---------------------------------------------------------------------|--------------------------------------------------------------------------|
| Lack of realism in generated faces                                  | Switched models, explored more humanistic face generation                |
| Workflow getting too reliant on one tool                            | Expanded exploration to InvokeAI, A1111, Replicate                       |
| Prompt not giving desired scar effect                               | Tweaked prompts and used ControlNet with mask editing in ComfyUI         |
| Unclear consistency between runs                                    | Discussed with mentor about future integration with AI stack team       |

---

## 📎 Links

- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [ControlNet Guide](https://github.com/lllyasviel/ControlNet)
- [InvokeAI](https://github.com/invoke-ai/InvokeAI)
- [Automatic1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Replicate API](https://replicate.com/)

---

## Goals for Next Week

- Implement Hugging Face login flow with Gradio
- Show user identity after Google login
- Fix environment issues in Spaces (Python version, OAuth vars)

---

## 📸 Screenshots (Optional)

> Add before/after images, mask editor view, scar rendering outputs

---

> _"This week taught me that tool flexibility matters as much as skill depth—great workflows come from trying, tweaking, and switching when needed."_


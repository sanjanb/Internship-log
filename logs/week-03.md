# Week 3 – Internship Progress Log

**Week**: 03  
**Dates**: June 15, 2025 – June 22, 2025 
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.
**Mentor**: Praveen Kulkarni sir.

---

## Goals for the Week

- Set up local and cloud development environments
- Understand Hugging Face Spaces and OAuth login system
- Deploy first working Gradio interface with login button
- Begin learning how to customize Label Studio deployment

---

## Tasks Completed

| Task                                             | Status  | Notes |
|--------------------------------------------------|---------|-------|
| Set up Python virtual environment & tools        | ✅ Done | Fixed PowerShell errors with correct activation |
| Explored Hugging Face Space OAuth docs           | ✅ Done | Read [docs](https://huggingface.co/docs/hub/spaces-oauth) |
| Added `LoginButton` using Gradio Blocks          | ✅ Done | Implemented with basic `OAuthProfile` usage |
| Configured metadata in `README.md`               | ✅ Done | Enabled `hf_oauth`, set proper `sdk_version`, etc. |
| Troubleshot Docker build errors                  | ✅ Done | Corrected Python version mismatch & metadata errors |
| Attempted Label Studio deployment via Docker     | ⚠️ Partial | Facing `/data` permission issues |

---

## Key Learnings

- Difference between `OAuthToken` and `OAuthProfile`
- How to properly configure Hugging Face metadata
- Understanding of Docker container permissions
- Gradio event handling for login flow

---

## Problems Faced & Solutions

| Problem                                     | Solution                                |
|--------------------------------------------|------------------------------------------|
| `source env/bin/activate` failed on Windows| Used `.\env\Scripts\Activate.ps1` instead |
| `OAUTH_CLIENT_ID not set` error            | Fixed with `hf_oauth: true` in metadata |
| Docker: `Permission denied: '/data'`       | Need to use HF persistent storage or custom volume |
| `OAuthProfile` missing `.email` or `.sub`  | Switched to `.username` & `.name` fields |

---

## 📎 Links

- [OAuth Login Demo Space (private)](https://huggingface.co/spaces/your-username/your-space-name)
- [Related GitHub Repo](https://github.com/your-username/your-project)

---

## Goals for Week 2

- Finalize Label Studio setup using persistent storage
- Integrate login-controlled access for different features
- Start documenting how interns can replicate the setup

---

## 📸 Screenshots (Optional)

> Add screenshots or demo GIFs here

---

> 🗒️ _"Week 1 was mostly setup-focused, but I now have a solid grip on the core tech stack and the Hugging Face environment."_  


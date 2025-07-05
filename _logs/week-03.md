---
layout: default
title: Week 03
parent: Weekly Logs
nav_order: 3
---

# Week 03 – Gradio OAuth, Docker & Label Studio Setup

**Dates**: June 15, 2025 – June 22, 2025  
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.  
**Mentor**: Praveen Kulkarni Sir

---

{: .callout-info }
### Focus
This week was centered around setting up development environments, implementing OAuth-based login via Gradio in Hugging Face Spaces, and debugging Label Studio deployment.

---

## Goals for the Week

- Set up local and cloud development environments
- Understand Hugging Face Spaces and OAuth login system
- Deploy first working Gradio interface with login button
- Begin learning how to customize Label Studio deployment

---

## Tasks Completed

| Task                                             | Status       | Notes                                                     |
|--------------------------------------------------|--------------|-----------------------------------------------------------|
| Set up Python virtual environment & tools        | ✅ Completed  | Fixed PowerShell errors with correct activation script     |
| Explored Hugging Face Space OAuth docs           | ✅ Completed  | Referenced [Spaces OAuth Guide](https://huggingface.co/docs/hub/spaces-oauth) |
| Added `LoginButton` using Gradio Blocks          | ✅ Completed  | Implemented using `OAuthProfile` input object             |
| Configured metadata in `README.md`               | ✅ Completed  | Enabled `hf_oauth`, set `sdk_version`, and updated fields |
| Troubleshot Docker build errors                  | ✅ Completed  | Fixed Python version mismatch, adjusted README configs     |
| Attempted Label Studio deployment via Docker     | ⚠️ Partial    | Encountered `/data` permission issues                     |

---

## Key Learnings

{: .callout-success }
- Difference between `OAuthToken` (for private API access) and `OAuthProfile` (for display info)
- How to write a valid `README.md` to configure Hugging Face Spaces (OAuth, Python version, etc.)
- Handling platform-specific issues (e.g., Windows virtualenv vs. POSIX shells)
- Basics of Docker permission handling and volume management for apps like Label Studio

---

## Problems Faced & Solutions

| Problem                                       | Solution                                                      |
|----------------------------------------------|---------------------------------------------------------------|
| `source env/bin/activate` failed on Windows  | Used `.\env\Scripts\Activate.ps1` for PowerShell              |
| OAuth error: `OAUTH_CLIENT_ID` not set       | Fixed by setting `hf_oauth: true` in `README.md` metadata     |
| Docker permission error on `/data`           | Identified need for HF persistent storage or Docker volumes   |
| Missing profile fields in `OAuthProfile`     | Used `.username` and `.name` instead of unavailable `.email`  |

---

## 📎 References

- [Hugging Face OAuth Guide](https://huggingface.co/docs/hub/spaces-oauth)
- [Gradio LoginButton Docs](https://www.gradio.app/guides/sharing-your-app#o-auth-login-via-hugging-face)
- [Gradio OAuthToken vs OAuthProfile](https://www.gradio.app/docs/loginbutton)
- [Related GitHub Repo](https://github.com/your-username/your-project)

---

## Goals for Next Week

- Finalize Label Studio setup using persistent storage
- Integrate user access control for login-specific features
- Create documentation for replicating OAuth-enabled setup

---

## Screenshots (Optional)

> Add screenshot of the login-enabled Gradio Space, Docker error log, and permission setup changes.

---

{: .callout }
_“This week built the foundation for all user-authenticated workflows and taught me how to navigate cross-platform issues and Docker-related edge cases.”_

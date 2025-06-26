#  Week 02 – Internship Progress Log

**Week**: 02  
**Dates**: 2025-06-08 – 2025-06-14  
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.  
**Mentor**: Pradeep Kulkarni sir

---

## Goals for the Week

- Explore Hugging Face Spaces and OAuth flow
- Implement login button using Gradio in a Hugging Face Space
- Display user info after Google/HF login

---

## Tasks Completed

| Task                                                 | Status     | Notes                                    |
|------------------------------------------------------|------------|------------------------------------------|
| Read Hugging Face OAuth docs                         | ✅ Completed | Understood login flow and scopes         |
| Set up basic Gradio login button in Space            | ✅ Completed | Tested with `hf_oauth: true`             |
| Display username and HF ID on login                  | ✅ Completed | Used `gr.OAuthProfile`                   |
| Fixed Python version issues in Space config          | ✅ Completed | Corrected from `python 3.1` to `3.10`    |
| Investigated Label Studio deployment errors          | ✅ Completed | Permission issue with `/data` resolved   |

---

## Key Learnings

- How Hugging Face Spaces use Gradio’s `gr.LoginButton()` for authentication
- Role of environment variables in OAuth (`OAUTH_CLIENT_ID`, etc.)
- Handling common Docker and permission issues on HF

---

## Problems Faced & Solutions

| Problem                                      | Solution                                           |
|---------------------------------------------|----------------------------------------------------|
| OAuth error – `OAUTH_CLIENT_ID` missing     | Enabled `hf_oauth: true` in README.md              |
| Wrong Python version (`3.1` not found)      | Fixed `python_version: 3.10` in README config      |
| `OAuthProfile` missing attributes like `.email` | Used available fields like `.name` and `.username` |
| Label Studio: Permission denied on `/data`  | Noted to use persistent storage or correct `DATA_DIR` env var |

---

## 📎 Links

- [Hugging Face Space (Login Demo)](https://huggingface.co/spaces/your-username/login-demo)
- [OAuth Reference](https://huggingface.co/docs/hub/spaces-oauth)

---

## Goals for Next Week

- Improve login flow UI with logout and refresh
- Work on real-time updates or logged-in features
- Start integrating project-specific APIs post-login

---

## 📸 Screenshots (Optional)

> Add screenshots of working login UI, HF profile rendering, error traces resolved, etc.

---

> _"Every error taught me something new about OAuth, Docker, and deploying production-ready Spaces."_

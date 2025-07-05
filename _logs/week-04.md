---
layout: default
title: Week 04
parent: Weekly Logs
nav_order: 4
---

# Week 04 – OAuth Integration & Space Debugging

**Dates**: 2025-06-23 – 2025-06-30  
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.  
**Mentor**: Praveen Kulkarni Sir

---

{: .callout-info }
### Focus
This week involved implementing a working OAuth login experience in Hugging Face Spaces using Gradio and resolving technical deployment issues like Python versions and Label Studio permissions.

---

## Goals for the Week

- Explore Hugging Face Spaces and OAuth flow
- Implement login button using Gradio in a Hugging Face Space
- Display user identity after login with Google/HF credentials

---

## Tasks Completed

| Task                                                 | Status       | Notes                                     |
|------------------------------------------------------|--------------|-------------------------------------------|
| Read Hugging Face OAuth docs                         | ✅ Completed  | Understood login flow and scopes          |
| Set up basic Gradio login button in Space            | ✅ Completed  | Used `LoginButton()` with `hf_oauth: true` |
| Display username and HF ID after login               | ✅ Completed  | Accessed data via `OAuthProfile` object   |
| Fixed Python version issues in Space config          | ✅ Completed  | Replaced `python_version: 3.1` with `3.10` |
| Investigated Label Studio deployment errors          | ✅ Completed  | Found permission issues on `/data` volume |

---

## Key Learnings

{: .callout-success }
- Hugging Face OAuth is easy to set up using `LoginButton()` and metadata config
- Environment variables (e.g., `OAUTH_CLIENT_ID`) must be managed through Space config
- Docker containers need explicit write permissions for persistent volumes
- Matching Python versions in README prevents HF build errors

---

## Problems Faced & Solutions

| Problem                                        | Solution                                               |
|-----------------------------------------------|--------------------------------------------------------|
| OAuth error: `OAUTH_CLIENT_ID` missing         | Enabled `hf_oauth: true` in `README.md`                |
| Wrong Python version (`3.1` not supported)     | Changed to `python_version: 3.10`                      |
| `OAuthProfile` missing expected fields         | Used `.name`, `.username` instead of `.email`          |
| Label Studio permission denied on `/data`      | Considered using HF Persistent Storage or setting envs |

---

## 📎 References

- [Login Demo Space](https://huggingface.co/spaces/your-username/login-demo)
- [OAuth Config Docs](https://huggingface.co/docs/hub/spaces-oauth)

---

## Goals for Next Week

- Add logout functionality and refresh detection to UI
- Begin API integration for user-specific actions post-login
- Set up secure Label Studio storage configuration

---

## Screenshots (Optional)

> Include interface login, authenticated profile, and HF build fixes if available.

---

{: .callout }
_“Every error this week became a stepping stone to mastering OAuth, container environments, and platform-specific configs.”_

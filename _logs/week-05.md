---
layout: default
title: Week 05
parent: Weekly Logs
nav_order: 5
---

# Week 05 – Site Design, Jekyll Themes & Visual Enhancements

**Dates**: 2025-07-01 – 2025-07-07  
**Internship**: AI/ML Intern at SynerSense Pvt. Ltd.  
**Mentor**: Praveen Kulkarni Sir

---

{: .callout-info }
### Focus
This week focused on enhancing the internship documentation website by integrating a new theme (`just-the-docs`), applying custom styles, callouts, Mermaid diagrams, and preparing it for long-term use and readability.

---

## Goals for the Week

- Improve GitHub Pages interface using the Just the Docs theme
- Add custom styles, callouts, Mermaid diagrams, and banners
- Organize internship logs with navigation and search
- Set up a more expressive and accessible documentation layout

---

## Tasks Completed

| Task                                                  | Status       | Notes                                                           |
|-------------------------------------------------------|--------------|-----------------------------------------------------------------|
| Migrated site to `just-the-docs` Jekyll theme         | ✅ Completed  | Applied remote theme with `jekyll-remote-theme`                |
| Configured sidebar navigation using `navigation.yml`  | ✅ Completed  | Indexed weeks under “Weekly Logs” section                      |
| Enabled custom SCSS styling for callout visibility    | ✅ Completed  | Ensured dark theme compatibility with readable colors          |
| Added homepage banner and visual structure            | ✅ Completed  | Responsive image support with fallback checks                  |
| Tested Mermaid diagram rendering in markdown          | ✅ Completed  | Enabled Mermaid v9.4.3 in `_config.yml`                        |
| Fixed asset path issues (`/assets/...`)               | ✅ Completed  | Used `site.baseurl` for consistent loading                     |

---

## Key Learnings

{: .callout-success }
- Learned full configuration of GitHub Pages using Jekyll + custom SCSS
- Understood how themes handle layouts, nav orders, and permalinks
- Enabled scripting and diagramming tools like Mermaid.js for visual flow
- Became comfortable with `_config.yml`, front matter, and theme customization

---

## Problems Faced & Solutions

| Problem                                             | Solution                                                      |
|-----------------------------------------------------|---------------------------------------------------------------|
| Callout text invisible in dark mode                 | Overrode `.callout-*` SCSS with accessible background colors  |
| Mermaid diagrams not rendering                      | Enabled proper version and checked markdown compatibility     |
| Image not loading on hosted site                    | Fixed baseurl path using `{{ site.baseurl }}`                 |
| Theme build failed (`just-the-docs` not found)      | Used `remote_theme` correctly, not as a gem-based theme       |

---

## 📎 References

- [Just the Docs Theme](https://just-the-docs.com/)
- [Mermaid Docs](https://mermaid.js.org/)
- [Jekyll GitHub Pages Guide](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)
- [Custom SCSS Callouts](https://just-the-docs.com/docs/customization/#callouts)

---

## Goals for Next Week

- Add custom components like badges, tabs, or cards to logs
- Integrate reusable templates for each log page
- Finalize mobile responsiveness and visual polish

---

## Screenshots (Optional)

> Include: Banner view, Mermaid graph preview, dark-mode callouts comparison

---

{: .callout }
_“This week’s progress turned my raw logs into a well-organized documentation platform — and gave me the confidence to build developer-friendly websites from scratch.”_

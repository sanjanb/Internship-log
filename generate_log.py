# generate_log.py

import os
from datetime import datetime, timedelta

WEEK_NUMBER = input("Enter week number (e.g., 02): ").zfill(2)
start_date = input("Start date (e.g., 2025-06-08): ")
end_date = input("End date (e.g., 2025-06-14): ")

file_path = f"logs/week-{WEEK_NUMBER}.md"

template = f"""#  Week {WEEK_NUMBER} – Internship Progress Log

**Week**: {WEEK_NUMBER}  
**Dates**: {start_date} – {end_date}  
**Internship**: [AI/ML Intern at SynerSense Pvt. Ltd.]  
**Mentor**: [Pradeep Kulkarni sir]

---

## Goals for the Week

- [ ] 
- [ ] 
- [ ] 

---

## Tasks Completed

| Task                              | Status  | Notes |
|-----------------------------------|---------|-------|
|                                   |         |       |
|                                   |         |       |

---

## Key Learnings

- 
- 

---

## Problems Faced & Solutions

| Problem      | Solution     |
|--------------|--------------|
|              |              |

---

## 📎 Links

- [Related Repo]()
- [Space Link]()

---

## Goals for Next Week

- [ ] 
- [ ] 

---

## 📸 Screenshots (Optional)

> Add screenshots here

---

> _"Week {WEEK_NUMBER} summary quote or reflection here."_
"""

os.makedirs("logs", exist_ok=True)
with open(file_path, "w", encoding="utf-8") as file:

    file.write(template)

print(f"Log created: {file_path}")

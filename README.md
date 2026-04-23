# 🔐 AI Kill Chain Monitor  
### Human-Guided AI Cybersecurity Testing System

A hybrid cybersecurity assessment framework that combines **AI-driven automation** with **human decision-making** to perform safe, efficient, and accurate vulnerability testing. The system follows a structured *kill chain approach* including scanning, validation, prioritization, and reporting.

---

## 🚀 Features

- 🔍 Smart port scanning using Nmap  
- 🧠 AI-inspired risk tagging (rule-based for now)  
- ⚠️ Severity classification (High / Medium / Low)  
- 🧩 Modular architecture (scanner, validator, reporting)  
- 📊 Structured JSON output for easy integration  
- 🛡️ Human-in-the-loop validation for safer testing  

---

## 🏗️ System Workflow

1. **Setup & Planning** – Define target system  
2. **Smart Scanning** – Discover ports and services  
3. **Validation** – Remove duplicates & classify risks  
4. **Prioritization** – Assign severity levels  
5. **Reporting** – Generate structured results  

---

## ⚙️ Tech Stack

- **Backend:** FastAPI  
- **Scanning Tool:** Nmap  
- **Language:** Python  
- **API Testing:** Swagger UI  

---

## 📁 Project Structure

ai-kill-chain/

│
├── main.py # FastAPI app

├── scanner.py # Phase 2: Scanning logic

├── validator.py # Phase 3: Validation & severity

├── models.py # Input schema

├── data/

│ └── scan_results.json

├── requirements.txt

└── README.md

🎯 Key Concepts Implemented

1. Human-Guided AI Decision Model
2. Vulnerability Discovery & Analysis
3. Risk Prioritization
4. Modular Backend Design
5. Ethical & Controlled Testing Approach
   
🔮 Future Scope

1. 🤖 Integrate ML/AI models for smarter detection
2. ☁️ Cloud-based scanning support
3. 📊 Dashboard with visual analytics
4. 🛡️ Real-time monitoring system
5. 📄 Automated PDF report generation

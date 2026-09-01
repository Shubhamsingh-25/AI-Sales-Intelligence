# 🤖 AI Sales Intelligence Dashboard

An interactive **AI-powered Sales Intelligence Dashboard** built with Python, Streamlit, Pandas, Plotly and Google Gemini.

The dashboard transforms sales data into actionable business insights through interactive analytics, performance tracking, visualizations and AI-powered analysis.

---

## 🚀 Live Demo

👉 **[Open AI Sales Intelligence Dashboard](https://ai-sales-intelligence.streamlit.app/)**

You can open and explore the live dashboard directly in your browser without installing anything.

---

## 📊 Dashboard Preview

![AI Sales Intelligence Dashboard](AI_Sales_dash.png)

---

## ✨ Key Features

### 📈 Sales Performance Analytics

Track important business KPIs including:

- 💰 Primary Sales
- 🛒 Secondary Sales
- 🎯 Achievement %
- 📦 Orders
- 📊 Units Sold
- 📋 Sales Records

---

### 🎛️ Interactive Dashboard Filters

Users can dynamically analyze the sales data using multiple filters:

- 📅 Date Range
- 👤 Employee
- 🌎 Region
- 📍 State
- 📦 Category
- Other available business dimensions

The dashboard automatically updates the analysis based on the selected filters.

---

## 🧠 AI Sales Intelligence

The dashboard includes an AI-powered business analysis layer using **Google Gemini**.

Users can ask business questions and receive data-driven insights based on the currently filtered sales data.

### ⚡ Quick AI Analysis

The dashboard provides predefined AI analysis options such as:

- 📊 Executive Summary
- ⚠️ Find Risks
- 🚀 Find Opportunities
- 🎯 Target Analysis

Users can also enter their own business questions and ask the AI to analyze the filtered sales data.

---

## 📊 Interactive Visualizations

The dashboard uses interactive **Plotly** visualizations to analyze sales performance across different business dimensions.

Users can explore trends, comparisons and performance patterns through interactive charts.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🎈 Streamlit | Interactive dashboard application |
| 🐼 Pandas | Data processing and analysis |
| 📊 Plotly | Interactive data visualizations |
| 🧠 Google Gemini | AI-powered sales intelligence |
| 📗 Excel | Sales dataset / data source |

---

## 📁 Project Structure

```text
AI-Sales-Intelligence/
│
├── 📂 Data/
│   └── AI_Sales_Intelligence_Dataset.xlsx
│
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 README.md
└── 🖼️ AI_Sales_dash.png
```

---

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Shubhamsingh-25/AI-Sales-Intelligence.git
```

### 2. Open the project

```bash
cd AI-Sales-Intelligence
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 🔐 Gemini API Configuration

The AI functionality uses a **Google Gemini API key**.

For security, the API key should **never be hard-coded into the source code or committed to GitHub**.

For Streamlit deployment, configure the API key through **Streamlit Secrets**.

Example:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

---

## 💡 How It Works

```text
Sales Data
    ↓
Data Processing
    ↓
Interactive Filters
    ↓
Sales KPIs & Visualizations
    ↓
Filtered Business Data
    ↓
Google Gemini AI
    ↓
Business Insights
    ↓
Risks • Opportunities • Recommendations
```

---

## 🎯 Project Objective

The objective of this project is to combine **traditional sales analytics with Generative AI** to create an interactive business intelligence solution.

Instead of only displaying historical numbers, the dashboard allows users to explore the data and ask AI-driven questions to understand:

- What is happening?
- Why is performance changing?
- What are the major business risks?
- Where are the opportunities?
- What actions should management consider?

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud** and connected directly to the GitHub repository.

### Live Application

👉 **[AI Sales Intelligence Dashboard](https://ai-sales-intelligence.streamlit.app/)**

---

## 👨‍💻 Author

### Shubham Singh

AI Sales Intelligence Dashboard

Built with **Python • Streamlit • Pandas • Plotly • Google Gemini**

---

⭐ If you find this project useful, consider giving the repository a **Star**.

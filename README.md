## 🧠 Agentic ML Assistant

An intuitive, agent-powered ML assistant that enables non-technical users to:
- Explore datasets
- Clean and transform data
- Get ML model recommendations
- Split data and generate synthetic datasets
- Visualize results — all through a simple web UI

Built with Python, Streamlit, and OpenAI.

---

### 🔧 Features

| Task | Description |
|------|-------------|
| 📊 Plot Chart | Select X/Y columns from any CSV and generate visual plots |
| 🧼 Clean Dataset | Drop null-heavy columns, fill missing values, encode categorical columns |
| 🧾 Feature Summary | View per-column type, nulls, and stats (mean, std, etc.) |
| 🧠 Model Suggestion (LLM) | Use GPT to suggest models based on natural-language problem descriptions |
| ✂️ Train/Test Split | Split dataset with user-defined features/target and ratio |
| 🧪 Generate Synthetic Data | Create mock datasets based on schema and row count |

---

### 🖥️ UI Snapshot

Built with **Streamlit**, the UI supports:

✅ File upload + preview  
✅ Task selection with dynamic forms  
✅ Instant feedback and result previews  
✅ Automatic interaction history tracking in sidebar

---

### 📁 Folder Structure

```
agenticai/
├── app.py                  # Streamlit UI
├── main.py                 # Agentic Python functions
├── metadata.json           # Trigger metadata for each agent
├── requirements.txt        # All dependencies
├── sample_*.csv            # Sample datasets for demo
└── output files            # Plots, splits, cleaned data etc.
```

---

### ⚙️ Setup Instructions

1. **download the project**

```bash
cd agenticai
```

2. **Install dependencies**

```bash
py -3.11 -m venv MRUDULA
source MRUDULA/bin/activate  # On Windows use MRUDULA\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

---

### 🔐 Using the LLM (Optional)

To enable GPT-powered model suggestion, set your OpenAI API key in the secrets section:

```python
secrets = {
    "OPENAI_API_KEY": "sk-xxxxxxxxxx"
}
```

Or set it in terminal:

```bash
export OPENAI_API_KEY=sk-xxxxxxxxxx
```

---

### 📦 Dependencies

- `pandas`
- `matplotlib`
- `scikit-learn`
- `streamlit`
- `openai` (for LLM suggestions)

---

### 🙌 Credits

Developed by **Mrudula**  
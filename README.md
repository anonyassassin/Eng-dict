# ⚙️ Engineering Dictionary

A terminal-based engineering reference tool powered by the **Groq API** and **LLaMA 3.1**. Enter any engineering concept and get a structured, professional breakdown instantly — streamed live in your terminal with rich markdown formatting.

---

## ✨ Features

- 🔍 **Instant definitions** for any engineering concept, system, or component
- 📐 **Structured output** — every response follows a consistent technical format
- ⚡ **Live streaming** responses rendered in real-time via `rich`
- 🎨 **Rich markdown** formatting with styled terminal output
- 🧠 Powered by `llama-3.1-8b-instant` via Groq's ultra-fast inference

---

## 📋 Output Format

Every concept is explained using this fixed structure:

1. **Summary Paragraph** — 2–3 sentence overview of the concept and its core principle
2. **Core Components** — The 4–5 most vital parts with technical explanations
3. **Auxiliary Components** — Supporting systems that improve efficiency or operation
4. **Efficiency / Conclusion** — Key performance metric or thermal efficiency note

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/engineering-dictionary.git
cd engineering-dictionary
```

### 2. Install dependencies

```bash
pip install groq rich
```

### 3. Set your Groq API key

Get your free API key from [console.groq.com](https://console.groq.com).

**Linux / macOS:**
```bash
export GROQ_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

### 4. Run the app

```bash
python main.py
```

---

## 🖥️ Usage

```
Engineering Dictionary Active. Press Ctrl+C to exit.

Enter the concept: Rankine Cycle
```

Type any engineering concept — thermodynamic cycles, mechanical systems, electrical components, fluid dynamics principles, etc. — and receive a structured breakdown immediately.

Press `Ctrl+C` at any time to exit gracefully.

---

## 📁 Project Structure

```
engineering-dictionary/
├── main.py       # Main application
└── README.md     # This file
```

---

## ⚙️ Configuration

You can tweak the following constants in `main.py`:

| Parameter     | Default                  | Description                          |
|---------------|--------------------------|--------------------------------------|
| `model`       | `llama-3.1-8b-instant`   | Groq model used for inference        |
| `temperature` | `0.2`                    | Lower = more precise, less creative  |
| `max_tokens`  | `500`                    | Maximum response length              |

---

## 📦 Dependencies

| Package | Purpose                              |
|---------|--------------------------------------|
| `groq`  | Groq API client for LLM inference    |
| `rich`  | Terminal markdown rendering & styling |

---

## 📄 License

MIT License — free to use, modify, and distribute.

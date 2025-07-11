# 🤖 Gemini AI Assistant (Command-Line)

An intelligent command-line assistant powered by **Google's Gemini-Pro API**, designed to interact using prompt engineering principles. Built to answer questions, summarize text, create stories or poems, and provide actionable advice — all from your terminal!

🔗 **[🎥 Demo Video](https://www.awesomescreenshot.com/video/41304306?key=b8fff6e939ad9492a2a45a30e213ee3b)**

---

## 🚀 Features

- 🔍 **Answer Factual Questions** – Instantly retrieve answers from the Gemini AI model.
- 📚 **Text Summarization** – Get concise summaries of long paragraphs or articles.
- ✨ **Creative Content Generation** – Write poems, stories, or novel ideas with style.
- 💡 **Advice & Tips** – Study hacks, stress management, time organization — just ask!
- 📥 **User Feedback Logger** – Logs all prompts, AI responses, and user feedback into `feedback_log.txt`.

---

## 💻 Tech Stack

- **Language**: Python 3
- **API**: Google AI Studio (Gemini-Pro)
- **Libraries**:
  - [`google-generativeai`](https://pypi.org/project/google-generativeai/)
  - [`python-dotenv`](https://pypi.org/project/python-dotenv/)

---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/Gemini-AI-Assistant-CLI.git
cd Gemini-AI-Assistant-CLI
````

### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Configure Environment**

Create a `.env` file in the root directory and add your API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your key from 👉 [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### 4. **Run the Assistant**

```bash
python assistant.py
```

---

## 🧠 Prompt Categories & Variations

| Category  | Prompt Example                |
| --------- | ----------------------------- |
| Q\&A      | “What is gravity?”            |
| Summarize | “Summarize: \[text]”          |
| Creative  | “Write a poem about courage.” |
| Advice    | “Give study tips for exams.”  |

You can choose from suggested prompts or enter your own custom query.

---

## 📂 Project Structure

```
Gemini-AI-Assistant-CLI/
├── assistant.py
├── .env                # Not tracked in Git
├── feedback_log.txt    # All AI responses + feedback
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📄 Feedback Logging Format

Every interaction is saved:

```
=== New Interaction ===
Category     : summarize
User Prompt  : Summarize the following paragraph...
AI Response  : The main idea is...
Feedback     : yes
```

---

## ✍️ Author

**Saket Chaudhary**
🔗 [LinkedIn](https://www.linkedin.com/in/saket-chaudhary22)
📧 [saketrishu64821@gmail.com](mailto:saketrishu64821@gmail.com)

---

## 📌 License

This project is open-source and available under the [MIT License](LICENSE).

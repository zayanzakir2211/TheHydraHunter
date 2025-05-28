# 🔍 The Hydra Hunter

The Hydra Hunter is an **OSINT (Open Source Intelligence)** tool written in Python that helps gather publicly available information about a target using Bing. It generates a neat HTML report containing the discovered links, including potential results from popular social media platforms.

---

## 📦 Features

- 🌐 Searches public data using Bing search engine
- 📱 Includes queries across major social platforms
- 📝 Generates an organized, clickable HTML report
- 🎯 Lets you set a custom report filename
- 🧠 Easy to use CLI interface

---

## 🛠 Requirements

- Python 3.6 or higher
- Internet connection

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python thehydrahunter.py
```

You will be prompted to input:

- **Full name** of the target  
- **Country**  
- **Home town**  
- **Optional**: custom report filename (e.g. `report.html`)  

An **HTML report** will be saved in the current directory.

---

## 📁 Sample Output

Example filename:

```
hydra_report_John_Doe.html
```

Open it in your browser to view all the discovered links categorized by search queries.

---

## 🧪 Sample Search Queries

- `"John Doe" "United States" "New York"`
- `"John Doe" site:facebook.com`
- `"John Doe" site:instagram.com`
- ...and many more!

---

## ⚠️ Legal Notice

This tool is for **educational and ethical use only**.  
Do **not** use it for harassment, stalking, or any illegal activity.  
The creator is **not responsible** for any misuse of this tool.

Always comply with your local laws when using OSINT tools.

---

## 🤝 Contributing

Pull requests and forks are welcome!  
Feel free to improve and extend **The Hydra Hunter**.

---

## 📄 License

This project is licensed under the **MIT License**.

# ✨ Daily Motivation - A Beautiful Streamlit Quotes App

Welcome to **Daily Motivation**, a feel-good Streamlit web app that delivers a daily dose of motivational quotes 🌞. Whether you're looking for inspiration to start your day or just a push to keep going, this app has you covered with randomly generated quotes and the ability to add your own!

![App Screenshot](https://wallpapers.com/images/high/beautiful-dark-night-with-shooting-stars-kc0lgr6rplku557j.webp)

---

## 🌟 Features

- 🎯 **Quote of the Day**: A unique quote based on the current day.
- 🎲 **Random Quote Generator**: Pick a category and get a random motivational quote.
- ✍️ **Add Your Own Quotes**: Share your wisdom or favorite quotes with the world.
- 📁 **Quotes Saved in JSON**: All quotes are stored locally in a `quotes_db.json` file.
- 🎨 **Beautiful UI**: Custom CSS styling with a night-sky background and glowing quote cards.

---

## ✨ Getting Started

### 1. **Clone the Repository**

```bash
git clone https://github.com/muzaffar401/Daily_Motivational_Quotes_App-.git
cd Daily_Motivational_Quotes_App
```

### 2. **Install Dependencies**

You need Python 3.7+ and Streamlit.

```bash
pip install streamlit
```

### 3. **Run the App**

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
daily-motivation-app/
│
├── main.py              # Main Streamlit application file
├── quotes_db.json      # JSON file storing all user and default quotes
├── README.md           # Project documentation (this file)
```

---

## 🧠 How It Works

- All quotes are organized into **categories** inside a single JSON file.
- The app shows a **Quote of the Day** based on the current date using modular logic.
- Users can select a category and generate a **Random Quote** from that group.
- Anyone can contribute by **adding a new quote** via a simple form.
- All quotes are saved using Python’s `json` module and persist even after you close the app.

---

## 🎨 Styling & Customization

The app uses custom HTML/CSS for styling inside Streamlit’s markdown rendering:

- Background: Starry night via a high-quality wallpaper URL
- Quotes: Displayed in a glassmorphic style container with shadows and padding
- Buttons: Animated hover effects with custom color
- Inputs: Styled radio buttons and textarea components

---

## 💡 Example Categories

Here are a few categories you can start with:

- **Success**
- **Perseverance**
- **Mindfulness**
- **Confidence**
- **Hustle**

---

## ✅ To-Do / Future Improvements

- 🔐 Add user authentication
- 📄 Export all quotes to CSV or PDF
- 🌐 Host the app on Streamlit Cloud or HuggingFace Spaces
- 🧠 Add AI-generated quotes using OpenAI or Gemini API
- 🌍 Enable sharing quotes on social media

---

## 🤝 Contributing

Pull requests are welcome! If you have a great quote, UI idea, or new feature suggestion, feel free to fork the repo and submit a PR.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- Developed with ❤️ using [Streamlit](https://streamlit.io)
- Background Image from [Wallpapers.com](https://wallpapers.com)
- Inspired by everyone who needs a little motivation 💪

---

## 🔗 Let's Connect

If you like this project, give it a ⭐ and share it with your friends!

> *"Keep going. Each day brings new strength and new thoughts."* – *Unknown*


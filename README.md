# 🌤 Weather Detector

A clean, responsive weather web app built with **Django** and the **OpenWeatherMap API**. 
Search any city and instantly get live weather data — with a sleek UI and optional dark mode.

---

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Displays temperature, humidity, pressure, coordinates, and description
- 🌙 Dark mode toggle with preference saved via `localStorage`
- ⚠️ Graceful error handling for invalid city names
- 📱 Fully responsive layout
- 🎨 Modern UI with [Tabler Icons](https://tabler.io/icons) and [Inter](https://fonts.google.com/specimen/Inter) font



## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Django |
| Frontend | HTML, CSS (custom), Tabler Icons |
| API | [OpenWeatherMap API](https://openweathermap.org/api) |
| Font | Inter (Google Fonts) |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-detector.git
cd weather-detector
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get an API key

1. Sign up at [openweathermap.org](https://openweathermap.org/)
2. Go to **API keys** in your account dashboard
3. Copy your key

### 5. Configure the API key

Create a `.env` file in the project root (or set it directly in `views.py`):

```env
OPENWEATHER_API_KEY=your_api_key_here
```

### 6. Run migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📁 Project Structure

```
weather-detector/
├── weather/
│   ├── templates/
│   │   └── weather/
│   │       └── index.html      # Main UI template
│   ├── views.py                # Handles API requests and rendering
│   ├── urls.py
│   └── models.py
├── weatherapp/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🌐 API Response Fields

The app displays the following data from the OpenWeatherMap API:

| Field | Description |
|---|---|
| `country_code` | Country abbreviation (e.g. `IN`) |
| `coordinate` | Latitude and longitude |
| `temp` | Current temperature |
| `pressure` | Atmospheric pressure in hPa |
| `humidity` | Relative humidity percentage |
| `description` | Weather condition summary |

---

## 🎨 UI Highlights

- **Search bar** — pill-shaped input with a live search button
- **Weather card** — tinted header with a large weather icon, city name, and country badge
- **Data rows** — each stat has a contextual icon and clean label/value layout
- **Dark mode** — toggled via a navbar button; preference persists across sessions using `localStorage`
- **Error alert** — styled red banner shown for unknown or misspelled city names

---

## 📦 requirements.txt

```
Django>=4.0
requests>=2.28
python-dotenv>=1.0
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

---



## 👨‍💻 Author

Made with ☁️ by dev-lov-oper

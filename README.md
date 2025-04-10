# Supplier Risk Dashboard

## What's This About?
This is a **Supplier Risk Dashboard** that helps businesses visualize how risky their suppliers are based on current news. The idea is to analyze news from suppliers' countries and calculate a risk score. The dashboard shows a map with each supplier’s location, and the colors of the markers change based on their risk score.

## Features
- **Interactive map**: View supplier locations on a world map.
- **Live risk assessment**: Pulls in the latest news from NewsAPI and uses it to assess risk.
- **Risk scoring**: Suppliers get a risk score based on how the news looks (e.g., protests, strikes, delays).

## Technologies I Used
- **Python**: For backend scripting and working with APIs.
- **Dash**: The web framework I used to build the dashboard.
- **Plotly**: To make interactive plots and maps.
- **NewsAPI**: For getting the latest news from different countries.
- **Flask**: To serve the Dash app.

## How to Run It
1. Clone the repo:
    ```bash
    git clone https://github.com/YOUR_USERNAME/supplier-risk-dashboard.git
    ```

2. Go to the project folder:
    ```bash
    cd supplier-risk-dashboard
    ```

3. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Mac/Linux
    ```

4. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the app:
    ```bash
    python dashboard.py
    ```

6. Open your browser and go to `http://127.0.0.1:8050` to see the dashboard.

## API Key
- This app uses **NewsAPI** to get news. You’ll need to grab your own API key from [NewsAPI](https://newsapi.org/).
- Once you get the key, put it in `risk_assessment.py` so the app can start fetching data.

## Contributing
Feel free to fork this repo, submit pull requests, or open issues if you find any bugs or have feature requests!


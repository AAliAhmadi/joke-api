# joke-api
This is a simple Python project that fetches random jokes from different APIs using a clean object-oriented design.

## Structure
joke_project/

├── jokers/

│ ├── base.py # Abstract Joker class

│ ├── joker_a.py # Uses jokeapi.dev

│ ├── joker_b.py # Uses icanhazdadjoke.com

│ └── joker_c.py # Uses api-ninjas.com (API key required)

├── main.py # CLI entry point

└── notebooks/

└── main.ipynb # Interactive demo (optional)



## How to Run

1. **Install dependencies**  
   You need Python 3.7+ and the `requests` library.

   ```bash
   pip install requests

2. **Run the main script**

   ```python main.py```

3. **(Optional): Try the interactive notebook:**

Open ```notebooks/main.ipynb``` in Jupyter or upload to Google Colab.


## API Notes
- `JokerC` requires a free API key from [api-ninjas.com](https://api-ninjas.com/api/jokes).
Add it in the main.py or notebook where marked.

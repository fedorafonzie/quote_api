import requests
URL = 'https://generationterrorists.com/cgi-bin/quotes.cgi?start=50&section=Love+and+Dreams&per_page=50'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    with open("pagina_2_output.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("SUCCESS: HTML van pagina 2 opgeslagen in 'pagina_2_output.html'.")
except Exception as e:
    print(f"FOUT: {e}")
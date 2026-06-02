import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape_headlines():

    # News Website
    url = "https://www.bbc.com/news"

    # User-Agent Header
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        print("Fetching latest headlines...\n")

        response = requests.get(url, headers=headers)

        # Check response
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find headline tags
        headlines = soup.find_all(["h2", "h3"])

        unique_headlines = []

        for headline in headlines:

            text = headline.get_text(strip=True)

            if text and text not in unique_headlines:
                unique_headlines.append(text)

        # Save headlines to file
        with open("headlines.txt", "w", encoding="utf-8") as file:

            file.write("NEWS HEADLINES REPORT\n")
            file.write("=" * 60 + "\n")
            file.write(
                f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
            )

            for index, title in enumerate(unique_headlines, start=1):
                file.write(f"{index}. {title}\n")

        print(f"Successfully saved {len(unique_headlines)} headlines.")
        print("Check headlines.txt file.")

    except requests.exceptions.RequestException as error:

        print("Request Error:")
        print(error)

    except Exception as error:

        print("Unexpected Error:")
        print(error)


if __name__ == "__main__":
    scrape_headlines()
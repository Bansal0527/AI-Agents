# import requests
# from bs4 import BeautifulSoup

# url = "https://timesofindia.indiatimes.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# headlines = soup.find_all('div', class_='headline')
# for headline in headlines[:10]:  # Top 10 headlines
#     print(headline.text.strip())

# import requests
# from bs4 import BeautifulSoup

# r = requests.get("https://timesofindia.indiatimes.com/briefs")
# soup = BeautifulSoup(r.content, 'html5lib')

# headings = soup.find_all('h2')

# headings = headings[0:-13] # removing footer links
# print(headings)


# import requests
# from bs4 import BeautifulSoup

# def scrape_inshorts(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     articles = []
#     for headline, body in zip(
#         soup.find_all('span', itemprop='headline'),
#         soup.find_all('div', itemprop='articleBody')
#     ):
#         articles.append({
#             'title': headline.text.strip(),
#             'content': body.text.strip(),
#             'category': url.split('/')[-1]  # e.g., "national" or "technology"
#         })
#     return articles

# # Example usage
# national_news = scrape_inshorts('https://inshorts.com/en/read/sports')
# print(national_news)


import requests
from bs4 import BeautifulSoup

def scrape_inshorts(category="national"):
    url = f"https://inshorts.com/en/read/{category}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    articles = []
    for card in soup.find_all('div', class_='news-card'):
        title = card.find('span', itemprop='headline').text.strip()
        content = card.find('div', itemprop='articleBody').text.strip()
        image = card.find('div', class_='news-card-image')['style'].split("url('")[1].split("')")[0]
        time = card.find('span', class_='time').text
        articles.append({"title": title, "content": content, "image": image, "time": time})
    
    return articles

# Example: Fetch real-time national news :cite[9]
national_news = scrape_inshorts("national")
print(national_news)
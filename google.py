import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import random

def google_search(keyword):
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'SEARCH_SAMESITE=CgQIuJsB; HSID=A2LoTamyJ9iM4Zt4D; SSID=AiMSI1yNcx_ueaLrx; APISID=wi-frzOi1biL_sZX/A1bp5I6p37hO_mV7v; SAPISID=OvprtPtS2_2tYdWr/A-iDDoThLaLCQSX58; __Secure-1PAPISID=OvprtPtS2_2tYdWr/A-iDDoThLaLCQSX58; __Secure-3PAPISID=OvprtPtS2_2tYdWr/A-iDDoThLaLCQSX58; SID=g.a000mwgk0ATbFYRM8PtDyFMA8NiHr3S83flXUa1OasA7C4V0mxXDD7UCHVE_ZU6si-lkHEd_WAACgYKAZkSARISFQHGX2MiwtArVo_mxzRkY4TzGZDqBxoVAUF8yKowk78Ybvhxn3sxtvxE3W8n0076; __Secure-1PSID=g.a000mwgk0ATbFYRM8PtDyFMA8NiHr3S83flXUa1OasA7C4V0mxXDdLttIQkixNtablPalOQZIAACgYKAV0SARISFQHGX2MisxJVlfEYJbC4lsSO1TwVOxoVAUF8yKqP17iG9tfle93AjfZKsVjp0076; __Secure-3PSID=g.a000mwgk0ATbFYRM8PtDyFMA8NiHr3S83flXUa1OasA7C4V0mxXDUNCbSOnlJWlSKgOmpeUhQAACgYKAQoSARISFQHGX2MiYxuOij9tFJ5Tx0bWElEj9hoVAUF8yKoBjHG0yLOxgFgKLfdcxGNW0076; OGPC=19025003-1:; AEC=AVYB7cp9uyoiPc8uyQQ_Mn-WUbMea7IKKUZJEW-N5j6yMh3mKoDMBEh5x10; NID=516=iPnR8noasYjHaw466-xjWFQGlWm2Eu_BtDiiHlk4-VaK-gdmV5CvVq1MTWXkZNHgYkbGb9-Al9C2WCxoQcGwH85P_0MHQRfiIgve59VyyU42IWqixZ_equrXt37dn5WoUFcY9l_rA5qyuRze63lZvYI-48LSM6uAf0zSFiaW922Qqy-3lYiscJJMXr-ob9Pv7FGMh35WE2clg97jWSuIo4Sf7_ntP8vE2s05XR1lW2euBTBwwmfRBfSCqVd8YDQ25q4rl-6rABT1NuraXjJY38JXniNBdhjMlpua568U1pvSsnGMpPfdNT8NhloJ700D7gQ8w-2gc3kXUFYGb98HgSwHfVwU7nu0JXsam4rA39humcI0UP83R4Zy5QALeq0RyxpXtCQ9NnRgFBUQcJOIM7qTwSe540OPgGSSUT_i_uBX0zh44lf6kZTKx8jXxBhBbIowYgdL9jAyCpIBIk6ReOXEOzial9NANsfd0lwVA3jPtimhufyCQH_LQ-CtspiOTXaJbdmdwtb6DAxFnjdmWkBjDJ9joR_rRAdhla2krzm2vRSTMxbosUqSAOU7aMHAd5p1t9PPx7NJJfepvfoiwhmugmngXqzxboDUj_dFfsF2d9BWakI2DU8f4ItghDbVxln7DnO2m5n9AOLCv8KwB-T8Pj58jIMyAK5LykDyEGUXOjvcmZaJ_QM9JNuMreAv83CH1Rz_C22ibOTzov5Nw0_wS56j2FUh0Z8nHXK1asOwXCZ8X87aa_t8UJ6xRtATNGdJwF7j8-WwCNqs5HuHIFUXWCXhPHhahj6kaxjwPQIBe-PFFaXm5kjLZXv9-5DkDkJihdq2F3OUkfEmzTd_30sRciLDEyZvh_ENcHrSKpmUShl14LCAQd1lxn33eaZkKITS4UaAUgnWZ1mOoueSR50X9JFSRw; __Secure-1PSIDTS=sidts-CjEBUFGohyzUrbgcc0oftymTgkcds7AAFuQSeEV4gOMk__rfFrp09RCxV2sEESSuUnALEAA; __Secure-3PSIDTS=sidts-CjEBUFGohyzUrbgcc0oftymTgkcds7AAFuQSeEV4gOMk__rfFrp09RCxV2sEESSuUnALEAA; DV=8-zSgDMXqkRYUFqe9AjqK6S9zp7FFVmls1cWBzvveAAAANDMM2lHtAn8MAAAAKhfz8hqWLzWFAAAALn1Nrq_BAmKCwAAAA; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNzIzODMxMjg1NDM0MDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IC0yNzg3NTczNzYKICBsb25naXR1ZGVfZTc6IC01NDQ2Njk2OTYKfQpyYWRpdXM6IDE2ODcwMjAuMzMyODgyNzE2Ngpwcm92ZW5hbmNlOiA2Cg==; SIDCC=AKEyXzVUY4MhxYcRGDarRr0NRi4VHSGbRMchoLwVx0HkMNa1kdlQCRpSpoOXAkX0gmAkw23PtGGS; __Secure-1PSIDCC=AKEyXzXwrJTQl17RcUARR2WmWJJC7Awy6eKcW6ye_gqvyK9_3DWtCpAVOCwTSNjFm6Thj53NoS8; __Secure-3PSIDCC=AKEyXzW7KvRBXDFsk2lp4SjKivTpdUskY-DQgoViw-zmteS7PWVuQPWKYqR3kJ3biSHwaDo4h3cE',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera GX";v="112"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"112.0.5197.60"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera GX";v="112.0.5197.60"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0 (Edition std-1)',
    'x-client-data': 'COzcygE=',
}
    url = f"https://www.google.com/search?q={keyword}"
    response = requests.get(url, headers=headers)
    return response.text

def extract_organic_results(html): # Items that are not paid advertisements
    soup = BeautifulSoup(html, 'html.parser')
    organic_results = []
    for result in soup.select('div.g')[:8]:
        title = result.select_one('h3')
        link = result.select_one('a')
        if title and link:
            organic_results.append({
                'title': title.text,
                'url': link['href']
            })
    return organic_results

def extract_people_also_ask(html):
    soup = BeautifulSoup(html, 'html.parser')
    paa_questions = [] # List created for the People Also Ask questions 
    
    # Try different possible selectors because the google html frequently changes 
    selectors = [
        'div.related-question-pair',
        'div.related-questions-pair',
        'div.g.related-question',
        'div.match-mod-horizontal-padding',
        'div[data-q]',
        'div.jsname'
    ]
    
    for selector in selectors: # Searching through the selectors until an question is found 
        questions = soup.select(selector)
        if questions:
            for question in questions[:4]: #
                question_text = question.get_text(strip=True)
                if question_text:
                    paa_questions.append(question_text)
            if paa_questions:
                break  # Stop if we found questions

    # If still no questions found, try a more general approach
    if not paa_questions:
        potential_questions = soup.find_all('div', class_=lambda x: x and 'related' in x)
        for item in potential_questions[:4]:
            question_text = item.get_text(strip=True)
            if question_text:
                paa_questions.append(question_text)

    return paa_questions

def scrape_google(keywords):
    results = []
    for keyword in keywords:
        print(f"Scraping for keyword: {keyword}")
        try:
            html = google_search(keyword)  # Removed debug=True
            organic_results = extract_organic_results(html)
            paa_questions = extract_people_also_ask(html)
            
            results.append({
                'keyword': keyword,
                'organic_results': organic_results,
                'paa_questions': paa_questions
            })
            
            print(f"Found {len(organic_results)} organic results and {len(paa_questions)} PAA questions")
        except Exception as e:
            print(f"Error scraping for keyword '{keyword}': {str(e)}")
        
        time.sleep(random.uniform(2, 5))
    
    return results

def write_to_csv(results, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Keyword', 'Organic Result #', 'Title', 'URL', 'PAA Question #', 'Question']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for result in results:
            keyword = result['keyword']
            for i, organic in enumerate(result['organic_results'], 1):
                writer.writerow({
                    'Keyword': keyword,
                    'Organic Result #': i,
                    'Title': organic['title'],
                    'URL': organic['url']
                })
            
            for i, question in enumerate(result['paa_questions'], 1):
                writer.writerow({
                    'Keyword': keyword,
                    'PAA Question #': i,
                    'Question': question
                })

def write_to_json(results, filename):
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(results, jsonfile, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    keywords = ['webscraping', 'dark matter', 'lechuga', 'dark energy', 'python jobs',  'git']  # Add your keywords here
    results = scrape_google(keywords)
    if results:
        write_to_csv(results, "google_search_results.csv")
        write_to_json(results, "google_search_results.json")
        print("Scraping completed. Results saved to google_search_results.csv and google_search_results.json")
    else:
        print("No results were found. Please check your internet connection or try again later.")
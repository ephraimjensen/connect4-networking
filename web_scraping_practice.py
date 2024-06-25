import requests
import re

regex_string = re.compile(r'<span class="date h6">([^<]+)</span>\s*<span class="location h4">([^<]+)</span>\s*<span class="location h5">([^<]+)</span>')

with requests.Session() as session, open("highwaymen_tour.txt", "w", encoding='utf-8') as file1:

    for i in range(1990, 1997):
        url = f"https://www.johnnycash.com/about/tour-history/?tour-year={i}&band=the-highwaymen"

        r = session.get(url)
        if r.status_code == 200:

            # print(r)

            # print(r.content)

            web_string = r.content.decode('utf-8')

            tour_places = re.findall(regex_string, web_string)

            file1.write(f"{tour_places}\n\n")

            print(f"{i} done")
        else:
            print(f"{i} not found")


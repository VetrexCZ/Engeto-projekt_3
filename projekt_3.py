"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Daniel Skřivánek
email: ddaniel.skrivanek@seznam.cz
discord: vetrex89cz #3080
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup

def input_check():
    # to check if all required arguments has been entered
    if len(sys.argv) != 3:
        print("Requiered (3) parameters not entered.")
        print("Shutting down the program..")
        exit()

    # to check if requiered URL has been entered
    if "https://volby.cz/pls/ps2017nss/ps32" not in sys.argv[1]:
        print("URL parameter not valid.")
        print("Shutting down the program..")
        exit()

    # to check if required outpout file name has been entered
    if not sys.argv[2].endswith(".csv"):
        print("Invalid output file name.")
        print("Shutting down the program..")
        exit()

def get_response(url: str) -> str:
    # get data from url
    response = requests.get(url)
    return response

def parse_response(response: str) -> BeautifulSoup:
    # parse the response to html format
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def get_table_row(soup: BeautifulSoup) -> list:
    # to get required html tag data
    tag_tr = soup.find_all('tr')
    table_row = []
    for table_r in tag_tr:
        table_row.append(table_r.get_text().strip().splitlines())
    print("Downloading data from current URL")
    return table_row

def get_number_of_city(table_row: list) -> list:
    # from html get list of numbers and names of the cities
    city_number_list = []
    for sublist in table_row[2:]:
        if sublist[0] == "-" or sublist[0] == "Obec" or sublist[0] == "číslo":
            continue
        else:
            city_number_list.append(sublist[0])
    return city_number_list
    
def get_name_of_city(table_row: list) -> list:
    # getting the name of cities and saving them in a list
    city_name_list = []
    for sublist in table_row[2:]:
        if sublist[1] == "název" or sublist[1] == "Výběrokrsku" or sublist[1] == "-":
            continue
        else:
            city_name_list.append(sublist[1])
    return city_name_list

def get_urls(soup: BeautifulSoup) -> list:    
    # getting urls from the soup and saving them in list
    tables = soup.find_all("table")
    url_list = []
    for table in tables:
        a_tags = table.find_all("a")
        for tag in a_tags:
            href = tag.get("href")
            if "vyber=" in href and href not in url_list:
                url_list.append(href)
    return url_list    

def get_url_to_process(url_list: list) -> list:
  # processing each url and creating a full url to be processed
  url_base = "https://volby.cz/pls/ps2017nss/"
  urls_to_process = []
  for url in url_list:
      whole_url = url_base + url
      urls_to_process.append(whole_url)
  return urls_to_process

def process_url(urls_to_process: list) -> list:
    # to parse and process all the needed urls
    processed_urls = []
    for url in urls_to_process:
        processed_url = parse_response(get_response(url))
        processed_urls.append(processed_url)
    return processed_urls

def get_voters_count(processed_urls: BeautifulSoup) -> list:
    # to get the count of voters in each url (city)
    voters_count = []
    for url in processed_urls:
        voters = url.find("td", {"class": "cislo"}, headers="sa2").get_text()
        voters_count.append(int(voters.replace("\xa0", "")))
    return voters_count

def get_envelopes(processed_urls: BeautifulSoup) -> list:
    # to get a count of envelopes for each url (city)
    envelopes_count = []
    for envelopes in processed_urls:
        envelope = envelopes.find("td", {"class": "cislo"}, headers="sa3").get_text()
        envelopes_count.append(int(envelope.replace("\xa0", "")))
    return envelopes_count

def get_valid_votes(processed_urls: BeautifulSoup) -> list:
    # to get count of all valid votes for each url (city)
    valid_votes_count = []
    for votes in processed_urls:
        vote = votes.find("td", {"class": "cislo"}, headers="sa6").get_text()
        valid_votes_count.append(int(vote.replace("\xa0", "")))
    return valid_votes_count

def get_all_votes_for_each_party(processed_urls: BeautifulSoup) -> list:
    # to get votes for each seperated party
    all_party_votes = []
    for url in processed_urls:
        votes = url.find_all("td", headers=["t1sb3", "t2sb3"])
        each_party_votes = []
        for vote in votes:
            if  vote.get_text().strip() == "-":
                continue
            else:
                each_party_votes.append(vote.get_text().replace("\xa0", ""))
        all_party_votes.append(each_party_votes)
    return all_party_votes

def get_political_parties_names(soup: BeautifulSoup) -> list:
    # to get all the political parties names from one url
    political_parties = []
    td_tags = soup.find_all("td", {"class": "overflow_name"})
    for tag in td_tags:
            political_parties.append(tag.get_text())
    return political_parties

def main(url: str):
    input_check()
    soup = parse_response(get_response(url))
    city_codes = get_number_of_city(get_table_row(soup))
    city_names = get_name_of_city(get_table_row(soup))
    get_urls(soup)
    get_url_to_process(get_urls(soup))
    processed_urls = process_url(get_url_to_process(get_urls(soup)))
    reg_voters = get_voters_count(processed_urls)
    envelopes = get_envelopes(processed_urls)
    valid_votes = get_valid_votes(processed_urls)
    all_votes = get_all_votes_for_each_party(processed_urls)
    parties = get_political_parties_names(processed_urls[0])

    # creating a header with data for the csv file
    header = ["code", "location", "registered voters", "envelopes", "valid votes", *parties]

    # creating a single list of the zipped data collected
    data = list(zip(city_codes, city_names, reg_voters, envelopes, valid_votes))
    
    # adding all_votes to the data variable, creating lists of data for csv
    for i in range(len(data)):
        data[i] = list(data[i]) + all_votes[i]
    
    return {"header": header, "data": data}

def to_csv(filename: str, data):
    # write data to csv.file
    try:
        with open(filename, mode="w", encoding="utf-8-sig", newline="") as file:

            writer = csv.writer(file, delimiter=";")

            writer.writerow(data["header"])

            # writing row by row in the csv filer
            for row in data["data"]:
                writer.writerow(row)

        print(f"The program finished successfully.\n"
              f"Your output file: {sys.argv[2]} has been created")

    #exception handling: PermissionError, can appear when file being used by different program
    except PermissionError:
        print("Permission denied. File might be opened in different program.\n"
        "Check and rerun")
        exit()

if __name__ == "__main__":
    data = main(sys.argv[1])
    to_csv(sys.argv[2], data)
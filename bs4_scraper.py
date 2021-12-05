from bs4 import BeautifulSoup
import requests
import re

def scrape_site(website,tag):
    r = requests.get(website)
    web_text = r.text
    soup = BeautifulSoup(web_text,'html.parser')
    total_tags = []

    for item in soup.find_all(tag):
        total_tags.append(item)
    return total_tags


def remove_tags(tag_list,tag):
    content_list = []
    for tag in tag_list:
        back_tag = False
        for letter in tag:
            contents = ""
            if back_tag == False and letter == ">":
                back_tag = True
            if back_tag == True and letter = "<":
                content_list.append(contents)
                break
            if back_tag == True:
                contents += letter
    return content_list

def write_to_file(filename,list):
    f = open("scraped.txt",'w')
    for item in list:
        f.write(str(item) + "\n")
    f.close()

from bs4 import BeautifulSoup
import requests

def help():
    print("""
    This project is a general purpose made web scraper to grab tags, tag variable and etc using BeautifulSoup.

    Here are the following functions:

        scrape_site()
        website (str) : website url
        tag (str) : tag name you are looking for
        RETURNS : a list of tags

        remove_tags(tag_list)
        tag_list (list): a list of scraped tags (use results from scrape_site)
        RETURNS : a list of the contents inbetween opening and closing tags

        write_to_file(filename, list)
        filename (str): name of file to write to (does not have to exist)
        list (str): list of items to write to file (writes one item per line)

        grab_tag_variable(tag_list, variable)
        tag_list (str): list of tags (use results of scrape_site)
        variable (str): A variable used inside of a tag (ex: href, class )
        RETURNS : a list of the contents inside the variables " "
    """)




def scrape_site(website,tag):
    r = requests.get(website)
    web_text = r.text
    soup = BeautifulSoup(web_text,'html.parser')
    total_tags = []

    for item in soup.find_all(tag):
        total_tags.append(item)
    return total_tags


def remove_tags(tag_list):
    content_list = []
    for tag in tag_list:
        back_tag = False
        contents = ""
        for letter in str(tag):
            if back_tag == False and letter == ">":
                back_tag = True
            elif back_tag == True and letter == "<":
                content_list.append(contents)
                break
            elif back_tag == True:
                contents += str(letter)
    return content_list


def write_to_file(filename,list):
    f = open(filename,'w+')
    for item in list:
        f.write(str(item) + "\n")
    f.close()


def grab_tag_variable(tag_list,variable):
    content_list = []
    variable += '="'
    for tag in tag_list:
        if variable in str(tag):
            variable_string = ""
            variable_index = 0
            variable_found = False
            contents = ""
            for letter in str(tag):
                if letter == variable[variable_index] and variable_found == False:
                    variable_string += letter
                    if variable_index < (len(variable) -1):
                        variable_index += 1
                if variable_string == variable:
                    variable_found = True

                if variable_found == True and letter != '"':
                    contents += letter

                elif variable_found == True and letter == '"':
                    if contents:
                        content_list.append(contents)
                        break
    return content_list

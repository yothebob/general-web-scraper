from bs4 import BeautifulSoup
import requests

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
        print(tag)
        back_tag = False
        contents = ""
        for letter in str(tag):
            # print(letter)
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
    print(variable)
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
                    print(variable,variable_string, variable_index)

                if variable_string == variable:
                    variable_found = True

                if variable_found == True and letter != '"':
                    print("added to contents")
                    contents += letter

                elif variable_found == True and letter == '"':
                    if contents:
                        print(f"appended {contents} to content_list")
                        content_list.append(contents)
                        break
                # elif letter == variable[variable_index] and variable_found == False:
                #     print(variable,variable_string)
                #     variable_string += letter
                #     variable_index += 1
                #     contents += letter
    return content_list

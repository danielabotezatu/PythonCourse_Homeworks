from selenium import webdriver
import pandas as pd
from operator import sub

chrome = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
website = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"
const = ["2020", "ora", "13", "00"]


def intCast(elem):
    if "." in elem:
        elem = elem.replace(".", "")
    return int(elem)


def castList(list):
    list = [intCast(elem) for elem in list]
    return list


def getTableInfo(day, month):
    chrome.get(website + "-".join([str(day), str(month)] + const) + "/")
    table = chrome.find_element_by_xpath('/html/body/div[3]/div/div[1]/main/article/div/div/table[1]')
    tableHeads = table.find_elements_by_tag_name("tr")[0].find_elements_by_tag_name("td")
    tableHeads = [i.text for i in tableHeads]
    dictionary = {i: [] for i in tableHeads}

    rowsWithoutHeader = table.find_elements_by_tag_name("tr")[1:]
    rowsWithoutTotal = rowsWithoutHeader[:-1]

    for row in rowsWithoutTotal:
        td = row.find_elements_by_tag_name("td")
        for i in range(len(tableHeads)):
            dictionary[tableHeads[i]].append(td[i].text)

    dictionary[tableHeads[0]].append("")
    dictionary[tableHeads[1]].append(str(rowsWithoutHeader[-1].find_elements_by_tag_name("td")[0].text).lstrip(" "))
    dictionary[tableHeads[2]].append(rowsWithoutHeader[-1].find_elements_by_tag_name("td")[1].text)

    return dictionary, tableHeads


ziua1 = input("Introduceti prima zi: ")
ziua2 = input("Introduceti a doua  zi: ")
luna = input("Introduceti luna pentru care sa se calculeze cazurile confirmate: ")

try:
    ziua1 = int(ziua1)
    ziua2 = int(ziua2)
except ValueError:
    print("Input gresit, reincercati")

dict1, tableHeads1 = getTableInfo(ziua1, luna)
dict2, tableHeads2 = getTableInfo(ziua2, luna)
chrome.close()

chosenDict = dict1
if len(dict1[tableHeads1[0]]) != len(dict2[tableHeads2[0]]):
    chosenDict = dict1 if len(dict1[tableHeads1[0]]) > len(dict2[tableHeads2[0]]) else dict2
    chosenDict[tableHeads1[0]].pop(len(chosenDict[tableHeads1[0]]) - 2)
    chosenDict[tableHeads1[1]].pop(len(chosenDict[tableHeads1[1]]) - 2)
    chosenDict[tableHeads1[2]].pop(len(chosenDict[tableHeads1[2]]) - 2)

listaCazuri1 = castList(dict1[tableHeads1[2]])
listaCazuri2 = castList(dict2[tableHeads2[2]])

newList = list(map(sub, listaCazuri2, listaCazuri1))
chosenDict[tableHeads1[2]] = newList
chosenDict["NR cazuri " + str(ziua1) + " - " + str(ziua2) + " " + luna] = chosenDict.pop(tableHeads1[2])

df = pd.DataFrame(chosenDict)
df.to_excel("NrCazuri" + str(ziua1) + " - " + str(ziua2) + " " + luna + ".xls", index=False)

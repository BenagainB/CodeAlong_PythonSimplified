# mechSoup_scraper.py
""" Web Scraping Databases with Mechanical Soup and SQlite """

import mechanicalsoup
import pandas as pd
import sqlite3

WIKI_LINUX_URL = "https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions"

browser = mechanicalsoup.StatefulBrowser()
browser.open(WIKI_LINUX_URL)

# extract table headers
table_headers = browser.page.find_all("th", attrs={"class": "table-rh"})
    # gets all the tags
distribution = [value.text.replace("\n", "") for value in table_headers]
    #gets only the text values from tags
# print(distribution)   # we see headers for ALL the tables on the page
# print(distribution.index("Zorin OS"))
    # 97
distribution = distribution[:98]
    # slice off everything after Zorin OS (last item in first table)
# print(distribution)

# extract table data
table_data = browser.page.find_all("td")
columns = [value.text.replace("\n", "") for value in table_data]
# print(columns.index("AlmaLinux Foundation"))
# 8
# print(columns.index("Binary blobs"))
# 1086
columns = columns[8:1086]
# print(columns)
# There are 11 columns after the row header

column_names = ["Founder",
                "Maintainer",
                "Initial_Release",
                "Current_Stable_Version",
                "Security_Updates",
                "Release_Date",
                "System_Distribution_Commitment",
                "Forked_From",
                "Target_Audience",
                "Cost",
                "Status"]

dictionary = {"Distribution": distribution}

# select every 11th item
# columns[0:][::11]
# columns[1:][::11]
# columns[2:][::11]     # and so on

for idx, key in enumerate(column_names):
    dictionary[key] = columns[idx:][::11]

df = pd.DataFrame(data = dictionary)
print(df.head())
#    Distribution               Founder  ...  Cost  Status
# 0     AlmaLinux  AlmaLinux Foundation  ...  None  Active
# 1  Alpine Linux     Alpine Linux Team  ...  None  Active
# 2     ALT Linux        ALT Linux Team  ...  None  Active
# 3         antiX       Anticapitalista  ...  None  Active
# 4      ArchBang    Willensky Aristide  ...  None  Active
# [5 rows x 12 columns]

print(df.tail())
#     Distribution                  Founder  ...                                               Cost    Status
# 93  Webconverger               Kai Hendry  ...                                         Commercial  Inactive
# 94       Xandros     Xandros Incorporated  ...                                         Commercial  Inactive
# 95       Zentyal        eBox Technologies  ...                   Some editions are free of charge         ?
# 96       Zenwalk  Jean-Philippe Guillemin  ...                                               None    Active
# 97      Zorin OS              Zorin Group  ...  Zorin OS Lite & Core are free, while Business ...    Active
# [5 rows x 12 columns]

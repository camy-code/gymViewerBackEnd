import requests as rq
from bs4 import BeautifulSoup

def dum_scrape():
    # Time to organzie
    myLs = []

    days = ["Wednesday, April 30", "Thursday, May 1"] # This is just a loop for all days
    for day in days:

        temp_dict = dict()
        # 1. Do the name
        temp_dict["name"] = day

        # 2. Do expand
        temp_dict["expand"] = False

        # 3. Do activities
        temp_act = []
            # Do some work here later
        temp_act.append( {"color":"#E0E0E0", "gym":"red gym", "sport":"hockey", "time":"12-1pm"})

        temp_dict["activities"] = temp_act


        myLs.append(temp_dict)

    # return ["one", "two", "three"]
    return myLs

# Following this tutorial
    # https://realpython.com/beautiful-soup-web-scraper-python/
class table:
    def __init__(self, URL):
        pass


def realScrape():

    # Calling the scraper
    URL = "https://schedules.oval.ucalgary.ca/MobileOpenGymTimes.aspx"
    page = rq.get(URL)

    # This is setting up our parser
    soup = BeautifulSoup(page.content, "html.parser")

    # This grabs the table that we are looking for
    results = soup.find(id=("ctl00_MainContent_ASPxGridViewDetails_DXMainTable"))

    # Grab all the needed rows (this is raw html still put still gather
    table_rows = results.find_all("tr",  class_="dxgvDataRow_PlasticRed")
    t_size = (len(table_rows))
    data_ls = []

    # t_size = 1 # Do this so it is easy to print things
    for i in range(t_size):
        htmlROW = table_rows[i]
        mTempHTML = htmlROW.find_all("td", class_="dxgv") # Grab all table entries
        mTempText = list(map( lambda a : a.text,mTempHTML)) # convert to string

        # Bring the data in variables
        mDate = mTempText[0]
        mStart =mTempText[1]
        mEnd =mTempText[2]
        mLocation =mTempText[3]
        mActivity =mTempText[4]

        data_ls.append([mDate,mStart,mEnd,mLocation,mActivity])

    # Time to get all days
    timeLs = set(list(map(lambda x: x[0],data_ls)))

    # Time to get location
    locationLs = set(list(map(lambda x: x[3],data_ls)))

    # Time to get activity
    activityLs =  set(list(map(lambda x: x[4],data_ls)))

    print(timeLs,"\n",locationLs,"\n",activityLs)


# Remove the below later
print("-----")
realScrape()
print("-----")

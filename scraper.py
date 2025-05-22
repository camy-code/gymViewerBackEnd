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
        self.timeLs = list(dict.fromkeys(list(map(lambda x: x[0],data_ls))))

        # Time to get location
        self.locationLs = set(list(map(lambda x: x[3],data_ls)))

        # Time to get activity
        self.activityLs =  set(list(map(lambda x: x[4],data_ls)))

        # Time to get the 2D table
        self.table = data_ls


    def getTable(self):
        return self.table

    def getDays(self):
        return self.timeLs

    def getActivities(self):
        return self.activityLs

    def getLocations(self):
        return self.locationLs

    def getColor(self, x):
        x = str(x).lower()
        if "gold" in x:
            return "#D97706"
        elif "red" in x:
            return "#B91C1C"
        else:
            return "#4338CA"

    # This function returns the JSON for all the gym days
    def getBigJSONformat(self):
        myLs = []

        days = self.getDays()

        for day in days:

            temp_dict = dict()
            # 1. Do the name
            temp_dict["name"] = day

            # 2. Do expand
            temp_dict["expand"] = False

            # 3. Do activities
            temp_act = []
                # Do some work here later
            actLS = filter((lambda x: day == x[0]),self.getTable())
            for a in actLS: # find all activities and append them
                temp_act.append({"color":self.getColor(a[3]), "gym":a[3], "sport":a[4], "time":str(f"{a[1]} - {a[2]}")})



            temp_dict["activities"] = temp_act
            myLs.append(temp_dict)

        return myLs


URL = "https://schedules.oval.ucalgary.ca/MobileOpenGymTimes.aspx"
x = table(URL)

# print(x.getDays())
# print(x.getTable())

# print(x.getActivities())
# for i in (x.getBigJSONformat()[0]["activities"]):
#     print(i)

# Make some new methods later to do your grabs
def realScrape():
    return x.getBigJSONformat()

def sportTime():
    return ["Any"]+ list(x.getActivities())


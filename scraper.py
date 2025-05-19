# const tempArr = [
#         {name:"Wednesday, April 30",
#             expand:false,
#             activities:[
#             {color:"#E0E0E0", gym:"red gym", sport:"hockey", time:"12-1pm"},
#             {color:"#E0E0E0", gym:"red gym", sport:"hockey", time:"12-1pm"},
#             {color:"#E0E0E0", gym:"red gym", sport:"hockey", time:"12-1pm"},
#         ]
#     },
#
#     ]
#
# end goal where we can have more jsons in here!

def dum_scrape():
    # Time to organzie
    myLs = []

    days = ["Wednesday, April 30", "Thursday, May 1"] # This is just a loop for all days
    for day in days:
        pass
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

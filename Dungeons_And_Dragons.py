import json
import urllib.request

test = "!zombie type"
#######################JSON STUFF##############################################################
with urllib.request.urlopen("http://wizardslair.us/dd.json") as j:
    data = j.read().decode()
    result = json.loads(data)
    rawjson = json.dumps(result, indent=4, sort_keys=True) #replace all items named results in function getThing with pretty

with open("currentgame.JSON") as game:
    gamedata = game.read()
    gameInstance = json.loads(gamedata)
    #print(gameInstance)
##################END JSON###########################

messageconv = test[1:len(test)+1]
players = []





def getThing(name, get):
    if get != None:
        for item in result[name]:
            print(item[get])
    else:
        for item in result[name]:

            for each in item:
                print(each, " = ", item[each])


def onMessage(msg):
    message = msg.split(" ")
    arg1 = message[0]
    try:
        arg2 = message[1]
    except IndexError:
        arg2 = None
    getThing(arg1, arg2)

def Assign_Players(messageAuthor):
    global gameInstance
    ma = str(messageAuthor)
    playerExist = False
    for item in gameInstance["players"]:
        for each in item:
            #print(item[each])
            if item[each] == ma:
                playerExist = True
                print("player already in game")
    if playerExist == False:
        for item in gameInstance['players']:
            for key in item:
                if item[key] == None:

                    gameInstance["players"][0][key] = ma
                    newInstance = json.dumps(gameInstance)
                    #json.dump(newInstance, game) #this writes to the json file, commented for testing

                    print(newInstance)
                    return



def Session(saveData):
    data = saveData
    playerNumber = 0
    for player in data["players"]:
        if player != None:
            playerNumber += 1



Assign_Players("fisher60")

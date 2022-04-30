import json
import psycopg2
from flatten_json import flatten
import sys


def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def int2BoolStr (value):
    if value == 0:
        return 'False'
    else:
        return 'True'
    
def usersTableParse():
    print("ALERT: Now Beginning Users Parse Function")
    with open('yelp_user.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
    
        conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
      
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            time = data['yelping_since'].split(' ')
            
            users = "INSERT INTO UserInfo(averageStars, cool, funny, totalLikes, fans, user_latitude, user_longitude, username, totalTips, useful, user_id, accountDate," \
                "accountTime)" "VALUES (" + str(data["average_stars"]) + "," + str(data["cool"]) + "," + str(data["funny"]) + ", 0," \
                + str(data["fans"]) + ", '0', '0','" + cleanStr4SQL(data["name"]) + "'," + str(data["tipcount"]) + "," + str(data["useful"]) + ",'" + cleanStr4SQL(data["user_id"]) + \
                    "','" + str(time[0]) + "','" + str(time[1]) + "0, 0');"
                    
            try:
                current.execute(users)
            except:
                conn.commit()
                
            conn.commit()
            
            line = f.readline()
            count_line = count_line + 1 
            
        current.close()
        conn.close()
        print(count_line)
        f.close()
    
def tipsTableParse():
    print("ALERT: Now Beginnning Tips Table Parse Function")
    with open('./yelp_tip.JSON', 'r') as f:
    
        line = f.readline()
        count_line = 0
        
        
        conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
       
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            time = data['date'].split(' ')
            
            tips = "INSERT INTO Tips(business_id, user_id, likesCount, textOfTips, dateOfTips, timeOfTips)" \
                "VALUES ('" + cleanStr4SQL(data["business_id"]) + "','" + cleanStr4SQL(data["user_id"]) + "'," + str(data["likes"]) + ",'" + \
                    cleanStr4SQL(data["text"]) + "','" + cleanStr4SQL(time[0]) + "','" + \
                    cleanStr4SQL(time[1]) + "');"
            
            
            current.execute(tips)
            
            conn.commit()
            line = f.readline()
            count_line = count_line + 1
        
        
        current.close()
        conn.close()
    print(count_line)
    f.close()

def checkInTableParse():
    print("ALERT: Now Beginning Check In Table Parse Function")
    with open('yelp_checkin.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
       
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            time = data['date'].split(',')
            
            for t in time:
                time = t.split(' ')
                date = time[0].split('-')
                checkIn = "INSERT INTO CheckIn(business_id, yearOfCheckIn, dateOfCheckIn, monthOfCheckIn, timeOfCheckIn) " "VALUES ('" + cleanStr4SQL(data["business_id"]) +\
                    "','" + str(date[0]) + "'," + str(date[1]) + ",'" + cleanStr4SQL(date[2]) + "','" + cleanStr4SQL(time[1]) + "');"
                
    
                current.execute(checkIn)
                conn.commit()
            
                count_line = count_line + 1
                
                
            line = f.readline()
            
        current.close()
        conn.close()
        
    print(count_line)
    f.close()
    
def friendTableParse():
    print("ALERT: Now Beginning Friend Table Parse Function")
    with open('yelp_user.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        
        conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            
            for friend in data['friends']:
                friend = "INSERT INTO Friend(user_id, friend_id)" "VALUES ('" + cleanStr4SQL(data["user_id"]) + "','" + cleanStr4SQL(friend) + "');"
                
                current.execute(friend)
                conn.commit()
                
                count_line = count_line + 1
                    
            line = f.readline()   
        current.close()
        conn.close()
        
    print(count_line)
    f.close()
    
def parseCheckInData():
    with open('yelp_checkin.JSON', 'r') as f:
        outfile = open('checkin.txt', 'w')
        line = f.readline()
        count_line = 0
        
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['business_id'])+'\t')
            dates = data["date"]
            
            parseDates = dates.split(' ')
            remaining = []
            
            for d in parseDates:
                d.split(' ')
                a = d.split('-')
                remaining.append(a)
            
            outfile.write(str(remaining)+'\t')

        outfile.write('\n')
        line = f.readline()
        count_line = count_line + 1
            
    print(count_line)
    outfile.close()
    f.close()

def parseUserData():
    # TO-DO : write code to parse yelp_user.JSON
    with open('yelp_user.JSON', 'r') as infile:
        outfile = open("info.txt", 'w')
        stringLine = infile.readline()
        lineCount = 0

        while stringLine:
            data = json.loads(stringLine)
            outfile.write(str(data["average_stars\t"]))
            outfile.write(str(data["cool\t"]))
            outfile.write(str(data["fans\t"]))
            outfile.write(str(data["friends\t"]))
            outfile.write(str(data["funny\t"]))
            outfile.write(str(data["name\t"]))
            outfile.write(str(data["tipcount\t"]))
            outfile.write(str(data["useful\t"]))
            outfile.write(str(data["user_id\t"]))
            outfile.write(cleanStr4SQL(data["yelping_since\t"]))

            outfile.write("\n")
            stringLine = infile.readline()
            lineCount = lineCount + 1
            
        print(lineCount)
        outfile.close()
        infile.close()
            
def parseTipData():
    with open('yelp_user.JSON', 'r') as infile:
        outfile = open("tips.txt", 'w')
        stringLine = infile.readline()
        lineCount = 0

        while stringLine:
            data = json.loads(stringLine)
            outfile.write(cleanStr4SQL(data['business_id'] + "\t"))
            outfile.write(str(data["date\t"]))
            outfile.write(str(data["likes\t"]))
            outfile.write(str(data["text\t"]))
            outfile.write(str(data["user_id\t"]))

            outfile.write("\n")
            stringLine = infile.readline()
            lineCount = lineCount + 1
            
        print(lineCount)
        outfile.close()
        infile.close()
def insertCategories():
    print("ALERT: Now Beginning parse fo Categories")
    with open('yelp_business.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            categories = data["categories"].split(', ')
            for c in categories:
                business_category = "INSERT INTO Categories(business_id, category_name) VALUES ('" + data['business_id'] + "', '" + cleanStr4SQL(str(c)) + "'""); "
                

                current.execute(business_category)
                conn.commit()
                
                count_line = count_line + 1
                    
            line = f.readline()
            
    print(count_line)
    f.close()

def insertAttributes():
    print("ALERT: Now Beginning parse for Attributes")
    with open('yelp_business.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            flat = flatten(data["attributes"])
            for k, v in flat.items():
                if(k and v):
                    if(k.startswith("GoodForMeal")):
                        if(k == 'GoodForMeal'):
                            updatedKey = k.split("_")
                        else:
                            updatedKey = k.split('_')
                        if (v == 'None'):
                            updatedValue = 'False'
                        else:
                            updatedValue = v
                            meal = "INSERT INTO GoodMeals(business_id, typeOfMeal, valueOfGoodMeals) VALUES ('" + data['business_id'] + "','" + str(updatedKey[1]) + \
                                "'," + cleanStr4SQL(str(updatedValue)) + "); "
                        
                        
                            current.execute(meal)
                            conn.commit()
                            count_line = count_line + 1
                        
                            
                    elif(k.startswith("Ambience")):
                        if(k == 'Ambience'):
                            updatedKey = (k, k)
                        else:
                            updatedKey = k.split('_')
                        if(v == 'None'):
                            updatedValue = 'False'
                        else:
                            updatedValue = v
                            ambience = "INSERT INTO Ambience(business_id, typeOfAmbience, valueOfAmbience) VALUES ('" + data['business_id'] + "','" + str(updatedKey[1]) + "'," + \
                                cleanStr4SQL(str(updatedValue)) + ");"
                        
                        
                            current.execute(ambience)
                            conn.commit()
                            count_line = count_line + 1
                            
                    elif(k.startswith('BusinessParking')):
                        if(k == 'BusinessParking'):
                            updatedKey = (k, k)
                        else:
                            updatedKey = k.split('_')
                        if(v == 'None' or v == '{}'):
                            updatedValue = 'False'
                        else:
                            updatedValue = v
                        
                            parking = "INSERT INTO parking(business_id, typeOfParking, valueOfParking) VALUES ('" + data['business_id'] + "','" + str(updatedKey[1]) + "'," + \
                            cleanStr4SQL(str(updatedValue)) + ");"
                        
                        
                            current.execute(parking)
                            conn.commit()
                            count_line = count_line + 1
                            
                    else:
                        attribute = "INSERT INTO Attributes(business_id, nameOfAttribute, valueOfAttribute) VALUES ('" + data['business_id'] + "','" + str(k) + "', '" \
                            + cleanStr4SQL(str(v)) + "'""); "
                        
                        
                        current.execute(attribute)
                        conn.commit()
                        
                        count_line = count_line + 1
             
            line = f.readline()
    
            
    current.close()
    conn.close()
    print(count_line)
    f.close()
    
def insertHours():
    print("ALERT: Now Beginning parse for Hours")
    with open('yelp_business.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        current = conn.cursor()
        while line:
            data = json.loads(line)
            hours = []
            for k, v in data['hours'].items():
                if(k and v):
                    time = v.split(' ')
                    hours = "INSERT INTO HoursOfBusiness(business_id, dayOfBusiness, openTime, closeTime) VALUES ('" + data['business_id'] + "','" + str(k) + "','" \
                        + cleanStr4SQL(str(time[0])) + "','" + cleanStr4SQL(str(time[0])) + "'""); "
                    
                    current.execute(hours)
                    conn.commit()
                    
                    count_line = count_line + 1
            
            
            line = f.readline()
    current.close()
    conn.close()
    print(count_line)
    f.close()
                            
    
def insertBusinessTable():
    print("ALERT: Beginning INSERT to Business Table Function ")
    with open('yelp_business.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        print("Now in Database")
            
        current = conn.cursor()
        
        while line: 
            data = json.loads(line)
            business = "INSERT INTO Business(business_id, business_name, addressOfBusiness, stateOfBusiness, city, zipCode, latitude, longitude, stars, numCheckins, numberTips, ifopen, reviewCount)"\
                "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + cleanStr4SQL(data["name"]) + "','" + cleanStr4SQL(data["address"]) + "','" + \
                    cleanStr4SQL(data["state"]) + "','" + cleanStr4SQL(data["city"]) + "','" + data["postal_code"] + "'," + str(data["latitude"]) + "," + \
                        str(data["longitude"]) + "," + str(data["stars"]) +", 0 , 0 ," + str(data["is_open"]) + ", 0 );"
    
            try:
               current.execute(business)
            except:
                conn.commit()
                line = f.readline()
                count_line = count_line + 1
            
            conn.commit()
            line = f.readline()
            count_line = count_line + 1
            
    current.close()
    conn.close()
    print(count_line)
    f.close()
            
        
if __name__ == "__main__":
    usersTableParse()
    insertBusinessTable()   
    insertCategories()
    insertAttributes()
    insertHours()  
    checkInTableParse()
    tipsTableParse()
    friendTableParse()                      
    print("ALERT: Now Done")                  
                                                                                        
                                                                                                 
            
            
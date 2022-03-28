import json
import psycopg2
from flatten_json import flatten

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def int2BoolStr (value):
    if value == 0:
        return 'False'
    else:
        return 'True'
    
def usersTableParse():
    print("ALERT: Now Beginning Users Parse Function")
    with open('./usersTable.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        try:
            conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password:'project'")
        except:
            print('ERROR: Could not connect to database :(')
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            time = data['yelping_since'].split(' ')
            
            users = "INSERT INTO users (avg_stars, cool, funny, totalLikes, fans, user_latitude, user_longitude, userName, tipCount, useful, user_id, yelping_since" \
                "startInYelp, latitude, longitude)" "VALUES (" + str(data["average_stars"]) + "," + str(data["cool"]) + "," str(data["funny"]) + ", 0," + \ 
                str(data["fans"]) + ", '0', '0','" + cleanStr4SQL(data["name"]) + "'," + str(data["tipCount"]) + "," + str(data["useful"]) + ",'" + cleanStr4SQL(data["user_id"]) + \
                    "','" + str(time[0]) + "','" + str(time[1]) + "'0, 0");"
                    
            try:
                current.execute(users)
            except:
                print("ERROR: INSERT to users unsuccessful")
                print(users)
            conn.commit()
            
            line = f.readline()
            count_line = count_line + 1 
            
        current.close()
        conn.close()
    print(count_lines)
    f.close()
    
def tipsTableParse():
    print("ALERT: Now Beginnning Tips Table Parse Function")
    with open('./tips.JSON', 'r') as f:
    
        line = f.readline()
        count_line = 0
        
        try:
            conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        except:
            print("ERROR: Connection to database unsuccessful :(")
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            time = data['date'].split(' ')
            
            tips = "INSERT INTO (business_id, user_id, likes, tipText, tipDate, tipTime)" \
                "VALUES ('" + cleanStr4SQL(data["business_id"]) + "','" + cleanStr4SQL(data["user_id"]) + "'," + str(data["likes"]) + ",'" + \
                    cleanStr4SQL(data["text"].encode('unicode_escape').decode('unicode_escape')) + "','" + cleanStr4SQL(time[0]) + "','" \
                    cleanStr4SQL(time]) +"');"
            
            try:
                current.execute(tips)
            except:
                print("ERROR: INSERT to tips unsuccessful")
                print(tips)
            conn.commit()
        
            line = f.readline()
            count_line = count_line + 1
        
        current.close()
        conn.close()
    print(count_line)
    f.close()

def checkInTableParse():
    print("ALERT: Now Beginning Check In Table Parse Function")
    with open('./checkIn.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        try:
            conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        except:
            print('ERROR: Connection To Database Unsuccessful')
        current = conn.cursor()
        
        while line:
            data = json.loads(line)
            time = data['date'].split(' ')
            
            for t in time:
                time = x.split(' ')
                date = time[0].split('-')
                
                checkIn = "INSERT INTO checkIn (business_id, c_year, c_date, c_month, c_time) " "VALUES ('" + cleanStr4SQL(data["business_id"]) +\
                    "','" + str(date[0]) + "'," + str(date[2]) + ",'" + cleanStr4SQL(date[1]) + "','" + cleanStr4SQL(time[1]) + "');"
                
                try:
                    current.execute(checkIn)
                except:
                    print("ERROR: INSERT to Check In table unsuccessful")
                    print(checkIn)
                conn.commit()
                
            line = f.readline()
            count_line = count_line + 1
            
        current.close()
        conn.close()
        
    print(count_line)
    f.close()
    
def friendTableParse():
    print("ALERT: Now Beginning Friend Table Parse Function")
    with open('./users.JSON', 'r') as f:
        line = f.readline()
        count_line = 0
        
        try:
            conn = psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        except:
            print("ERROR: Connection to Database Unsuccessful")
        
        while line:
            data = json.loads(line)
            
            for friend in data['friends']:
                friend = "INSERT INTO friends (user_id, friend_id)" "VALUES ('" + cleanStr4SQL(data["user_id"]) + "','" + cleanStr4SQL(friend_id) + "');"
                
                try:
                    current.execute(friend)
                except:
                    print("ERROR: INSERT to Friend Table Unsuccessful")
                    print(friend)
                conn.commit()
                
            line = f.readline()
            count_line = count_line + 1
            
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
        
def insertBusinessTable():
    print("ALERT: Beginning INSERT to Business Table Function ")
    with open("./business.JSON", "r") as f:
        line = f.readline()
        count_line = 0
        
        try:
            conn.psycopg2.connect("dbname='business' user='postgres' host='localhost' password='project'")
        except:
            print("ERROR: INSERT to Business Table Unsuccessful")
        current = conn.cursor()
        
        while line: 
            data = json.loads(line)
            business = "INSERT INTO business (business_id, name, address, state, city, zipcode, latitude, longtitude, stars, numCheckins, numTips, is_open" \
                "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + cleanStr4SQL(data["name"]) + "','" + cleanStr4SQL(data["address"]) + "','" \
                    cleanStr4SQL(data["state"]) + "','" + cleanStr4SQL(data["city"]) + "','" + data["postal_code"] + "'," + str(data["latitude"]) + "," \
                        str(data["longitude"]) +"," + str(data["stars"])) +", 0 , 0 ," + str(data["is_open"]) + ", 0 );"
            try:
                current.execute(business)
            except:
                printf("ERROR: INSERT to Business Table Unsuccessful")
            conn.commit()
            
            categories = data["categories"].split(' ')
            for c in categories:
                business_category = "INSERT INTO businessCategory(business_id, category) VALUES ('" + data['business_id'] +"', '" + cleanStr4SQL(str(c)) + "'"); "
                
                try:
                    current.execute(business_category)
                except:
                    print("ERROR: INSERT to Business Category Table Unsuccesful")
                    print(business_category)
                conn.commit()
                
            flat = flatten(data["attributes"])
            for k, v in flat.items():
                if(k and v):
                    if(k.startswith("GoodForMeal")):
                        if(key == 'GoodForMeal'):
                            updatedKey = (k, k)
                        else:
                            updatedKey = k.split('_')
                        if (v == 'None'):
                            updatedValue = 'False'
                        else:
                            updatedValue = value
                            meal = "INSERT INTO Categories(business_id, category_name) VALUES ('" + data['business_id'] + "','" + str(updatedKey[1]) + \
                                "'," + cleanStr4SQL(str(updatedValue)) + "); "
                        try:
                            current.execute(meal)
                        except:
                            print("ERROR: INSERT to Categories Table Unsuccessful")
                            print(meal)
                            
                    elif(k.startswith("Ambience")):
                        if(k == 'Ambience'):
                            updatedKey = (k, k)
                        else:
                            updatedKey = k.split('_')
                        if(v = 'None'):
                            updatedValue = 'False'
                        else:
                            updatedValue = v
                            ambience = "INSERT INTO ambience(business_id, a_type, a_value) VALUES ('" + data['business_id'] + "','" + str(updatedKey[1]) + "'," + \
                                cleanStr4SQL(str(updatedValue)) + ");"
                        try:
                            current.execute(ambience)
                        except:
                            print("ERROR: INSERT Into Ambience Unsuccessful")
                            print(ambience)
                    elif(k.startswith('BusinessParking')):
                        if(k == 'BusinessParking'):
                            updatedKey = (k, k)
                        else:
                            updatedKey = k.split('_')
                        if(v == 'None' or v == '{}'):
                            updatedValue = 'False'
                        else:
                            updatedValue = v
                        
                        parking = "INSERT INTO parking(business_id, p_type, p_val) VALUES ('" + data['business_id'] + "','" + str(updatedKey[1]) + "'," + \
                            cleanStr4SQL(str(updatedValue)) + ");"
                        try:
                            current.execute(parking)
                        except:
                            print("ERROR: INSERT into Parking Unsuccessful")
                            print(parking)
                        
                    else:
                        attribute = "INSERT INTO attributes(business_id, a_name, a_value) VALUES ('" + data['business_id'] + "','" + str(k) + "','" + \
                            cleanStr4SQL(str(updatedValue)) + "'""); "
                        try:
                            current.execute(attribute)
                        except:
                            print("ERROR: INSERT into Attributes Unsuccessful")
                            print(attribute)
                    conn.commit()
                    
            hours = []
            for k, v in data['hours'].items():
                if(k and v):
                    time = v.split('-')
                    hours = "INSERT INTO hours(business_id, day, openTime, closeTime" VALUES ('" + data['business_id'] + "','" + str(k) + "','" + \
                        cleanStr4SQL(str(time[0])) + "','" + cleanStr4SQL(str(time[0])) + "'""); "
                    try:
                        current.execute(hours)
                    except:
                        print("ERROR: INSERT into Hours Unsuccessful")
                        print(hours)
                conn.commit()
                
            line = f.readline()
            count_line = count_line + 1
            
        print(count_line)
        f.close()
            
        
                        
                        
                                                                                        
                                                                                                 
            
            
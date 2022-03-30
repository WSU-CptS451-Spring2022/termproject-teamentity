CREATE TABLE Business(
    business_id VARCHAR(25) NOT NULL,
    business_name VARCHAR(100) NOT NULL, 
    addressOfBusiness VARCHAR(100) NOT NULL.
    city VARCHAR(30) NOT NULL,
    latitude NUMERIC(9, 5),
    longitude NUMERIC(9, 5),
    stateOfBusiness CHAR(2) NOT NULL,
    zipCode CHAR(5) NOT NULL,
    reviewCount INT NOT NULL,
    numCheckins INT,
    stars REAL,
    ifopen INT NOT NULL,
    numberTips INT,
    PRIMARY KEY(business_id)
);

CREATE TABLE CheckIn(
    business_id VARCHAR(25) NOT NULL,
    yearOfCheckIn CHAR(4) NOT NULL,
    dateOfCheckIn CHAR(10) NOT NULL,
    monthOfCheckIn CHAR(2) NOT NULL,
    timeOfCheckIn CHAR(8) NOT NULL,
    PRIMARY KEY(business_id, dateOfCheckIn, monthOfCheckIn, yearOfCheckIn, timeOfCheckIn),
    FOREIGN KEY (business_id) REFERENCES Business(business_id)
);

CREATE TABLE Tips(
    business_id VARCHAR(25) NOT NULL,
    user_id VARCHAR(25) NOT NULL,
    likesCount INT, 
    textOfTips VARCHAR(510) NOT NULL,
    dateOfTips CHAR(10) NOT NULL,
    timeOfTips CHAR(8) NOT NULL,
    PRIMARY KEY (business_id, user_id, dateOfTips, timeOfTips),
    FOREIGN KEY (business_id) REFERENCES Business(business_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Categories(
    business_id VARCHAR(25) NOT NULL,
    category_name VARCHAR(35),
    PRIMARY KEY(business_id, category_name),
    FOREIGN KEY(business_id) REFERENCES Business(business_id)
);

CREATE TABLE Attributes(
    valueOfAttribute VARCHAR(35) NOT NULL,
    nameOfAttribute VARCHAR(35) NOT NULL,
    business_id VARCHAR(25) NOT NULL,
    PRIMARY KEY(business_id, nameOfAttribute),
    FOREIGN KEY(business_id) REFERENCES Business(business_id)
);

CREATE TABLE GoodMeals(
    business_id VARCHAR(25) NOT NULL,
    valueOfGoodMeals BOOLEAN,
    typeOfMeal VARCHAR(30) NOT NULL,
    PRIMARY KEY(business_id, typeOfMeal),
    FOREIGN KEY(business_id) REFERENCES Business(business_id)
);

CREATE TABLE Ambience(
    business_id VARCHAR(25) NOT NULL,
    valueOfAmbience BOOLEAN,
    typeOfAmbience VARCHAR(20) NOT NULL,
    PRIMARY KEY(business_id, typeOfAmbience),
    FOREIGN KEY(business_id) REFERENCES Business(business_id)
);

CREATE TABLE Users(
    totalLikes INT, 
    fans INT NOT NULL,
    cool INT NOT NULL,
    averageStars REAL,
    user_latitude CHAR(13),
    user_longitude CHAR(13),
    user_id VARCHAR(25) NOT NULL,
    useful INT NOT NULL,
    username VARCHAR(40) NOT NULL,
    totalTips INT NOT NULL,
    accountDate CHAR(10) NOT NULL,
    accountTime CHAR(8) NOT NULL,
    funny INT NOT NULL,
    latitude2 NUMBERIC(9, 5),
    longitude NUMERICE(9, 5),
    PRIMARY KEY(user_id)
);

CREATE TABLE Parking(
    business_id VARCHAR(25) NOT NULL,
    valueOfParking BOOLEAN,
    typeOfParking VARCHAR(20) NOT NULL,
    PRIMARY KEY(business_id, typeOfParking),
    FOREIGN KEY(business_id) REFERENCES Business(business_id)
);

CREATE TABLE HoursOfBusiness(
    business_id VARCHAR(25) NOT NULL,
    openTime VARCHAR(5),
    closeTime VARCHAR(5),
    dayOfBusiness VARCHAR(9) NOT NULL,
    PRIMARY KEY(business_id, dayOfBusiness),
    FOREIGN KEY(business_id) REFERENCES Business(business_id)
);

CREATE TABLE Friend(
    user_id VARCHAR(25) NOT NULL,
    friend_id VARCHAR(25) NOT NULL,
    PRIMARY KEY(user_id, friend_id),
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY (friend_id) REFERENCES Users(user_id)
)
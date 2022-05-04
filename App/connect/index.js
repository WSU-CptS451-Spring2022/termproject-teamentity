const express = require('express');
const bodyParser = require('body-parser');
const server = express();
server.use(bodyParser.json());
server.use(bodyParser.urlencoded({ extended: false }));
const db = require('./queries.js');

// Add headers
server.use(function (req, res, next) {

    //port for local host
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');


    next();
});

server.use(bodyParser.json())
server.use(
    bodyParser.urlencoded({
        extended: true,
    })
);

server.get('/', (request, response) => {
    response.json({ info: 'Node.js, Express, and Postgres API' })
});

server.listen(3000, function () {
	console.log("Listening in on Port 3000");
});

server.get('/state', db.getAllStates)
server.get('/state/:state', db.getState)
server.get('/city/:state', db.getCitiesInState)
server.get('/zipcode/:city', db.getZipcodeInCity)
server.get('/category/:zipcode', db.getCategoriesInZipcode)

server.get('/businesses/', db.getAllBusinesses)

server.get('/count/state/:state', db.getBusinessSC)
server.get('/count/city/:city', db.getBusinessCC)
server.get('/count/zipcode/:zipcode', db.getBusinessZCC)
server.get('/count/category/:category', db.getBusinessCAC)

server.get('/business/:zipcode/:categories', db.getBusinessesfromCategories)

//user Information
server.get('/name', db.getAllNames)
server.get('/name/:name', db.getName)
server.get('/userid/:name', db.getIDFromName)
server.get('/userinfo/:userid', db.getUserinfoInID)
server.get('/userinfo/', db.getAllUserInfo)

server.get('/favoriteBusinesses/:userID', db.getFavoriteBusinesses)
server.get('/friends/:userID', db.getUserFriends)
server.get('/latesttips/:userID', db.getFriendTips)

server.get('/businessInfo/:businessID', db.getAllBusinessInfo)

server.get('/businessinfo/:businessID/sort/:sortby', db.getBusinessInfoOrder)
server.get('/reviews/:businessID', db.getBusinessReviews)
server.post('/checkin/', db.postAddCheckin)
server.post('/review/', db.postAddReview)

server.delete('/favoritebusiness/:businessID/:userID', db.delRemoveFavBusiness)

server.post('/favbusiness/', db.postAddFavBusiness)

server.put('/location/:userID', db.putEditUserLocation)


server.get('/getCategories/:businessID', db.getBusinessCategories)
server.get('/getTime/:businessID', db.getBusinessTime)

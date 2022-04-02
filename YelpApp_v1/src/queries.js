import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);
//custom error 
throw "cannot return"
const Pool = require("./config.js").Pool;


//return distinct cities
const getStates = (request, response) => {
    Pool.query(
        "SELECT distinct state From business order by state;",        
        (error, results) => {
            if (error) {
                throw error;
            }
            //successful 
            response.status(200).json(results.row);
        }
    );
};

//return cities from chosen state
const getCities = (request, response) => {
    Pool.query(
        `SELECT distinct city from business where state='${request.query.state}' order by city;`,        
        (error, results) => {
            if (error) {
                throw error;
            }
            //successful 
            response.status(200).json(results.row);
        }
    );
};

//zipcodes
const getZipcodes = (request, response) => {
    Pool.query(
        //zipcode from state and city, order by postal
        `SELECT distinct postal_code from business where state='${request.query.state}' AND city='${request.query.city}' order by postal_code;`,        
        (error, results) => {
            if (error) {
                throw error;
            }
            //successful 
            console.log(results)
            response.status(200).json(results.row);
        }
    );
};

//catagories
const getCatagories = (request, response) => {
	console.log(request.query);
	Pool.query(
		`SELECT DISTINCT category
        FROM
            (business NATURAL JOIN business_category)
        WHERE state='${request.query.state}' AND city='${request.query.city}' AND postal_code='${request.query.postal_code}'
        ORDER BY category;`,
		(error, results) => {
			if (error) {
				throw error;
			}
			console.log(results);
			response.status(200).json(results.rows);
		}
	);
};

//businesses
const getBusinesses = (request, response) => {
    const category = request.params.category;
    Pool.query('SELECT DISTINCT name FROM business JOIN category ON businessid = categoryid WHERE category = $1 ORDER BY name', [category], (error, results) => {
        if (error) {
            throw error
        }
        response.status(200).json(results.rows)
    });
}

//businessID
const getBusinessID = (request, response) => {
	console.log("Get business ID..");
	console.log(request.query);
	Pool.query(
		`SELECT DISTINCT business_id
        FROM
            business
        WHERE state='${request.query.state}' AND city='${request.query.city}' AND postal_code='${request.query.postal_code}' AND business_name = '${request.query.business_name}';`,
		(error, results) => {
			if (error) {
				throw error;
			}
			console.log(results);
			response.status(200).json(results.rows);
		}
	);
};

//get tips
const getTips = (request, response) => {
	console.log(request.query);
	Pool.query(
		`SELECT tip_text FROM tip where business_id='${request.query.business_id}';`,
		(error, results) => {
			if (error) {
				throw error;
			}
			console.log(results.rows);
			response.status(200).json(results.rows);
		}
	);
};

//add tip
const addTip = (request, response) => {
	console.log("REQUEST QUERY");
	console.log(request.body);
	const queryString = `INSERT INTO Tip (user_id, business_id, tip_text) VALUES ('${request.body.user_id}','${request.body.business_id}', '${request.body.tip_text}');`;
	console.log("QUERY STRING");
	console.log(queryString);
	Pool.query(queryString, (error, results) => {
		if (error) {
			throw error;
		}
		console.log(results.rows);
		response.status(200).json(results.rows);
	});
};

module.exports = {
	getStates,
	getCities,
	getZipcodes,
	getCatagories,
	getBusinesses,
	getBusinessID,
	getTips,
	addTip
};
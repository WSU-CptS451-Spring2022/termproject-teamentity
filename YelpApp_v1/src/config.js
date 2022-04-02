const Pool = require("pg").Pool;
const pool = new Pool({
	user: "postgres",
	host: "localhost",
	database: "milestone2",
	password: "none",
	port: 3000
});

module.exports = pool;
/*
Create by : Sio Wei Siong
Purpose : Sync the data between firebase and mariadb
*/

//requisite
const mariadb = require('mariadb');
const functions = require('firebase-functions');

//connect both database
const mariaDB = connectMariadb();
const firebaseDB = connectFirebase();



firebaseDB.ref('user').on("child_added", function(snapshot, prevChildKey) {
  	var newPost = snapshot.val();
  	console.log("Author: " + newPost.name);
  	console.log("Title: " + newPost.email);
  	console.log("Previous Post ID: " + newPost.user_type);
	
	mariaDB.query("INSERT INTO `tabMobile User` value (?, ?)", [1, "mariadb"]);
	
});
	
/*/sync firebase user table
exports.syncUsers = functions.database.ref('/user/{userId}').onWrite(event => {
	getFirebaseRef("user");
	
		
	var userId = event.params.userId;
	var eventSnapshot = event.data;
	
	console.log(event.data);
	console.log(event.params.userId);
	//if(!event.data.exist()) {}
})
*/
//write into mariadb
	/*conn.query("desc `tabMobile User")
	.then((rows)=>{
		console.log(rows);	
		conn.end();
	})
	.catch(err=>{
		console.log("error occure: " + err);
		conn.end();
	})*/

//write into firebase	
/*useref.push({
 
     "name": "sio wei siong",
      "email": "weisiongsio@gmail.com",
      "user_type" : "resident"

})	
*/

//mariadb query
/*
		console.log("DELETE User by Id " + userId);
		var DELETE_USER_SQL = "DELETE FROM `tabMobile User` WHERE `idx` = ?";
		var params = {
			userId		
		}
		conn.query(DELETE_USER_SQL, params);
		console.log("write succeed!!");
*/


//get firebase reference data
function getFirebaseRef(table){
	console.log("Load into '" + table + "' firebase reference...");
	console.log(firebaseDB.ref(table));
	return firebaseDB.ref(table);
}

//connect to mariadb
function connectMariadb() {

	const conn = mariadb.createConnection ({
			user:"root",
			database:"_8eec7bc461808e0b",
			password:"root",
			host:"localhost",
			port:3306
		})
		.catch(err=>{
			console.log("Error:" + err.message);
		})

	console.log("connected to mariadb");
	return conn;
}

//connect to firebase
function connectFirebase() {

	var admin = require("firebase-admin");

	var serviceAccount = require("./serviceAccountKey.json");

	admin.initializeApp({
  		credential: admin.credential.cert(serviceAccount),
  		databaseURL: "https://re-444ac.firebaseio.com"
	});
	console.log("Connected to firebase real-time database.");
	
	return admin.database();
}

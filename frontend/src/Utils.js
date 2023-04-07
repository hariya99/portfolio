import React, { useState, useEffect } from "react";

function GetHome(path) {
	const [data, setdata] = useState({
        firstName: "John",
        lastName: "Doe",
        intro: "Missing",
        about : "Missing",
        portfolios : []
        });
    
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
        fetch(path).then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    firstName : data.first_name,
                    lastName : data.last_name,
                    intro : data.intro,
                    about : data.about,
                    portfolios : data.portfolios
                });
            })
        )
    .catch((err) => {
        console.log("Control coming to err")
        console.log(err)
    });
    }, []);
    
    return data; 

}

export default GetHome;
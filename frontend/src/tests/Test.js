import React, { useState, useEffect } from "react";

function Test() {
	// usestate for setting a javascript
	// object for storing and using data
	const [data, setdata] = useState({
        firstName: "John",
        lastName: "Doe",
        about : "Missing"
        });
    
        // Using useEffect for single rendering
        useEffect(() => {
            // Using fetch to fetch the api from
            // flask server it will be redirected to proxy
            fetch("/home").then((res) =>
                res.json().then((data) => {
                    // Setting a data from api
                    setdata({
                        firstName : data.first_name,
                        lastName : data.last_name,
                        about : data.about
                    });
                })
            )
        .catch((err) => {
          console.log("Control coming to err")
          console.log(err)
        });
        }, []);
    
        return (
            <div className="App">
                <header className="App-header">
                    <h1>React and flask</h1>
                    {/* Calling a data from setdata for showing */}
                    <p>{data.firstName}</p>
                    <p>{data.lastName}</p>
                    <p>{data.about}</p>
    
                </header>
            </div>
    
        );
}

export default Test;
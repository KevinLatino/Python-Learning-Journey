# Basic dictionary example
user = {"name": "Kevin", "lastName": "Latino", "age": 18}
# console: "name", "lastName", "age"
print(user.keys())

# console: "Kevin", "Latino", 18
print(user.values())

# console: (name: "Kevin") ("lastName": "Latino") ("age": 18)
print(user.items())

#other dictionary example
users =  { "Kevin": { "lastName": "Latino", "age": 18 },
        "Marcel": { "lastName": "Marín", "age": 30 }}

# console: info about Kevin
print(users["Kevin"])

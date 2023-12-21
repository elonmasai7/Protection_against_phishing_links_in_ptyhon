import datetime
import json

# Create a file to store the data
data_file = open("data.json", "w")

# Write the data to the file
data = {
    "date": datetime.datetime.now().strftime("%Y-%m-%d"),
    "data": {
        "name": "John Doe",
        "age": 30,
        "gender": "male",
        "occupation": "software engineer",
    },
}
json.dump(data, data_file)

# Close the file
data_file.close()
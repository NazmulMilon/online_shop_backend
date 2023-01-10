import json

with open("/home/uzzal/Downloads/people.txt", "r") as file:
    read = file.read()
    dict_obj = json.loads(read)
    for data in dict_obj["results"]:
        print(f"{data['full_name']}, {data['email']}, {data['join_date']}")
        # print(data["full_name"])
        # print(data["email"])
        # print(data["join_date"])

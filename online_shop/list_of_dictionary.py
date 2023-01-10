list_of_dict = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    },
    {
        "color": "cyan",
        "value": "#0ff"
    },
    {
        "color": "magenta",
        "value": "#f0f"
    },
    {
        "color": "yellow",
        "value": "#ff0"
    },
    {
        "color": "black",
        "value": "#000"
    }
]


print(list_of_dict)

for data in list_of_dict:
    if "color" and "value" in data.keys():
        print(data["color"], ": ", data["value"])
    else:
        for key, val in data.items():
            print(val)



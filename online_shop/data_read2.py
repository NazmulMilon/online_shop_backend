import json

with open("/home/uzzal/Downloads/data.json", "r") as file:
    data = file.read()
    data_lst = json.loads(data)
    # list_of_dict = []
    # for data in data_lst:
    #     for service in data["services"]:
    #         data_dict = {
    #             "program_title": data["program"]["title"],
    #             "service_name": service["name"],
    #             "service_status": service["status"],
    #         }
    #         list_of_dict.append(data_dict)
    # print(list_of_dict)

    list_of_dict = []
    for data in data_lst:
        for service in data["services"]:
            id_dict = {
                service["id"],
            }
            final_dict = {

                "service_name": service["name"],
                "program_title": data["program"]["title"],
                "program_mission": data["program"]["mission"],
            }

            nested_dict = dict.fromkeys(id_dict, final_dict)
            list_of_dict.append(nested_dict)
    print(list_of_dict)

import json

with open("/home/uzzal/Downloads/data.json", "r") as file:
    data = file.read()
    data_list = json.loads(data)
    # list_of_dict = []
    # for data in data_list:
    #     for service in data["services"]:
    #         data_dict = {
    #             "program_title": data["program"]["title"],
    #             "service_name": service["name"],
    #             "service_status": service["status"],
    #         }
    #         list_of_dict.append(data_dict)
    # print(list_of_dict)

    # list_of_dict = []
    # for data in data_list:
    #     for service in data["services"]:
    #         id_dict = {
    #             service["id"],
    #         }
    #         final_dict = {
    #
    #             "service_name": service["name"],
    #             "program_title": data["program"]["title"],
    #             "program_mission": data["program"]["mission"],
    #         }
    #
    #         nested_dict = dict.fromkeys(id_dict, final_dict)
    #         list_of_dict.append(nested_dict)
    # print(list_of_dict)
    #
    list_of_dict = []
    service_id = None
    program_id = None
    for data in data_list:
        d = {}
        program_id = data["id"]
        empty_dict = {}
        for service in data["services"]:
            service_id = service["id"]
            another_dict = {
                "service_name": service["name"],
                "program_title": data["program"]["title"],
                "program_mission": data["program"]["mission"]
            }
            empty_dict[service_id] = another_dict
        d[program_id] = empty_dict
        list_of_dict.append(d)
    print(list_of_dict)

import json

import null as null
import json

with open("/home/uzzal/Downloads/people.txt", "r") as file:
    read = file.read()
    dict_obj = json.loads(read)
    # for data in dict_obj["results"]:
    #     print(f"{data['full_name']}, {data['email']}, {data['join_date']}")
    #     # print(data["full_name"])
    #     # print(data["email"])
    #     # print(data["join_date"])

    # print People_contact address_1 and address_2:
    #     dict_res = dict_obj["results"]
    #     for data in dict_res:
    #         if data["people_contact"]:
    #             print(f"'Address_1: '{data['people_contact']['address_1']} , 'Address_2: ', {data['people_contact']['address_2']}")
    #             # for key in data["people_contact"]:
    #             #     print(key, end=" ")
    #             # print()
    #
    #
    # # print People_contact country details:
    #     dict_res = dict_obj["results"]
    #     for data in dict_res:
    #         if data["people_contact"]:
    #             country_dict = data["people_contact"]["country"]
    #             print(country_dict["name"])
    #
    #

    #
    # # print People_contact city details:
    #     dict_res = dict_obj["results"]
    #     for data in dict_res:
    #         if data["people_contact"]:
    #             country_dict = data["people_contact"]["city"]
    #             print(country_dict["name"])
    #

    # # print People_contact state details:
    #     dict_res = dict_obj["results"]
    #     for data in dict_res:
    #         if data["people_contact"]:
    #             country_dict = data["people_contact"]["state"]
    #             print(country_dict["name"])

    #
    # # print People_contact state details:
    #     dict_res = dict_obj["results"]
    #     for data in dict_res:
    #         if data["people_contact"]:
    #             country_dict = data["people_contact"]["zip"]
    #             print(country_dict["name"])



    # final_dict = {}
    # for data in dict_obj["results"]:
    #     final_dict["full_name"] = f"{data['full_name']}"
    #     print(f"Email: ,{data['email']}")
    #     print(f"Join Date, {data['join_date']}")
    #
    #     if data["people_contact"]:
    #         print(
    #             f"'Address_1: '{data['people_contact']['address_1']} , 'Address_2: ', {data['people_contact']['address_2']}")
    #         print(f"Country: ,{data['people_contact']['country']['name']}")
    #         print(f"City: ,{data['people_contact']['city']['name']}")
    #         print(f"State: ,{data['people_contact']['state']['name']}")
    #         print(f"Zip: ,{data['people_contact']['zip']['name']}")
    #         print()
    #     else:
    #         print()
    # print(final_dict)


    # final_dict = {}
    # for data in dict_obj["results"]:
    #     final_dict["full_name"] = f"{data['full_name']}"
    #     final_dict["email"] = f"{data['email']}"
    #     final_dict["Join Date"] = f"{data['join_date']}"
    #
    #     if data["people_contact"]:
    #         final_dict["Address 1"] = f"{data['people_contact']['address_1']}"
    #         final_dict["Address 2"] = f"{data['people_contact']['address_2']}"
    #         final_dict["Country name"] = f"{data['people_contact']['country']['name']}"
    #         final_dict["City Name"] = f"{data['people_contact']['city']['name']}"
    #         final_dict["State Name"] = f"{data['people_contact']['state']['name']}"
    #         final_dict["Zip Code"] = f"{data['people_contact']['zip']['name']}"
    #     else:
    #         print("")
    # print(final_dict)
    list_of_dict = []
    final_dict = {}
    for i in dict_obj:
        for data in dict_obj["results"]:
            final_dict = {
                "full_name":  i.data["full_name"]
            }
            list_of_dict.append(final_dict)
    print(list_of_dict)

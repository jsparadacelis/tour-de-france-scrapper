def get_data_from_riders(riders_list):
    riders_info_list = []
    for rider in riders_list[1:]:
        riders_info_list.append([info.text for info in rider[1:]])
    return riders_info_list

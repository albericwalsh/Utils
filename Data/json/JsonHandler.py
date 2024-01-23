import json

def read_json_file(path):
    """

    :param path:
    :return:
    """
    with open(path, 'r') as f:
        return json.load(f)

def write_json_file(path, data):
    """

    :param path:
    :param data:
    :return:
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def get_json_data(path):
    """

    :param path:
    :return:
    """
    return read_json_file(path)

def set_json_data(path, data):
    """
    
    :param path: 
    :param data: 
    :return: 
    """
    write_json_file(path, data)
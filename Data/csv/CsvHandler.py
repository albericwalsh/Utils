import pandas as pd

def load_csv(path):
    """
    Load csv file from path and return it as a pandas dataframe.

    :param path: path to the csv file
    :type path: str

    :return: pandas dataframe
    :rtype: pandas.DataFrame
    """
    data = pd.read_csv(path, sep=';')
    return data

def save_csv(path, data):
    """
    Save pandas dataframe to csv file.

    :param path: path to the csv file
    :type path: str
    :param data: pandas dataframe
    :type data: pandas.DataFrame
    """
    data.to_csv(path, sep=';', index=False)

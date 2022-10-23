"""  """
from typing import Union

from data.manufacturers import manufactures


def get_info(data_of_dict: dict) -> str:
    """ Method for displaying of result - response or error.

    Primary the function is called to determine the manufacturer of the board,
    then to determine the audio signal of this board.
    """
    try:
        return get_dict_data(get_dict_data(data_of_dict))
    except KeyError:
        return 'ENTERED A VALUE NOT FROM THE LIST!'
    except Exception:
        return 'INPUT ERROR!'


def get_dict_data(data: dict) -> Union[str, dict]:
    """ Method for displaying a list of available values and getting input from the user """
    print('===== List of value =====')
    for v in data.items():
        print(v[0])

    return data[input('Enter a value from the list above (character to character): ')]


if __name__ == '__main__':
    print('\n Result:', get_info(manufactures))

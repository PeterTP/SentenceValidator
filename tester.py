from SentenceValidator import SentenceValidator as sv
from SentenceValidator import Status
import json
from pathlib import Path

# File location
TEST_FILE_PATH: Path = Path(__file__).parent.joinpath("tests.json")


def test_validator(show_string = False):
    """
    Validates strings within a json file and compares expected and resulted assertions
    Shows fail if assertion is false and successful if assertion is true
    If show_string is true, it will show the string in the log
    """

    # Opens file
    with open(TEST_FILE_PATH, 'r') as f:
        data = json.load(f)["tests"]  # parses json file as a python dict
        for x in data:
            if show_string:
                print(x['string'])

            try:
                result: Status = sv.validate(x['string'])  # validate sentence
                print(f'Expected: {x["assert"]:<20} Result: {result.name:<20}', end="") # print log
                assert result.name == x['assert']  # checks if assertion is true

            except AssertionError:
                print(f'Test Failed')
            
            else:
                print(f'Test Successful')

            if show_string:
                print('\n')


# Main
if __name__ == '__main__':
    test_validator(True)

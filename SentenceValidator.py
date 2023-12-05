from enum import Enum

class Status(Enum):
    """
    Enum that conatins error codes.
    """
    
    OK = 0
    CAPITAL_ERROR = 1
    QUOTATION_ERROR = 2
    TERMINATION_ERROR = 3
    PERIOD_ERROR = 4
    NUMBER_ERROR = 5


class SentenceValidator:
    """
    Validates sentences by set rules.\n
    Use the validate function within this class to invoke .
    """

    def validate(sentence: str) -> Status:
        """
        Validates a sentence by set rules.\n
        Accepts a str parameter and returns a Status.
        """

        termination_list: list = ['.', '?', '!']

        # Check if first character in string is capitals
        if not sentence[0].isUpper():
            return Status.CAPITAL_ERROR
        
        # Check if last character in string is one of the characters in termination_list
        if not sentence[-1] in termination_list:
            return Status.TERMINATION_ERROR

        quotation_count: int = 0
        number_buffer: list = []  # Stores the number temporarily for parsing later
        number_mode = False  # Mode that changes whether the loop checks for consequent numbers

        for i in sentence[1:-1]:
            if number_mode:
                # Checks if it is a number, else, end number mode or return an error
                if i.isdigit():
                    number_buffer += i
                elif int(number_buffer) > 13:
                    return Status.NUMBER_ERROR
                else:
                    number_mode = False
            else:
                if i == '"':
                    quotation_count += 1
                    continue
                # Check if there are periods in sentence (aside from the last one)
                elif i == '.':
                    return Status.PERIOD_ERROR
                elif i.isdigit():
                    number_mode = True
                    number_buffer += i
        
        # Check if quotations_count is even
        if quotation_count % 2 == 1:
            return Status.QUOTATION_ERROR
            

if __name__ == '__main__':
    sentence: str = 'The quick brown fox "23".'
    SentenceValidator.validate(sentence)
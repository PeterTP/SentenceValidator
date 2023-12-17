from enum import Enum

class Status(str, Enum):
    """
    Enum that conatins error codes.
    """
    
    OK = "OK"
    CAPITAL_ERROR = "CAPITAL_ERROR"
    QUOTATION_ERROR = "QUOTATION_ERROR"
    TERMINATION_ERROR = "TERMINATION_ERROR"
    PERIOD_ERROR = "PERIOD_ERROR"
    NUMBER_ERROR = "NUMBER_ERROR"


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
        if not sentence[0].isupper():
            return Status.CAPITAL_ERROR
        
        # Check if last character in string is one of the characters in termination_list
        if not sentence[-1] in termination_list:
            return Status.TERMINATION_ERROR

        quotation_count: int = 0
        number_buffer: str = ""  # Stores the number temporarily for parsing later
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
            elif i.isdigit():
                number_mode = True
                number_buffer += i
                
            if i == '"':
                    quotation_count += 1
                    continue
            # Check if there are periods in sentence (aside from the last one)
            elif i == '.':
                return Status.PERIOD_ERROR
        
        # Check if quotations_count is even
        if quotation_count % 2 == 1:
            return Status.QUOTATION_ERROR
            
        return Status.OK
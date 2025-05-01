class Scanner:
    @classmethod
    def read_int(self, given_input: any) -> int:
        """
        Reads the argument given_input and
        checks whether type is of int.

        Arguments:
            given_input: any input passed through
                         the function

        Returns:
            int(given_input) if type(given_input)
            is int else None
        """
        try:
            given_input = int(given_input)
            return given_input
        except ValueError:
            print("Input should be an interger!")

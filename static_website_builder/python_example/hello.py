def hello(inputString):
    """
    **Description**:

       This is an example of a method documented in the google docstrings format
       (https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

       This is describing how to run a simple hello-world style method that takes a single  input

    ----
        **Parameters**
        :param inputString: value to print in the return of the method
        :type inputString: any

    ----
        **Exceptions**

        No Exceptions  are specified in the method
    ----
        **Returns**

       No return is created but a string is printed to the console
    """
    return f"Hello {inputString}"

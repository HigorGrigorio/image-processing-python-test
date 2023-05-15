class MissingParameter(Exception):
    def __init__(self, parameter):
        super().__init__(f'Missing parameter: {parameter}')

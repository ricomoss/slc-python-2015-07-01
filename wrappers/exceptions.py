class RandomWrapperException(Exception):
    def __init__(self):
        msg = 'Oh, my.  You just had a random exception!'
        super(RandomWrapperException, self).__init__(msg)


class ExhaustedWrapperException(Exception):
    def __init__(self):
        msg = 'All wrappers have been exhausted with no meaningful responses.'
        super(ExhaustedWrapperException, self).__init__(msg)

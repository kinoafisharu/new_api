
class BaseProcessor():

    def __init__(self, *args, **kwargs):
        self.item = kwargs.pop('item', None)
        

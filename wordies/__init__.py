from .letters import Letters

class Wordie:
    """Class for wordie.
    
    Args:
        a (int): The first number.
        b (float, optional): The second number. Defaults to 1.0.
    
    Attributes:
        a (int): The first number.
    """
    def __init__(self, a: int, b: float=1.0):
        self.a = a
        self._b = b
    
    def my_method(self, c: str):
        """My method.
        
        Args:
            c (str): The c.
        """
        pass

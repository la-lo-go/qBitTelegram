import datetime
from dataclasses import dataclass

@dataclass
class Message():
    """Message class for a message received to the bot."""    
    type: str
    data: object
    time: datetime.datetime = datetime.datetime.now() 
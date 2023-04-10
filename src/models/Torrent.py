from dataclasses import dataclass

@dataclass
class Torrent():
    magnet: str
    tag: str = None
    added: bool = False
from dataclasses import dataclass


@dataclass()
class Post:
    user: str
    likes: int = 0

b1 = Post('Hello World', 2)
print(b1)
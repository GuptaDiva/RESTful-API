from pydantic import BaseModel

class Comment(BaseModel):
    post_id: str
    text: str
    likes: int = 0
    dislikes: int = 0

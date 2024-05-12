from fastapi import APIRouter, HTTPException
from bson import ObjectId
from ..models.comment import Comment
from ..db import db

router = APIRouter()

@router.post("/")
async def create_comment(comment: Comment):
    result = await db.comments.insert_one(comment.dict())
    new_comment = await db.comments.find_one({"_id": result.inserted_id})
    new_comment['_id'] = str(new_comment['_id'])
    return new_comment

@router.get("/{post_id}")
async def read_comments(post_id: str):
    comments = []
    async for comment in db.comments.find({"post_id": post_id}):
        comment['_id'] = str(comment['_id'])
        comments.append(comment)
    return comments

@router.put("/{comment_id}")
async def update_comment(comment_id: str, comment: Comment):
    result = await db.comments.update_one({"_id": ObjectId(comment_id)}, {"$set": comment.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment updated successfully"}

@router.put("/{comment_id}/like")
async def like_comment(comment_id: str):
    result = await db.comments.update_one({"_id": ObjectId(comment_id)}, {"$inc": {"likes": 1}})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment liked successfully"}

@router.put("/{comment_id}/dislike")
async def dislike_comment(comment_id: str):
    result = await db.comments.update_one({"_id": ObjectId(comment_id)}, {"$inc": {"dislikes": 1}})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment disliked successfully"}

from fastapi import APIRouter, HTTPException
from bson import ObjectId
from bson.errors import InvalidId
from ..models.post import Post
from ..db import db

router = APIRouter()

@router.post("/")
async def create_post(post: Post):
    result = await db.posts.insert_one(post.dict())
    new_post = await db.posts.find_one({"_id": result.inserted_id})
    new_post['_id'] = str(new_post['_id'])
    return new_post

@router.get("/{post_id}")
async def read_post(post_id: str):
    try:
        post = await db.posts.find_one({"_id": ObjectId(post_id)})
        if post:
            post['_id'] = str(post['_id'])
            return post
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except InvalidId:
        raise HTTPException(status_code=422, detail="Invalid post ID format")

@router.get("/")
async def read_all_posts():
    posts = []
    async for post in db.posts.find():
        post['_id'] = str(post['_id'])
        posts.append(post)
    return posts

@router.put("/{post_id}")
async def update_post(post_id: str, post: Post):
    result = await db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": post.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post updated successfully"}

@router.delete("/{post_id}")
async def delete_post(post_id: str):
    result = await db.posts.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}

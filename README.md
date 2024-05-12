# Blogging Platform API

This is a RESTful API for a simple blogging platform built using the FastAPI framework in Python. The API allows users to perform CRUD operations on blog posts, comment on posts, and like/dislike comments. Data is stored in a MongoDB database.

## Setup Instructions

1. **Clone the Repository:**
   Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install dependencies:
   ```
   pip install fastapi uvicorn motor python-dotenv
   ```

3. **Create `.env` file:**
   Create a `.env` file in the project src directory with the following content:
    ```
    MONGODB_URL=<your_mongodb_url>
    ```

4. **Run the API:**
   Start the API server using Uvicorn:
   ```
   uvicorn main:app --reload
   ```

## API Documentation

### Posts

- **Create Post:** `POST /posts/`
  - Create a new post with a title and content.
- **Read Post:** `GET /posts/{post_id}`
  - Retrieve details of a specific post by ID.
- **Read All Posts:** `GET /posts/`
  - Retrieve details of all posts.
- **Update Post:** `PUT /posts/{post_id}`
  - Update an existing post by ID.
- **Delete Post:** `DELETE /posts/{post_id}`
  - Delete a post by ID.

### Comments

- **Create Comment:** `POST /comments/`
  - Create a new comment associated with a post.
- **Read Comments:** `GET /comments/{post_id}`
  - Retrieve all comments associated with a specific post by ID.
- **Update Comment:** `PUT /comments/{comment_id}`
  - Update an existing comment by ID.
- **Like Comment:** `PUT /comments/{comment_id}/like`
  - Increment the like count of a comment by ID.
- **Dislike Comment:** `PUT /comments/{comment_id}/dislike`
  - Increment the dislike count of a comment by ID.

## Data Models

### Post
```python
{
  "title": str,   # Title of the post
  "content": str  # Content of the post
}
```

### Comment
```python
{
  "post_id": str,  # ID of the post to which the comment belongs
  "text": str,     # Text content of the comment
  "likes": int,    # Number of likes for the comment
  "dislikes": int  # Number of dislikes for the comment
}
```

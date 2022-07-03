from fastapi import APIRouter

from src.posts.graphic_data_service.by_tags.getData import (get_post_numbers_by_tag)

router = APIRouter()


@router.get('/posts/byTags')
async def posts_by_tags():
  tags, post_by_tags = await get_post_numbers_by_tag()
  return {"tags": tags, "postByTags": post_by_tags}
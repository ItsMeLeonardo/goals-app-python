from src.posts.collection import (post_collection)

## pipelines
posts_by_tag_pipeline = [
  {
    '$lookup': {
      'from': 'tags',
      'localField': 'tags',
      'foreignField': '_id',
      'as': 'tags'
    }
  }, {
    '$project': {
      'title': 1,
      'tags': '$tags.name'
    }
  }, {
    '$unwind': {
      'path': '$tags'
    }
  }, {
    '$group': {
      '_id': '$tags',
      'posts_numbers': {
        '$sum': 1
      }
    }
  }
]


async def get_post_numbers_by_tag():
  tag_names = []
  posts_number_by_tags = []

  async for post in post_collection.aggregate(posts_by_tag_pipeline):
    tag_names.append(post['_id'])
    posts_number_by_tags.append(post['posts_numbers'])

  return tag_names, posts_number_by_tags

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogWebsite.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Category, Post, Comment

# 1. User Table
users_data = [
    ("johnsmith", "johnsmith@example.com"),
    ("emilyjones", "emilyjones@example.com"),
    ("davidwilson", "davidwilson@example.com"),
    ("sarahbrown", "sarahbrown@example.com"),
    ("michaelscott", "michaelscott@example.com"),
    ("lisajohnson", "lisajohnson@example.com"),
    ("alexturner", "alexturner@example.com"),
    ("jessicabaker", "jessicabaker@example.com"),
    ("matthewwright", "matthewwright@example.com"),
    ("oliviawalker", "oliviawalker@example.com"),
]
for u, e in users_data:
    User.objects.get_or_create(username=u, email=e)

# 2. Category Table
categories_data = [
    "Programming", "Productivity", "Travel", "Art", "Technology",
    "Health", "Books", "Design", "Wellness", "Self-Improvement"
]
for c in categories_data:
    Category.objects.get_or_create(name=c)

# 3. Post Table
posts_data = [
    {"id": 1, "title": "Introduction to Django", "content": "Lorem ipsum dolor sit amet", "category": "Programming", "date_published": "2023-01-01 00:00:00"},
    {"id": 2, "title": "Tips for Effective Time Management", "content": "Lorem ipsum dolor sit amet", "category": "Productivity", "date_published": "2023-01-05 00:00:00"},
    {"id": 3, "title": "Exploring the Wonders of Nature", "content": "Lorem ipsum dolor sit amet", "category": "Travel", "date_published": "2023-01-10 00:00:00"},
    {"id": 4, "title": "The Art of Photography", "content": "Lorem ipsum dolor sit amet", "category": "Art", "date_published": "2023-01-15 00:00:00"},
    {"id": 5, "title": "Understanding Machine Learning Algorithms", "content": "Lorem ipsum dolor sit amet", "category": "Technology", "date_published": "2023-01-20 00:00:00"},
    {"id": 6, "title": "Healthy Eating Habits for a Balanced Lifestyle", "content": "Lorem ipsum dolor sit amet", "category": "Health", "date_published": "2023-01-25 00:00:00"},
    {"id": 7, "title": "Exploring the World of Literature", "content": "Lorem ipsum dolor sit amet", "category": "Books", "date_published": "2023-02-01 00:00:00"},
    {"id": 8, "title": "Mastering the Basics of Graphic Design", "content": "Lorem ipsum dolor sit amet", "category": "Design", "date_published": "2023-02-05 00:00:00"},
    {"id": 9, "title": "The Benefits of Yoga and Meditation", "content": "Lorem ipsum dolor sit amet", "category": "Wellness", "date_published": "2023-02-10 00:00:00"},
    {"id": 10, "title": "The Power of Positive Thinking", "content": "Lorem ipsum dolor sitamet", "category": "Self-Improvement", "date_published": "2023-02-15 00:00:00"},
]
for p in posts_data:
    cat = Category.objects.get(name=p["category"])
    Post.objects.get_or_create(id=p["id"], title=p["title"], content=p["content"], category=cat, date_published=p["date_published"])

# 4. Comment Table
comments_data = [
    {"post_id": 1, "user_id": 2, "content": "Great introduction to Django!"},
    {"post_id": 1, "user_id": 5, "content": "Very informative article."},
    {"post_id": 2, "user_id": 3, "content": "These tips are really helpful."},
    {"post_id": 3, "user_id": 7, "content": "I love traveling and exploring nature!"},
    {"post_id": 4, "user_id": 4, "content": "Beautifully written article about photography."},
    {"post_id": 6, "user_id": 8, "content": "Healthy eating is so important for overall well-being."},
    {"post_id": 7, "user_id": 9, "content": "I enjoy reading different genres of books."},
    {"post_id": 8, "user_id": 10, "content": "Graphic design is such a creative field."},
    {"post_id": 9, "user_id": 6, "content": "Yoga and meditation have changed my life."},
    {"post_id": 10, "user_id": 1, "content": "Positive thinking can make a huge difference in one's life."},
]
for c in comments_data:
    post = Post.objects.get(id=c["post_id"])
    user = User.objects.get(id=c["user_id"])
    Comment.objects.get_or_create(post=post, user=user, content=c["content"])

print("Data inserted successfully!")
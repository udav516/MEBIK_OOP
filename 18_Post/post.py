import datetime


class Post:
    def __init__(self, author):
        self.author = author
        self.timestamp = datetime.datetime.now()
        self.likes = 0
        self.text = ""
        self.comments = []

    def add_like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        return f"Автор: {self.author}\nВремя: {self.timestamp}\nЛайки: {self.likes}\nТекст: {self.text}\nКомментарии: {self.comments}"


post = Post("Сергей Дорохов")
post.text = "Примерный пост."
post.add_like()
post.add_comment("Отличный пост!")
print(post)

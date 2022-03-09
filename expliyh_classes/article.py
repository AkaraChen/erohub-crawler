import json


class Article:
    def __init__(self, name, link, cover, category, content):
        self.name = name
        self.link = link
        self.cover = cover
        self.category = category
        self.content = content
        return

    def gen_dict(self):
        dic = {
            'name': self.name,
            'link': self.link,
            'cover': self.cover,
            'category': self.category,
            'content': self.content
        }
        return dic

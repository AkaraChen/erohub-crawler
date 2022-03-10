class Article:
    def __init__(self, title, link, cover, category, content, date):
        self.title = title
        self.link = link
        self.cover = cover
        self.category = category
        self.content = content
        self.date = date
        return

    def gen_dict(self):
        dic = {
            'title': self.title,
            'stamp':self.date
            'link': self.link,
            'cover': self.cover,
            'category': self.category,
            'content': self.content
        }
        return dic

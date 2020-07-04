from datetime import datetime
import re
import random

class Article:
    current_id = 0

    def __init__(self, title, author, content, publication_date):
        self.title = title
        self.author = author
        self.content = content
        self.publication_date = publication_date
        self.id = self.current_id
        self.last_edited = None
        Article.current_id += 1

    def __repr__(self):
        return f'<Article title={repr(self.title)} author={repr(self.author)} ' \
               f'publication_date={repr(self.publication_date.isoformat())}>'

    def __len__(self):
        return len(self.content)

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    def short_introduction(self, n_characters: int):
        if self.content[-n_characters] != ' ' or self.content[-n_characters] != '\n':
            last_space = self.content[:n_characters].rfind(' ')
            last_line = self.content[:n_characters].rfind('\n')
            return self.content[:max(last_space, last_line)]
        else:
            return self.content[:n_characters]

    def most_common_words(self, n_words):
        first_dict = {}
        output = {}
        for each in re.split('[^A-Za-z]', self.content):
            if each != '':
                each = each.lower()
                if each in first_dict:
                    first_dict[each] += 1
                else:
                    first_dict[each] = 1

        for i in range(n_words):
            this_max = max(first_dict, key=first_dict.get)
            output[this_max] = first_dict[this_max]
            del first_dict[this_max]
        return output

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, value):
        self.last_edited = datetime.now()


articles = []

# for i in range(15):
#     articles.append(Article(f'generated{i}',
#                             f'{random.choice(["mr.", "mrs."])} generated{i}', f'{random.randint(0, 12387646)}, {random.randint(0, 12387646)}, {random.randint(0, 12387646)}', datetime(random.randint(1, 2020), random.randint(1, 12), random.randint(1, 31))))

test1 = Article('title1', 'author1', 'bahla alsdfoaiu enasdjfh', datetime.now())

#test1.test_attribute = 'asdhfh'

print(test1.content)

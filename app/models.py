class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self, id, name, description,url):
        self.id =id
        self.name = name
        self.description = description
        self.url = url


class Articles:
    '''
    defines the articles objects
    '''

    def __init__(self, id, title, author, description, urlToImage, publishedAt, url):
        self.title = title
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url
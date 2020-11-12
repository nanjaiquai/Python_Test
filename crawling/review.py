import urllib.request
from bs4 import BeautifulSoup

class Review:
    def __init__(self, comment, date, star, good, bad):
        self.comment = comment
        self.date = date
        self.star = star
        self.good = good
        self.bad = bad

    def show(self):
        print("내용: " + self.comment +
        "\n날짜: " + self.date +
        "\n별점: " + self.star +
        "\n좋아요: " + self.good +
        "\n싫어요: " + self.bad)

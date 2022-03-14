import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    page_count = 0
    book_count = 1

    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/category&sort=purchased_365&order=DESC&filter_category_all=true&path=1&filter_in_stock=1"
    ]

    def parse(self, response, **kwargs):
        book_names = response.css("div.name.ellipsis a::attr(title)").extract()
        author_names = response.css("div.author.compact.ellipsis a::text").extract()
        publisher_names = response.css("div.publisher a span::text").extract()

        for i in zip(book_names,author_names,publisher_names):
            with open("deneme.txt", "a", encoding="utf-8") as file:
                file.write(f"{self.book_count}.\nKitap İsmi : {i[0]}\nYazar İsmi : {i[1].replace('  ','',1)}\nYayınevi : {i[2]}\n")
                file.write("*" * 100 + "\n")

            self.book_count +=1
            """yield {
                "title" : i[0],
                "author" : i[1],
                "publisher" : i[2]
            }"""

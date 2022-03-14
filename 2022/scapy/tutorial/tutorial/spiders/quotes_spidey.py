import scrapy


class QuotesSpider(scrapy.Spider):
    name = "books"

    page_count = 0
    book_count = 1

    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/category&filter_category_all=true&path=1&filter_in_stock=1&sort=purchased_365&order=DESC&page=1"
    ]

    def parse(self, response, **kwargs):
        book_names = response.css("div.name.ellipsis a::attr(title)").extract()
        author_names = response.css("div.author.compact.ellipsis a::text").extract()
        publisher_names = response.css("div.publisher a span::text").extract()

        for i in zip(book_names,author_names,publisher_names):
            with open("all_books.txt", "a", encoding="utf-8") as file:
                file.write(f"{self.book_count}.\nKitap İsmi : {i[0]}\nYazar İsmi : {i[1].replace('  ','',1)}\nYayınevi : {i[2]}\n")
                file.write("*" * 100 + "\n")

            self.book_count +=1

        self.page_count += 1
        next_url = response.css("div.links a.next::attr(href)").extract_first()

        if next_url is not None:
            yield scrapy.Request(url = next_url, callback = self.parse)

        #if next_url is not None and self.page_count != 5:
        #    yield scrapy.Request(url = next_url, callback = self.parse)

        # yield {
        #   "book_names" : book_names
        #   "author_names" : author_names
        #   "publisher_names" : publisher_names
        #}


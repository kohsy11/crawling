import requests
from bs4 import BeautifulSoup
from naverlist import extract_info
import csv

file = open("naver_books.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["title", "price", "img_src", "link", "author", "publisher"])

final_result = []
for i in range(6):
    book_html = requests.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("ol", {"class" : "basic"})

    a = book_soup.select_one('#category_section > ol')

    book_list = a.find_all("li")

    final_result = final_result + extract_info(book_list)

print(final_result)

for book in final_result:
    row = []
    row.append(book["title"])
    row.append(book["price"])
    row.append(book["img_src"])
    row.append(book["link"])
    row.append(book["author"])
    row.append(book["publisher"])
    writer.writerow(row)
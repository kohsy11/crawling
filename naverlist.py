def extract_info(book_list):
    result = []
    for book in book_list:
        
        if book.select_one('div > div > a > img') is not None:
            book_img = book.select_one('div > div > a > img')['src']
        if book.select_one('dl > dt > a') is not None :
            book_title = book.select_one('dl > dt > a').string
        if book.find("em", {"class" : "price"}) is not None :
            book_price = book.find("em", {"class" : "price"}).string
        if book.select_one('dl > dt > a') is not None:
            book_src = book.select_one('dl > dt > a')['href']
        if book.select_one('dl > dd > a') is not None :
            book_author = book.select_one('dl > dd > a').string
        if book.find('a', {'class': 'N=a:bta.publisher'}) is not None:
            book_comp = book.find('a', {'class': 'N=a:bta.publisher'}).string
        
        # print(book.find("em", {"class" : "price"}))
        
        # print(book.find("img")["src"])
        # if book.find("img")["src"] is not None :
        #     img_src = book.find("img")["src"]

        book_info = {
            "title" : book_title,
            "price" : book_price,
            "img_src" : book_img,
            "link" : book_src,
            "author" : book_author,
            "publisher" : book_comp,
        }
        result.append(book_info)
    
    print(result)
    return result
        
    #     title = book_list[0].find("a", {"class" : "N=a:bta.title"}).string
    #     price = book_list[0].find("em", {"class" : "price"}).string
    #     book_info = {
    #         "title" : title,
    #         "price" : price,
    #     }
    #     result.append(book_info)
    
    # return result

#this is a regular python file you can import from wherever you want 
import bs4


def ex_func():
    soup = bs4.BeautifulSoup("<p>Some<b>bad<i>HTML")
    return soup.prettify()

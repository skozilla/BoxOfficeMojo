__author__ = 'rastko'

import bs4
import re
import requests
import movie

BOMURL = "http://www.boxofficemojo.com"

class BoxOfficeMojo(object):
    """API client object for interacting with BoxOfficeMojo website"""

    def __init__(self):
        self.letters = ['NUM']
        self.movie_urls = {}
        self.total_movies = 0
        for i in range(65, 91):
            self.letters.append(chr(i))

    def find_number_of_pages(self, soup):
        """Returns the number of sub-pages a certain letter will have"""
        pages = soup.findAll(href=re.compile("page"))
        if len(pages) > 0:
            max_page_url = pages[-1]['href']
            max_page = re.findall("\d+", max_page_url)[0]
            return int(max_page)
        else:
            return 1

    def clean_html(self, soup):
        """Get rid of all bold, italic, underline and link tags"""
        invalid_tags = ['b', 'i', 'u', 'nobr', 'font']
        for tag in invalid_tags:
            for match in soup.findAll(tag):
                match.replaceWithChildren()

    def find_urls_in_html(self, soup):
        """Adds all the specific movie urls to the movie_urls dictionary"""
        urls = soup.findAll(href=re.compile("id="))
        # First URL is an ad for a movie so get rid of it
        del(urls[0])

        self.total_movies += len(urls)
        for url in urls:
            movie_name = url.renderContents()
            suffix = 1
            while movie_name in self.movie_urls.keys():
                movie_name = url.renderContents() + '(' + str(suffix) + ')'
                suffix += 1
            self.movie_urls[movie_name] = BOMURL + url["href"]

    def crawl_for_urls(self):
        """Gets all the movie urls and puts them in a dictionary"""
        for letter in self.letters:
            print 'Processing letter: ' + letter
            url = BOMURL + "/movies/alphabetical.htm?letter=" + letter
            r = requests.get(url)
            if r.status_code != 200:
                print r.status_code
            soup = bs4.BeautifulSoup(r.content)
            self.clean_html(soup)
            num_pages = self.find_number_of_pages(soup)
            self.find_urls_in_html(soup)
            for num in range(2, num_pages+1):
                new_url = url + "&page=" + str(num)
                r = requests.get(new_url)
                if r.status_code != 200:
                    print r.status_code
                soup = bs4.BeautifulSoup(r.content)
                self.clean_html(soup)
                self.find_urls_in_html(soup)

    def get_movie_details(self, url):
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.content)
        return movie.Movie(soup)


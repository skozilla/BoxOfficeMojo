__author__ = 'rastko'

import bs4
import re
import requests
import movie
import utils


class BoxOfficeMojo(object):
    """API client object for interacting with BoxOfficeMojo website"""

    BOMURL = "http://www.boxofficemojo.com/movies"

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
            #save only the movie ids
            a = re.findall(r'id=((\w|[-(),\':\s.])+).htm', url["href"])
            if len(a) == 1:
                self.movie_urls[a[0][0]] = movie_name

    def crawl_for_urls(self):
        """Gets all the movie urls and puts them in a dictionary"""
        for letter in self.letters:
            print 'Processing letter: ' + letter
            url = self.BOMURL + "/alphabetical.htm?letter=" + letter
            r = requests.get(url)
            if r.status_code != 200:
                print "HTTP Status code returned:", r.status_code
            soup = bs4.BeautifulSoup(r.content)
            self.clean_html(soup)
            num_pages = self.find_number_of_pages(soup)
            self.find_urls_in_html(soup)
            for num in range(2, num_pages+1):
                new_url = url + "&page=" + str(num)
                r = requests.get(new_url)
                if r.status_code != 200:
                    print "HTTP Status code returned:", r.status_code
                soup = bs4.BeautifulSoup(r.content)
                self.clean_html(soup)
                self.find_urls_in_html(soup)

    @utils.catch_connection_error
    def get_movie_summary(self, url_or_id):
        if 'http' in url_or_id.lower():
            soup = utils.get_soup(url_or_id)
            if soup is not None:
                return movie.Movie(soup)
            else:
                print "Not able to parse url: " + url_or_id
                pass
        elif url_or_id in self.movie_urls.keys():
            url = self.BOMURL + "/?page=main&id=" + url_or_id + ".htm"
            soup = utils.get_soup(url)
            if soup is not None:
                return movie.Movie(soup)
            else:
                print "Not able to parse url: " + url
                pass
        else:
            print "Invalid movie name or URL ", url_or_id

    @utils.catch_connection_error
    def get_weekly_summary(self, url_or_id):
        if 'http' in url_or_id.lower():
            soup = utils.get_soup(url_or_id)
            if soup is not None:
                return movie.Weekly(soup)
            else:
                print "Not able to parse url: " + url_or_id
                pass
        elif url_or_id in self.movie_urls.keys():
            url = self.BOMURL + "/?page=weekly&id=" + url_or_id + ".htm"
            soup = utils.get_soup(url)
            if soup is not None:
                return movie.Weekly(soup)
            else:
                print "Not able to parse url: " + url
                pass
        else:
            print "Invalid movie name or URL ", url_or_id

    def get_all_movies(self):
        for key, val in self.movie_urls.iteritems():
            movie = self.get_movie_details(key)
            movie.clean_data()
            print movie.to_json()


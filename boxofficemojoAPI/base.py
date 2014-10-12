__author__ = 'rastko'

import bs4
import json
from bson import json_util

class MovieBase(object):

    def __init__(self, html_soup):
        """Movie class which parses html BeautifulSoup object and extracts information about the movie"""

        self.data = {}
        assert isinstance(html_soup, bs4.BeautifulSoup)
        self.soup = html_soup

        self.clean_html()
        self.extract_data()

    def clean_html(self):
        """Get rid of all bold, italic, underline, link tags, script tag, img tag, etc"""
        invalid_tags = ['a', 'b', 'i', 'u', 'nobr', 'font']
        for tag in invalid_tags:
            for match in self.soup.findAll(tag):
                match.replaceWithChildren()

        # delete all contents in script and img tags
        [x.extract() for x in self.soup.findAll('script')]
        [x.extract() for x in self.soup.findAll('img')]
        [x.extract() for x in self.soup.findAll('br')]
        [x.extract() for x in self.soup.findAll('div', id='hp_banner')]
        [x.extract() for x in self.soup.findAll('ul', id='leftnav')]

    def print_to_file(self, file_name):
        """"Print a pretty and clean html string to a file"""
        f = open(file_name, 'w')
        f.write(self.soup.prettify().encode('utf8'))
        f.close()

    def extract_data(self):
        pass

    def clean_data(self):
        pass

    def to_json(self):
        """Returns a JSON string of the Data member"""
        return json.dumps(self.data, indent=4, sort_keys=True, default=json_util.default)
__author__ = 'rastko'

import bs4
import re
import json
import time

from . import utils


class Movie(object):
    def __init__(self, html_soup):
        """Movie class which parses html BeautifulSoup object and extracts information about the movie"""

        self.Data = {}

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
        """Extract all the relevant information from the html file"""
        title = self.soup.title.contents[0].encode('utf8')
        self.Data["Title"] = title.replace(" - Box Office Mojo", "")
        try:
            center = self.soup.findAll("center")

            if len(center) == 0:
                pass

            table = center[0].find("table")

            if len(center) is None:
                pass

            rows = table.findAll('tr')
            for tr in rows:
                cols = tr.findAll('td')
                contents = [a.renderContents() for a in cols]
                for con in contents:
                    keyval = con.split(":")
                    key = keyval[0]
                    val = keyval[1].strip()
                    self.Data[key] = val

            tables = self.soup.find_all("div", "mp_box")

            for table in tables:
                box_table_name = table.find("div", "mp_box_tab").string

                if box_table_name == "Total Lifetime Grosses":
                    rows = table.findAll('tr')
                    for tr in rows:
                        cols = tr.findAll('td')
                        if len(cols) > 1:
                            contents = [re.sub(r'[(\xc2|\xa0|+|=|:|$|,)]', '', a.renderContents()) for a in cols]
                            key = contents[0]
                            val = contents[1]
                            self.Data[key] = val

                elif box_table_name == "Domestic Summary":
                    pass

                elif box_table_name == "The Players":
                    # Exclude any results which are just whitespaces or cast member descriptors (i.e. (Voice), (Minor role))
                    exclude_pattern = '(^\s*\(.+\)|^\s+$)'
                    rows = table.findAll('tr')
                    for tr in rows:
                        cols = tr.findAll('td')
                        if len(cols) > 1:
                            key = cols[0].text
                            val = cols[1]
                            key = key.replace(':', '')
                            if key[-1] != 's':
                                key += 's'
                            self.Data[key] = [re.sub('\*+\s*$', '', child.encode('utf-8')) for child in val.children
                                              if re.search(exclude_pattern, child) is None]
                else:
                    pass
        except:
            print "Error parsing movie: ", title
            raise

    def clean_data(self):
        """Formats all the extracted data into the appropriate types"""
        self._convert_financial_field("Domestic")
        self._convert_financial_field("Worldwide")
        self._convert_financial_field("Foreign")
        self._convert_financial_field("Production Budget")
        #self._convert_date_field("Release Date")
        self._convert_runtime_field("Runtime")
        for key, value in self.Data.iteritems():
            if "Total Gross" in key:
                self.Data.pop(key)
                break

    @utils.na_or_empty
    def _convert_financial_field(self, key):
        """Formats financial values in the Data dictionary"""
        if key == "Production Budget":
            digits = re.findall(r'\$([\d\.\d]+)', self.Data[key])
            digits = float(digits[0])
            if 'million' in self.Data[key]:
                self.Data[key] = digits*1000000.0
            elif 'thousand' in self.Data[key]:
                self.Data[key] = digits*1000.0
            else:
                self.Data[key] = digits
        else:
            self.Data[key] = float(self.Data[key])

    @utils.na_or_empty
    def _convert_date_field(self, key):
        """Formats date values in the Data dictionary"""
        self.Data[key] = time.strptime(self.Data[key], "%B %d, %Y")

    @utils.na_or_empty
    def _convert_runtime_field(self, key):
        """Formats date values in the Data dictionary"""
        m = re.match(r"^((\d*) hrs\. )?(\d*)", self.Data[key])
        if m.group(2) is None:
            self.Data[key] = int(m.group(3))
        else:
            self.Data[key] = int(m.group(2))*60 + int(m.group(3))

    def to_json(self):
        """Returns a JSON string of the Data member"""
        return json.dumps(self.Data, indent=4, sort_keys=True)
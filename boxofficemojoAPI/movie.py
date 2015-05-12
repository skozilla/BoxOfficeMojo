__author__ = 'rastko'

import bs4
import re
import json
from bson import json_util

from . import utils
from base import MovieBase


class Movie(MovieBase):
    def __init__(self, html_soup):
        """Movie class which parses html BeautifulSoup object and extracts information about the movie"""

        MovieBase.__init__(self, html_soup)

    def extract_data(self):
        """Extract all the relevant information from the html file"""
        title = self.soup.title.contents[0].encode('utf8')
        self.data["Title"] = title.replace(" - Box Office Mojo", "")
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
                    self.data[key] = val

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
                            self.data[key] = val

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
                            self.data[key] = [re.sub('\*+\s*$', '', child.encode('utf-8')) for child in val.children
                                              if re.search(exclude_pattern, child) is None]
                else:
                    pass
        except:
            print "Error parsing movie: ", title
            raise

    def clean_data(self):
        """Formats all the extracted data into the appropriate types"""
        utils.convert_financial_field(self.data, "Domestic")
        utils.convert_financial_field(self.data, "Worldwide")
        utils.convert_financial_field(self.data, "Foreign")
        utils.convert_financial_field(self.data, "Production Budget")
        utils.convert_date_field(self.data, "Release Date")
        utils.convert_runtime_field(self.data, "Runtime")

        for key, value in self.data.iteritems():
            if "Total Gross" in key or "." in key:
                self.data.pop(key)
                break
        utils.standardize_keys(self.data)


class Weekly(MovieBase):
    def __init__(self, html_soup):
        """Movie class which parses html BeautifulSoup object and extracts information about the movie"""

        MovieBase.__init__(self, html_soup)

    def extract_data(self):
        """Extract all the relevant information from the html file"""
        title = self.soup.title.contents[0].encode('utf8')
        self.data["Title"] = title.replace(" - Weekly Box Office Results - Box Office Mojo", "")
        try:
            center = self.soup.findAll("center")

            x = center[1].contents[0::2]
            years = [year.encode('utf-8') for year in x]

            tables = self.soup.find_all("table", "chart-wide")

            results_collection = []
            year = 0
            if len(tables) == 0:
                self.data["Weekly"] = None
                pass

            for table in tables:
                rows = table.findAll("tr")
                del(rows[0])

                for tr in rows:
                    results_week = {}
                    cols = tr.findAll("td")
                    results_week["Week"] = re.sub(ur'(\u2013|\u0096)[\s\w\s]+', '', cols[0].renderContents().decode("utf-8")) + ", " + years[year]
                    results_week["Rank"] = cols[1].renderContents()
                    results_week["Gross"] = cols[2].renderContents()
                    results_week["Week Over Week Change"] = cols[3].renderContents()
                    results_week["Theaters"] = cols[4].renderContents()
                    results_week["Theatre Change"] = cols[5].renderContents()
                    results_week["Average Per Theatre"] = cols[6].renderContents()
                    results_week["Gross To Date"] = cols[7].renderContents()
                    results_week["Week Number"] = cols[8].renderContents()
                    results_collection.append(results_week)
                year += 1

            self.data["Weekly"] = results_collection
        except:
            print "Error parsing movie: ", title
            raise

    def clean_data(self):
        """Formats all the extracted data into the appropriate types"""

        for results in self.data["Weekly"]:
            utils.convert_financial_field(results, "Average Per Theatre")
            utils.convert_financial_field(results, "Gross")
            utils.convert_financial_field(results, "Gross To Date")
            utils.convert_percent_field(results, "Week Over Week Change")
            utils.convert_date_field(results, "Week")
            utils.convert_int_field(results, "Rank")
            utils.convert_int_field(results, "Theaters")
            utils.convert_int_field(results, "Theatre Change")
            utils.convert_int_field(results, "Week Number")

        for key, value in self.data.iteritems():
            if "Total Gross" in key or "." in key:
                self.data.pop(key)
                break
        utils.standardize_keys(self.data)

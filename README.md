BoxOfficeMojo
=============

A simple python module for scrapping movie information from www.boxofficemojo.com

The module is used to extract information for any movie in the www.boxofficemojo.com domain. The information that it obtains
includes financial information (domestic gross, foreign gross, budget), cast, directors, composers, runtime, raiting, etc..
Not all the information is present on their website, so it gets what it can. 

### Example 

```python
import boxofficemojoAPI as bom

box_office_mojo = bom.BoxOfficeMojo()
box_office_mojo.crawl_for_urls()


movie = box_office_mojo.get_movie_details("Titanic")
movie.clean_data()
print movie.to_json()

```

the output would be 

'''json
{
    "Actors": [
        "Leonardo DiCaprio", 
        "Kate Winslet", 
        "Billy Zane", 
        "Kathy Bates", 
        "Bill Paxton", 
        "Bernard Hill", 
        "Ioan Gruffudd"
    ], 
    "Composers": [
        "James Horner"
    ], 
    "Directors": [
        "James Cameron"
    ], 
    "Distributor": "Paramount", 
    "Domestic": 658672302.0, 
    "Domestic Total Gross": "$600,788,188Domestic Lifetime Gross", 
    "Foreign": 1528100000.0, 
    "Genre": "Romance", 
    "MPAA Rating": "PG-13", 
    "Producers": [
        "Jon Landau"
    ], 
    "Production Budget": 200000000.0, 
    "Release Date": "December 19, 1997", 
    "Runtime": 194, 
    "Title": "Titanic (1997)", 
    "Worldwide": 2186772302.0, 
    "Writers": [
        "James Cameron"
    ]
}
'''

### Known Issues
Any field containing "Domestic Total Gross" as a key is redundant, as the "Domestic" field contains the correct domestic
earnings of the movie. I will fix this later

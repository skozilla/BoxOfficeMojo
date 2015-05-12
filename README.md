BoxOfficeMojo
=============

A simple python module for scrapping movie information from www.boxofficemojo.com

The module is used to extract information for any movie in the www.boxofficemojo.com domain. The information that it obtains
includes financial information (domestic gross, foreign gross, budget), cast, directors, composers, runtime, raiting, etc.. 
It could also be used to get the weekly performance of the movie in the box office. 
Not all the information is present on the website, so it gets whatever is available. 

Feel free to make suggestions about the code or the functionality, as they would be greatly appreciated. Contributions are welcome. 

### Example 

```python
import boxofficemojoAPI as bom

box_office_mojo = bom.BoxOfficeMojo()
box_office_mojo.crawl_for_urls()


movie = box_office_mojo.get_movie_summary("titanic")
movie.clean_data()
print movie.to_json()

weekly = box_office_mojo.get_weekly_summary("titanic")
weekly.clean_data()
print weekly.to_json()

```

the output would be 

```json
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

{
    "Title": "Titanic (1997)", 
    "Weekly": [
        {
            "Average Per Theatre": 19539.0, 
            "Gross": 52969336.0, 
            "Gross To Date": 52969336.0, 
            "Rank": 1, 
            "Theaters": 2711, 
            "Theatre Change": null, 
            "Week": "Dec 19, 1997", 
            "Week Number": 1, 
            "Week Over Week Change": null
        }, 
        {
            "Average Per Theatre": 26257.0, 
            "Gross": 71183357.0, 
            "Gross To Date": 124152693.0, 
            "Rank": 1, 
            "Theaters": 2711, 
            "Theatre Change": null, 
            "Week": "Dec 26, 1997", 
            "Week Number": 2, 
            "Week Over Week Change": 0.344
        }, 
        .
        .
        .
    ]
}
```

### Known Issues

The library is a work in progress and has not been tested on all movies present on BoxOfficeMojo, so it might crash sometimes. 
This library is not compatible with python 3.x

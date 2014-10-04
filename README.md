BoxOfficeMojo
=============

A simple python module for scrapping movie information from www.boxofficemojo.com

The module is used to extract information for any movie in the www.boxofficemojo.com domain. The information that it obtains
includes financial information (domestic gross, foreign gross, budget), cast, directors, composers, runtime, raiting, etc.. 
It could also be used to get the weekly performance of the movie in the box office. 
Not all the information is present on their website, so it gets what it can. 

Feel free to make suggestions about the code or the functionality, as they would be greatly appreciated. Contributions are welcome. 

### Example 

```python
import boxofficemojoAPI as bom

box_office_mojo = bom.BoxOfficeMojo()
box_office_mojo.crawl_for_urls()


movie = box_office_mojo.get_movie_summary("Titanic")
movie.clean_data()
print movie.to_json()

weekly = box_office_mojo.get_weekly_summary("Titanic")
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
        {
            "Average Per Theatre": 16506.0, 
            "Gross": 45012810.0, 
            "Gross To Date": 169165503.0, 
            "Rank": 1, 
            "Theaters": 2727, 
            "Theatre Change": 16, 
            "Week": "Jan 2, 1998", 
            "Week Number": 3, 
            "Week Over Week Change": -0.368
        }, 
        {
            "Average Per Theatre": 13681.0, 
            "Gross": 37568867.0, 
            "Gross To Date": 206734370.0, 
            "Rank": 1, 
            "Theaters": 2746, 
            "Theatre Change": 19, 
            "Week": "Jan 9, 1998", 
            "Week Number": 4, 
            "Week Over Week Change": -0.165
        }, 
        {
            "Average Per Theatre": 15405.0, 
            "Gross": 42626796.0, 
            "Gross To Date": 249361166.0, 
            "Rank": 1, 
            "Theaters": 2767, 
            "Theatre Change": 21, 
            "Week": "Jan 16, 1998", 
            "Week Number": 5, 
            "Week Over Week Change": 0.135
        }, 
        {
            "Average Per Theatre": 11848.0, 
            "Gross": 32831865.0, 
            "Gross To Date": 282193031.0, 
            "Rank": 1, 
            "Theaters": 2771, 
            "Theatre Change": 4, 
            "Week": "Jan 23, 1998", 
            "Week Number": 6, 
            "Week Over Week Change": -0.23
        }, 
        {
            "Average Per Theatre": 11264.0, 
            "Gross": 32134797.0, 
            "Gross To Date": 314327828.0, 
            "Rank": 1, 
            "Theaters": 2853, 
            "Theatre Change": 82, 
            "Week": "Jan 30, 1998", 
            "Week Number": 7, 
            "Week Over Week Change": -0.021
        }, 
        {
            "Average Per Theatre": 9833.0, 
            "Gross": 29066469.0, 
            "Gross To Date": 343394297.0, 
            "Rank": 1, 
            "Theaters": 2956, 
            "Theatre Change": 103, 
            "Week": "Feb 6, 1998", 
            "Week Number": 8, 
            "Week Over Week Change": -0.095
        }, 
        {
            "Average Per Theatre": 12702.0, 
            "Gross": 38131241.0, 
            "Gross To Date": 381525538.0, 
            "Rank": 1, 
            "Theaters": 3002, 
            "Theatre Change": 46, 
            "Week": "Feb 13, 1998", 
            "Week Number": 9, 
            "Week Over Week Change": 0.312
        }, 
        {
            "Average Per Theatre": 8591.0, 
            "Gross": 25825294.0, 
            "Gross To Date": 407350832.0, 
            "Rank": 1, 
            "Theaters": 3006, 
            "Theatre Change": 4, 
            "Week": "Feb 20, 1998", 
            "Week Number": 10, 
            "Week Over Week Change": -0.32299999999999995
        }, 
        {
            "Average Per Theatre": 7974.0, 
            "Gross": 24200714.0, 
            "Gross To Date": 431551546.0, 
            "Rank": 1, 
            "Theaters": 3035, 
            "Theatre Change": 29, 
            "Week": "Feb 27, 1998", 
            "Week Number": 11, 
            "Week Over Week Change": -0.063
        }, 
        {
            "Average Per Theatre": 7192.0, 
            "Gross": 22315779.0, 
            "Gross To Date": 453867325.0, 
            "Rank": 1, 
            "Theaters": 3103, 
            "Theatre Change": 68, 
            "Week": "Mar 6, 1998", 
            "Week Number": 12, 
            "Week Over Week Change": -0.078
        }, 
        {
            "Average Per Theatre": 7536.0, 
            "Gross": 23481767.0, 
            "Gross To Date": 477349092.0, 
            "Rank": 1, 
            "Theaters": 3116, 
            "Theatre Change": 13, 
            "Week": "Mar 13, 1998", 
            "Week Number": 13, 
            "Week Over Week Change": 0.052000000000000005
        }, 
        {
            "Average Per Theatre": 7163.0, 
            "Gross": 22699938.0, 
            "Gross To Date": 500049030.0, 
            "Rank": 1, 
            "Theaters": 3169, 
            "Theatre Change": 53, 
            "Week": "Mar 20, 1998", 
            "Week Number": 14, 
            "Week Over Week Change": -0.033
        }, 
        {
            "Average Per Theatre": 5822.0, 
            "Gross": 18824028.0, 
            "Gross To Date": 518873058.0, 
            "Rank": 1, 
            "Theaters": 3233, 
            "Theatre Change": 64, 
            "Week": "Mar 27, 1998", 
            "Week Number": 15, 
            "Week Over Week Change": -0.171
        }, 
        {
            "Average Per Theatre": 4724.0, 
            "Gross": 15422392.0, 
            "Gross To Date": 534295450.0, 
            "Rank": 2, 
            "Theaters": 3265, 
            "Theatre Change": 32, 
            "Week": "Apr 3, 1998", 
            "Week Number": 16, 
            "Week Over Week Change": -0.18100000000000002
        }, 
        {
            "Average Per Theatre": 3787.0, 
            "Gross": 12363764.0, 
            "Gross To Date": 546659214.0, 
            "Rank": 3, 
            "Theaters": 3265, 
            "Theatre Change": null, 
            "Week": "Apr 10, 1998", 
            "Week Number": 17, 
            "Week Over Week Change": -0.198
        }, 
        {
            "Average Per Theatre": 2994.0, 
            "Gross": 9017561.0, 
            "Gross To Date": 555676775.0, 
            "Rank": 4, 
            "Theaters": 3012, 
            "Theatre Change": -253, 
            "Week": "Apr 17, 1998", 
            "Week Number": 18, 
            "Week Over Week Change": -0.271
        }, 
        {
            "Average Per Theatre": 2077.0, 
            "Gross": 6047868.0, 
            "Gross To Date": 561724643.0, 
            "Rank": 4, 
            "Theaters": 2912, 
            "Theatre Change": -100, 
            "Week": "Apr 24, 1998", 
            "Week Number": 19, 
            "Week Over Week Change": -0.329
        }, 
        {
            "Average Per Theatre": 1849.0, 
            "Gross": 4917197.0, 
            "Gross To Date": 566641840.0, 
            "Rank": 6, 
            "Theaters": 2660, 
            "Theatre Change": -252, 
            "Week": "May 1, 1998", 
            "Week Number": 20, 
            "Week Over Week Change": -0.187
        }, 
        {
            "Average Per Theatre": 1755.0, 
            "Gross": 3959752.0, 
            "Gross To Date": 570601592.0, 
            "Rank": 4, 
            "Theaters": 2256, 
            "Theatre Change": -404, 
            "Week": "May 8, 1998", 
            "Week Number": 21, 
            "Week Over Week Change": -0.195
        }, 
        {
            "Average Per Theatre": 1400.0, 
            "Gross": 2785717.0, 
            "Gross To Date": 573387309.0, 
            "Rank": 7, 
            "Theaters": 1990, 
            "Theatre Change": -266, 
            "Week": "May 15, 1998", 
            "Week Number": 22, 
            "Week Over Week Change": -0.29600000000000004
        }, 
        {
            "Average Per Theatre": 2116.0, 
            "Gross": 4248586.0, 
            "Gross To Date": 577635895.0, 
            "Rank": 7, 
            "Theaters": 2008, 
            "Theatre Change": 18, 
            "Week": "May 22, 1998", 
            "Week Number": 23, 
            "Week Over Week Change": 0.525
        }, 
        {
            "Average Per Theatre": 1668.0, 
            "Gross": 2605134.0, 
            "Gross To Date": 580241029.0, 
            "Rank": 9, 
            "Theaters": 1562, 
            "Theatre Change": -446, 
            "Week": "May 29, 1998", 
            "Week Number": 24, 
            "Week Over Week Change": -0.387
        }, 
        {
            "Average Per Theatre": 1993.0, 
            "Gross": 2429418.0, 
            "Gross To Date": 582670447.0, 
            "Rank": 8, 
            "Theaters": 1219, 
            "Theatre Change": -343, 
            "Week": "Jun 5, 1998", 
            "Week Number": 25, 
            "Week Over Week Change": -0.067
        }, 
        {
            "Average Per Theatre": 1892.0, 
            "Gross": 1844218.0, 
            "Gross To Date": 584514665.0, 
            "Rank": 10, 
            "Theaters": 975, 
            "Theatre Change": -244, 
            "Week": "Jun 12, 1998", 
            "Week Number": 26, 
            "Week Over Week Change": -0.24100000000000002
        }, 
        {
            "Average Per Theatre": 2017.0, 
            "Gross": 1633956.0, 
            "Gross To Date": 586148621.0, 
            "Rank": 11, 
            "Theaters": 810, 
            "Theatre Change": -165, 
            "Week": "Jun 19, 1998", 
            "Week Number": 27, 
            "Week Over Week Change": -0.114
        }, 
        {
            "Average Per Theatre": 2318.0, 
            "Gross": 1432567.0, 
            "Gross To Date": 587581188.0, 
            "Rank": 14, 
            "Theaters": 618, 
            "Theatre Change": -192, 
            "Week": "Jun 26, 1998", 
            "Week Number": 28, 
            "Week Over Week Change": -0.12300000000000001
        }, 
        {
            "Average Per Theatre": 1529.0, 
            "Gross": 945021.0, 
            "Gross To Date": 588526209.0, 
            "Rank": 13, 
            "Theaters": 618, 
            "Theatre Change": null, 
            "Week": "Jul 3, 1998", 
            "Week Number": 29, 
            "Week Over Week Change": -0.34
        }, 
        {
            "Average Per Theatre": 1352.0, 
            "Gross": 626171.0, 
            "Gross To Date": 589152380.0, 
            "Rank": 14, 
            "Theaters": 463, 
            "Theatre Change": -155, 
            "Week": "Jul 10, 1998", 
            "Week Number": 30, 
            "Week Over Week Change": -0.337
        }, 
        {
            "Average Per Theatre": 3006.0, 
            "Gross": 2605789.0, 
            "Gross To Date": 591758169.0, 
            "Rank": 12, 
            "Theaters": 867, 
            "Theatre Change": 404, 
            "Week": "Jul 17, 1998", 
            "Week Number": 31, 
            "Week Over Week Change": 3.16
        }, 
        {
            "Average Per Theatre": 3028.0, 
            "Gross": 2540298.0, 
            "Gross To Date": 594298467.0, 
            "Rank": 14, 
            "Theaters": 839, 
            "Theatre Change": -28, 
            "Week": "Jul 24, 1998", 
            "Week Number": 32, 
            "Week Over Week Change": -0.025
        }, 
        {
            "Average Per Theatre": 2629.0, 
            "Gross": 2022007.0, 
            "Gross To Date": 596320474.0, 
            "Rank": 15, 
            "Theaters": 769, 
            "Theatre Change": -70, 
            "Week": "Jul 31, 1998", 
            "Week Number": 33, 
            "Week Over Week Change": -0.204
        }, 
        {
            "Average Per Theatre": 2330.0, 
            "Gross": 1586588.0, 
            "Gross To Date": 597907062.0, 
            "Rank": 13, 
            "Theaters": 681, 
            "Theatre Change": -88, 
            "Week": "Aug 7, 1998", 
            "Week Number": 34, 
            "Week Over Week Change": -0.215
        }, 
        {
            "Average Per Theatre": 2037.0, 
            "Gross": 1210134.0, 
            "Gross To Date": 599117196.0, 
            "Rank": 17, 
            "Theaters": 594, 
            "Theatre Change": -87, 
            "Week": "Aug 14, 1998", 
            "Week Number": 35, 
            "Week Over Week Change": -0.237
        }, 
        {
            "Average Per Theatre": 1616.0, 
            "Gross": 921292.0, 
            "Gross To Date": 600038488.0, 
            "Rank": 16, 
            "Theaters": 570, 
            "Theatre Change": -24, 
            "Week": "Aug 21, 1998", 
            "Week Number": 36, 
            "Week Over Week Change": -0.239
        }, 
        {
            "Average Per Theatre": 862.0, 
            "Gross": 432673.0, 
            "Gross To Date": 600471161.0, 
            "Rank": 18, 
            "Theaters": 502, 
            "Theatre Change": -68, 
            "Week": "Aug 28, 1998", 
            "Week Number": 37, 
            "Week Over Week Change": -0.53
        }, 
        {
            "Average Per Theatre": 246.0, 
            "Gross": 109840.0, 
            "Gross To Date": 600581001.0, 
            "Rank": 17, 
            "Theaters": 447, 
            "Theatre Change": -55, 
            "Week": "Sep 4, 1998", 
            "Week Number": 38, 
            "Week Over Week Change": -0.746
        }, 
        {
            "Average Per Theatre": 236.0, 
            "Gross": 79689.0, 
            "Gross To Date": 600660690.0, 
            "Rank": 13, 
            "Theaters": 337, 
            "Theatre Change": -110, 
            "Week": "Sep 11, 1998", 
            "Week Number": 39, 
            "Week Over Week Change": -0.27399999999999997
        }, 
        {
            "Average Per Theatre": 365.0, 
            "Gross": 17894.0, 
            "Gross To Date": 600678584.0, 
            "Rank": 15, 
            "Theaters": 49, 
            "Theatre Change": -288, 
            "Week": "Sep 18, 1998", 
            "Week Number": 40, 
            "Week Over Week Change": -0.775
        }, 
        {
            "Average Per Theatre": 172.0, 
            "Gross": 4473.0, 
            "Gross To Date": 600683057.0, 
            "Rank": 15, 
            "Theaters": 26, 
            "Theatre Change": -23, 
            "Week": "Sep 25, 1998", 
            "Week Number": 41, 
            "Week Over Week Change": -0.75
        }
    ]
}
```

### Known Issues

The library is a work in progress and has not been tested on all movies present on BoxOfficeMojo, so it might crash sometimes. 
This library is not compatible with python 3.x

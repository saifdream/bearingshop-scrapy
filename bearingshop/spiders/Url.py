import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class ProductUrl(scrapy.Spider):
    name = 'product-url'
    start_urls = [
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html",
        "http://www.bearingshop.org/radial-roller-bearings/spherical-roller-bearings.html",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-angular-contact-ball-bearings.html",
        "http://www.bearingshop.org/combined-axial-radial-bearings-22/needle-roller-axial-cylindrical-roller-bearings.html",
        "http://www.bearingshop.org/pillow-block-bearings.html",
        "http://www.bearingshop.org/rotary-table-bearings.html",
        "http://www.bearingshop.org/crossed-roller-bearings.html",
        "http://www.bearingshop.org/linear-bearing.html",
        "http://www.bearingshop.org/linear-guide.html",
        "http://www.bearingshop.org/track-rollers.html",
        "http://www.bearingshop.org/plain-bearings.html",
        "http://www.bearingshop.org/bicycle-bearings.html",
        "http://www.bearingshop.org/skate-bearings.html",
        "http://www.bearingshop.org/belts-pulleys.html",
        "http://www.bearingshop.org/electric-motors.html",
        "http://www.bearingshop.org/hand-spinner.html",
        "http://www.bearingshop.org/clamp.html",
        "http://www.bearingshop.org/mro-1.html",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=2",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=3",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=4",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=5",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=6",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=7",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=8",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=9",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=10",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=11",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=12",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=13",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=14",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=15",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=16",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=17",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=18",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=19",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=20",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=21",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=22",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=23",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=24",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=25",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=26",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=27",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=28",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=29",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=30",
        "http://www.bearingshop.org/radial-roller-bearings/cylindrical-roller-bearings.html?p=31",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=2",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=3",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=4",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=5",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=6",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=7",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=8",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=9",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=10",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=11",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=12",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=13",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=14",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=15",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=16",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=17",
        "http://www.bearingshop.org/radial-ball-bearings/deep-groove-ball-bearings.html?p=18",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=2",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=3",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=4",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=5",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=6",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=7",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=8",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=9",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=10",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=11",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=12",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=13",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=14",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=15",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=16",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=17",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=18",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=19",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=20",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=21",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=22",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=23",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=24",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=25",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=26",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=27",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=28",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=29",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=30",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=31",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=32",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=33",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=34",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=35",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=36",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=37",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=38",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=39",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=40",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=41",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=42",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=43",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=44",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=45",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=46",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=47",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=48",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=49",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=50",
        "http://www.bearingshop.org/radial-ball-bearings/radial-insert-ball-bearings.html?p=51",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=2",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=3",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=4",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=5",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=6",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=7",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=8",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=9",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=10",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=11",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=12",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=13",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=14",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=15",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=16",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=17",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=18",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=19",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=20",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=21",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=22",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=23",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=24",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=25",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=26",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=27",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=28",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=29",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=30",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=31",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=32",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=33",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=34",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=35",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=36",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=37",
        "http://www.bearingshop.org/radial-ball-bearings/angular-contact-ball-bearings.html?p=38",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=2",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=3",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=4",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=5",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=6",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=7",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=8",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=9",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=10",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=11",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=12",
        "http://www.bearingshop.org/axial-ball-bearings/thrust-deep-groove-ball-bearings.html?p=13",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=2",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=3",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=4",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=5",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=6",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=7",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=8",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=9",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=10",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=11",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=12",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=13",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=14",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=15",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=16",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=17",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=18",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=19",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=20",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=21",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=22",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=23",
        "http://www.bearingshop.org/radial-roller-bearings/tapered-roller-bearings.html?p=24",
        "http://www.bearingshop.org/combined-axial-radial-bearings-22/needle-roller-axial-cylindrical-roller-bearings.html?p=2",
        "http://www.bearingshop.org/linear-guide.html?p=2",
        "http://www.bearingshop.org/linear-guide.html?p=3",
        "http://www.bearingshop.org/linear-guide.html?p=4",
        "http://www.bearingshop.org/linear-guide.html?p=5",
        "http://www.bearingshop.org/linear-guide.html?p=6",
        "http://www.bearingshop.org/linear-guide.html?p=7",
        "http://www.bearingshop.org/linear-guide.html?p=8",
        "http://www.bearingshop.org/linear-guide.html?p=9",
        "http://www.bearingshop.org/linear-bearing.html?p=2",
        "http://www.bearingshop.org/linear-bearing.html?p=3",
        "http://www.bearingshop.org/linear-bearing.html?p=4",
        "http://www.bearingshop.org/linear-bearing.html?p=5",
        "http://www.bearingshop.org/linear-bearing.html?p=6",
        "http://www.bearingshop.org/linear-bearing.html?p=7",
        "http://www.bearingshop.org/linear-bearing.html?p=8",
        "http://www.bearingshop.org/linear-bearing.html?p=9",
        "http://www.bearingshop.org/linear-bearing.html?p=10",
        "http://www.bearingshop.org/linear-bearing.html?p=11",
        "http://www.bearingshop.org/linear-bearing.html?p=12",
        "http://www.bearingshop.org/linear-bearing.html?p=13",
        "http://www.bearingshop.org/linear-bearing.html?p=14",
        "http://www.bearingshop.org/linear-bearing.html?p=15",
        "http://www.bearingshop.org/linear-bearing.html?p=16",
        "http://www.bearingshop.org/linear-bearing.html?p=17",
        "http://www.bearingshop.org/linear-bearing.html?p=18",
        "http://www.bearingshop.org/linear-bearing.html?p=19",
        "http://www.bearingshop.org/linear-bearing.html?p=20",
        "http://www.bearingshop.org/linear-bearing.html?p=21",
        "http://www.bearingshop.org/linear-bearing.html?p=22",
        "http://www.bearingshop.org/linear-bearing.html?p=23",
        "http://www.bearingshop.org/linear-bearing.html?p=24",
        "http://www.bearingshop.org/linear-bearing.html?p=25",
        "http://www.bearingshop.org/linear-bearing.html?p=26",
        "http://www.bearingshop.org/linear-bearing.html?p=27",
        "http://www.bearingshop.org/linear-bearing.html?p=28",
        "http://www.bearingshop.org/linear-bearing.html?p=29",
        "http://www.bearingshop.org/linear-bearing.html?p=30",
        "http://www.bearingshop.org/linear-bearing.html?p=31",
        "http://www.bearingshop.org/linear-bearing.html?p=32",
        "http://www.bearingshop.org/linear-bearing.html?p=33",
        "http://www.bearingshop.org/linear-bearing.html?p=34",
        "http://www.bearingshop.org/linear-bearing.html?p=35",
        "http://www.bearingshop.org/linear-bearing.html?p=36",
        "http://www.bearingshop.org/linear-bearing.html?p=37",
        "http://www.bearingshop.org/linear-bearing.html?p=38",
        "http://www.bearingshop.org/linear-bearing.html?p=39",
        "http://www.bearingshop.org/linear-bearing.html?p=40",
        "http://www.bearingshop.org/linear-bearing.html?p=41",
        "http://www.bearingshop.org/linear-bearing.html?p=42",
        "http://www.bearingshop.org/linear-bearing.html?p=43",
        "http://www.bearingshop.org/linear-bearing.html?p=44",
        "http://www.bearingshop.org/linear-bearing.html?p=45",
        "http://www.bearingshop.org/linear-bearing.html?p=46",
        "http://www.bearingshop.org/linear-bearing.html?p=47",
        "http://www.bearingshop.org/linear-bearing.html?p=48",
        "http://www.bearingshop.org/linear-bearing.html?p=49",
        "http://www.bearingshop.org/linear-bearing.html?p=50",
        "http://www.bearingshop.org/linear-bearing.html?p=51",
        "http://www.bearingshop.org/linear-bearing.html?p=52",
        "http://www.bearingshop.org/plain-bearings.html?p=2",
        "http://www.bearingshop.org/plain-bearings.html?p=3",
        "http://www.bearingshop.org/plain-bearings.html?p=4",
        "http://www.bearingshop.org/plain-bearings.html?p=5",
        "http://www.bearingshop.org/plain-bearings.html?p=6",
        "http://www.bearingshop.org/plain-bearings.html?p=7",
        "http://www.bearingshop.org/plain-bearings.html?p=8",
        "http://www.bearingshop.org/plain-bearings.html?p=9",
        "http://www.bearingshop.org/plain-bearings.html?p=10",
        "http://www.bearingshop.org/plain-bearings.html?p=11",
        "http://www.bearingshop.org/plain-bearings.html?p=12",
        "http://www.bearingshop.org/plain-bearings.html?p=13",
        "http://www.bearingshop.org/plain-bearings.html?p=14",
        "http://www.bearingshop.org/plain-bearings.html?p=15",
        "http://www.bearingshop.org/plain-bearings.html?p=16",
        "http://www.bearingshop.org/plain-bearings.html?p=17",
        "http://www.bearingshop.org/plain-bearings.html?p=18",
        "http://www.bearingshop.org/bicycle-bearings.html?p=2",
        "http://www.bearingshop.org/bicycle-bearings.html?p=3",
        "http://www.bearingshop.org/bicycle-bearings.html?p=4",
        "http://www.bearingshop.org/bicycle-bearings.html?p=5",
        "http://www.bearingshop.org/bicycle-bearings.html?p=6",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=2",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=3",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=4",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=5",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=6",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=7",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=8",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=9",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=10",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=11",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=12",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=13",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=14",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=15",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=16",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=17",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=18",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=19",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=20",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=21",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=22",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=23",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=24",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=25",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=26",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=27",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=28",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=29",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=30",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=31",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=32",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=33",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=34",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=35",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=36",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=37",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=38",
        "http://www.bearingshop.org/pillow-block-bearings.html?p=39",
        "http://www.bearingshop.org/track-rollers.html?p=2",
        "http://www.bearingshop.org/track-rollers.html?p=3",
        "http://www.bearingshop.org/track-rollers.html?p=4",
        "http://www.bearingshop.org/track-rollers.html?p=5",
        "http://www.bearingshop.org/track-rollers.html?p=6"
        "http://www.bearingshop.org/track-rollers.html?p=7"
        "http://www.bearingshop.org/track-rollers.html?p=8"
        "http://www.bearingshop.org/track-rollers.html?p=9"
        "http://www.bearingshop.org/track-rollers.html?p=10"
        "http://www.bearingshop.org/track-rollers.html?p=11"
        "http://www.bearingshop.org/track-rollers.html?p=12"
        "http://www.bearingshop.org/track-rollers.html?p=13"
        "http://www.bearingshop.org/track-rollers.html?p=14"
        "http://www.bearingshop.org/track-rollers.html?p=15"
        "http://www.bearingshop.org/track-rollers.html?p=16"
        "http://www.bearingshop.org/track-rollers.html?p=17"
        "http://www.bearingshop.org/track-rollers.html?p=18"
        "http://www.bearingshop.org/track-rollers.html?p=19"
        "http://www.bearingshop.org/track-rollers.html?p=20"
        "http://www.bearingshop.org/track-rollers.html?p=21"
        "http://www.bearingshop.org/track-rollers.html?p=22"
        "http://www.bearingshop.org/track-rollers.html?p=23"
        "http://www.bearingshop.org/track-rollers.html?p=24"
        "http://www.bearingshop.org/track-rollers.html?p=25"
        "http://www.bearingshop.org/track-rollers.html?p=26"
        "http://www.bearingshop.org/track-rollers.html?p=27"
        "http://www.bearingshop.org/track-rollers.html?p=28"
        "http://www.bearingshop.org/track-rollers.html?p=29"
        "http://www.bearingshop.org/track-rollers.html?p=30"
        "http://www.bearingshop.org/track-rollers.html?p=31"
        "http://www.bearingshop.org/track-rollers.html?p=32"
        "http://www.bearingshop.org/track-rollers.html?p=33"
        "http://www.bearingshop.org/track-rollers.html?p=34"
        "http://www.bearingshop.org/track-rollers.html?p=35"
        "http://www.bearingshop.org/track-rollers.html?p=36"
        "http://www.bearingshop.org/track-rollers.html?p=37"
        "http://www.bearingshop.org/track-rollers.html?p=38"
        "http://www.bearingshop.org/track-rollers.html?p=39"
        "http://www.bearingshop.org/track-rollers.html?p=40"
        "http://www.bearingshop.org/track-rollers.html?p=41"
        "http://www.bearingshop.org/track-rollers.html?p=42"
        "http://www.bearingshop.org/track-rollers.html?p=43"
        "http://www.bearingshop.org/track-rollers.html?p=44"
        "http://www.bearingshop.org/track-rollers.html?p=45"
        "http://www.bearingshop.org/track-rollers.html?p=46"
        "http://www.bearingshop.org/track-rollers.html?p=47"
        "http://www.bearingshop.org/track-rollers.html?p=48"
        "http://www.bearingshop.org/track-rollers.html?p=49"
        "http://www.bearingshop.org/track-rollers.html?p=50"
        "http://www.bearingshop.org/track-rollers.html?p=51"
        "http://www.bearingshop.org/track-rollers.html?p=52"
        "http://www.bearingshop.org/track-rollers.html?p=53"
        "http://www.bearingshop.org/track-rollers.html?p=54"
        "http://www.bearingshop.org/track-rollers.html?p=55"
        "http://www.bearingshop.org/track-rollers.html?p=56"
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse, errback=self.err_back, dont_filter=True)

    def parse(self, response):
        # f = open("paint.html", "w")
        # f.write(response.body.decode("utf-8"))
        # f.close()
        for u in response.xpath('//div[@class="product-grid-container"]//div[@class="images-container"]'):
            yield {
                'category-url': response.url,
                'product-url': u.xpath("./a/@href").get(),
            }

    def err_back(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

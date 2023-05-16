# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

from dateutil import parser

_d = parser.parse

pwd_hash = "$2b$12$QLpUyPzW8PF6Kidk/fMXM.AQQSCI7UK7OsUr4k.2qVAbPq7yPdrhy" # pwd:asdasdasd
principals = [
    {"id": 1, "username": "alice"},
    {"id": 2, "username": "bod"},
    {"id": 3, "username": "carol"},
]

moviegoers = [
    {"id": 1,"principal_id": 1, "name": "Alice A."},
    {"id": 2, "principal_id": 2, "name": "Bob B."},
    {"id": 3, "principal_id": 3, "name": "Carol C."}
]

credentials = [
    {"principal_id": 1, "password": pwd_hash },
    {"principal_id": 2, "password": pwd_hash },
    {"principal_id": 3, "password": pwd_hash }
]

movies = [
    {"id": 3, "title": "Inception", "rating": "PG-13", "release_date": _d("16-Jul-2010")},
    {"id": 41, "title": "Star Wars", "rating": "PG", "release_date": _d("25-May-1977")},
    {"id": 43, "title": "It's complicated", "rating": "R", "release_date": _d("25-Dec-2009")},
    {"title": "Toy Story", "rating": "G", "release_date": _d("22-Nov-1995")},
    {"title": "Aladdin", "rating": "G", "release_date": _d("25-Nov-1992")},
    {"title": "The Terminator", "rating": "R", "release_date": _d("26-Oct-1984")},
    {"title": "When Harry Met Sally", "rating": "R", "release_date": _d("21-Jul-1989")},
    {"title": "The Help", "rating": "PG-13", "release_date": _d("10-Aug-2011")},
    {"title": "Chocolat", "rating": "PG-13", "release_date": _d("5-Jan-2001")},
    {"title": "Amelie", "rating": "R", "release_date": _d("25-Apr-2001")},
    {"title": "2001: A Space Odyssey", "rating": "G", "release_date": _d("6-Apr-1968")},
    {"title": "The Incredibles", "rating": "PG", "release_date": _d("5-Nov-2004")},
    {
        "title": "Raiders of the Lost Ark",
        "rating": "PG",
        "release_date": _d("12-Jun-1981"),
    },
    {"title": "Chicken Run", "rating": "G", "release_date": _d("21-Jun-2000")},
    {"title": "O Vingador", "rating": "NAO SEI", "release_date": _d("17-Apr-2019")},
]

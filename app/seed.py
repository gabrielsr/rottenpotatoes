# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

from dateutil import parser

_d = parser.parse

pwd_hash = "$2b$12$QLpUyPzW8PF6Kidk/fMXM.AQQSCI7UK7OsUr4k.2qVAbPq7yPdrhy"
users = [
    {"username": "admin", "email": "1@d.m", "pwd": pwd_hash},
    {"username": "admin2", "email": "2@d.m", "pwd": pwd_hash},
]

movies = [
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

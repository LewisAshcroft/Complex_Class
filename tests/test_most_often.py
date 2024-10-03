from lib.most_often import *

def test_add_function():
    starting_list = []
    mostoften = MostOften(starting_list)
    mostoften.add_new("Giraffe")
    assert mostoften.starting_list == ["Giraffe"]

def test_get_most_often_returns_highest_item():
    starting_list = ["Giraffe","Giraffe","Bat",1,1,1]
    mostoften = MostOften(starting_list)
    result = mostoften.get_most_often()
    assert result == 1

def test_get_most_often_returns_no_clear_winner():
    starting_list = ["Giraffe","Giraffe","Bat","Bat"]
    mostoften = MostOften(starting_list)
    result = mostoften.get_most_often()
    assert result == "no clear winner"


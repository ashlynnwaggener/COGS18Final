from functions import *

def test_all ():
    assert callable(holiday_drink_quiz)
    assert callable(find_drink)
    assert callable(check_end_quiz)
    assert callable(check_yes)
    assert callable(check_no)
    assert callable(check_replay)
    assert callable(check_answer_a)
    assert callable(check_answer_b)
    assert callable(check_answer_c)
    assert callable(check_answer_d)
    assert check_answer_a('a') == True
    assert check_answer_b('b') == True
    assert check_answer_c('d') == False
    assert check_answer_d('d') == True
    assert check_replay('again') == True
    assert check_end_quiz('yes') == False
    assert check_yes('yeah') == True
    assert check_no('bye') == False
    assert find_drink([['a'], ['b',],['c','c','c'], []]) == 3
    assert find_drink([['a'], ['b',],['c','c',], ['d']]) == 2
    assert find_drink([['a', 'a' ], ['b'],['c'], ['d']]) == 2
    assert find_drink([[], [],['c','c','c','c','c'], []]) == 5
    assert find_drink([[], ['b',],['c','c','c','c'], []]) == 4
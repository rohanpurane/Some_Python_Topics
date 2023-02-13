# import my_code
# import pytest
# import sys
'''
Commands : 
    (1) pytest test_my_code.py              => to test code
    (2) pytest test_my_code.py -v           => to test code in details
    (3) py.test and py.test -v              => you can use this also to test code
    (4) pytest test_my_code.py::test_add    => if you want to test perticuar func only then use (pytest test_filename.py::test_func_name)
    (5) pytest -v -k "add"                  => if you want to test those func which has some similarity in name then you can use this cmd
    (6) (pytest -v -k "add or string")  (pytest -v -k "add and string")
    (7) (pytest -v -m strings) or (pytest -v -m number) => if you want mark some func and test only those func... and to do this you need to add this decorator (@pytest.mark.number) or (pytest -v -m strings) like this
    (8) pytest -v -x                        => the -x is use when we want that, if perticular func will get error(failed) then the below func will not be executed 
    (9) pytest -v --maxfail=2               => if we want that, after getting 2 failed-func the test-process will getting stoped, we can mention any number of instead of 2  
   (10) pytest -v -rsx                      => to see the reaseon of skipped funcions
   (11) pytest -v -s or pytest -v --capture=no => to see the print statement in functions
   (12) pytest -v -q                        => this is the quite mode, it doesn't print unneccessory information
'''

'''
# @pytest.mark.skipif(sys.version_info > (3, 3),reason='trying to learn skipped tests again') #*********** you can add conditional statement if-else on this skip
# @pytest.mark.skipif(sys.version_info < (3, 3),reason='trying to learn skipped tests') #*********** you can add conditional statement if-else on this skip
# @pytest.mark.skip(reason='trying to learn skipped tests') #*********** This decorator is use to skip the func
# @pytest.mark.number
def test_add():
    assert my_code.add(3,5) == 8
    assert my_code.add(3) == 5
    assert my_code.add(10,5) == 15
    print(my_code.add(10,5),'----------********* Print *********----------')

# @pytest.mark.number
def test_product():
    assert my_code.product(3,5) == 15
    assert my_code.product(5) == 10
    assert my_code.product(7) == 14

# @pytest.mark.strings
def test_add_string():
    result = my_code.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'zxcv' not in result

# @pytest.mark.strings
def test_product_string():
    result = my_code.product('Hello ', 3)
    assert result == 'Hello Hello Hello '
    assert type(result) is str
    assert 'Hel' in result
'''

'''
# if you want to test one func with multiple different arguments at a time.


@pytest.mark.parametrize('num1, num2, result', 
    [
        (7, 3, 10),
        ('Hello', ' World','Hello World'),
        (10.5, 20.5, 31)
    ]
)
def test_add(num1, num2, result):
    assert my_code.add(num1, num2) == result
'''

#***************************************************************************************#

from my_code import StudentDB
import pytest


'''
# in this method the problem is, that if we are working with big data then we need to define thousands of functions like this and then the work-flow will be very lenghty and costly, so to tackle this...

def test_manoj_data():
    db = StudentDB()
    db.connect('data.json')
    manoj_data = db.get_data('manoj')
    assert manoj_data['id'] == 1
    assert manoj_data['name'] == 'manoj'
    assert manoj_data['result'] == 'pass'

def test_mohini_data():
    db = StudentDB()
    db.connect('data.json')
    mohini_data = db.get_data('mohini')
    assert mohini_data['id'] == 2
    assert mohini_data['name'] == 'mohini'
    assert mohini_data['result'] == 'fail'
'''

# db = StudentDB()
# def setup_medule(module):
#     print('------------------------ Setup ------------------------')
#     global db             # we need to define that db is global variable
#     db = StudentDB()
#     db.connect('data.json')

# def teardown_module(module): # to initialize this func you need to define close method in StudentDB class
#     print('------------------------ teardown ------------------------')
#     db.close()


# def test_manoj_data():
#     manoj_data = db.get_data('manoj')
#     assert manoj_data['id'] == 1
#     assert manoj_data['name'] == 'manoj'
#     assert manoj_data['result'] == 'pass'

# def test_mohini_data():
#     mohini_data = db.get_data('mohini')
#     assert mohini_data['id'] == 2
#     assert mohini_data['name'] == 'mohini'
#     assert mohini_data['result'] == 'fail'
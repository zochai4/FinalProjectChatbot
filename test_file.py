from have_a_medical_chat import *

def test_greet():
    test1 = 'hi'
    test2 = 'hey'
    test3 = 'hope you are well'
    test4 = 'glad you found your way here'
    assert isinstance(greet(['hi']), str)
    assert is_greeting(['hi']) == test1 or test2 or test3 or test4
    assert callable(greet)
    assert isinstance(greet(['hey']), str)
    assert is_greeting(['hey']) == test1 or test2 or test3 or test4
    
    
def test_BMI_index():
    assert isinstance(weight('60'),int)
    assert isinstance(height('60', int)
    assert BMI_index([0.0166]) == True
    assert callable(BMI_index)


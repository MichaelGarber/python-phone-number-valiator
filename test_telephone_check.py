from telephone_check import  telephone_check

def test_telephone_check():
    assert(telephone_check("555-555-5555")) == True
    assert(telephone_check("1 555-555-5555")) == True
    assert(telephone_check("1 (555) 555-5555")) == True
    assert(telephone_check("5555555555")) == True
    assert(telephone_check("555-555-5555")) == True
    assert(telephone_check("(555)555-5555")) == True
    assert(telephone_check("1(555)555-5555")) == True
    assert(telephone_check("555-5555")) == False
    assert(telephone_check("5555555")) == False
    assert(telephone_check("1 555)555-5555")) == False
    assert(telephone_check("1 555 555 5555")) == True
    assert(telephone_check("1 456 789 4444")) == True
    assert(telephone_check("123**&!!asdf")) == False
    assert(telephone_check("55555555")) == False
    assert(telephone_check("(6054756961)")) == False
    assert(telephone_check("2 (757) 622-7382")) == False
    assert(telephone_check("0 (757) 622-7382")) ==  False
    assert(telephone_check("-1 (757) 622-7382")) == False
    assert(telephone_check("2 757 622-7382")) ==  False
    assert(telephone_check("10 (757) 622-7382")) == False
    assert(telephone_check("27576227382")) == False
    assert(telephone_check("(275)76227382")) == False
    assert(telephone_check("2(757)6227382")) == False
    assert(telephone_check("2(757)622-7382")) == False
    assert(telephone_check("555)-555-5555")) == False
    assert(telephone_check("(555-555-5555")) == False
    assert(telephone_check("(555)5(55?)-5555")) == False
    print("YOUR CODE IS CORRECT!")



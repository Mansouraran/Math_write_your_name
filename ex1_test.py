import write_your_name as name


def test_hi_my_name_is():
    R = name.hi_my_name_is()
    print('ourput: ', R)
    assert len(R)  > 1 


test_hi_my_name_is()

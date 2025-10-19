def ex_feature1(a, b, *args, values=[], **kwargs):
    
    print(a, b, args, kwargs, values)
    

ex_feature1("a", 1, 2, 3, key=2, value=7, values=[1,2,3])

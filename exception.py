def exceptional():
    try:
        a = 10
        b = 12
        c = a+b
        print (c)
    except:
        print("ERROR: can add only numbers......")
    else:
        print("There is no exception")
    finally:
        print("EXCECUTED")
exceptional()


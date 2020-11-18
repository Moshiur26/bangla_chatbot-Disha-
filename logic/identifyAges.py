import variables.ConstantVariable as cv
import variables.Variables as v

def findAge(user_input):

    for i in cv.ages:
        if i in user_input :
            v.info_map["age"]=i
            v.checker["age"]=True
            return True


    return v.checker["age"]

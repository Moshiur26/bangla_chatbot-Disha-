import variables.ConstantVariable as cv
import variables.Variables as v

def findBloodGroup(user_input):

    for i in cv.blood_group:
        if i in user_input :
            v.info_map["blood group"]=i
            v.checker["blood group"]=True
            return True

    return v.checker["blood group"]

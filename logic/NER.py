import variables.Variables as v
import variables.ConstantVariable as cv
import  chat as c
def ner(user_input):
    for i in cv.names:
        if i in user_input :
            v.info_map["name"]=i
            v.checker["name"]=True
            c.answar='আপনাকে ধন্যবাদ '+i
            if v.checker["age"]==False:
                c.answer=""
                c.answer='ধন্যবাদ '+v.info_map["name"]+'।আপনার বয়স বলুন।'
            return True
    return False

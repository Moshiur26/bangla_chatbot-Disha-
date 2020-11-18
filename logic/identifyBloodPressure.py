import variables.ConstantVariable as cv
import variables.Variables as v
import re
#import chat as c

banglaToEnglish={
    '০':'0',
    '১':'1',
    '২':'2',
    '৩':'3',
    '৪':'4',
    '৫':'5',
    '৬':'6',
    '৭':'7',
    '৮':'8',
    '৯':'9',
}

def findBloodPressure(user_input):

    banglaNumbers=[]
    englishNumbers=[]

    for word in user_input.split():
        if re.match(r"^[\u09E6-\u09EF]+$", word):
            banglaNumbers.append(word)
    #print(banglaNumbers)
    if len(banglaNumbers)==2:
        v.info_map["blood pressure"]=banglaNumbers[0]+" থেকে "+banglaNumbers[1]
        v.checker["blood pressure"]=True
        for i in range(len(banglaNumbers)):
            w=banglaNumbers[i]
            temp=""
            for j in range(len(w)):
                #w[j]=banglaToEnglish[w[j]]
                temp+=banglaToEnglish[w[j]]
            englishNumbers.append(int(temp))
        #print(englishNumbers)
        if englishNumbers[0]>englishNumbers[1]:
            temp=englishNumbers[0]
            englishNumbers[0]=englishNumbers[1]
            englishNumbers[1]=temp
        if englishNumbers[0]<60 or englishNumbers[1]>120:
            v.answer="আপনার রক্তচাপ অসাভাবিক। আপনি আপনার এই সমস্যার জন্য হৃদরোগ বিশেষজ্ঞ [Cardiologis] ডাক্তার দেখাতে পারেন।\nআপনাকে আর কিভাবে সাহায্য করতে পারি? "
            return True
        v.answer='ব্লাড প্রেসার দেওয়ার জন্য আপনাকে ধন্যবাদ।\nআপনাকে কিভাবে সাহায্য করতে পারি?'
        return True

    return False



#print(findBloodPressure("১২ ত্রেত্য্য ৩৪"))
#print(v.info_map["blood pressure"])
#print(v.answer)

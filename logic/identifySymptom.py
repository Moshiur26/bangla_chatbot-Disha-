import re, math
from collections import Counter
import variables.ConstantVariable as cv
import variables.Variables as v
import chat as c
#symptom_list = ["matha betha","kan betha"]

WORD = re.compile(r'\w+')
#text1="fd fgf wer ad hg"
def similarity(user_input):
    maxSim=0.0
    identifiedSymptom=""
    for symptom in cv.symptomsList:
        vector1 = text_to_vector(symptom)
        vector2 = text_to_vector(user_input)
        cosine = get_cosine(vector1, vector2)
        if cosine>maxSim:
            maxSim=cosine
            identifiedSymptom=symptom

    if maxSim>0.0:
        #print(identifiedSymptom)
        for i in range(len(cv.symptomsList)):
            if identifiedSymptom==cv.symptomsList[i]:
                if v.symptomMatrix[0,i]==0:
                    v.symptomMatrix[0,i]=1
                    v.symptom_counter+=1
                    c.answer=""
                    #c.answer="আরও থাকলে লিখুন। না থাকলে না বলুন।"

                else:
                    c.answer=""
                    c.answer="এইটা আমাদের পূর্বেই সংরক্ষণে ছিলো। "
                break

        return True
    return False


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)


#similarity("হাঁটুর ব্যাথা হচ্ছে।")

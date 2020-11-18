import numpy as np

checker = {"name" : False,
           "age" : False,
           "symptom": True,
           "blood group": False,
           "blood pressure" : False,
           "already identify disease":False

}

symptom_counter=0
symptomMatrix = np.zeros([1,132])

c_name=False
c_old=False
c_symptom=True

answer=""

info_map = {"name" : "Me",
            "age" : "আমাদের সংরক্ষনে নেই।",
            "blood group":"আমাদের সংরক্ষনে নেই।",
            "blood pressure" : "আমাদের সংরক্ষনে নেই।",

}



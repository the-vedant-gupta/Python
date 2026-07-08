# Keyword Arguments
def calculate_marks(maths, eng, hindi, compt, history=0):
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"hindi = {hindi}")
    print(f"compt = {compt}")
    print(f"history = {history}")
    total_marks = maths + eng + hindi + compt + history
    print(f"Total marks scored = {total_marks}")


calculate_marks(eng=34, compt=34, history=45, maths=33, hindi=34)

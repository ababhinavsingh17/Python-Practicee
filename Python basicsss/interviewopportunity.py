cgpa = 7.5
coding_score = 55
certificate = True

if cgpa >= 7.0:
    if coding_score >= 60 or certificate:
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
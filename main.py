import json
import time

score =0
with open ("questions.json") as f:
    questions=json.load(f)

for i,q in enumerate(questions):
    print(f"\n Q{i+1}: {q['question']}")
    start=time.time()
    for j,o in enumerate(q['options']):
       print(f"\n {j+1}.{o}", end="\t\t")
       if (j%2==1):
          print()
    uservalue=(input("Choose an Option or s to skip \n").strip())
    end=time.time()
    if end-start>60:
       print("Times Up!!!Question Skipped:\n")
       continue
    if uservalue.lower()=="s":
        print("Skipped")
        continue
    user=int(uservalue)
    if user==q['answer']:
       print("Correct")
       score+=4
    else:
       print("Wrong")
       score-=1
print(f"Your Final Score Is : {score}")
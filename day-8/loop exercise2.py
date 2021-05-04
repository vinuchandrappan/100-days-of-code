#For finding thr max score from a class
score=input("Input the scores ").split()
for n in range(0, len(score)):
  score[n]=int(score[n])
print(score)  

max_score=0
for s in score:
  if max_score<s:
    max_score=s
print(f"The maximum score is {max_score}")  

  
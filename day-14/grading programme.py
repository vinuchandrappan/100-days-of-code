student_score={
  "Harry":82,
  "Ron":79,
  "Heromione":99,
  "Draco":76,
  "Neville":70, 
}

student_grades={}
for student in student_score:
  score=student_score[student]  
  if score>90:
   student_grades[student]="Outstanding"
  elif score>80:
    student_grades[student]="Exeeds expectations"
  elif score>70:
    student_grades[student]="Acceptable"
  else:
    student_grades[student]="fails"   

print(student_grades)
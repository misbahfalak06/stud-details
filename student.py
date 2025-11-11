import sys
if len(sys.argv) ==6:
    script_name=sys.argv[0]
    m1=sys.argv[1]
    m2=sys.argv[2]      
    m3=sys.argv[3]
    m4=sys.argv[4]
    m5=sys.argv[5]
else:
    script_name=input("Enter script name: ")
    m1="88"
    m2="76"
    m3="90"
    m4="85"
    m5="79"
total_marks=int(m1)+int(m2)+int(m3)+int(m4)+int(m5)
average_marks=total_marks/5
print("Script Name:",script_name)
print("Total Marks:",total_marks)
print("Average Marks:",average_marks)
if average_marks>=90:
    grade="A"
elif average_marks>=80:
    grade="B"
elif average_marks>=70:
    grade="C"
elif average_marks>=60:
    grade="D"
else:
    grade="F"
print("Grade:",grade)

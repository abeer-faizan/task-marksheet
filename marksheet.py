sindhi = int(input('Mark Obtain in Sindhi: '))
english = int(input('Mark Obtain in English: '))
pakstd = int(input('Mark Obtain in Pakistan Studies: '))
biologyTh = int(input('Mark Obtain in Biology Theory: '))
biologyPr = int(input('Mark Obtain in Biology Practical: '))
chemistryTh = int(input('Mark Obtain in Chemistry Theory: '))
chemistryPr = int(input('Mark Obtain in Chemistry Practical: '))
grade = ''

print('\n\t\t\t\tSTATEMENT OF MARKS')

print('SUBJECT\t\t\tMAX MARKS\t MINPASS MARKS\t MARKS OBTAIN\t STATUS')
if sindhi >= 25:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('SINDHI\t\t\t  075\t\t      25\t\t '+str(sindhi)+'\t  '+status)
if english >= 25:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('ENGLISH\t\t\t  075\t\t      25\t\t '+str(english)+'\t  '+status)
if pakstd >= 25:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('PAKISTAN STUDIES\t  075\t\t      25\t\t '+str(pakstd)+'\t  '+status)
if biologyTh >= 28:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('BIOLOGY TH\t\t  085\t\t      28\t\t '+str(biologyTh)+'\t  '+status)
if biologyPr >= 5:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('BIOLOGY PRACT\t  015\t\t      05\t\t '+str(biologyPr)+'\t  '+status)
if chemistryTh >= 28:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('CHEMISTRY TH\t  085\t\t      25\t\t '+str(chemistryTh)+'\t  '+status)

if chemistryPr >= 5:
    status = 'PASS'
else:
    status = 'FAIL'
    grade = 'F'
print('CHEMISTRY PRACT\t  015\t\t      05\t\t '+str(chemistryPr)+'\t  '+status)

totalMarksObt = sindhi + english + pakstd
totalMarksObt += biologyPr + biologyTh + chemistryPr + chemistryTh
percentageTotal = totalMarksObt / 425 * 100

if grade != 'F':
    if percentageTotal >= 80:
        grade = 'A+'
    elif (percentageTotal < 80 and percentageTotal >= 70):
        grade = 'A'
    elif (percentageTotal < 70 and percentageTotal >= 60):
        grade = 'B'
    elif (percentageTotal < 60 and percentageTotal >= 50):
        grade = 'C'
    elif (percentageTotal < 50 and percentageTotal >= 40):
        grade = 'D'
    elif (percentageTotal > 40):
        grade = 'E'

print('\n\nTOTAL MARKS OBTAIN   '+str(totalMarksObt)+'   OUT OF 425')
print('PERCENTAGE: '+str(round(percentageTotal, 2))+'%')
print('GRADE: '+grade+'\n')

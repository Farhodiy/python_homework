universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrolment_stats(l:list):
    students=[]
    tuition=[]
    for i in l:
        students.append(i[1])
        tuition.append(i[2])
    return students,tuition


def mean(values):
    return sum(values) / len(values)


def median(values):
    values = sorted(values)
    n = len(values)
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid - 1] + values[mid]) / 2
students, tuition = enrolment_stats(universities)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition):,}\n")

print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,.0f}\n")

print(f"Tuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {median(tuition):,.0f}")

    
import datetime
import matplotlib.pyplot as plt

dates = []
times = []

with open('indiana_covid-19_data_spring_2023.txt', 'r') as fo:
    lines = fo.readlines()
    for i in lines:
        sep = i.rstrip().split()
        cases = float(sep[2])
        times.append(cases)

    # Divide each element in the 'times' list by 1000
    t = [case / 1000 for case in times]

    for u in lines:
        sepa = u.rstrip().split()
        dat = sepa[0]
        dates.append(dat)

# Adding on prior weeks' case data:
t_cases = 0
total = []
for n in t:
    t_cases += n
    total.append(t_cases)

X = []
for date in dates:
    y, m, d = date.split('-')
    dt = datetime.date(int(y), int(m), int(d))
    X.append(dt)

# Create the bar chart
fig, ax = plt.subplots()
ax.bar(X, total, width=7, color='b')

# Set titles and labels
ax.set_title("Weekly Positive COVID-19 Cases in Indiana (cugboh)")
ax.set_xlabel("Date")
ax.set_ylabel("Number of Cases (in thousands)")

fig.autofmt_xdate()
plt.show()

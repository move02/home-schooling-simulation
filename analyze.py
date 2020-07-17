import csv
import numpy as np
import matplotlib.pyplot as plt

days = 200
trials = 10000
datas = []

peak_values_per_trial = []

for d in range(trials):
    datas.append([])

with open("non-policy.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    trial_list = []
    for row in reader:
        trial = int(row[0])
        day = int(row[1])
        value = int(row[2])

        trial_list.append(value)

        if day == days:
            datas[trial] = trial_list
            peak_values_per_trial.append(value)
            trial_list = []

peak_values_per_trial = np.array(peak_values_per_trial)
infimum = np.percentile(peak_values_per_trial, 25)
supereme = np.percentile(peak_values_per_trial, 75)

i = 0
quantilized_trial_index = []
for t in peak_values_per_trial:
    if t >= infimum and t <= supereme:
        quantilized_trial_index.append(i)
    i += 1

datas = np.array(datas)
quantilized_datas = datas[quantilized_trial_index]

averaged_datas = np.array([])
for day in range(days):
    averaged_datas = np.append(averaged_datas, np.mean(quantilized_datas[:, day]))



# 4분위 박스플롯
# X = np.array(range(trials))
# peak_value_boxplot = plt.boxplot(peak_values_per_trial)

# 히스토그램
# plt.hist(peak_values_per_trial)


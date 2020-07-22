# 초기 세팅
import csv
import numpy as np

# get_ipython().run_line_magic('matplotlib', 'inline')

days = 200
trials = 10000
datas = []

peak_values_per_trial = []

for d in range(trials):
    datas.append([])


# 파일읽기
with open("day14-10000.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    trial_list = []
    for row in reader:
        trial = int(row[0])
        day = int(row[1])
        value = int(row[2])

        trial_list.append(value)

        if day == 200:
            datas[trial] = trial_list
            peak_values_per_trial.append(value)
            trial_list = []


# 4분위로 데이터 나누기
peak_values_per_trial = np.array(peak_values_per_trial)
infimum = np.percentile(peak_values_per_trial, 25)
supereme = np.percentile(peak_values_per_trial, 75)

i = 0
quantilized_middle_index = []
quantilized_low_index = []
quantilized_high_index = []
for t in peak_values_per_trial:
    if t >= infimum and t <= supereme:
        quantilized_middle_index.append(i)
    elif t < infimum:
        quantilized_low_index.append(i)
    elif t > supereme:
        quantilized_high_index.append(i)
    i += 1


# 4분위로 데이터 나누기2
datas = np.array(datas)
quantilized_middle_datas = datas[quantilized_middle_index]
quantilized_low_datas = datas[quantilized_low_index]
quantilized_high_datas = datas[quantilized_high_index]  


# 4분위로 나누어진 데이터의 일별 평균 구하기
averaged_middle_datas = np.array([])
averaged_low_datas = np.array([])
averaged_high_datas = np.array([])

for day in range(days):
    averaged_middle_datas = np.append(averaged_middle_datas, np.mean(quantilized_middle_datas[:, day]))
    averaged_low_datas = np.append(averaged_low_datas, np.mean(quantilized_low_datas[:, day]))
    averaged_high_datas = np.append(averaged_high_datas, np.mean(quantilized_high_datas[:, day]))


# 박스플롯
import matplotlib.pyplot as plt
X = np.array(range(trials))
peak_value_boxplot = plt.boxplot(peak_values_per_trial)


# 히스토그램
peak_value_hist = plt.hist(peak_values_per_trial, bins=10)


# 전체 플롯
plt.plot(range(1, days+1), averaged_middle_datas)
plt.plot(range(1, days+1), averaged_high_datas)
plt.plot(range(1, days+1), averaged_low_datas)
plt.xlabel("day")
plt.ylabel("infected-average")
plt.legend(["middle", "high", "low"])
plt.show



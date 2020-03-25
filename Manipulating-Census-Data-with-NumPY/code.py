# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter = ",", skip_header = 1)

#New record
new_record = [[50,  9,  4,  1,  0,  0, 40,  0]]

census = np.concatenate((data, new_record))
print(census)

#Code starts here



# --------------
#Code starts here

age = census[:,0]

max_age = age.max()
min_age= age.min()
age_mean = age.mean()
age_std = np.std(age) 

print("Max age:", max_age)
print("Min age:", min_age)
print("Mean age:", age_mean)
print("SD of age:", age_std)


# --------------
#Code starts here

race_0 = census[census[ : , 2] == 0]
race_1 = census[census[ : , 2] == 1]
race_2 = census[census[ : , 2] == 2]
race_3 = census[census[ : , 2] == 3]
race_4 = census[census[ : , 2] == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

length_list = [len_0, len_1, len_2, len_3, len_4]

minority_race = length_list.index(min(length_list))

print('Race with minimum number of citizens is:', minority_race)


# --------------
#Code starts here

senior_citizens = census[census[:,0] > 60]

working_hours_sum = sum(senior_citizens[:,6])

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum/senior_citizens_len

print(avg_working_hours)



# --------------
#Code starts here

high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)
avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)

if (avg_pay_high > avg_pay_low):
    print("Better education leads to better pay")
else:
    print("Better education does not lead to better pay")




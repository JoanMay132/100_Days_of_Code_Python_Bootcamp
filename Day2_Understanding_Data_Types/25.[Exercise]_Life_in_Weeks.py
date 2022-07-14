# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
death_days= 90 * 365
death_weeks=90 * 52
death_months=90*12
age_days= int(age)*365
age_weeks=int(age)*52
age_months=int(age)*12
time_left_days= death_days-age_days
time_left_weeks=death_weeks-age_weeks
time_left_months=death_months-age_months

print(f"You have {time_left_days} days, {time_left_weeks} weeks, and {time_left_months} months left.")

# Another way
age_as_int=int(age)
years_remaining=90-age_as_int
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12

message=f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
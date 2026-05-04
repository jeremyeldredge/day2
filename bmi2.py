"""
Inputs
-  name
-  height
-  weight
-  age
-  sex

Processes
-  Input validation
-  Caculate BMI - (weight/height^2) * 703
-  Categorize BMI:
    - Underweight < 18.5
    - Healthy 18.4-24.9
    - Overweight 25.0-29.9
    - Obesity 30-39.9
    - Severe obesity 40+

Outputs
-  Report for an individual

"""

# collect inputs
name = input("Name: ")
age = input("Age: ")
sex = input("Sex: ")
height = input("Height (inches): ")
weight = input("Weight (pounds): ")


# input validation
age = age.replace(".", "", 1)
age_is_int = age.isdigit()
if age_is_int == True:
    age = int(age)
age_is_reasonable = False
if age_is_int == True and age < 140 and age > 1:
    age_is_reasonable = True

sex = sex.lower()
sex_is_valid = False
if sex == "male" or sex == "female":
    sex_is_valid = True

height = height.replace(".","",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = False
if height_is_int == True and height > 12 or height < 140:
    height_is_reasonable = True

weight = weight.replace(".","",1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_is_reasonable = False
if weight_is_int == True and weight >12 or weight < 1200:
    weight_is_reasonable = True



ready_to_process = True

# input validation error messages
if age_is_int == False or age_is_reasonable == False:
    print("You entered a non-expected age, please use whole numbers>")
    ready_to_process = False

if sex_is_valid == False:
    print("You entered a non-expected sex, please use male or female.")
    ready_to_process = False

if height_is_int == False or height_is_reasonable == False:
    print("You entered a non-expected height, please use whole numbers between 12-140 inches.")
    ready_to_process = False

if weight_is_int == False or weight_is_reasonable == False:
    print("You entered a non-expected weight, please use whole numbers between 12-1200 pounds.")
    ready_to_process = False

# BMI calculation and categorization
"""
-  Caculate BMI - (weight/height^2) * 703
-  Categorize BMI:
    - Underweight < 18.5
    - Healthy 18.4-24.9
    - Overweight 25.0-29.9
    - Obesity 30-39.9
    - Severe obesity 40+
"""

if ready_to_process == True:
    bmi = (weight / height ** 2) * 703
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi <= 24.9:
        bmi_category = "Healthy"
    elif bmi <= 29.9:
        bmi_category = "Overweight"
    elif bmi <= 39.9:
        bmi_category = "Obesity"
    else:
        bmi_category = "Severe obesity"

    # output report
    print(f"Report for {name}\n"
        f"{age} year old {sex}\n"
        f"Your BMI is {bmi:.2f}.\n"
        f"Your BMI cateogory is: {bmi_category}")
#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter
import joblib

def predict_state():
    signs_inputs = [float(age_entry.get())]
    for entry in entries:
        signs_inputs.append(float(entry.get()))



    signs_inputs = vital_signs_scaler.transform([signs_inputs])
    signs_predict = vital_signs_model.predict(signs_inputs)

    if signs_predict == 1:
        label.set("We are sorry to tell you that but you suffer from diabetes disease. \nPlease consult doctor quickly. \nHere are some advices to do until you see a doctor:\n" + '\n'.join(diabetic_advices))
    elif signs_predict == 0:
        label.set("Congratulations. You don't suffer from diabetes disease. \nHere are some advices to stay with good health:\n" + '\n'.join(non_diabetic_advices))
    else:
        label.set("Your sybtoms indicate that you suffer from diabetes but your vital signs indicate that you don't suffer from it. \nSo we advise you to consult a doctor. \nHere are some advices to do until you see a doctor:\n" + '\n'.join(non_diabetic_advices))
    
    result_frame.config(borderwidth=2, background='#999999')
    result_label.config(background='#cccccc')

    print(signs_predict)


i = 0
j = 0
genders = ['Male', 'Female']
vital_signs = ["Urea", "HbA1c", "Cholesterol", "Triglycerides", "VLDL", "BMI"]
entries = []

vital_signs_scaler = joblib.load('signs_scaler.h5')
vital_signs_model = joblib.load('signs_model.h5')

diabetic_advices = ["1. Choose healthier carbohydrates", "2. Eat less salt", "3. Eat less red and processed meat", "4. Eat more fruit and veg", "5. Choose healthier fats", "6. Cut down on added sugar", "7. Be smart with snacks"]
non_diabetic_advices = ["1. Losing weight and keeping it off", "2. Following a healthy eating plan", "3. Get regular exercise", "4. Don't smoke", "5. Talk to your health care provider"]

main_window = tkinter.Tk()
main_window.title("Diabetes Detector")
main_window.geometry("640x480")
main_window.state("zoomed")
main_window.configure(padx=20, pady=20)

base_info_frame = tkinter.Frame(main_window)
base_info_frame.grid(row=0, column=0, sticky='nsew')

tkinter.Label(base_info_frame, text="Gender", font=('Comic Sans MS', 20)).grid(row=0, column=0, sticky='w')
gender = tkinter.StringVar(main_window)
gender.set("Select gender")
gender_menu = tkinter.OptionMenu(base_info_frame, gender, *genders)
gender_menu.grid(row=0, column=1, sticky='w')
gender_menu.config(font=('Comic Sans MS', 14))

tkinter.Label(base_info_frame, text="Age", font=('Comic Sans MS', 20)).grid(row=1, column=0, sticky='w')
age_entry = tkinter.Entry(base_info_frame, font=('Comic Sans MS', 14))
age_entry.grid(row=1, column=1, sticky='w', ipadx=5, ipady=3)
age_entry.config(width=10)

vital_signs_frame = tkinter.Frame(main_window)
vital_signs_frame.grid(row=1, column=0, pady=50)

for sign in vital_signs:
    tkinter.Label(vital_signs_frame, text=sign, font=('Comic Sans MS', 20)).grid(row=i, column=j, sticky='w')
    sign_entry = tkinter.Entry(vital_signs_frame, font=('Comic Sans MS', 14))
    sign_entry.grid(row=i, column=j+1, sticky='w', ipadx=5, ipady=3, padx=10)
    sign_entry.config(width=10)
    entries.append(sign_entry)
    j += 2
    if j == 4:
        i += 1
        j = 0
else:
    i = 1
    j = 0



predict_button = tkinter.Button(main_window, text="Predict", font=('Comic Sans MS', 22), command=predict_state)
predict_button.grid(row=3, column=0, sticky='w', pady=30)
predict_button.config(background='blue')

result_frame = tkinter.LabelFrame(main_window, text="Result Report", font=('Comic Sans MS', 22), borderwidth=0)
result_frame.grid(row=0, column=1, rowspan=3, sticky='nsew', padx=100)
label = tkinter.StringVar()
result_label = tkinter.Label(result_frame, textvariable=label, font=('Comic Sans MS', 18), wraplength=480, justify="left")
result_label.grid(row=0, column=0, sticky='nsew', ipadx=10, ipady=10)

main_window.mainloop()


# In[ ]:





# In[ ]:





from tkinter import *
import numpy as np

x_data = np.array([-6.258, -6.232, -6.180, -6.105, -6.007, -5.888, -5.753, -5.603, -5.439, -5.261,
                   -5.070, -4.865, -4.648, -4.419, -4.177, -3.923, -3.657, -3.379, -3.089, -2.788,
                   -2.476, -2.153, -1.819, -1.475, -1.121, -0.757, -0.383, 0.000, 0.391, 0.790,
                   1.196, 1.612, 2.036, 2.468, 2.909, 3.358, 3.814, 4.279, 4.750, 5.228,
                   5.714, 6.206, 6.704, 7.209, 7.720, 8.237, 8.759, 9.288, 9.822, 10.362,
                   10.907, 11.458, 12.013, 12.574, 13.139, 13.709, 14.283, 14.862, 15.445, 16.032,
                   16.624, 17.219, 17.819, 18.422, 19.030, 19.641, 20.255, 20.872])

y_data = np.array([-270, -260, -250, -240, -230, -220, -210, -200, -190, -180, 
                   -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, 
                   -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 
                   60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 
                   180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 
                   290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400])

def getTemp():
    emfValue = float(EMF_label_value.get())
    if(emfValue < 0):
        deg = 7
    else:
        deg = 10
    mymodel = np.poly1d(np.polyfit(x_data, y_data, deg))
    Temperature_value = round(mymodel(emfValue),3)
    result_label.config(text=f"Temperature of the given EMF value for T type thermocouple is {Temperature_value}")



root = Tk()
root.title("EMF To Temperature Converter")

root.geometry("600x200")

test = Label(root,text="EMF To Temperature Convertor ",font=("default",15))
test.grid(row=2,column=2,columnspan=12)

EMF_label = Label(root,text="EMF (mV): ")
EMF_label_value = Entry(root)
EMF_label.grid(row=5,column=1,pady=20,padx=2)
EMF_label_value.grid(row=5,column=2,pady=20,padx=2)
Submit_button = Button(root,text="Submit",command=getTemp)
Submit_button.grid(row=5,column=3,pady=20,padx=2)

result_label = Label(root)
result_label.grid(row=7,column=2,columnspan=12 )

root.mainloop()






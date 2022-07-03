#import math library
import math
from tkinter import *



window=Tk()
window.title("Rock Mass Index Calculator")
window.geometry('800x400')



label1=Label(window,text=' Unconfined Compressive Strength :',fg='#000',font=('Playfair',12))
label1.grid(row=0,column=0,padx=15,pady=10)

label2=Label(window,text=' Material Constant :',fg='#000',font=('Arial',12))
label2.grid(row=1,column=0,padx=15,pady=10)

label3=Label(window,text=' Geological Strength Index :',fg='#000',font=('Arial',12))
label3.grid(row=2,column=0,padx=15,pady=10)

label4=Label(window,text=' Intact Rock Deformation Modulus :',fg='#000',font=('Arial',12))
label4.grid(row=3,column=0,padx=15,pady=10)

label5=Label(window,text=' Disturbance Factor :',fg='#000',font=('Arial',12))
label5.grid(row=4,column=0,padx=15,pady=10)

label6=Label(window,text=' sigma 3:',fg='#000',font=('Arial',12))
label6.grid(row=5,column=0,padx=15,pady=10)

label7=Label(window,text=' A/Q requirement:',fg='#000',font=('Arial',12))
label7.grid(row=6,column=0,padx=15,pady=10)

# label8=Label(window,text='A/Q requirement:',fg='#000',font=('Arial',12))
# label8.grid(row=7,column=0,padx=15,pady=10)

data1=StringVar()

textbox1=Entry(window,textvariable=data1, fg='blue',font=('Arial',12))

textbox1.grid(row=0,column=1,padx=110)

data2=StringVar()
textbox2=Entry(window,textvariable=data2, fg='blue',font=('Arial',12))

textbox2.grid(row=1,column=1)

data3=StringVar()
textbox3=Entry(window,textvariable=data3, fg='blue',font=('Arial',12))

textbox3.grid(row=2,column=1)

data4=StringVar()
textbox4=Entry(window,textvariable=data4, fg='blue',font=('Arial',12))

textbox4.grid(row=3,column=1)

data5=StringVar()
textbox5=Entry(window,textvariable=data5, fg='blue',font=('Arial',12))

textbox5.grid(row=4,column=1)

data6=StringVar()
textbox6=Entry(window,textvariable=data6, fg='blue',font=('Arial',12))

textbox6.grid(row=5,column=1)

data7=StringVar()
textbox7=Entry(window,textvariable=data7, fg='blue',font=('Arial',12))

textbox7.grid(row=6,column=1)

# data8=StringVar()
# textbox8=Entry(window,textvariable=data8, fg='blue',font=('Arial',12))

# textbox8.grid(row=7,column=1)

e=2.718281828459045
pi1 = 22/7
def myfunction():

	try:
		temp1,temp2=float(data1.get()),float(data4.get())
		if float(data5.get()) > 1:

			emptylebel1.config(text="")
			emptylebel2.config(text="")
			emptylebel3.config(text="")
			textbox3.config(text="Disturbance Factor should be equal or less than 1")
		else:
			mb=float(data2.get())*e**((float(data3.get())-100)/(28-14* float(data5.get())))
			s = e**((float(data3.get())-100)/(9-3* float(data5.get())))
			a = 0.5 + (1/6)*(e**(-(float(data3.get()))/15) - e**(-20/3))
			sigma1=float(data6.get())+float(data1.get())*((((mb*float(data6.get()))/float(data1.get())) + s)**a)
			sigmat=float(data1.get())/(0.81*float(data2.get())+7)
			sigmacm=float(data1.get())*((mb+4*s-a*(mb-8*s))*((mb/4 + s)**(a-1)))/2*(1+a)*(2+a)
			# σ3max=0.47*sigmacm**0.06*σ
			# sigma3 taken so change it vishal
			sigma3=0.20108835594
			Phm=((math.asin((6*a*mb*((s+mb*sigma3)**(a-1)))/(2*(1+a)*(2+a)+6*a*mb*((s+mb*sigma3)**(a-1)))))*180)/pi1
			Cm=((float(data1.get())*((1+2*a)*s+(1-a)*mb*sigma3)*((s+mb*sigma3)**(a-1)))/(1+a)*(2+a)*(((1+6*a*mb*((s+mb*sigma3)**(a-1)))/(1+a)*(2+a))** 0.5))
			Erm=100000*((1-float(data5.get())/2)/(1+e**(75+25*float(data5.get())-float(data3.get()))/11))
			phm2 = math.asin(1 - 2/(2 + a*mb*(((((mb*float(data6.get()))/float(data1.get())) + s)**(a-1)))))*(180/pi1)
			sigmacm2 =  float(data1.get())*((((mb*float(data6.get()))/float(data1.get())) + s)**(a-1))*((((mb*float(data6.get()))/float(data1.get())) + s)-a*mb)
			Cm2 = sigmacm2*(1-math.sin(phm2))/(2*math.cos(phm2))
   
			emptylebel1.config(text="Erm :" + str(round(Erm,3)))
			emptylebel2.config(text="Phm :" + str(round(Phm,3)) + "degree")
			emptylebel3.config(text="Cm :" + str(round(Cm,3)))
			emptylebel4.config(text="sigmacm :" + str(round(sigmacm,3)))
			emptylebel5.config(text="sigmat :" + str(round(sigmat,3)))
   			# emptylebel6.config(text="Cm2 :" + str(round(Cm2,3)))
			emptylebel7.config(text="sigmacm2 :" + str(round(sigmacm2,3)))
			emptylebel8.config(text="phm2 :" + str(round(phm2,3)))
			textbox3.config(text="")

			
	except:
		textbox3.config(text="Enter all fields with correct Value")
		emptylebel1.config(text="")
		emptylebel2.config(text="")
		emptylebel3.config(text="")
		emptylebel4.config(text="")
		emptylebel5.config(text="")
  		# emptylebel6.config(text="")
		emptylebel7.config(text="")
		emptylebel8.config(text="")


 
button1=Button(window,command=myfunction, text="Result",bg='#288ba8',fg='white',font=('Arial',14))
button1.grid(row=8,column=1)

emptylebel1=Label(window ,fg='green',font=('Arial',12))
emptylebel1.grid(row=9,column=0,pady=20,padx=45)

emptylebel2=Label(window ,fg='green',font=('Arial',12))
emptylebel2.grid(row=10,column=0,pady=20,padx=45)

emptylebel3=Label(window ,fg='green',font=('Arial',12))
emptylebel3.grid(row=11,column=0,pady=20,padx=45)

emptylebel4=Label(window ,fg='green',font=('Arial',12))
emptylebel4.grid(row=12,column=0,pady=20,padx=45)

emptylebel5=Label(window ,fg='green',font=('Arial',12))
emptylebel5.grid(row=13,column=0,pady=20,padx=45)

# emptylebel6=Label(window ,fg='green',font=('Arial',12))
# emptylebel6.grid(row=11,column=0,pady=20,padx=45)

emptylebel7=Label(window ,fg='green',font=('Arial',12))
emptylebel7.grid(row=14,column=0,pady=20,padx=45)

emptylebel8=Label(window ,fg='green',font=('Arial',12))
emptylebel8.grid(row=15,column=0,pady=20,padx=45)

textbox3=Label(window, fg='red',font=('Arial',12))
textbox3.grid(row=9,column=1)

window.mainloop()
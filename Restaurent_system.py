from tkinter import *
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restraunt Management System")

text_Input = StringVar()
operator=""

Tops = Frame(root, width = 1600, height= 50, bg = "powder Blue", relief = SUNKEN)
Tops.pack(side=TOP)


f1 = Frame(root, width = 800,height =700 , relief = SUNKEN)
f1.pack(side=LEFT)


f2 = Frame(root, width = 300, height= 700,bg = "powder Blue", relief = SUNKEN)
f2.pack(side=RIGHT)


#======================================================Time==========================================
localtime = time.asctime(time.localtime(time.time()))

#======================================================Time==========================================
lbInfo = Label(Tops, font=('arial', 50, 'bold'), text = "Restaurent Management System", fg = 'Steel Blue', bd = 10, anchor='w')
lbInfo.grid(row= 0, column = 0)

lbInfo = Label(Tops, font=('arial', 15, 'bold'), text = localtime, fg = 'Steel Blue', bd = 10, anchor='w')
lbInfo.grid(row= 1 , column = 0)

#======================================================Calculator==========================================
def btnClick(numbers):
	global operator
	operator= operator + str(numbers)
	text_Input.set(operator)

txtDisplay = Entry(f2, font=('arial',20,'bold'), textvariable= text_Input, bd = 30, insertwidth = 4,
bg= 'powder blue', justify='right')
txtDisplay.grid(columnspan= 4)

def btnClearDisplay():
	global operator
	operator=""
	text_Input.set("")

def btnEqaulsInput():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator=""
	
def Ref():
	x = random.randint(12908, 60238)
	randomRef = str(x)
	rand.set(randomRef)
	
	CoF = float(FrenchFries.get())
	CoHashBrowns= float(Hash_browns.get())
	CoVegBurger= float(Veg_Burger.get())
	CoSandwich= float(Sandwich.get())
	CoDrinks = float(Drinks.get())
	CoExtraCheese = float(Cheese.get())
	
	CostofFries = CoF * 0.99
	CostofDrinks = CoDrinks * 1.00
	CostofSandwich = CoSandwich * 2.89
	CostofBurger = CoVegBurger * 3.49
	CostofExtraCheese = CoExtraCheese * 0.99
	CostofHashBrown = CoHashBrowns * 2.49

	CostofMeal = "$", str('%.sf' % (CostofBurger+CostofFries+ CostofDrinks+CostofSandwich+CostofExtraCheese+CostofHashBrown))
	
	PayTax = ((CostofBurger+CostofFries+ CostofDrinks+CostofSandwich+CostofExtraCheese+CostofHashBrown)*0.2)
	
	TotalCost = (CostofBurger+CostofFries+ CostofDrinks+CostofSandwich+CostofExtraCheese+CostofHashBrown)
	
	Ser_Charge =  ((CostofBurger+CostofFries+ CostofDrinks+CostofSandwich+CostofExtraCheese+CostofHashBrown)/99)
	
	Service = "$", str("%.2f" % Ser_Charge)
	
	OverallCost = "$", str("%.2f"%(PayTax+TotalCost+ Ser_Charge))
	PaidTax = "$", str("%.2f"% PayTax)
	
	Service_Charge.set(Service)
	
	Cost.set(CostofMeal)
	
	Tax.set(PaidTax)
	
	SubTotal.set(CostofMeal)
	
	Total.set(OverallCost)
	
	
	
def qExit():
	root.destroy()
	
def Reset():
	rand.set("")
	FrenchFries.set("")
	Hash_browns.set("")
	SubTotal.set("")
	Service_Charge.set("")
	Drinks.set("")
	Tax.set("")
	Cost.set("")
	Veg_Burger.set("")
	Cheese.set("")
	Sandwich.set("")
	Total.set("")
	
#=============================buttons======================================================================
btn7 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="7", bg="powder blue", command =lambda:btnClick(7)).grid(row=2, column = 0)

btn8 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="8", bg="powder blue", command =lambda:btnClick(8)).grid(row=2, column = 1)

btn9 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="9", bg="powder blue", command =lambda:btnClick(9)).grid(row=2, column = 2)

btnAddition = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="+", bg="powder blue", command =lambda:btnClick("+")).grid(row=2, column = 3)
#=============================buttons======================================================================

btn4 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="4", bg="powder blue", command =lambda:btnClick(4)).grid(row=3, column = 0)

btn5 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="5", bg="powder blue", command =lambda:btnClick(5)).grid(row=3, column = 1)

btn6 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="6", bg="powder blue", command =lambda:btnClick(6)).grid(row=3, column = 2)

btnSubtraction = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="-", bg="powder blue", command =lambda:btnClick("-")).grid(row=3, column = 3)

#=============================buttons======================================================================

btn1 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="1", bg="powder blue", command =lambda:btnClick(1)).grid(row=4, column = 0)

btn2 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="2", bg="powder blue", command =lambda:btnClick(2)).grid(row=4, column = 1)

btn3 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="3", bg="powder blue", command =lambda:btnClick(3)).grid(row=4, column = 2)

btnMultiply = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="*", bg="powder blue", command =lambda:btnClick("*")).grid(row=4, column = 3)

#=============================buttons======================================================================

btnClear = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="C", bg="powder blue", command= btnClearDisplay).grid(row=5, column = 0)

btn0 = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="0", bg="powder blue", command =lambda:btnClick(0)).grid(row=5, column = 1)

btnEqauls = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="=", bg="powder blue", command= btnEqaulsInput).grid(row=5, column = 2)

btnDivision = Button(f2, padx= 16, pady= 16, bd = 8, fg="Black", font=('arial', 20, 'bold'), 
text="/", bg="powder blue", command =lambda:btnClick("/")).grid(row=5, column = 3)

#=======================================Restaurent Info 1============================================================
rand= StringVar()
FrenchFries = StringVar()
Burger = StringVar()
Hash_browns = StringVar()
SubTotal = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Veg_Burger = StringVar()
Cheese = StringVar()
Sandwich = StringVar()
Total = StringVar()


lblReference = Label(f1,font=('arial', 16,'bold'), text="Reference", bd = 16,anchor='w')
lblReference.grid(row= 0, column= 0)
txtReference= Entry(f1,font=('arial', 16,'bold'), textvariable=rand, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtReference.grid(row= 0, column= 1)

lblFrenchFries = Label(f1,font=('arial', 16,'bold'), text="Spicy Fries", bd = 16,anchor='w')
lblFrenchFries.grid(row= 1, column= 0)
txtFrenchFries= Entry(f1,font=('arial', 16,'bold'), textvariable=FrenchFries, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtFrenchFries.grid(row= 1, column= 1)

lblVegBurger = Label(f1,font=('arial', 16,'bold'), text="Veg Burger", bd = 16,anchor='w')
lblVegBurger.grid(row= 2, column= 0)
txtVegBurger= Entry(f1,font=('arial', 16,'bold'), textvariable=Veg_Burger, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtVegBurger.grid(row= 2, column= 1)

lblHashbrowns = Label(f1,font=('arial', 16,'bold'), text="Hash browns", bd = 16,anchor='w')
lblHashbrowns.grid(row= 3, column= 0)
txtHashbrowns= Entry(f1,font=('arial', 16,'bold'), textvariable=Hash_browns, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtHashbrowns.grid(row= 3, column= 1)

lblSandwich = Label(f1,font=('arial', 16,'bold'), text="Cuban Sandwich", bd = 16,anchor='w')
lblSandwich.grid(row= 4, column= 0)
txtSandwich= Entry(f1,font=('arial', 16,'bold'), textvariable=Sandwich, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtSandwich.grid(row= 4, column= 1)


lblExtraCheese = Label(f1,font=('arial', 16,'bold'), text="Extra Cheese", bd = 16,anchor='w')
lblExtraCheese.grid(row= 5, column= 0)
txtExtraCheese= Entry(f1,font=('arial', 16,'bold'), textvariable=Cheese, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtExtraCheese.grid(row= 5, column= 1)


#=======================================Restaurent Info 2============================================================

lblDrinks = Label(f1,font=('arial', 16,'bold'), text="Drinks", bd = 16,anchor='w')
lblDrinks.grid(row= 0, column= 2)
txtDrinks= Entry(f1,font=('arial', 16,'bold'), textvariable=Drinks, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtDrinks.grid(row= 0, column= 3)

lblCost= Label(f1,font=('arial', 16,'bold'), text="Cost", bd = 16,anchor='w')
lblCost.grid(row= 1, column= 2)
txtCost= Entry(f1,font=('arial', 16,'bold'), textvariable=Cost, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtCost.grid(row= 1, column= 3)

lblService = Label(f1,font=('arial', 16,'bold'), text="Service", bd = 16,anchor='w')
lblService.grid(row= 2, column= 2)
txtService= Entry(f1,font=('arial', 16,'bold'), textvariable=Service_Charge, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtService.grid(row= 2, column= 3)

lblStateTax = Label(f1,font=('arial', 16,'bold'), text="State Tax", bd = 16,anchor='w')
lblStateTax.grid(row= 3, column= 2)
txtStateTax= Entry(f1,font=('arial', 16,'bold'), textvariable=Tax, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtStateTax.grid(row= 3, column= 3)

lblSubTotal = Label(f1,font=('arial', 16,'bold'), text="Sub Total", bd = 16,anchor='w')
lblSubTotal.grid(row= 4, column= 2)
txtSubTotal= Entry(f1,font=('arial', 16,'bold'), textvariable=SubTotal, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtSubTotal.grid(row= 4, column= 3)

lblTotal = Label(f1,font=('arial', 16,'bold'), text="Total", bd = 16,anchor='w')
lblTotal.grid(row= 5, column= 2)
txtTotal= Entry(f1,font=('arial', 16,'bold'), textvariable=Total, bd = 16,insertwidth= 4, bg="powder blue", justify= "right")
txtTotal.grid(row= 5, column= 3)

#============================================================================================================================
btnTotal = Button(f1, padx= 16, pady= 8, fg= "Black", font=('arial', 16, 'bold'), width= 10 , text = "Total",bg= "Powder Blue", command = Ref).grid(row= 7, column = 1)

btnReset = Button(f1, padx= 16, pady= 8, fg= "Black", font=('arial', 16, 'bold'), width= 10 , text = "Reset",bg= "Powder Blue", command = Reset).grid(row= 7, column = 2)

btnExit = Button(f1, padx= 16, pady= 8, fg= "Black", font=('arial', 16, 'bold'), width= 10 , text = "Exit",bg= "Powder Blue", command = qExit).grid(row= 7, column = 3)


root.mainloop()


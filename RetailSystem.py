from tkinter import *
from tkinter import messagebox
import random
import os,tempfile,smtplib



#Functionality part
def clear_entry():
    clearEntry()

    
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnoEntry.delete(0,END)
    textarea.delete(1.0,END)

    cosmeticpriceEntry.delete(0,END)
    groocerypriceEntry.delete(0,END)
    colddrinkspriceEntry.delete(0,END)
    cosmetictaxEntry.delete(0,END)
    groocerytaxEntry.delete(0,END)
    colddrinkstaxEntry.delete(0,END) 

    cosmeticpriceEntry.insert(0,0)
    groocerypriceEntry.insert(0,0)
    colddrinkspriceEntry.insert(0,0)
    cosmetictaxEntry.insert(0,0)
    groocerytaxEntry.insert(0,0)
    colddrinkstaxEntry.insert(0,0)
   



def email_button():
    def send():
        try:
                    
            obj = smtplib.SMTP('smtp.gmail.com', 587)
            obj.starttls()
            obj.login(senderEntry.get(),passeordEntry.get())
            message = emailtextarea.get(.0,END)
            reciever_address = reciverEntry.get()
            obj.sendmail(senderEntry.get(), reciever_address, message)
            obj.quit()
            messagebox.showinfo("Success", "Email sent successfully",parent = emailwindow)
            emailwindow.destroy()
        except:
            messagebox.showerror("Error", "Failed to send email",parent = emailwindow)



    if textarea.get(1.0,END) == '\n':
        messagebox.showerror("Error", "Bill is empty")
    else:
        emailwindow = Toplevel()
        emailwindow.title("Send Email")
        emailwindow.resizable(0,0)
        emailwindow.config(bg='gray20')
        emailwindow.grab_set()

        sender_frame = LabelFrame(emailwindow,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='gold')
        sender_frame.grid(row=0,column=0,padx=40,pady=20)

        senderlebel = Label(sender_frame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        senderlebel.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        senderEntry = Entry(sender_frame,font=('arial',12,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=10)


        passeordlebel = Label(sender_frame,text="Password",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        passeordlebel.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        passeordEntry = Entry(sender_frame,font=('arial',12,'bold'),bd=2,width=23,relief=RIDGE,show='x')
        passeordEntry.grid(row=1,column=1,padx=10,pady=10)



        recipentframe = LabelFrame(emailwindow,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='gold')
        recipentframe.grid(row=1,column=0,padx=40,pady=20)

        reciverlebel = Label(recipentframe,text="Email Address",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        reciverlebel.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        reciverEntry = Entry(recipentframe,font=('arial',12,'bold'),bd=2,width=24,relief=RIDGE)
        reciverEntry.grid(row=0,column=1,padx=10,pady=10)

        messagelebel = Label(recipentframe,text="Message",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        messagelebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        emailtextarea = Text(recipentframe,bd=2,width=48,height=16)
        emailtextarea.grid(row=2,column=0,padx=10,pady=5,columnspan=2)
        emailtextarea.delete(1.0,END)
        emailtextarea.insert(END,textarea.get(1.0,END))

        sendbutton = Button(emailwindow,text='SEND',font=('arial',16,'bold'),width=15,background='gold',activebackground='gold',command=send)
        sendbutton.grid(row=2,column=0,padx=10,pady=10)







        emailwindow.mainloop()



def print_bill():
    if textarea.get(1.0,END) =='\n':
        messagebox.showerror("Error", "Bill is empty Details are requried")
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')




def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnoEntry.get():
            f = open(f'bills/{i}','r')
            textarea.delete(1.0,END)

            for data in f:
                textarea.insert(END,data)
            f.close()  
            break

    else:
        messagebox.showerror("Error","Bill not found")

    pass


def savebill():
    result = messagebox.askyesno('Confirm','Do you want to save the bill')
    
    if result:
        bill_content = textarea.get(1.0,END)
        file = open(f"bills/{billno}.txt","w") 
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill {billno} saved successfully')
    



def billGenerate():

    #Getting the values from the entry fields
    
    # if nameEntry.get()=='' or phoneEntry.get()=='':
    #     messagebox.showerror("Error", "Customer Details Are Requires")

    # elif cosmeticpriceEntry.get() == '' and groocerypriceEntry.get() =='' and colddrinkspriceEntry.get() == '':
    #     messagebox.showerror("Error", "Product Is Not Selected")

    # elif cosmeticpriceEntry.get() == '0.0 Rs' and groocerypriceEntry.get() =='0.0 Rs' and colddrinkspriceEntry.get() == '0.0 Rs':
    #     messagebox.showerror("Error", "Product Is Not Selected")

    # else:
    global billno
    billno = random.randint(999,9999)
    
    textarea.delete(1.0,END)
    textarea.insert(END,'*'*48+'\n')
    textarea.insert(END,'\t\t**Welcome Customer**\n')
    textarea.insert(END,'*'*48+'\n')
    textarea.insert(END,f'\n Bill Number   : {billno}')
    textarea.insert(END,f'\n Customer Name : {nameEntry.get()}')
    textarea.insert(END,f'\n Phone Number  : {phoneEntry.get()}')
    textarea.insert(END,'\n'+'*'*48+'\n')
    textarea.insert(END,' Product\t\t\tQIT\t\t'+'  Price')
    textarea.insert(END,'\n'+'*'*48+'\n')

    if bathsoapEntry.get() != '0':
        textarea.insert(END,'\n Bath Soap\t\t\t'+' '+bathsoapEntry.get()+'\t\t '+''+str(bathsoapprice)+' Rs')

    if facecreamEntry.get() != '0':
        textarea.insert(END,'\n Face Cream\t\t\t'+' '+facecreamEntry.get()+'\t\t '+''+str(facecreamprice)+' Rs')   

    if facewashEntry.get() != '0':
        textarea.insert(END,'\n Face Wash \t\t\t'+' '+facewashEntry.get()+'\t\t '+''+str(facewashprice)+' Rs')

    if hairsparyEntry.get() != '0':
        textarea.insert(END,'\n Hair Spary\t\t\t'+' '+hairsparyEntry.get()+'\t\t '+''+str(hairsparyprice)+' Rs')
    
    if hairgelEntry.get() != '0':
        textarea.insert(END,'\n Hair Gel\t\t\t'+' '+hairgelEntry.get()+'\t\t '+''+str(hairgelprice)+' Rs')  
         
    if bodylotionEntry.get() != '0':
        textarea.insert(END,'\n Body Lotion\t\t\t'+' '+bodylotionEntry.get()+'\t\t '+''+str(bodylotionprice)+' Rs')
    
    if riseEntry.get() != '0':
        textarea.insert(END,'\n Rise\t\t\t'+' '+riseEntry.get()+'\t\t '+''+str(riceprice)+' Rs')

    if oliveoilEntry.get() != '0':
        textarea.insert(END,'\n Olive Oil\t\t\t'+' '+oliveoilEntry.get()+'\t\t '+''+str(oliveoilprice)+' Rs')

    if dalEntry.get() != '0':
        textarea.insert(END,'\n Split Grain\t\t\t'+' '+dalEntry.get()+'\t\t '+''+str(dalprice)+' Rs')

    if wheatEntry.get() != '0':
        textarea.insert(END,'\n Wheat\t\t\t'+' '+wheatEntry.get()+'\t\t '+''+str(wheatprice)+' Rs')

    if sugarEntry.get() != '0':
        textarea.insert(END,'\n Sugar\t\t\t'+' '+sugarEntry.get()+'\t\t '+''+str(sugarprice)+' Rs')   

    if TeaEntry.get() != '0':
        textarea.insert(END,'\n Tea\t\t\t'+' '+TeaEntry.get()+'\t\t '+''+str(Teaprice)+' Rs')

    if maazaEntry.get() != '0':
        textarea.insert(END,'\n Maaza\t\t\t'+' '+maazaEntry.get()+'\t\t '+''+str(maazaPrice)+' Rs')

    if pepsiEntry.get() != '0':
        textarea.insert(END,'\n Pepsi\t\t\t'+' '+pepsiEntry.get()+'\t\t '+''+str(pepsiPrice)+' Rs')

    if spriteEntry.get() != '0':
        textarea.insert(END,'\n Sprite\t\t\t'+' '+spriteEntry.get()+'\t\t '+''+str(spritePrice)+' Rs')

    if dewEntry.get() != '0':
        textarea.insert(END,'\n Dew\t\t\t'+' '+dewEntry.get()+'\t\t '+''+str(dewPrice)+' Rs')

    if frootiEntry.get() != '0':
        textarea.insert(END,'\n Frooti\t\t\t'+' '+frootiEntry.get()+'\t\t '+''+str(frootiPrice)+' Rs')

    if cocacolaEntry.get() != '0':
        textarea.insert(END,'\n Coca Cola\t\t\t'+' '+cocacolaEntry.get()+'\t\t '+''+str(cocacolaPrice)+' Rs')

    textarea.insert(END,'\n'+'-'*48)

    if cosmetictaxEntry.get() != '0':
        textarea.insert(END,'\n Csmetics Tax\t\t\t'+str(cosmetictaxEntry.get()))

    if groocerytaxEntry.get() != '0':
        textarea.insert(END,'\n Groocery Tax\t\t\t'+str(groocerytaxEntry.get()))
    
    if colddrinkstaxEntry.get() != '0':
        textarea.insert(END,'\n Cold Drinks Tax\t\t\t'+str(colddrinkstaxEntry.get()))

    textarea.insert(END,'\n\n\n Total Bill \t\t\t'+str(totalbill))
    textarea.insert(END,'\n'+'*'*48)
    savebill()



def clearEntry():

    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairsparyEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    bodylotionEntry.delete(0,END)

    riseEntry.delete(0,END)
    oliveoilEntry.delete(0,END)
    dalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    sugarEntry.delete(0,END)
    TeaEntry.delete(0,END)

    maazaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    dewEntry.delete(0,END)
    frootiEntry.delete(0,END)
    cocacolaEntry.delete(0,END)

    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsparyEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)

    riseEntry.insert(0,0)
    oliveoilEntry.insert(0,0)
    dalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    TeaEntry.insert(0,0)

    maazaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    dewEntry.insert(0,0)
    frootiEntry.insert(0,0)
    cocacolaEntry.insert(0,0)



def total():
    global bathsoapprice,facecreamprice,facewashprice,hairgelprice,hairsparyprice,bodylotionprice

    bathsoapprice = int(bathsoapEntry.get()) * 20
    facecreamprice = int(facecreamEntry.get()) * 50
    facewashprice = int(facewashEntry.get()) * 100
    hairsparyprice = int(hairsparyEntry.get()) * 150
    hairgelprice = int(hairgelEntry.get()) * 80
    bodylotionprice = int(bodylotionEntry.get()) * 60


    global riceprice,oliveoilprice,dalprice,wheatprice,sugarprice,Teaprice

    riceprice = int(riseEntry.get()) * 40
    oliveoilprice = int(oliveoilEntry.get()) * 200
    dalprice = int(dalEntry.get()) * 100
    wheatprice = int(wheatEntry.get()) * 50
    sugarprice = int(sugarEntry.get()) * 20
    Teaprice = int(TeaEntry.get()) * 80

    global maazaPrice,pepsiPrice,spritePrice,dewPrice,frootiPrice,cocacolaPrice 

    maazaPrice = int(maazaEntry.get()) * 50
    pepsiPrice = int(pepsiEntry.get()) * 50
    spritePrice = int(spriteEntry.get()) * 50
    dewPrice = int(dewEntry.get()) * 50
    frootiPrice = int(frootiEntry.get()) * 50
    cocacolaPrice = int(cocacolaEntry.get()) * 50

    cosmeticpriceEntry.delete(0,END)
    totalcosmetic = bathsoapprice + facewashprice + facecreamprice + hairsparyprice + hairgelprice + bodylotionprice
    cosmeticpriceEntry.insert(0,str(totalcosmetic * 1.0) + ' Rs')
    
    groocerypriceEntry.delete(0,END)
    totalgroocery = riceprice + oliveoilprice + dalprice + wheatprice + sugarprice + Teaprice
    groocerypriceEntry.insert(0,str(totalgroocery * 1.0) +' Rs')

    colddrinkspriceEntry.delete(0,END)
    totalcoldrnks = maazaPrice + pepsiPrice + spritePrice + dewPrice + frootiPrice + cocacolaPrice
    colddrinkspriceEntry.insert(0,str(totalcoldrnks * 1.0) + ' Rs')
    
    global totalbill
    cosmeticstax = totalcosmetic * 0.12
    groocerystax = totalgroocery * 0.05
    coldrnkstax = totalcoldrnks * 0.09
    totaltax = cosmeticstax + groocerystax + coldrnkstax
    
    cosmetictaxEntry.delete(0,END)
    groocerytaxEntry.delete(0,END)
    colddrinkstaxEntry.delete(0,END)

    cosmetictaxEntry.insert(0,str(cosmeticstax) + ' Rs')
    groocerytaxEntry.insert(0,str(groocerystax) + ' Rs')
    colddrinkstaxEntry.insert(0,str(coldrnkstax) + ' Rs')

    totalbill = totaltax + totalgroocery + totalcoldrnks + totalcosmetic



    


    # taxEntry.insert(0,str(totaltax * 1.0) + ' Rs')




#Mail Window GUI
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685+0+0')
root.resizable(0,0)
root.grab_set()
root.iconbitmap('bill.ico')
root.config(background='gold')

f = ('times new roman',15,'bold')
ef = ('times new roman',15,'bold')

headingLable = Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLable.pack(fill=X,pady=5)

#customer details frame

customer_details_frame = LabelFrame(root,text='Customer Details',font=f,fg ='gold',bd=8,relief=GROOVE,bg = 'gray20')
customer_details_frame.pack(fill=X)

nameLabel= Label(customer_details_frame,text='Name -',bg = 'gray20',font=f,fg='gold')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry = Entry(customer_details_frame,font=f,bd=4,width=18)
nameEntry.grid(row=0,column=1,padx=8)


phoneLabel= Label(customer_details_frame,text='Phone Number -',bg = 'gray20',font=f,fg='gold')
phoneLabel.grid(row=0,column=2,padx=20)

phoneEntry = Entry(customer_details_frame,font=f,bd=4,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnoLabel= Label(customer_details_frame,text='Bill Number -',bg = 'gray20',font=f,fg='gold')
billnoLabel.grid(row=0,column=4,padx=20)

billnoEntry = Entry(customer_details_frame,font=f,bd=4,width=18)
billnoEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customer_details_frame,text='SEARCH',font= ('times new roman',15,'bold'),width=10,background='gold',activebackground='gold',command=search_bill)
searchButton.grid(row=0,column=6,padx=25,pady=8)


#Product frame
productsFrame = Frame(root,background='gold')
productsFrame.pack(pady=10)

cosmaticsFrame = LabelFrame(productsFrame,text='Cosmatics',font=f,fg ='gold',bd=8,relief=GROOVE,bg = 'gray20')
cosmaticsFrame.grid(row=0,column=0)

bathsoapLabel = Label(cosmaticsFrame,text='Bath Soap',bg = 'gray20',font=f,fg='snow')
bathsoapLabel.grid(row=0,column=0,pady=9,sticky=W,padx=10)
bathsoapEntry = Entry(cosmaticsFrame,font=f,width=10,bd=2)
bathsoapEntry.grid(row=0,column=1,padx=20)


facecreamLabel = Label(cosmaticsFrame,text='Face Cream',bg = 'gray20',font=f,fg='snow')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky=W)
facecreamEntry = Entry(cosmaticsFrame,font=f,width=10,bd=2)
facecreamEntry.grid(row=1,column=1,padx=10,pady=9)

facewashLabel = Label(cosmaticsFrame,text='Face Wash',bg = 'gray20',font=f,fg='snow')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky=W)
facewashEntry = Entry(cosmaticsFrame,font=f,width=10,bd=2)
facewashEntry.grid(row=2,column=1,padx=10,pady=9)

hairsparyLabel = Label(cosmaticsFrame,text='Hair Spary',bg = 'gray20',font=f,fg='snow')
hairsparyLabel.grid(row=3,column=0,pady=9,padx=10,sticky=W)
hairsparyEntry = Entry(cosmaticsFrame,font=f,width=10,bd=2)
hairsparyEntry.grid(row=3,column=1,padx=10,pady=9)

hairgelLabel = Label(cosmaticsFrame,text='Hair Gel',bg = 'gray20',font=f,fg='snow')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky=W)
hairgelEntry = Entry(cosmaticsFrame,font=f,width=10,bd=2)
hairgelEntry.grid(row=4,column=1,padx=10,pady=9)

bodylotionLabel = Label(cosmaticsFrame,text='Body Lotion',bg = 'gray20',font=f,fg='snow')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky=W)
bodylotionEntry = Entry(cosmaticsFrame,font=f,width=10,bd=2)
bodylotionEntry.grid(row=5,column=1,padx=10,pady=9)


#Groocery
grooceryFrame = LabelFrame(productsFrame,text='Groocery',font=f,fg ='gold',bd=8,relief=GROOVE,bg = 'gray20')
grooceryFrame.grid(row=0,column=1,padx=5)


riseLabel = Label(grooceryFrame,text='Rise',bg = 'gray20',font=f,fg='snow')
riseLabel.grid(row=0,column=0,pady=9,sticky=W,padx=10)
riseEntry = Entry(grooceryFrame,font=f,width=10,bd=2)
riseEntry.grid(row=0,column=1,padx=20)


oliveoilLabel = Label(grooceryFrame,text='Olive Oil',bg = 'gray20',font=f,fg='snow')
oliveoilLabel.grid(row=1,column=0,pady=9,padx=10,sticky=W)
oliveoilEntry = Entry(grooceryFrame,font=f,width=10,bd=2)
oliveoilEntry.grid(row=1,column=1,padx=10,pady=9)

dalLabel = Label(grooceryFrame,text='Split Grain',bg = 'gray20',font=f,fg='snow')
dalLabel.grid(row=2,column=0,pady=9,padx=10,sticky=W)
dalEntry = Entry(grooceryFrame,font=f,width=10,bd=2)
dalEntry.grid(row=2,column=1,padx=10,pady=9)

wheatLabel = Label(grooceryFrame,text='Wheat',bg = 'gray20',font=f,fg='snow')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky=W)
wheatEntry = Entry(grooceryFrame,font=f,width=10,bd=2)
wheatEntry.grid(row=3,column=1,padx=10,pady=9)

sugarLabel = Label(grooceryFrame,text='Suger',bg = 'gray20',font=f,fg='snow')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky=W)
sugarEntry = Entry(grooceryFrame,font=f,width=10,bd=2)
sugarEntry.grid(row=4,column=1,padx=10,pady=9)

TeaLabel = Label(grooceryFrame,text='Tea',bg = 'gray20',font=f,fg='snow')
TeaLabel.grid(row=5,column=0,pady=9,padx=10,sticky=W)
TeaEntry = Entry(grooceryFrame,font=f,width=10,bd=2)
TeaEntry.grid(row=5,column=1,padx=10,pady=9)

#Cold Drinks frame
colddrinksFrame = LabelFrame(productsFrame,text='Cold Drinks',font=f,fg ='gold',bd=8,relief=GROOVE,bg = 'gray20')
colddrinksFrame.grid(row=0,column=2)

maazaLabel = Label(colddrinksFrame,text='Maaza',bg = 'gray20',font=f,fg='snow')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky=W)
maazaEntry = Entry(colddrinksFrame,font=f,width=10,bd=2)
maazaEntry.grid(row=0,column=1,padx=10,pady=9)

pepsiLabel = Label(colddrinksFrame,text='Pepsi',bg = 'gray20',font=f,fg='snow')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky=W)
pepsiEntry = Entry(colddrinksFrame,font=f,width=10,bd=2)
pepsiEntry.grid(row=1,column=1,padx=10,pady=9)

spriteLabel = Label(colddrinksFrame,text='Sprite',bg = 'gray20',font=f,fg='snow')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky=W)
spriteEntry = Entry(colddrinksFrame,font=f,width=10,bd=2)
spriteEntry.grid(row=2,column=1,padx=10,pady=9)

dewLabel = Label(colddrinksFrame,text='Dew',bg = 'gray20',font=f,fg='snow')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky=W)
dewEntry = Entry(colddrinksFrame,font=f,width=10,bd=2)
dewEntry.grid(row=3,column=1,padx=10,pady=9)

frootiLabel = Label(colddrinksFrame,text='Frooti',bg = 'gray20',font=f,fg='snow')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky=W)
frootiEntry = Entry(colddrinksFrame,font=f,width=10,bd=2)
frootiEntry.grid(row=4,column=1,padx=10,pady=9)

cocacolaLabel = Label(colddrinksFrame,text='Coca Cola',bg = 'gray20',font=f,fg='snow')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky=W)
cocacolaEntry = Entry(colddrinksFrame,font=f,width=10,bd=2)
cocacolaEntry.grid(row=5,column=1,padx=10,pady=9)

#Bill area frame

billFrame =Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=5)

billareaLabel = Label(billFrame,text='Bill Area',font=f,bd=7,relief=GROOVE)

billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT)

textarea = Text(billFrame,height=16,width=48,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)



#Bill frame
billmanuFrame = LabelFrame(root,text='Bill Menu',font=f,fg ='gold',bd=8,relief=GROOVE,bg = 'gray20')
billmanuFrame.pack(fill=X)

cosmeticpriceLabel = Label(billmanuFrame,text='Cosmetic Price',bg = 'gray20',font=f,fg='snow')
cosmeticpriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky=W)
cosmeticpriceEntry = Entry(billmanuFrame,font=f,width=10,bd=2)
cosmeticpriceEntry.grid(row=0,column=1,padx=10,pady=9)

groocerypriceLabel = Label(billmanuFrame,text='Groocery Price',bg = 'gray20',font=f,fg='snow')
groocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky=W)
groocerypriceEntry = Entry(billmanuFrame,font=f,width=10,bd=2)
groocerypriceEntry.grid(row=1,column=1,padx=10,pady=9)

colddrinkspriceLabel = Label(billmanuFrame,text='Cold Drinks Price',bg = 'gray20',font=f,fg='snow')
colddrinkspriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky=W)
colddrinkspriceEntry = Entry(billmanuFrame,font=f,width=10,bd=2)
colddrinkspriceEntry.grid(row=2,column=1,padx=10,pady=9)

#Tax

cosmetictaxLabel = Label(billmanuFrame,text='Cosmetic Tax',bg = 'gray20',font=f,fg='snow')
cosmetictaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky=W)
cosmetictaxEntry = Entry(billmanuFrame,font=f,width=10,bd=2)
cosmetictaxEntry.grid(row=0,column=3,padx=10,pady=9)

groocerytaxLabel = Label(billmanuFrame,text='Groocery Tax',bg = 'gray20',font=f,fg='snow')
groocerytaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky=W)
groocerytaxEntry = Entry(billmanuFrame,font=f,width=10,bd=2)
groocerytaxEntry.grid(row=1,column=3,padx=10,pady=9)

colddrinkstaxLabel = Label(billmanuFrame,text='Cold Drinks Tax',bg = 'gray20',font=f,fg='snow')
colddrinkstaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky=W)
colddrinkstaxEntry = Entry(billmanuFrame,font=f,width=10,bd=2)
colddrinkstaxEntry.grid(row=2,column=3,padx=10,pady=9)


#Buttonframe
buttonFrame = Frame(billmanuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=10)

totalbutton = Button(buttonFrame,text='Total',font=f,width=9,background='gray20',foreground='gold',activebackground='gray20',activeforeground='gold',command=total)
totalbutton.grid(row=0,column=0,padx=5,pady=20)

billbutton = Button(buttonFrame,text='Bill',font=f,width=9,background='gray20',foreground='gold',activebackground='gray20',activeforeground='gold',command=billGenerate)
billbutton.grid(row=0,column=1,padx=5,pady=20)

emailbutton = Button(buttonFrame,text='Email',font=f,width=9,background='gray20',foreground='gold',activebackground='gray20',activeforeground='gold',command=email_button)
emailbutton.grid(row=0,column=2,padx=5,pady=20)

printbutton = Button(buttonFrame,text='Print',font=f,width=9,background='gray20',foreground='gold',activebackground='gray20',activeforeground='gold',command=print_bill)
printbutton.grid(row=0,column=3,padx=5,pady=20)

clearbutton = Button(buttonFrame,text='Clear',font=f,width=9,background='gray20',foreground='gold',activebackground='gray20',activeforeground='gold',command=clear_entry)
clearbutton.grid(row=0,column=4,padx=5,pady=10)

clearEntry()



root.mainloop()
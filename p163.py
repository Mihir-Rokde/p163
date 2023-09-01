from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Heart Report")
root.geometry("400x00")
root.configure(background="red")

q1rb=StringVar(value="0")
q1=Label(root,text="Do you experience shortness of breathing during routine activities?")
q1.pack()
q1r1=Radiobutton(root,text="yes",variable=q1rb,value="yes")
q1r1.pack()
q1r2=Radiobutton(root,text="no",variable=q1rb,value="no")
q1r2.pack()

q2rb=StringVar(value="0")
q2=Label(root,text="Do you have swelling in the feet/ankles/legs or abdomen ?")
q2.pack()
q2r1=Radiobutton(root,text="yes",variable=q2rb,value="yes")
q2r1.pack()
q2r2=Radiobutton(root,text="no",variable=q2rb,value="no")
q2r2.pack()

q3rb=StringVar(value="0")
q3=Label(root,text="Do you feel any of the symptoms - disorientation,confusion,or loss of memory ?")
q3.pack()
q3r1=Radiobutton(root,text="yes",variable=q3rb,value="yes")
q3r1.pack()
q3r2=Radiobutton(root,text="no",variable=q3rb,value="no")
q3r2.pack()

q4rb=StringVar(value="0")
q4=Label(root,text="Do you shortness of breath while at rest or lying down?")
q4.pack()
q4r1=Radiobutton(root,text="yes",variable=q4rb,value="yes")
q4r1.pack()
q4r2=Radiobutton(root,text="no",variable=q4rb,value="no")
q4r2.pack()

q5rb=StringVar(value="0")
q5=Label(root,text="Do you experience persistent wheezing/coughing that produces white or ping blood?")
q5.pack()
q5r1=Radiobutton(root,text="yes",variable=q5rb,value="yes")
q5r1.pack()
q5r2=Radiobutton(root,text="no",variable=q5rb,value="no")
q5r2.pack()


def feverscore():
    score=0
    if q1rb.get()=="yes":
        score=score+20
        print(score)
    if q2rb.get()=="yes":
        score=score+20
        print(score)
    if q3rb.get()=="yes":
        score=score+20
        print(score)
    if q4rb.get()=="yes":
         score=score+20
         print(score)
    if q5rb.get()=="yes":
         score=score+20
         print(score)
    if score<=40:
        messagebox.showinfo("Report","You dont need to visit a Doctor.")
    elif score>10 and score<=30:
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    else:
        messagebox.showinfo("Report","I strongly advice you to visit a doctor")
btn=Button(root,text="Click Me",command=feverscore)
btn.pack()

root.mainloop()
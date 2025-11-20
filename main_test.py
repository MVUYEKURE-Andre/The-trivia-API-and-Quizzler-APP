from tkinter import *
THEME_COLOR = "#375362"
current_score=0
window=Tk()
window.title("Quizzler")

# window.geometry("500x500")
window.config(padx=20,pady=20,bg=THEME_COLOR)

score_label=Label(text=f"score:{current_score}",fg="white",bg=THEME_COLOR,
                  font=("arial",30,"bold"))
score_label.grid(row=0,column=1)

# score_mark_label=Label(text="0")
# score_mark_label.pack()
canvas=Canvas(width=300,height=250,bg="white")
queation=canvas.create_text(150,125,width=280,text="here is the question on the card",
                            font=("arial",20,"italic"),fill=THEME_COLOR)
canvas.grid(row=1,column=0,columnspan=2,pady=20)
true_img=PhotoImage(file="images/true.png")
false_img=PhotoImage(file="images/false.png")

yes_button=Button(image=true_img,bg=THEME_COLOR,highlightthickness=0)
yes_button.grid(row=2,column=0)
no_button=Button(image=false_img,bg=THEME_COLOR,highlightthickness=0)
no_button.grid(row=2,column=1)






window.mainloop()
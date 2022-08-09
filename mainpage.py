from tkinter import *
from timeit import default_timer as timer
import random
import csv


#from PIL import ImageTk,Image
canvas=Tk()
canvas.title('Typing Speed Test - Menu')
canvas.geometry('550x600')
canvas.config(background='#23272A')
def icon(i):
      i.iconbitmap(r"icon.ico")
def hide(x):
      #a function that hides button
      x.place_forget()
icon(canvas)

def Login():
      global login
      #login window
      login=Tk()
      login.title('login')
      login.geometry('550x175')
      login.config(background='#23272A')
      icon(login)
      username = Label(login, text=" Username :",bg="#23272A",fg='#FFFFFF',font=("Arial Black",10)).place(relx=0.1, rely=0.2)
      login_username = Entry(login, width=50,bg="white", fg ="black", borderwidth="4")
      login_username.place(relx=0.3, rely=0.2)
      
      password = Label(login, text=" Password :",bg="#23272A",fg='#FFFFFF',font=("Arial Black",10)).place(relx=0.1, rely=0.4)
      login_passwd = Entry(login, width=50, bg="white", fg ="black", borderwidth="4",show='*')
      login_passwd.place(relx=0.3, rely=0.4)
            
      def SignUp():
            login.destroy()
            #destroys login window and Signup window appears      
            signup=Tk()
            signup.title('Create New Account')
            signup.geometry('550x300')
            signup.config(background='#23272A')
            icon(signup)    
            def back():
                  #this fuction destroys signup window and restarts login window
                  signup.destroy()
                  Login()
            
            
            username = Label(signup, text=" Username:",bg="#23272A",fg='#FFFFFF',font=("Arial Black",10)).place(relx=0.1, rely=0.2)
            create_username = Entry(signup, width=50, bg="white", fg ="black", borderwidth="4")
            create_username.place(relx=0.3, rely=0.2)
            
            password = Label(signup, text=" Password:",bg="#23272A",fg='#FFFFFF',font=("Arial Black",10)).place(relx=0.1, rely=0.4)
            create_pass = Entry(signup, width=50, bg="white", fg ="black", borderwidth="4")
            create_pass.place(relx=0.3, rely=0.4)

            password = Label(signup, text="Confirm\nPassword:",bg="#23272A",fg='#FFFFFF',font=("Arial Black",10)).place(relx=0.1, rely=0.55)
            confirmpass = Entry(signup, width=50, bg="white", fg ="black", borderwidth="4")
            confirmpass.place(relx=0.3, rely=0.6)

            def savedetails():
                  found = False
                  with open('Regfile.csv', 'r',newline='') as fs:
                        read = csv.reader(fs)                
                        for row in read:
                              if row[0]==create_username.get():
                                    username = Label(signup, text="\tusername taken!\t",bg="#23272A",fg='red').place(relx=0.3, rely=0.7)
                                    found = True
                  if create_username.get()=='' or create_pass.get()=='':
                        username = Label(signup, text="Enter your data!",bg="#23272A",fg='red').place(relx=0.3, rely=0.7)
                  if len(create_username.get())>7:
                        username = Label(signup, text="Enter less that 7 charecters",bg="#23272A",fg='red').place(relx=0.3, rely=0.7)             
                  else:
                        if found==False:
                              
                              if create_pass.get()==confirmpass.get():
                                    with open('Regfile.csv', 'a+',newline='') as fs:
                                          accuracy = 0
                                          highscore = 0
                                          w = csv.writer(fs)
                                          w.writerow([create_username.get(),create_pass.get(),highscore,accuracy])
                                          fs.close()
                                          hide(B6)
                                          username = Label(signup, text="\tRegistered\t",bg="#23272A",fg='green').place(relx=0.3, rely=0.7)

                              else:
                                    username = Label(signup, text="Passwords do not match!\t\t\t",bg="#23272A",fg='red').place(relx=0.3, rely=0.7)
                  
                        
            B6=Button(signup,text="Sign In",width=12,height=2,bg='#5865F2',fg='white',
                  font=("Arial Black",10),command = savedetails)
            B6.place(relx=0.39,rely=0.8)
            
            B7=Button(signup,text="Back",width=12,height=2,bg='#5865F2',fg='white',
                  font=("Arial Black",10),command=back)
            B7.place(relx=0.69,rely=0.8)
            #signup window ends here

      def logindetails():
                global unique_code
                #To check whether the login details correct
                with open('Regfile.csv', 'r',newline='') as fs:
                    read = csv.reader(fs)
                    r=list(read)
                    for row in r:
                        if row[0]==login_username.get() and row[1]==login_passwd.get():
                            unique_code = r.index(row)
                            Game()
                            return unique_code,True
                            
                        else:
                           error = Label(login, text="Wrong Username\n or password\t",bg="#23272A",fg='red').place(relx=0.1, rely=0.6)    
                    fs.close()
      def error():
        if login_username.get()=='' or login_passwd.get()=='':
              error = Label(login, text="\tEnter your\n\tDetails\t",bg="#23272A",fg='red').place(relx=0.1, rely=0.6)  
        
        else:
              logindetails()
              
      #buttons used in login window
      B4=Button(login,text="Sign Up",width=12,height=2,bg='#5865F2',fg='white',command=SignUp)
      B4.place(relx=0.39,rely=0.6)
      
      B5=Button(login,text="Login",width=12,height=2,bg='#5865F2',fg='white',command=error)
      B5.place(relx=0.69,rely=0.6)
      #login window ends here
def Profile():
      profile=Tk()
      profile.title('profile')
      profile.geometry('250x285')
      profile.config(background='#23272A')
      label = Label(profile,text = 'PROFILE',bg="#23272A",fg='#5865F2')
      label.configure(font=("ariel", 25, "bold"))
      label.place(relx=0.2,rely=0.05)

      f = open('Regfile.csv')
      r = csv.reader(f)
      data = list(r)
      username = data[unique_code][0]
      wpm = data[unique_code][2]
      acc = data[unique_code][3]
      f.close()

      label = Label(profile,text = "Name:\t" + username,bg="#23272A",fg='#FFFFFF')
      label.configure(font=("ariel", 15, "bold"))
      label.place(relx=0.2,rely=0.3)
      label = Label(profile,text = "HIGHSCORES",bg="#23272A",fg='#5865F2')
      label.configure(font=("ariel", 15, "bold"))
      label.place(relx=0.2,rely=0.45)
      label = Label(profile,text = "WPM:\t" + wpm+ "\nAccuracy:   "+ acc+"%",bg="#23272A",fg='#FFFFFF')
      label.configure(font=("ariel", 15, "bold"))
      label.place(relx=0.2,rely=0.6)
      def destroy():
            profile.destroy()
      B5=Button(profile,text="BACK",width=10,height=2,bg='#5865F2',fg='white',command=destroy)
      B5.place(relx=0.35,rely=0.8)


def Game():
      login.destroy()
      
      start=Tk()
      start.title('Lets Begin')
      start.geometry('550x500')
      start.config(background='#23272A')
      #game starts here
      def Test():
            game=Tk()
            game.title('Typing speed test')
            game.geometry('900x600')
            game.config(background='#23272A')

            #select_story=['hi how are you','we did our projet in lab','you can dance but i cant','My cat is weird and my dog barks.']
            select_story = ["He walked over to the window and reflected on his old-fashioned surroundings. He had always loved sunny New York with its open, old-fashioned oceans.", "Then he saw something in the distance, or rather someone. It was the figure of Sameer.", "Tom gulped. He glanced at his own reflection. He was a tight-fisted, controlling, wine drinker with ruddy feet and skinny toes.", "The clouds danced like gyrating pigeons, making Tom irritable.As Tom stepped outside and Sameer came closer, he could see the blue glint in his eye.", "Plot Generator contains a wide variety of tools for creating blurbs, movies and short stories. The Plot Generator Meme is just a taster."]
            choice = random.randint(0, (len(select_story)-1))

            show = Label(game, text=select_story[choice], bg="#5865F2",fg='#FFFFFF',width = 50,height=5,wraplength=600,font=("ariel",20,'bold')).place(relx=0.02, rely=0.1)
            
            entry = Text(game,height=5,width=95,bg='white')
            entry.place(relx=0.02,rely=0.4)
            start = timer() 
            def check_result():
                  j=error=0
                  answer = entry.get('1.0','end-1c') #stores the entered text in a variable and gets the first charecter and the last charecter
                  end = timer()
                  time_taken = end-start #time-taken in seconds
                  
                  check_ans = answer.split()
                  check_select = select_story[choice].split()

                  if len(check_select)>=len(check_ans):
                        error=len(check_select)-len(check_ans)
                        for i in check_ans:
                              if i == check_select[j]:
                                    pass
                              else:
                                    error +=1
                              j+=1
                  elif len(check_select)<=len(check_ans):
                        error=len(check_ans)-len(check_select)
                        for i in check_select:
                              if i ==check_ans[j]:
                                    pass
                              else:
                                    error+=1
                              
                              j+=1
            
                  wpm = int(((len(answer)/5)-error)/(time_taken/60))
                  acc = int(((len(select_story[choice])-error)/len(select_story[choice]))*100)
                  
                  

                  if answer=='' or answer.isspace()==True:
                        intro = Label(game, text="Enter the displayed text in the text box. now, Please try again",bg="#23272A",fg='red',font=('Arial Black',10)).place(relx=0.1, rely=0.6)
                  elif wpm<0:
                        result='You have a lot of errors, Please Try again'
                        intro = Label(game, text=result,bg="#23272A",fg='red',font=('Arial Black',10)).place(relx=0.1, rely=0.6)
                  else:
                        result = "Time taken : "+str(wpm)+' Words Per Minute.'+'\nAccuracy is: '+str(acc)+'%'
                        intro = Label(game, text=result,bg="#23272A",fg='green',font=('Arial Black',10)).place(relx=0.1, rely=0.6)

                        r = csv.reader(open('Regfile.csv')) 
                        data = list(r)
                        highscore = data[unique_code][2]
                        if int(highscore) <= wpm:
                              data[unique_code][2] = wpm
                              data[unique_code][3] = acc
                              writer = csv.writer(open('Regfile.csv', 'w',newline=''))
                              writer.writerows(data)
                  hide(submitb)
                  
            def Try():
                  game.destroy()
                  Test()
            def stop():
                  game.destroy()
                  
            submitb=Button(game,text="SUBMIT",width=10,height=2,bg='orange',fg='white',command=check_result,font=("Arial Black",10))
            submitb.place(relx=0.4,rely=0.7)
            backb=Button(game,text="QUIT",width=10,height=2,bg='teal',fg='white',command=stop,font=("Arial Black",10))
            backb.place(relx=0.6,rely=0.7)
            tryb = Button(game,text="TRY AGAIN",width=10,height=2,bg='cyan',fg='white',command=Try,font=("Arial Black",10))
            tryb.place(relx=0.8,rely=0.7)
      def logout():
            Login()
            start.destroy()
      intro = Label(start, text="TEST YOUR TYPING SPEED!",bg="#23272A",fg='white',font=('ariel',20,'bold')).place(relx=0.15, rely=0.2)
      readyb=Button(start,text="READY!",width=10,height=2,bg='orange',fg='white',
            font=("Arial Black",10),command=Test)
      readyb.place(relx=0.4,rely=0.3)
      outb=Button(start,text="LOGOUT",width=10,height=2,bg='teal',fg='white',
            font=("Arial Black",10),command=logout)
      outb.place(relx=0.4,rely=0.45)
      profb=Button(start,text="PROFILE",width=10,height=2,bg='orange',fg='white',
            font=("Arial Black",10),command=Profile)
      profb.place(relx=0.4,rely=0.6)

      start.mainloop()
        


def ExitGame():
      canvas.destroy()
def leaderboard():
      lead=Tk()
      lead.title('Leaderboard')
      lead.geometry('810x500')
      lead.config(background='#23272A')
      def back():
            lead.destroy()
      #bubble sort used here
      with open('Regfile.csv', 'r') as fs:
            data,need = [],[]
            read = csv.reader(fs)      
            for row in read:
                  if row[2] != '0':
                        need = [row[0],row[2],row[3]]
                        data.append(need)
                        n = len(data)
                        for i in range(n):
                              for j in range(0,n-i-1):
                                    
                                    if data[j][1] < data[j+1][1]:
                                          data[j],data[j+1] = data[j+1],data[j]
                                    if data[j][1] == data[j+1][1] and data[j][2] > data[j+1][2]:
                                          data[j],data[j+1] = data[j+1],data[j]
            
            text1 = '1st\t'+ data[0][0] + '\t\t' + data[0][1] + '\t\t' + data[0][2]+"%"+ '\t'
            text2 = '2nd\t'+ data[1][0] + '\t\t' + data[1][1] + '\t\t' + data[1][2]+"%"+ '\t'
            text3 = '3rd\t'+ data[2][0] + '\t\t' + data[2][1] + '\t\t' + data[2][2]+"%"+ '\t'
            text4 = '4th\t'+ data[3][0] + '\t\t' + data[3][1] + '\t\t' + data[3][2]+"%"+ '\t'
            text5 = '5th\t'+ data[4][0] + '\t\t' + data[4][1] + '\t\t' + data[4][2]+"%"+ '\t'

            label = Label(lead,text = 'LEADERBOARD',bg="#23272A",fg='#FFFFFF')
            label.configure(font=("ariel", 50, "bold"))
            label.place(relx=0.2,rely=0.05)
            label = Label(lead,text = 'RANK\tUSERNAME\tWPM\tACCURACY',bg="#23272A",fg='#5865F2')
            label.configure(font=("ariel", 20, "bold"))
            label.place(relx=0.07,rely=0.3)
            label = Label(lead,text = text1+'\n'+text2+'\n'+text3+'\n'+text4+'\n'+text5 ,bg="#23272A",fg='#FFFFFF')
            label.configure(font=("ariel", 20, "bold"))
            label.place(relx=0.07,rely=0.4)
            B3=Button(lead,text="BACK",width=18,height=2,bg='#5865F2',fg='white',command=back)
            B3.place(relx=0.4,rely=0.8)
            
            


label = Label(canvas,text = 'T Y P I N G\nS P E E D\n',bg="#23272A",fg='#FFFFFF')
label.configure(font=("ariel", 50, "bold"))
label.place(relx=0.2,rely=0.1)


frame = LabelFrame(canvas, text="MAIN MENU",bg="#23272A",fg='#5865F2',borderwidth=8)
frame.place(relx=0.34,rely=0.45,width = 180,height=300)
frame.configure(font=("ariel", 20, "bold"))

B1=Button(canvas,text="PLAY",width=18,height=3,bg='#5865F2',fg='white',command=Login)
B1.place(relx=0.38,rely=0.55)

B2=Button(canvas,text="LEADERBOARD",width=18,height=3,bg='#5865F2',fg='white',command=leaderboard)
B2.place(relx=0.38,rely=0.67)

B3=Button(canvas,text="QUIT",width=18,height=3,bg='#5865F2',fg='white',command=ExitGame)
B3.place(relx=0.38,rely=0.8)

canvas.mainloop()

    
   
      

        


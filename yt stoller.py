from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from PIL import Image , ImageTk


def main():
    """
        create a main windows
        and display it on the screen
    """

    ws  =tk.Tk()
    ws.geometry("800x450+{}+{}".format(int(ws.winfo_screenwidth()/2 - 400), int(ws.winfo_screenheight()/2 - 225)))
    ws.title("Kaiwinta's YouTube Downloader")
    ws.resizable(False,False)
    ws.config(background='#FF9F1C')
    ws.bind('<Escape>', lambda e: ws.destroy())


    #Creation of the top frame with title and logo
    top = tk.Frame(ws , bg = '#FFBF69')
    top.place(rely = 0.05 , relx=0.05, relheight = 0.25 , relwidth= 0.9) 

    yt_Image = Image.open('youtube (1).png')
    yt_Image = ImageTk.PhotoImage(yt_Image)

    ws.iconbitmap(True,"ytico2.ico")
    frLogo =tk.Label(top, bg='#FFBF69',image=yt_Image)
    frLogo.place(rely = 0.2 , relx = 0.04 , relwidth=0.1 , relheight = 0.6)   

    frTitre =tk.Frame(top, bg='#FFBF69')
    frTitre.place(rely = 0.18 , relx = 0.17 , relwidth= 0.79 , relheight = 0.6)

    tittre = tk.Label(frTitre , text ='𝕐𝕠𝕦𝕋𝕦𝕓𝕖 𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕𝕖𝕣' ,font=('actual',45), bg ='#FFBF69') 
    tittre.pack(side='top')

    def download():
        """
            donwload is a function that donwload a yt video if the link exist
            if it doesn't exist then it show a message that depop 3 seconds later
        """

        labelerreur = tk.Label(bot ,bg ='gray' , text = "waiting")
        labelerreur.place(rely = 0.85 , relx=0.40 , relwidth=0.2 , relheight=0.1)
        bot.update()

        path = filedialog.askdirectory()
        print(path)
            
        
        #we ask the user to specificy the folder he want
        try :     
            if path :
                labelerreur.config(text="Downloading" , bg='green')
                bot.update()

                url = entreeUrl.get()
                # create YouTube object
                yt = YouTube(url)

                stream = yt.streams.get_highest_resolution()
                stream.download(output_path=path, filename=stream.default_filename)
                
        except:
            labelerreur.config(text="Link or path Error" , bg='red')
            bot.update()

        
       

        #2000 ms after we destroy it. No need to use time.sleep
        bot.after(2000, labelerreur.destroy)
        
    
    

    #Creation of the bottom frame with the entry and button
    bot = tk.Frame(ws , bg = '#FFBF69')
    bot.place(rely = 0.35 , relx=0.05, relheight = 0.6 , relwidth= 0.9)

    labelText = tk.Label(bot , anchor='center',justify='center',bg='#628B48',text=   "Whether you're looking to download a tutorial for offline viewing,"
                                                                                    +"\na music video for your personal collection,"
                                                                                    +"\n or just want to save a funny video for later."
                                                                                    +"\nJust copy and paste the YouTube video link,\nchoose your desired folder location, and hit download.",font=('actual',11))
    labelText.place(rely = 0.13 , relx = 0.1 , relheight = 0.4 , relwidth = 0.8)

    entreeUrl = tk.Entry(bot , bg='#628B48')
    entreeUrl.place(rely =  0.59, relx = 0.1 , relheight = 0.1 , relwidth = 0.8)

    btConfirm = tk.Button(bot , bg = '#628B48', activebackground='#6AB547', command = download,text='Download')
    btConfirm.place(rely = 0.73 , relx = 0.4 , relheight = 0.1 , relwidth =0.2 )
    
    #Execution of the windows
    ws.mainloop()

#Call the main function to start all
if __name__ == '__main__':
    main()
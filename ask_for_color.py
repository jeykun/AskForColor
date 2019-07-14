from tkinter import *    

class AskForColor:
    def __init__(self,default_color):
        self.__cor_default = default_color
        self.__cor = default_color
        self.__tk = Tk()
        self.__tk.title('Choose a color')
        self.__tk.resizable(False,False)
        
        self.__frame = Frame(self.__tk)
        self.__frame_botoes = Frame(self.__tk)
        self.__frame_labels = Frame(self.__tk)
        
        self.__frame.pack()
        self.__frame_labels.pack()
        self.__frame_botoes.pack()
        
        altura = 20
        comprimento = 320
        botoes_largura = 10
        

        self.__slider_r = Scale(self.__frame, from_=0, to=255, orient=HORIZONTAL,width=altura,length=comprimento,fg='#ff0000')
        self.__slider_g = Scale(self.__frame, from_=0, to=255, orient=HORIZONTAL,width=altura,length=comprimento,fg='#00ff00')
        self.__slider_b = Scale(self.__frame, from_=0, to=255, orient=HORIZONTAL,width=altura,length=comprimento,fg='#0000ff')        

        self.__slider_r['command'] = self.__setcor
        self.__slider_g['command'] = self.__setcor
        self.__slider_b['command'] = self.__setcor

        self.__slider_r.set(self.__hexstr2int(self.__cor_default[1:3]))
        self.__slider_g.set(self.__hexstr2int(self.__cor_default[3:5]))
        self.__slider_b.set(self.__hexstr2int(self.__cor_default[5:7]))
        
        self.__slider_r.pack()
        self.__slider_g.pack()
        self.__slider_b.pack()
        
        

        self.__label = Label(self.__frame_labels,text=f'{self.__cor_default[1:].upper()}: ')
        self.__label.grid(row=0,column=0)        
        
        self.__label_cor = Label(self.__frame_labels,text=' '*15)
        self.__label_cor['bg'] = self.__cor
        self.__label_cor.grid(row=0,column=1)
        
        
        self.__ok = Button(self.__frame_botoes,text='OK',width=botoes_largura)
        self.__ok['command'] = self.__retornook
        self.__ok.grid(row=0,column=0)
        
        
        self.__cancelar = Button(self.__frame_botoes,text='Cancel',width=botoes_largura)
        self.__cancelar['command'] = self.__retornocancel
        self.__cancelar.grid(row=0,column=1)
        

        
        self.__tk.protocol('WM_DELETE_WINDOW', self.__retornocancel)
        self.__tk.mainloop()
        
        

    def __setcor(self,valor):        
        __cor  = '#' + self.__int2hexstr(self.__slider_r.get())
        __cor += self.__int2hexstr(self.__slider_g.get())
        __cor += self.__int2hexstr(self.__slider_b.get())
        self.__label_cor['bg'] = __cor
        self.__label['text'] = __cor[1:].upper()+': '
        self.__cor = __cor

    def __retornook(self):
        self.__cor = self.__cor
        self.__tk.destroy()
        self.__tk.quit()
    
    def __retornocancel(self):
        self.__cor = self.__cor_default
        self.__tk.destroy()
        self.__tk.quit()

    def get(self):
        return self.__cor

    

    def __hexstr2int(self,string):
        string = string.lower()
        n = len(string)
        dictt = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
        valor = 0
        exponent = 0
        for i in range(n-1,-1,-1):
            valor += dictt[string[i]] * (16**exponent)
            exponent +=1
        return valor

    def __int2hexstr(self,intt):
        if len(hex(intt)[2:])==2:
            return hex(intt)[2:]
        else:
            return '0'+hex(intt)[2:]
        
    
        
        


#a = AskForColor('#123456')

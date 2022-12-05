from tkinter import *
from tkinter import ttk
from os import makedirs
from tkinter.font import Font

input_file_path = "input.txt"
output_path = "./output/"

sentences = []

with open(input_file_path) as file:
    sentences = [line.rstrip() for line in file]
    
makedirs(output_path, exist_ok=True)

num_of_sentences = len(sentences)
sentence = sentences[0]
current_row = 0



def approved():
    #write new line  into  outputfile
    global sentence
    with open(output_path+"empty_sentences.csv", 'a+') as f:
        f.write(sentence)
        print(f"writing sentence {sentence}")
        f.write("\n")
    show_next_sentence()

def disapproved():
    show_next_sentence()

def show_next_sentence():
    global sentence
    global sentence_label
    global current_row
    global row_label
    #read input file and set sentence
    current_row += 1
    sentence = sentences[current_row]
    sentence_label["text"]= sentence
    row_label["text"] = f"Satz {current_row} von {num_of_sentences}"
    if current_row%20 == 0:
        save()
    
def save():
    with open(input_file_path, 'w', encoding='utf-8') as fp: 
        for item in sentences[current_row:]: 
        # write each item on a new line 
            try: 
                fp.write(f"{item}\n")
            except:
                pass


root = Tk()
root.geometry("1000x400")
frm = ttk.Frame(root, padding=10)
l = ttk.Label(root, text="Der Satz gehört zu *keinem* der Nachhaltigkeitskriterien:")
l.pack()
l["font"] = Font(size=30)
ttk.Button(root, text="JA", command=approved).pack()
ttk.Button(root, text="NEIN", command=disapproved).pack()
ttk.Label(root, text="Die Kategorien sind: Mobilität, CO2-Entfernung, Energieeffizienz, Circular, \nErneuerbare, CO2-Einsparung, Prozessemissionen, Kompensation, Klimarisikpanalyse, Klimabilanz, Klimaresilienz, Lebensmittel, Transport").pack()
row_label=ttk.Label(root, text=f"Satz {current_row} von {num_of_sentences}")
# row_label.grid(column=0, row=3, sticky="news")
row_label.pack()
sentence_label = Message(root, text=sentence, font=('Arial', 25), width=750)
# sentence_label.grid(row=0, columnspan=2, sticky="news")
sentence_label.pack()
ttk.Button(root, text="save", command=save).pack()

root.mainloop()
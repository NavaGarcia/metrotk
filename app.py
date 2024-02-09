import tkinter as tk
import tkinter as tk
from tkinter import Label, ttk, Button
import PIL as pl
from PIL import Image, ImageTk
from collections import deque
from tkinter import messagebox
import heapq
from tkinter import *
from PIL import Image,ImageTk
class Graph:
    #Allows to change back from Letter to The station name for display
    def reverse_change(q,start_node):
        if start_node == "A":
            return "Ikebukuro"
        elif start_node == "B":
            return "Takadanobaba"
        elif start_node == "C":
            return "Shinjuku"
        elif start_node == "D":
            return "Harajuku"
        elif start_node == "E":
            return "Shibuya"
        elif start_node == "F":
            return "Ebisu"
        elif start_node == "G":
            return "Meguro"
        elif start_node == "H":
            return "Komagome"
        elif start_node == "I":
            return "Kitasenju"
        elif start_node == "J":
            return "Nishi-Nipori"
        elif start_node == "K":
            return "Asakusa"
        elif start_node == "L":
            return "Ueno"
        elif start_node == "M":
            return "Korakuen"
        elif start_node == "N":
            return "Iidabashi"
        elif start_node == "O":
            return "Shinjuku Sanchome"
        elif start_node == "P":
            return "Ichigaya"
        elif start_node == "Q":
            return "Kudanshita"
        elif start_node == "R":
            return "Akihabara"
        elif start_node == "S":
            return "Yotsuya"
        elif start_node == "T":
            return "Kanda"
        elif start_node == "U":
            return "Otemachi"
        elif start_node == "V":
            return "Nihonbashi"
        elif start_node == "W":
            return "Tokyo"
        elif start_node == "X":
            return "Nagatocho"
        elif start_node == "Y":
            return "Akasaka Mitsuke"
        elif start_node == "Z":
            return "Meijijingu mae"
        elif start_node == "a":
            return "Tameike-Sanno"
        elif start_node == "b":
            return "Kokkaigijidomae"
        elif start_node == "c":
            return "Kasumigaseki"
        elif start_node == "d":
            return "Yurakucho"
        elif start_node == "e":
            return "Ginza"
        elif start_node == "f":
            return "Tsukiji"
        elif start_node == "g":
            return "Shinbashi"
        elif start_node == "h":
            return "Roppongi"
        else:
            return start_node
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors
    #Runs the path obtained based on distance to obtain the total price of the ticket
    def calculate_total_cost(graph, path):
        cost = 0
        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]

            # Check if the nodes are connected in the graph
            if next_node in graph.graph[current_node]:
                cost += graph.graph[current_node][next_node]
            else:
                return None

        return cost
    #Check if the nodes selected are valid nodes
    def is_valid_node(self, node):
        return node in self.graph

#Calculates the heuristic values based on distance between stations    
def calculate_heuristic(station, goal, distances):
        return distances[station].get(goal, float('inf'))

#Algorithm fo search, using A*, saves the path for latter cost calculation
def a_star_search(metro_system, start, goal, distances):
    open_set = [(0, start)]#adds the station to the path 
    closed_set = set() # keeps track of the visited stations
    g_cost = {start: (0, None)} # cost to the Stations 
    while open_set:
        current_cost, current_station = heapq.heappop(open_set)
        costpath=''
        if current_station == goal: #returns the path if the current node visited is the same as the destination
            path = [current_station]
            while current_station in g_cost:
                current_station = g_cost[current_station][1] 
                path.insert(0, current_station)
            name=str(path)
            i=0
            path=[]
            for letter in name: #reconstruct the path as a series letters Ex: ADHCB
                i=i+1
                if letter.isalpha() and i>=6:
                    path.append(my_graph.reverse_change(letter))
                    costpath+=letter
            cost = g_cost[goal][0]
            return path, cost,costpath

        closed_set.add(current_station) #adds the station to the visited list

        for neighbor, cost in metro_system.graph[current_station].items():
            if neighbor in closed_set:
                continue

            tentative_g_cost = g_cost[current_station][0] + cost
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor][0]:
                g_cost[neighbor] = (tentative_g_cost, current_station)
                f_cost = tentative_g_cost + calculate_heuristic(neighbor, goal, distances)
                heapq.heappush(open_set, (f_cost, neighbor))

    return None, float('inf')

#Function to buy regular ticket   
def buy_ticket():
    def confirm_purchase():
        try:
            payment = float(entry.get())
            
            if payment < pago:
                messagebox.showwarning("Insufficient Funds", "Not enough money entered. Please enter the correct amount.")
            else:
                change = payment - pago
                label_result.config(text=f"Total cost: {pago}\nPayment: {payment}\nChange: {change}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.",parent=app)

    # Create the main window
    window = tk.Tk()
    window.title("Purchase Confirmation")

    # Disable window minimize button
    window.resizable(0, 0)
    window.attributes('-topmost', True)
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position to center the window
    x_position = (screen_width - window.winfo_reqwidth()) // 2
    y_position = (screen_height - window.winfo_reqheight())//6

    # Set the window size and position
    window.geometry(f"300x200+{x_position}+{y_position}")
    #Shows currency exvhange when called
    def help_clicked():
        messagebox.showinfo("Help", f"{pago}JPY to USD (United States Dollar):{pago/110:0.2f}USD\n JPY to EUR (Euro):{pago/130:0.2f} EUR \nJPY to GBP (British Pound):{pago/150:0.2f} GBP \nJPY to CNY (Chinese Yuan):{pago/16:0.2f} CNY\n JPY to AUD (Australian Dollar): {pago/80:0.2f} AUD\nJPY to MXN (Mexican Peso): {pago/8.7:0.2f} JPY.", parent=app)
    #Calculates total cost of the travel
    total_cost=my_graph.calculate_total_cost(costpath)
    if total_cost<=6:
        pago=180
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    if 6<total_cost<=11:
        pago=210
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    if 11<total_cost<=19:
        pago=260
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    if 19<total_cost<=27:
        pago=300
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    if 27<total_cost<40:
        pago=330
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    # Create and place components in the window
    button_help = tk.Button(window, text="?", command=help_clicked)
    entry = tk.Entry(window)
    button_confirm = tk.Button(window, text="Confirm purchase", command=confirm_purchase)
    label_result = tk.Label(window, text="")

    # Place components using grid with column weights
    label_title.grid(row=0, column=0, padx=5, pady=10, sticky=tk.E)
    button_help.grid(row=0, column=1, padx=5, pady=10, sticky=tk.W)
    entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
    button_confirm.grid(row=2, column=0, columnspan=2, pady=10)
    label_result.grid(row=3, column=0, columnspan=2, pady=10)

    # Adjust column weights for centering
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

#Function to buy replacement ticket   
def buy_replacement_ticket():
    def confirm_purchase():
        try:
            payment = float(entry.get())
            
            if payment < pago:
                messagebox.showwarning("Insufficient Funds", "Not enough money entered. Please enter the correct amount.")
            else:
                change = payment - pago
                label_result.config(text=f"Total cost: {pago}\nPayment: {payment}\nChange: {change}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.",parent=app)

    # Create the main window
    window = tk.Tk()
    window.title("Purchase Confirmation")

    # Disable window minimize button
    window.resizable(0, 0)
    window.attributes('-topmost', True)
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position to center the window
    x_position = (screen_width - window.winfo_reqwidth()) // 2
    y_position = (screen_height - window.winfo_reqheight())//6

    # Set the window size and position
    window.geometry(f"300x200+{x_position}+{y_position}")
    #Shows currency exvhange when called
    def help_clicked():
        messagebox.showinfo("Help", f"{pago}JPY to USD (United States Dollar):{pago/110:0.2f}USD\n JPY to EUR (Euro):{pago/130:0.2f} EUR \nJPY to GBP (British Pound):{pago/150:0.2f} GBP \nJPY to CNY (Chinese Yuan):{pago/16:0.2f} CNY\n JPY to AUD (Australian Dollar): {pago/80:0.2f} AUD\nJPY to MXN (Mexican Peso): {pago/8.7:0.2f} JPY.", parent=app)
    #Calculates total cost of the travel
    total_cost=my_graph.calculate_total_cost(costpath)
    # Create and place components in the window
    if total_cost<=6:
        pago=180
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    if 6<total_cost<=11:
        pago=210
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    if 11<total_cost<=19:
        pago=260
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    if 19<total_cost<=27:
        pago=300
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    if 27<total_cost<40:
        pago=330
        label_title = tk.Label(window, text="Total cost: "+str(pago)+" Yen",font=("arial",15))
    def help_clicked():
        messagebox.showinfo("Help", f"{pago}JPY to USD (United States Dollar):{pago/110:0.2f}USD\n JPY to EUR (Euro):{pago/130:0.2f} EUR \nJPY to GBP (British Pound):{pago/150:0.2f} GBP \nJPY to CNY (Chinese Yuan):{pago/16:0.2f} CNY\n JPY to AUD (Australian Dollar): {pago/80:0.2f} AUD\nJPY to MXN (Mexican Peso): {pago/8.7:0.2f} JPY.", parent=app)

    # Create and place components in the window
    button_help = tk.Button(window, text="?", command=help_clicked)
    entry = tk.Entry(window)
    button_confirm = tk.Button(window, text="Confirm purchase", command=confirm_purchase)
    label_result = tk.Label(window, text="")

    # Place components using grid with column weights
    label_title.grid(row=0, column=0, padx=5, pady=10, sticky=tk.E)
    button_help.grid(row=0, column=1, padx=5, pady=10, sticky=tk.W)
    entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
    button_confirm.grid(row=2, column=0, columnspan=2, pady=10)
    label_result.grid(row=3, column=0, columnspan=2, pady=10)

    # Adjust column weights for centering
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
#creates the graphs with names, distances values and time values
def graphs():
    my_graph2.add_edge('Ikebukuro', {'Takadanobaba': 1, 'Komagome': 2, 'Iidabashi':3, 'Korakuen':3})
    my_graph2.add_edge('Takadanobaba', {'Ikebukuro': 1, 'Shinjuku': 1, 'Iidabashi': 3})
    my_graph2.add_edge('Shinjuku', {'Takadanobaba': 2, 'Harajuku': 2, 'Shinjuku Sanchome': 2})
    my_graph2.add_edge('Harajuku', {'Shinjuku': 5, 'Shibuya': 1, 'Meijijingu mae':1})
    my_graph2.add_edge('Shibuya', {'Harajuku': 3, 'Ebisu': 1,'Akasaka Mitsuke':1})
    my_graph2.add_edge('Ebisu', {'Shibuya': 2,'Meguro':1,'Roppongi':1})
    my_graph2.add_edge('Meguro', {'Ebisu': 1,'Kokkaigijidomae':2})
    my_graph2.add_edge('Komagome', {'Ikebukuro': 1, 'Nishi-Nipori': 1, 'Korakuen': 2})
    my_graph2.add_edge('Kitasenju', {'Nishi-Nipori': 1,'Ueno':1})
    my_graph2.add_edge('Nishi-Nipori', {'Kitasenju': 1, 'Ueno': 1, 'Otemachi': 3})
    my_graph2.add_edge('Asakusa', {'Ueno': 1})
    my_graph2.add_edge('Ueno', {'Kitasenju': 1, 'Nishi-Nipori': 1, 'Asakusa': 3,'Akihabara':1})
    my_graph2.add_edge('Korakuen', {'Komagome': 1, 'Otemachi': 1, 'Iidabashi': 3})
    my_graph2.add_edge('Iidabashi', {'Takadanobaba': 5, 'Ichigaya': 1,'Kudanshita':2,'Korakuen':2})
    my_graph2.add_edge('Shinjuku Sanchome', {'Shinjuku': 3, 'Yotsuya': 1,'Meijijingu mae':2})
    my_graph2.add_edge('Ichigaya', {'Iidabashi': 2,'Yotsuya':2,'Akasaka Mitsuke':1})
    my_graph2.add_edge('Kudanshita', {'Iidabashi': 1, 'Otemachi': 1,'Nagatocho':1})
    my_graph2.add_edge('Akihabara', {'Ueno': 1, 'Kanda': 1, 'Iidabashi': 2})
    my_graph2.add_edge('Yotsuya', {'Ichigaya': 1,'Shinjuku Sanchome':1,'Nagatocho':1})
    my_graph2.add_edge('Kanda', {'Tokyo': 5, 'Akihabara': 1,'Nihonbashi':2,'Iidabashi':2})
    my_graph2.add_edge('Otemachi', {'Kudanshita': 5, 'Nishi-Nipori': 1,'Korakuen':2,'Nihonbashi':2})
    my_graph2.add_edge('Nihonbashi', {'Kanda': 1, 'Ginza': 1, 'Otemachi': 2})
    my_graph2.add_edge('Tokyo', {'Otemachi': 5, 'Nagatocho': 1,'Akasaka Mitsuke':2,'Shibuya':2})
    my_graph2.add_edge('Nagatocho', {'Kudanshita': 5, 'Ichigaya': 1,'Yotsuya':2,'Akasaka Mitsuke':2, 'Kokkaigijidomae': 1,'Tameike-Sanno':2})
    my_graph2.add_edge('Akasaka Mitsuke', {'Nagatocho': 5, 'Kudanshita': 1,'Ichigaya':2,'Yotsuya':2, 'Kokkaigijidomae': 1,'Tameike-Sanno':2})
    my_graph2.add_edge('Meijijingu mae', {'Harajuku': 1, 'Shibuya': 1, 'Shinjuku Sanchome': 3})
    my_graph2.add_edge('Tameike-Sanno', {'Kokkaigijidomae': 2, 'Nagatocho': 2,'Akasaka Mitsuke':2,'Kasumigaseki':2,'Meguro':2})
    my_graph2.add_edge('Kokkaigijidomae', {'Tameike-Sanno': 5, 'Nagatocho': 1,'Akasaka Mitsuke':2,'Kasumigaseki':2})
    my_graph2.add_edge('Kasumigaseki', {'Kokkaigijidomae': 3, 'Tameike-Sanno': 1, 'Ginza': 1,'Roppongi':1})
    my_graph2.add_edge('Yurakucho', {'Tokyo': 2,'Nagatocho': 5,'Shinbashi': 5})
    my_graph2.add_edge('Ginza', {'Tsukiji': 1,'Tokyo': 2,'Nihonbashi':2,'Kasumigaseki':2,'Shinbashi': 5})
    my_graph2.add_edge('Tsukiji', {'Ginza': 1, 'Akihabara': 1})
    my_graph2.add_edge('Shinbashi', {'Yurakucho': 1,'Kokkaigijidomae': 3, 'Tameike-Sanno': 1,'Ginza': 1})
    my_graph2.add_edge('Roppongi', {'Ebisu': 2,'Kasumigaseki':2})
    # Add edges to the graph with distance values
    my_graph.add_edge('A', distances['A'])
    my_graph.add_edge('B', distances['B'])
    my_graph.add_edge('C', distances['C'])
    my_graph.add_edge('D', distances['D'])
    my_graph.add_edge('E', distances['E'])
    my_graph.add_edge('F', distances['F'])
    my_graph.add_edge('G', distances['G'])
    my_graph.add_edge('H', distances['H'])
    my_graph.add_edge('I', distances['I'])
    my_graph.add_edge('J', distances['J'])
    my_graph.add_edge('K', distances['K'])
    my_graph.add_edge('L', distances['L'])
    my_graph.add_edge('M', distances['M'])
    my_graph.add_edge('N', distances['N'])
    my_graph.add_edge('O', distances['O'])
    my_graph.add_edge('P', distances['P'])
    my_graph.add_edge('Q', distances['Q'])
    my_graph.add_edge('R', distances['R'])
    my_graph.add_edge('S', distances['S'])
    my_graph.add_edge('T', distances['T'])
    my_graph.add_edge('U', distances['U'])
    my_graph.add_edge('V', distances['V'])
    my_graph.add_edge('W', distances['W'])
    my_graph.add_edge('X', distances['X'])
    my_graph.add_edge('Y', distances['Y'])
    my_graph.add_edge('Z', distances['Z'])
    my_graph.add_edge('a', distances['a'])
    my_graph.add_edge('b', distances['b'])
    my_graph.add_edge('c', distances['c'])
    my_graph.add_edge('d', distances['d'])
    my_graph.add_edge('e', distances['e'])
    my_graph.add_edge('f', distances['f'])
    my_graph.add_edge('g', distances['g'])
    my_graph.add_edge('h', distances['h'])
    #Time Graphs
    my_graph3.add_edge('A', time['A'])
    my_graph3.add_edge('B', time['B'])
    my_graph3.add_edge('C', time['C'])
    my_graph3.add_edge('D', time['D'])
    my_graph3.add_edge('E', time['E'])
    my_graph3.add_edge('F', time['F'])
    my_graph3.add_edge('G', time['G'])
    my_graph3.add_edge('H', time['H'])
    my_graph3.add_edge('I', time['I'])
    my_graph3.add_edge('J', time['J'])
    my_graph3.add_edge('K', time['K'])
    my_graph3.add_edge('L', time['L'])
    my_graph3.add_edge('M', time['M'])
    my_graph3.add_edge('N', time['N'])
    my_graph3.add_edge('O', time['O'])
    my_graph3.add_edge('P', time['P'])
    my_graph3.add_edge('Q', time['Q'])
    my_graph3.add_edge('R', time['R'])
    my_graph3.add_edge('S', time['S'])
    my_graph3.add_edge('T', time['T'])
    my_graph3.add_edge('U', time['U'])
    my_graph3.add_edge('V', time['V'])
    my_graph3.add_edge('W', time['W'])
    my_graph3.add_edge('X', time['X'])
    my_graph3.add_edge('Y', time['Y'])
    my_graph3.add_edge('Z', time['Z'])
    my_graph3.add_edge('a', time['a'])
    my_graph3.add_edge('b', time['b'])
    my_graph3.add_edge('c', time['c'])
    my_graph3.add_edge('d', time['d'])
    my_graph3.add_edge('e', time['e'])
    my_graph3.add_edge('f', time['f'])
    my_graph3.add_edge('g', time['g'])
    my_graph3.add_edge('h', time['h'])
#Changes the selected station
def change(start_node):
    if start_node == "Ikebukuro":
        start_node = "A"
    if start_node == "Takadanobaba":
        start_node = "B"
    if start_node == "Shinjuku":
        start_node = "C"
    if start_node == "Harajuku":
        start_node = "D"
    if start_node == "Shibuya":
        start_node = "E"
    if start_node == "Ebisu":
        start_node = "F"
    if start_node == "Meguro":
        start_node = "G"
    if start_node == "Komagome":
        start_node = "H"
    if start_node == "Kitasenju":
        start_node = "I"
    if start_node == "Nishi-Nipori":
        start_node = "J"
    if start_node == "Asakusa":
        start_node = "K"
    if start_node == "Ueno":
        start_node = "L"
    if start_node == "Korakuen":
        start_node = "M"
    if start_node == "Iidabashi":
        start_node = "N"
    if start_node == "Shinjuku Sanchome":
        start_node = "O"
    if start_node == "Ichigaya":
        start_node = "P"
    if start_node == "Kudanshita":
        start_node = "Q"
    if start_node == "Akihabara":
        start_node = "R"
    if start_node == "Yotsuya":
        start_node = "S"
    if start_node == "Kanda":
        start_node = "T"
    if start_node == "Otemachi":
        start_node = "U"
    if start_node == "Nihonbashi":
        start_node = "V"
    if start_node == "Tokyo":
        start_node = "W"
    if start_node == "Nagatocho":
        start_node = "X"
    if start_node == "Akasaka Mitsuke":
        start_node = "Y"
    if start_node == "Meijijingu mae":
        start_node = "Z"
    if start_node == "Tameike-Sanno":
        start_node = "a"
    if start_node == "Kokkaigijidomae":
        start_node = "b"
    if start_node == "Kasumigaseki":
        start_node = "c"
    if start_node == "Yurakucho":
        start_node = "d"
    if start_node == "Ginza":
        start_node = "e"
    if start_node == "Tsukiji":
        start_node = "f"
    if start_node == "Shinbashi":
        start_node = "g"
    if start_node == "Roppongi":
        start_node = "h"
    return start_node

total_cost=400
#Confirmation of travel
def confirm_traversal():
    global total_cost
    global costpath
    start_node = combo_start.get() # gets teh station from the combobox
    final_node = combo_final.get() # gets the final station from the combobox
    start_node = change(start_node) # change the the station name to a Letter to traverse the graph
    final_node = change(final_node) # change the the station name to a Letter to traverse the graph
    if not (my_graph.is_valid_node(start_node) and my_graph.is_valid_node(final_node)):
        label_res.config(text="Invalid node input.")
        return
    path, cost,costpath = a_star_search(my_graph,start_node, final_node, distances) #gets the optimal path as a list of stations
    total_cost=cost
    #Adds path to the table
    if path: #adds the stations and displays them in table
        i=0
        for x in path:
            i=i+1
            data.extend([(i,x)])
        for row in data:
            tree.insert("", "end", values=row)
    else:
        label_res.config(text="No path found.")
costpath=''
#confirms travel based on time
def confirm_traversal_time():
    global total_cost
    global costpath
    start_node = combo_start.get()
    final_node = combo_final.get()
    start_node = change(start_node)
    final_node = change(final_node)
    if not (my_graph3.is_valid_node(start_node) and my_graph3.is_valid_node(final_node)):
        label_res.config(text="Invalid node input.")
        return

    path,total_cost,costpath = a_star_search(my_graph3,start_node, final_node,time)
    label_res.config(text=f"Travel time: {total_cost} min.")
    #Adds path to the table
    if path:
        i=0
        for x in path:
            i=i+1
            data.extend([(i,x)])
        for row in data:
            tree.insert("", "end", values=row)
    else:
        label_res.config(text="No path found.")
#clears table when Regular travel is selected        
def clear_all():
    data.clear()
    for item in tree.get_children():
        tree.delete(item)
    table_frame.update
    confirm_traversal()
#clears table when travel optimized for time is selected
def clear_all_time():
    data.clear()
    for item in tree.get_children():
        tree.delete(item)
    table_frame.update
    confirm_traversal_time()
def help_clicked(event):
        messagebox.showinfo("Help", "1.- Select the station you are departing from\n2.-Select the station at your destination\n3.Press the search button corresponding to your preference, Distance or Time\n4.-Once your route is generated Buy your ticket or Replacement ticket in case you lost the original\n  4.1.-A replacement ticket allows you to get a refund in case the original ticket is found", parent=app)
#creation of window
app = tk.Tk()
app.title("Route Optimization")
background_image_path = "C:\metrotk\.venv\Image\Metro.png"  
background_image_path= Image.open(background_image_path)
resized_image = background_image_path.resize((1100, 100), Image.LANCZOS)
background_image = ImageTk.PhotoImage(resized_image)
background_image_path2 = "C:\metrotk\.venv\Image\draw.png"
background_image_path2= Image.open(background_image_path2)
resized_image2 = background_image_path2.resize((750, 100), Image.LANCZOS)
background_image2 = ImageTk.PhotoImage(resized_image2)


# Create a Canvas widget with the background image
canvas = tk.Canvas(app, width=resized_image2.width, height=resized_image2.height)

# Create a Canvas widget with the background image
canvas = tk.Canvas(app, width=resized_image.width, height=resized_image.height)
canvas.pack(side=tk.TOP)

# Draw the background image on the canvas
# Draw a round button on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
canvas.create_image(200, 0, anchor=tk.NW, image=background_image2)
button = canvas.create_oval(10, 10, 45, 45, fill="blue", outline="Black")
# Bind a function to the button click event
canvas.tag_bind(button, "<Button-1>", help_clicked)
button_text = canvas.create_text(30, 25, text="?", fill="black",font=("Impact",15,"bold"))
text2 = canvas.create_text(555, 50, text="Tokyo Metro System Route Optimizator", fill="gray",font=("Impact",30))
text = canvas.create_text(550, 50, text="Tokyo Metro System Route Optimizator", fill="black",font=("Impact",30))
canvas.place(x=1100, y=0, anchor="ne")
width=app.winfo_screenwidth()               
height= app.winfo_screenheight()
app.geometry("%dx%d" % (width,height))
app.state('zoomed')
# Create a graph
my_graph = Graph()
my_graph2=Graph()
my_graph3=Graph()
#distances between estations
distances = {
    'A': {'B': 2, 'H': 4, 'N': 5, 'M': 6},
    'B': {'A': 2, 'C': 3, 'N': 4},
    'C': {'B': 3, 'D': 2, 'O': 1},
    'D': {'C': 2, 'E': 1, 'Z': 1},
    'E': {'D': 1, 'F': 2, 'Y': 4},
    'F': {'E': 2, 'G': 2, 'h': 5},
    'G': {'F': 2, 'b': 7},
    'H': {'A': 7, 'J': 2, 'M': 4},
    'I': {'J': 5, 'L': 7},
    'J': {'I': 5, 'L': 2, 'U': 7},
    'K': {'L': 3},
    'L': {'I': 7, 'J': 2, 'K': 3, 'R': 2},
    'M': {'H': 4, 'U': 4, 'N': 1},
    'N': {'B': 5, 'P': 1, 'Q': 1, 'M': 1},
    'O': {'C': 1, 'S': 3, 'Z': 3},
    'P': {'N': 1, 'S': 1, 'X': 3},
    'Q': {'N': 1, 'U': 2, 'X': 3},
    'R': {'L': 2, 'T': 1, 'N': 3},
    'S': {'P': 1, 'O': 3, 'X': 1},
    'T': {'W': 1, 'R': 1, 'V': 1, 'N': 2},
    'U': {'Q': 2, 'J': 7, 'M': 2, 'V': 1,'W':1},
    'V': {'T': 1, 'e': 1, 'U': 1},
    'W': {'U': 1, 'X': 3, 'Y': 3, 'E': 6},
    'X': {'Q': 3, 'P': 2, 'S': 1, 'Y': 1, 'b': 2, 'a': 2},
    'Y': {'X': 1, 'Q': 3, 'P': 3, 'b': 3, 'a': 1},
    'Z': {'D': 1, 'E': 1, 'O': 3},
    'a': {'b': 1, 'X': 2, 'Y': 1, 'c': 2, 'G': 6},
    'b': {'a': 1, 'X': 2, 'Y': 2, 'c': 2},
    'c': {'b': 2, 'a': 2, 'e': 1, 'h': 2},
    'd': {'W': 1, 'X': 1, 'g': 1},
    'e': {'f': 1, 'W': 2, 'V': 1, 'c': 2, 'g': 1},
    'f': {'e': 1, 'R': 3},
    'g': {'d': 5, 'b': 4, 'a': 4, 'e': 3},
    'h': {'F': 5, 'c': 4}
}
#travel time between stations
time={
    'A': {'B': 4, 'H': 7, 'N': 15, 'M': 8},
    'B': {'A': 4, 'C': 5, 'N': 8},
    'C': {'B': 5, 'D': 4, 'O': 1},
    'D': {'C': 4, 'E': 3, 'Z': 4},
    'E': {'D': 3, 'F': 2, 'Y': 8},
    'F': {'E': 2, 'G': 3, 'h': 6},
    'G': {'F': 3, 'b': 6},
    'H': {'A': 12, 'J': 4, 'M': 7},
    'I': {'J': 6, 'L': 8},
    'J': {'I': 6, 'L': 3, 'U': 13},
    'K': {'L': 9},
    'L': {'I': 7, 'J': 3, 'K': 14, 'R': 4},
    'M': {'H': 7, 'U': 14, 'N': 8},
    'N': {'B': 8, 'P': 3, 'Q': 2, 'M': 8},
    'O': {'C': 1, 'S': 6, 'Z': 5},
    'P': {'N': 3, 'S': 1, 'X': 1},
    'Q': {'N': 1, 'U': 4, 'X': 4},
    'R': {'L': 5, 'T': 1, 'N': 4},
    'S': {'P': 1, 'O': 1, 'X': 9},
    'T': {'W': 3, 'R': 5, 'V': 7, 'N': 11},
    'U': {'Q': 4, 'J': 13, 'M': 14, 'V': 2,'W':8},
    'V': {'T': 7, 'e': 9, 'U': 2},
    'W': {'U': 8, 'X': 8, 'Y': 8, 'E': 21},
    'X': {'Q': 9, 'P': 9, 'S': 9, 'Y': 9, 'b': 4, 'a': 9},
    'Y': {'X': 9, 'Q': 9, 'P': 9, 'b': 9, 'a': 8},
    'Z': {'D': 1, 'E': 2, 'O': 4},
    'a': {'b': 8, 'X': 2, 'Y': 2, 'c': 8, 'G': 12},
    'b': {'a': 8, 'X': 8, 'Y': 9, 'c': 7},
    'c': {'b': 4, 'a': 8, 'e': 2, 'h': 4},
    'd': {'W': 2, 'X': 2, 'g': 2},
    'e': {'f': 2, 'W': 4, 'V': 9, 'c': 2, 'g': 6},
    'f': {'e': 1, 'R': 10},
    'g': {'d': 10, 'b': 9, 'a': 10, 'e': 7},
    'h': {'F': 12, 'c': 10}
}
#calls the graphs function
graphs()
#adds title to the window
label = tk.Label(app, text="Tokyo Metro System Route Optimizator",font=("impact",30))
#label.pack()
#Adds image to the window
image_path = r"C:\metrotk\.venv\Image\image.psd.png"
img = Image.open(image_path)

# Convert the PIL image to Tkinter PhotoImage and changes it size
resized_image= img.resize((1100,600), Image.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)
tk_img = ImageTk.PhotoImage(img)
image_label = tk.Label(app, image=new_image)
image_label.pack(side=tk.LEFT)
#adds table to the window
table_frame = tk.Frame(app)
table_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH)

table_label = tk.Label(table_frame, text="Routes", font=("Arial", 16, "bold"))
label_start = tk.Label(table_frame, text="Select Initial Station:")
table_label.pack()
label_start.pack()
#Adds Combobox to select the departure station
combo_start = ttk.Combobox(table_frame, values=list(my_graph2.graph.keys()))
combo_start.pack( side=tk.TOP, padx=5, pady=1)
combo_start.set('CHOOSE STATION')  # Set default value of station
label_final = tk.Label(table_frame, text="Select Final Station:")
label_final.pack(pady=10)
#Adds Combobox to select the destination station
combo_final = ttk.Combobox(table_frame, values=list(my_graph2.graph.keys()))
combo_final.pack( side=tk.TOP, padx=5, pady=1)
combo_final.set('CHOOSE STATION')  # Set default value of station
#Adds buttons to Select mode of Route calculation
ttk.Button(table_frame, text= "Route (Price)", command= clear_all, style="TButton").pack(side=tk.TOP, padx=5, pady=10)
ttk.Button(table_frame, text= "Route (Time)", command= clear_all_time, style="TButton").pack(side=tk.TOP, padx=5, pady=10)
style = ttk.Style()
style.configure("TButton", background="lightblue",
                foreground="black",
                font=("Arial", 12),
                padding=(10, 5),
                borderwidth=16,
                relief="raised",
                width=12,
                height=2,
                highlightcolor="yellow",
                cursor="hand2")
# Create Treeview for the table
columns = ("N.-","Prominent Stations")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

# Add column headings
for col in columns:
    tree.heading(col, text=col)

# Insert sample data (replace with your actual data)
data = [()]

for row in data:
    tree.insert("", "end", values=row)

# Pack the Treeview
tree.pack(fill=tk.BOTH, expand=True)
# Create and place components in the table frame
label_res = tk.Label(table_frame, text="")
label_res.pack(pady=10)
# Create Buy Ticket button
buy_ticket_button = Button(table_frame, text="Buy Ticket", command=buy_ticket)
buy_ticket_button.pack(side=tk.LEFT, padx=5, pady=10)

# Create Buy Replacement Ticket button
buy_replacement_ticket_button = Button(table_frame, text="Buy Replacement Ticket", command=buy_replacement_ticket)
buy_replacement_ticket_button.pack(side=tk.LEFT, padx=5, pady=10)

app.mainloop()

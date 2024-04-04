"""This file contains the code for creating Tkinter GUI elements, such as windows, forms, buttons, etc."""
import tkinter as tk
from tkinter import ttk, \
    messagebox  # ttk is the themed tk module for widgets that look like the OS, and messagebox is for displaying alerts
from tkinter import Tk
from PIL import ImageTk, Image  # Import the ImageTk and Image modules from the PIL package for working with images
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class LoginWindow:  # Class for the Log In Window to enter username and password to access the main GUI
    def __init__(self, master):
        self.master = master
        self.master.title("Log In to the Hotel Reservation Management System")
        self.master.configure(bg="white")  # Set the background color of the window to white

        # Calculate the coordinates for the top left corner of the window to center it
        window_width = 400
        window_height = 300
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)  # Calculate the top position
        position_right = int(screen_width / 2 - window_width / 2)  # Calculate the right position

        # Set the geometry of the window using the calculated coordinates at the center of the screen
        self.master.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Create the widgets for the Log In Window
        logo = Image.open("logo.png")  # Load the logo image
        logo = logo.resize((250, 150), Image.LANCZOS)  # Resize the logo image
        logo = ImageTk.PhotoImage(logo)  # Load the logo image
        logo_widget = ttk.Label(master, image=logo)  # Create a label widget to display the logo
        logo_widget.image = logo  # Keep a reference to the image to prevent garbage collection
        logo_widget.pack()

        self.label_username = ttk.Label(master, text="Username:", background="white")
        self.label_username.pack()

        self.entry_username = ttk.Entry(master)
        self.entry_username.pack()

        self.label_password = ttk.Label(master, text="Password:", background="white")
        self.label_password.pack()

        self.entry_password = ttk.Entry(master,
                                        show="*")  # Show * instead of the actual password to resemble a password field
        self.entry_password.pack()

        self.button = ttk.Button(master, text="Log In", command=self.login)
        self.button.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        print("Username: " + username)
        print("Password: " + password)

        # Check if username and password are alphanumeric
        if username.isalnum() and password.isalnum():
            messagebox.showinfo("Login Successful", "Welcome to the Hotel Reservation Management System!")
            print("Login successful")
            self.master.destroy()  # Close the Log In Window after successful login and open the main window
            root = Tk()
            my_gui = GUI(root)  # Open the main GUI  after successful login
            root.mainloop()  # Start the main GUI
        else:
            messagebox.showinfo("Login failed", "Invalid username or password. Please try again.")


class SearchPopup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Search Filters")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Arrival Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="w")
        self.arrival_date = ttk.Entry(self)
        self.arrival_date.grid(row=0, column=1, sticky="ew")

        ttk.Label(self, text="Length of Stay (days):").grid(row=1, column=0, sticky="w")
        self.length_of_stay = ttk.Entry(self)
        self.length_of_stay.grid(row=1, column=1, sticky="ew")

        ttk.Label(self, text="Number of Adults:").grid(row=2, column=0, sticky="w")
        self.no_of_adults = ttk.Entry(self)
        self.no_of_adults.grid(row=2, column=1, sticky="ew")

        ttk.Label(self, text="Number of Children:").grid(row=3, column=0, sticky="w")
        self.no_of_children = ttk.Entry(self)
        self.no_of_children.grid(row=3, column=1, sticky="ew")

        ttk.Label(self, text="Room Type:").grid(row=4, column=0, sticky="w")
        self.room_type = ttk.Combobox(self, values=["Single", "Double", "Suite"])
        self.room_type.grid(row=4, column=1, sticky="ew")

        ttk.Button(self, text="Search", command=self.search_rooms).grid(row=5, column=0, columnspan=2, pady=5)

    def search_rooms(self):
        # This method will be updated to perform the actual search
        print("Searching for rooms...")
        self.destroy()


class Dashboard:  # So far this class contains Amanda's code for the dashboard.py
    def __init__(self, master):
        self.master = master

        # Create widgets similar to dashboard amanda.py
        self.create_widgets()
        self.create_dashboard_placeholder()
        self.create_room_details_section()
        self.create_room_status_section()
        self.create_bookings_section()

    def create_widgets(self):
        search_btn = ttk.Button(self.master, text="Search Rooms", command=self.open_search_popup)
        search_btn.pack(pady=20)

    def open_search_popup(self):
        popup = SearchPopup(self.master)
        popup.grab_set()

    def create_dashboard_placeholder(self):
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.set_title('Visualization Placeholder')
        plot.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_room_details_section(self):
        room_details_frame = ttk.LabelFrame(self.master, text="Room Details")
        room_details_frame.pack(fill="x", padx=20, pady=10)
        ttk.Label(room_details_frame, text="Price:").grid(row=0, column=0)
        ttk.Entry(room_details_frame, state='readonly').grid(row=0, column=1)
        ttk.Label(room_details_frame, text="Capacity:").grid(row=1, column=0)
        ttk.Entry(room_details_frame, state='readonly').grid(row=1, column=1)

    def create_room_status_section(self):
        room_status_frame = ttk.LabelFrame(self.master, text="Room Status")
        room_status_frame.pack(fill="x", padx=20, pady=10)
        ttk.Label(room_status_frame, text="Occupied:").grid(row=0, column=0)
        ttk.Entry(room_status_frame, state='readonly').grid(row=0, column=1)
        ttk.Label(room_status_frame, text="Available:").grid(row=1, column=0)
        ttk.Entry(room_status_frame, state='readonly').grid(row=1, column=1)

    def create_bookings_section(self):
        bookings_frame = ttk.LabelFrame(self.master, text="Current Bookings")
        bookings_frame.pack(fill="both", expand=True, padx=20, pady=10)
        columns = ("booking_id", "room_type", "stay_length", "check_in", "check_out")
        self.bookings_table = ttk.Treeview(bookings_frame, columns=columns, show="headings")
        for col in columns:
            self.bookings_table.heading(col, text=col.replace("_", " ").title())
            self.bookings_table.column(col, anchor="center")
        self.bookings_table.pack(fill="both", expand=True)

        # Placeholder for sample booking data
        sample_data = [("B001", "Suite", "3", "2023-10-01", "2023-10-04"),
                       ("B002", "Double", "2", "2023-10-02", "2023-10-04")] * 5  # Multiplied to exceed 10 entries

        # Insert only the first 10 entries
        for booking in sample_data[:10]:
            self.bookings_table.insert("", "end", values=booking)


class Rooms:  # This class contains the code for the Rooms section of the GUI
    def __init__(self, master):
        self.master = master

    def create_rooms_display(self):
        """This method should contain the code to create and display the rooms section."""
        pass


class Bookings:  # This class contains the code for the Bookings section of the GUI to manage bookings
    def __init__(self, master):
        self.master = master
        self.bookings_frame = ttk.Frame(master)  # Create a frame to hold the bookings section
        self.bookings_frame.pack(fill='both', expand=True)  # Pack the frame to fill the window

    def create_bookings_display(self):
        ttk.Button(self.bookings_frame, text="Search Bookings", command=self.open_search_window).pack(pady=10)

        self.current_page = 0
        self.bookings = [("Booking ID", "Room Type", "Stay Length", "Check-in", "Check-out")] * 200

        self.bookings_display = ttk.Treeview(self.bookings_frame, columns=(1, 2, 3, 4, 5), show="headings")
        self.bookings_display.pack(fill='both', expand=True)
        for col in self.bookings_display['columns']:
            self.bookings_display.heading(col, text=col)

        pagination_frame = ttk.Frame(self.bookings_frame)
        pagination_frame.pack(fill='x', expand=False)
        ttk.Button(pagination_frame, text="<<", command=self.prev_page).pack(side='left')
        self.page_number_label = ttk.Label(pagination_frame, text=f"Page {self.current_page + 1}")
        self.page_number_label.pack(side='left', padx=10)
        ttk.Button(pagination_frame, text=">>", command=self.next_page).pack(side='left')

        # CRUD buttons frame
        crud_frame = ttk.Frame(self.bookings_frame)
        crud_frame.pack(fill='x', pady=5)

        # Create button
        top_frame = ttk.Frame(self.bookings_frame)
        top_frame.pack(fill='x', side='top')
        ttk.Button(top_frame, text="Create Booking", command=self.create_booking).pack(side='right', padx=5)

        # Update button
        action_frame = ttk.Frame(self.bookings_frame)
        action_frame.pack(fill='x', side='bottom', pady=5)
        self.update_btn = ttk.Button(action_frame, text="Update Booking", state='normal', command=self.update_booking)
        self.update_btn.pack(side='left', padx=5)
        self.delete_btn = ttk.Button(action_frame, text="Delete Booking", state='normal', command=self.delete_booking)
        self.delete_btn.pack(side='left', padx=5)
        self.bookings_display.bind('<<TreeviewSelect>>', self.on_item_selected)

        self.update_bookings_display()

    def on_item_selected(self, event):
        selected = self.bookings_display.selection()
        if selected:  # If an item is selected, enable the update and delete buttons
            self.update_btn['state'] = 'normal'
            self.delete_btn['state'] = 'normal'
        else:  # No selection disables the buttons
            self.update_btn['state'] = 'normal'
            self.delete_btn['state'] = 'normal'

    def delete_booking(self):
        selected_item = self.bookings_display.selection()
        self.bookings_display.delete(selected_item)
        # Add code here to delete the selected item from the database
        print("Booking deleted")

    def open_search_window(self):
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Search Bookings")
        self.search_window.geometry("300x200")  # Adjust size as needed

        # Example search filters: Booking ID and Room Type
        ttk.Label(self.search_window, text="Booking ID:").pack(pady=5)
        self.search_booking_id = ttk.Entry(self.search_window)
        self.search_booking_id.pack(pady=5)

        ttk.Label(self.search_window, text="Room Type:").pack(pady=5)
        self.search_room_type = ttk.Combobox(self.search_window, values=["Single", "Double", "Suite"])
        self.search_room_type.pack(pady=5)

        ttk.Button(self.search_window, text="Search", command=self.execute_search).pack(pady=10)

    def execute_search(self):
        booking_id = self.search_booking_id.get()
        room_type = self.search_room_type.get()
        print(f"Searching for Booking ID: {booking_id}, Room Type: {room_type}")
        self.search_window.destroy()

    def update_bookings_display(self):
        for item in self.bookings_display.get_children():
            self.bookings_display.delete(item)
        start = self.current_page * 50
        end = start + 50
        for booking in self.bookings[start:end]:
            self.bookings_display.insert('', 'end', values=booking)
        self.page_number_label.config(text=f"Page {self.current_page + 1}")

    def next_page(self):
        max_page = len(self.bookings) // 50
        if self.current_page < max_page:
            self.current_page += 1
            self.update_bookings_display()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_bookings_display()

    def create_booking(self):
        print("Create booking button clicked")

    def update_booking(self):
        print("Update booking button clicked")
        selected_item = self.bookings_display.selection()[0]  # Get selected item
        booking_data = self.bookings_display.item(selected_item, 'values')  # Fetch item data
        update_popup = UpdateBookingPopup(self.master, booking_data)
        update_popup.grab_set()  # Modal window

    def delete_booking(self):
        print("Delete booking button clicked")


class Charts:  # This class contains the code for the Charts section of the GUI to display data visualizations
    def __init__(self, master):
        self.master = master
        self.charts_frame = ttk.Frame(master)  # Create a frame to hold the charts section
        self.charts_frame.pack(fill='both', expand=True)  # Pack the frame to fill the window

    def create_charts_section(self):
        # Visualization type selection
        ttk.Label(self.charts_frame, text="Select Visualization:").pack(side='top', pady=5)
        self.vis_type = ttk.Combobox(self.charts_frame, values=["Room Occupancy Rate Over Time",
                                                                "Number of Bookings by Room Type",
                                                                "Current Occupancy",
                                                                "Average Stay Duration"])
        self.vis_type.pack(side='top', pady=5)
        self.vis_type.bind('<<ComboboxSelected>>', self.update_filters)

        self.filters_frame = ttk.Frame(self.charts_frame)
        self.filters_frame.pack(fill='x', padx=10, pady=5)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.plot = self.fig.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.charts_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_filters(self, event):
        for widget in self.filters_frame.winfo_children():
            widget.destroy()

        selected_vis = self.vis_type.get()
        if selected_vis == "Room Occupancy Rate Over Time":
            # Example: Filter by date range
            ttk.Label(self.filters_frame, text="Start Date:").pack(side='left', padx=(0, 10))
            start_date_entry = ttk.Entry(self.filters_frame)
            start_date_entry.pack(side='left', padx=(0, 10))

            ttk.Label(self.filters_frame, text="End Date:").pack(side='left', padx=(0, 10))
            end_date_entry = ttk.Entry(self.filters_frame)
            end_date_entry.pack(side='left', padx=(0, 10))

            ttk.Button(self.filters_frame, text="Update Chart", command=lambda: self.update_chart("occupancy")).pack(
                side='left', padx=(10, 0))

        elif selected_vis == "Number of Bookings by Room Type":
            ttk.Label(self.filters_frame, text="Start Date:").pack(side='left', padx=(0, 10))
            start_date_entry = ttk.Entry(self.filters_frame)
            start_date_entry.pack(side='left', padx=(0, 10))

            ttk.Label(self.filters_frame, text="End Date:").pack(side='left', padx=(0, 10))
            end_date_entry = ttk.Entry(self.filters_frame)
            end_date_entry.pack(side='left', padx=(0, 10))
            ttk.Button(self.filters_frame, text="Update Chart", command=lambda: self.update_chart("bookings")).pack(
                side='left', padx=(10, 0))

        elif selected_vis == "Current Occupancy":
            ttk.Label(self.filters_frame, text="Start Date:").pack(side='left', padx=(0, 10))
            start_date_entry = ttk.Entry(self.filters_frame)
            start_date_entry.pack(side='left', padx=(0, 10))

            ttk.Label(self.filters_frame, text="End Date:").pack(side='left', padx=(0, 10))
            end_date_entry = ttk.Entry(self.filters_frame)
            end_date_entry.pack(side='left', padx=(0, 10))
            ttk.Button(self.filters_frame, text="Update Chart", command=lambda: self.update_chart("bookings")).pack(
                side='left', padx=(10, 0))

        elif selected_vis == "Average Stay Duration":
            ttk.Label(self.filters_frame, text="Start Date:").pack(side='left', padx=(0, 10))
            start_date_entry = ttk.Entry(self.filters_frame)
            start_date_entry.pack(side='left', padx=(0, 10))

            ttk.Label(self.filters_frame, text="End Date:").pack(side='left', padx=(0, 10))
            end_date_entry = ttk.Entry(self.filters_frame)
            end_date_entry.pack(side='left', padx=(0, 10))
            ttk.Button(self.filters_frame, text="Update Chart", command=lambda: self.update_chart("bookings")).pack(
                side='left', padx=(10, 0))

    def update_chart(self, chart_type):
        # Placeholder function for updating the chart
        print(f"Updating chart: {chart_type}")
        self.plot.clear()
        if chart_type == "occupancy":
            # Generate occupancy rate over time plot
            pass  # Replace with actual plotting code
        elif chart_type == "bookings":
            # Generate number of bookings by room type plot
            pass  # Replace with actual plotting code
        self.canvas.draw()


class GUI:
    """ Responsible for the general GUI set up and layout, and instantiating the abovementioned classes to ensure the principle of Single-Responsibility that ensures efficient organization of the code """

    def __init__(self, master):
        self.master = master
        master.title("CCT211: Project 2: Hotel Reservation Management System")

        # Set the window to fullscreen
        self.fullscreen = False
        self.toggle_fullscreen()  # Call the function to toggle fullscreen

        # Bind Escape key to toggle fullscreen mode
        self.master.bind("<Escape>", self.toggle_fullscreen)

        # Create the main menu (tabs) for the GUI using ttk.Notebook which will hold the tabs
        self.notebook = ttk.Notebook(master)

        # Frames for each tab
        self.dashboard_frame = ttk.Frame(self.notebook)
        self.room_frame = ttk.Frame(self.notebook)
        self.bookings_frame = ttk.Frame(self.notebook)
        self.charts_frame = ttk.Frame(self.notebook)

        # Add the tabs to the notebook
        self.notebook.add(self.dashboard_frame, text="Dashboard")  # Add the dashboard tab
        self.notebook.add(self.room_frame, text="Rooms")  # Add the rooms tab
        self.notebook.add(self.bookings_frame, text="Bookings")  # Add the bookings tab
        self.notebook.add(self.charts_frame, text="Charts")  # Add the charts tab

        # Pack the notebook
        self.notebook.pack(expand=True, fill='both')

        # Initialize the sections for each tab using the respective classes
        self.dashboard = Dashboard(self.dashboard_frame)
        self.rooms = Rooms(self.room_frame)
        self.bookings = Bookings(self.bookings_frame)
        self.bookings.create_bookings_display()
        self.charts = Charts(self.charts_frame)
        self.charts.create_charts_section()

    # Function to toggle fullscreen
    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.master.attributes("-fullscreen", self.fullscreen)

        if not self.fullscreen:  # If exiting fullscreen mode set the window size to 1000x750
            # Calculate the coordinates for the top left corner of the window to center it
            window_width = 1000
            window_height = 750
            screen_width = self.master.winfo_screenwidth()  # Get the screen width
            screen_height = self.master.winfo_screenheight()  # Get the screen height
            position_top = int(screen_height / 2 - window_height / 2)
            position_right = int(screen_width / 2 - window_width / 2)

            # Set the geometry of the window using the calculated coordinates
            self.master.geometry(
                f"{window_width}x{window_height}+{position_right}+{position_top}")  # Set the window size and position to center it

    def on_tab_change(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text == "Bookings" and not self.bookings_initialized:
            self.create_bookings_display()
            self.bookings_initialized = True
        elif tab_text == "Charts" and not self.charts_initialized:
            self.create_charts_section()
            self.charts_initialized = True  # Ensure charts section is initialized once


class UpdateBookingPopup(tk.Toplevel):
    def __init__(self, parent, booking_data):
        super().__init__(parent)
        self.title("Update Booking")
        self.geometry("300x200")
        self.booking_data = booking_data  # Expected to be a tuple or list of booking details
        self.create_widgets()

    def create_widgets(self):
        # Assuming booking_data is like: (id, room_type, stay_length, check_in, check_out)
        ttk.Label(self, text="Room Type:").grid(row=0, column=0)
        self.room_type = ttk.Entry(self)
        self.room_type.grid(row=0, column=1)
        self.room_type.insert(0, self.booking_data[1])  # Pre-populate

        # Repeat for other fields as needed...

        ttk.Button(self, text="Commit Changes", command=self.commit_changes).grid(row=6, column=0, columnspan=2)

    def commit_changes(self):
        # Logic to update the booking with the new details
        # For demo, just print the new room type
        print("Updated Room Type:", self.room_type.get())
        self.destroy()  # Close the popup


root = Tk()
login_window = LoginWindow(root)

root.mainloop()
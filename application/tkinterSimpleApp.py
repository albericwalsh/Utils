import tkinter as tk


class SimpleWindow:

    def __init__(self, master=None, title="Simple Window", resolution="400x400", background="white",
                 resizable=(False, False), icon=None):
        """
        Create a simple window with a title, resolution, background color, resizable and an icon.

        :param master: master window
        :type master: tkinter.Tk
        :param title: title of the window
        :type title: str
        :param resolution: resolution of the window
        :type resolution: str
        :param background: background color of the window
        :type background: str
        :param resizable: resizable of the window
        :type resizable: tuple
        :param icon: icon of the window
        :type icon: str
        """
        self.master = master
        self.title = title
        self.resolution = resolution
        self.background = background
        self.resizable = resizable
        self.icon = icon
        self.window = None
        self.create_window()

    def create_window(self):
        """
        Create the window.
        """
        self.window = tk.Tk() if self.master is None else tk.Toplevel(self.master)
        self.window.title(self.title)
        self.window.geometry(self.resolution)
        self.window.configure(background=self.background)
        self.window.resizable(self.resizable[0], self.resizable[1])
        if self.icon is not None:
            self.window.iconbitmap(self.icon)

    def destroy_window(self):
        """
        Destroy the window.
        """
        self.window.destroy()

    def run(self):
        """
        Run the window.
        """
        self.window.mainloop()
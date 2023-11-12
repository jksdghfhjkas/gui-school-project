import tkinter as tk
from tkinter import ttk
from widget_update import config_widget
from process import CpuBar

y = True
x = False
class AppLication(tk.Tk, config_widget):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('GUI')
        self.resizable(height=False, width=False)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.cpu = CpuBar()
        self.set_ui()
        self.make_bar_cpu()
        self.config_cpu_bar()

    def set_ui(self):
        self.bar = ttk.LabelFrame(self, text="Manual")
        self.bar.pack(fill=tk.X)
        ttk.Button(self.bar, text='Main', command=self.main).pack(side=tk.RIGHT)
        ttk.Button(self.bar, text='Min', command=self.min).pack(side=tk.RIGHT)
        ttk.Button(self.bar, text='Move', command=self.configure_win).pack(side=tk.RIGHT)

        self.bar2 = ttk.LabelFrame(self, text='Power')
        self.bar2.pack(fill=tk.BOTH)

        self.bind('<Enter>', self.Enter)
        self.bind('<Leave>', self.Leave)

    def make_bar_cpu(self):
        ttk.Label(self.bar2, text=f'cores: {self.cpu.cpu_count}, logical cores: {self.cpu.cpu_count_logical}',
                  anchor=tk.CENTER).pack(fill=tk.X)
        self.list_label = []
        self.list_pbar = []

        for i in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.bar2, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar2, length=100))

        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_bar = ttk.Label(self.bar2, anchor=tk.CENTER)
        self.ram_bar.pack(fill=tk.X)
        self.ram_baR = ttk.Progressbar(self.bar2, length=100)
        self.ram_baR.pack(fill=tk.X)

    def make_minimal_win(self):
        self.average_bar = ttk.Progressbar(self, length=100)
        self.average_bar.pack(side=tk.LEFT)

        self.ram_baR_two = ttk.Progressbar(self, length=100)
        self.ram_baR_two.pack(side=tk.LEFT)

        ttk.Button(self, text='Main', width=5, command=self.main).pack(side=tk.RIGHT)
        ttk.Button(self, text='Full', width=5, command=self.full).pack(side=tk.RIGHT)
        ttk.Button(self, text='Move', width=5, command=self.configure_win).pack(side=tk.RIGHT)

        self.update()

    def full(self):
        global y
        if y is False:
            self.unbind_class('Tk', '<Enter>')
            self.unbind_class('Tk', '<Leave>')
            self.after_cancel(self.wheel_two)
            self.clear_win()
            self.set_ui()
            self.make_bar_cpu()
            self.config_cpu_bar()
            y = True

    def min(self):
        global y
        if y is True:
            self.unbind_class('Tk', '<Enter>')
            self.unbind_class('Tk', '<Leave>')
            self.after_cancel(self.wheel)
            self.clear_win()
            self.make_minimal_win()
            self.average_min()
            y = False

    def configure_win(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()

    def main(self):
        global x
        if x is False: x = True
        elif x is True: x = False

    def Enter(self, event):
        if x is True:
            self.attributes('-alpha', 1)

    def Leave(self, event):
        if x is True:
            self.attributes('-alpha', 0.01)

if __name__ == '__main__':
    root = AppLication()
    root.mainloop()






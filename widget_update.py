class config_widget:
    def config_cpu_bar(self):
        r = self.cpu.cpu_percent_return()

        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core {i+1}, usege: {r[i]}%')
            self.list_pbar[i].configure(value=r[i])

        ram = self.cpu.ram_downloads_return()
        self.ram_bar.configure(text=f'RAM usege: {ram[2]}%, used: {round(ram[3]/1048576)}Mb, available: {round(ram[1]/1048576)}Mb')
        self.ram_baR.configure(value=ram[2])

        self.wheel = self.after(1000, self.config_cpu_bar)

    def clear_win(self):
        for i in self.winfo_children():
            i.destroy()

    def average_min(self):
        ram = self.cpu.ram_downloads_return()
        average_two = self.cpu.cpu_one_return()
        self.average_bar.configure(value=average_two)
        self.ram_baR_two.configure(value=ram[2])

        self.wheel_two = self.after(1000, self.average_min)



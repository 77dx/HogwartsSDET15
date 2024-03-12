"""
@ Title:
@ Author: Cathy
@ Time: 2023/12/20 17:47
"""
import tkinter as tk
from forex_python.converter import CurrencyRates


class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("汇率转换器")

        # 创建标签、输入框和按钮
        self.amount_label = tk.Label(master, text="输入金额:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.result_label = tk.Label(master, text="结果:")
        self.result_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, textvariable=self.result_var, state="readonly")
        self.result_entry.grid(row=1, column=1, padx=10, pady=10)

        self.convert_button = tk.Button(master, text="转换", command=self.convert_currency)
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            currency_rates = CurrencyRates()

            # 获取汇率，这里以RUB（俄罗斯卢布）兑换CNY（人民币）为例
            exchange_rate = currency_rates.get_rate('RUB', 'CNY')

            result = amount * exchange_rate
            self.result_var.set(f"{amount} RUB = {result:.2f} CNY")
        except ValueError:
            self.result_var.set("请输入有效的数字")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.title = "Рассчёты"


class MainApp(App):


    def update_label1(self):
        self.lbl.text = "Метаболический алкалоз"
    def update_label2(self):
        self.lbl.text = "Ошибка"
    def update_label3(self):
        self.lbl.text = "Дыхательный алкалоз"
    def update_label4(self):
        self.lbl.text = "Дыхательный ацидоз"
    def update_label5(self):
        self.lbl.text = "Смешанный ацидоз"
    def update_label6(self):
        self.lbl.text = "Метаболический ацидоз"
    def update_label7(self):
        self.lbl.text = "Ошибка"
    def update_label8(self):
        self.lbl.text = "Смешанный алкалоз"
    def update_label9(self):
        self.lbl.text = "Всё хорошо!"
    def update_label10(self):
        self.lbl.text = "Заполнены не все окна"
    def build(self):
        main_layout = BoxLayout(orientation="vertical")

        self.lbl = Label(text="Введите ваши данные", font_size=40)
        self.solution1 = TextInput(hint_text='Введите pH', multiline=False, readonly=False, input_filter="float")
        self.solution2 = TextInput(hint_text='Введите PCO2', multiline=False, readonly=False, input_filter="float")
        self.solution3 = TextInput(hint_text='Введите C(HCO3)', multiline=False, readonly=False, input_filter="float")
        main_layout.add_widget(self.lbl)
        main_layout.add_widget(self.solution1)
        main_layout.add_widget(self.solution2)
        main_layout.add_widget(self.solution3)
        main_layout.add_widget(Button(on_press=self.on_click, text="Рассчитать"))
        return main_layout

    def on_click(self, instance):
        data = self.solution1.text
        data1 = self.solution2.text
        data2 = self.solution3.text

        if float(data) > 7.45 and float(data1) > 40.0 and float(data2) > 24.0:
                self.update_label1()
        if float(data) > 7.45 and float(data1) > 40.0 and float(data2) < 24.0:
                self.update_label2()
        if float(data) > 7.45 and float(data1) < 40.0 and float(data2) < 24.0:
                self.update_label3()
        if float(data) > 7.45 and float(data1) < 40.0 and float(data2) < 24.0:
                self.update_label4()
        if float(data) < 7.35 and float(data1) > 40.0 and float(data2) > 24.0:
                self.update_label5()
        if float(data) < 7.35 and float(data1) > 40.0 and float(data2) < 24.0:
                self.update_label6()
        if float(data) < 7.35 and float(data1) < 40.0 and float(data2) > 24.0:
                self.update_label7()
        if float(data) < 7.35 and float(data1) < 40.0 and float(data2) < 24.0:
                self.update_label8()
        if float(data) > 7.35 and float(data) < 7.45:
                self.update_label9()





if __name__ == '__main__':
    MainApp().run()


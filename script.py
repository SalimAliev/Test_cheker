from tkinter import Tk, Button, Label, Toplevel, messagebox
from tkinter import filedialog


# Текст инструкции
instruction_text = """Ассаляму алейкум, эта программа для проверки результатов выполнения теста. Инструкция использования программы.
    #     1. Необходимо ввести в программу правильные ответы загрузив файл в формате
    #         1.d
    #         2.c
    #         и т. д
    #     2. Необходимо внести ответы тестируемого. Их можно ввести аналогично способу указанному в пункте 1
    #     3. После ввода правильных ответов и ответов тестируемого программа выдаст либо положительный ответ если все ответы правильные
    #     либо выдаст отрицательный и укажет какие ответы неправильные"""

# переменные в которых хранятся правильные ответы и ответы тестируемого
correct_data = {}
tested_data = {}


# Функция-обработчик события нажатия на кнопку
def load_file(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            data = file.read()
            data = [i.split('.') for i in data.split()]
            print(data)
            return {i[0]:i[1] for i in data}
    except:
        messagebox.showinfo("Уведомление", "Произошла ошибка при открытии или чтении файла")

# Функция правильных ответов в переменную
def correct_answer():
    file_path = filedialog.askopenfilename()
    global correct_data
    correct_data = load_file(file_path)

# Функция записи ответов тестируемого в переменную
def tested_answer():
    file_path = filedialog.askopenfilename()
    global tested_data
    tested_data = load_file(file_path)

# Функция сверки правильных ответов с ответами тестируемого
def check_test(correct_data, tested_data):

    if not correct_data == {} or tested_data == {}:
        if len(tested_data) > len(correct_data):
            messagebox.showinfo("Уведомление", "У тестируемого ответов больше чем тестовых заданий, откорректируйте данные")
        else:
            flag = True
            res = []
            for key, value in correct_data.items():
                test_value = tested_data.get(key, '')
                if test_value != value:
                    flag = False
                    if test_value == '':
                        res.append(f'Задание №{key}: нет ответа')
                    else:
                        res.append(f'Задание №{key}: ответ тестируемого {test_value}, правильный ответ {value}')


            if flag:
                messagebox.showinfo("Уведомление", "В тесте нет ошибок!")
            else:
                mistakes = '\n'.join(res)
                messagebox.showinfo(f"Уведомление", f"Тест имеет следующие ошибки\n{mistakes}")
    else:
        messagebox.showinfo("Уведомление", "Не загружены значения привильных ответов либо ответов тестируемого")



def open_instruction():
    global instruction_text
    # Создаем новое окно
    instruction_window = Toplevel()

    # Устанавливаем название нового окна
    instruction_window.title("Дополнительное окно")

    root.geometry("400x300")

    instruction_text = Label(instruction_window, text=instruction_text, justify="left")
    instruction_text.pack(anchor="w")


root = Tk()
root.geometry("400x300")
root.title("Check test answer")

button = Button(root, text="Инструкция", command=open_instruction)
button.pack()

button = Button(root, text="Загрузить файл с правильными ответами", command=correct_answer)
button.pack()

button = Button(root, text="Загрузить файл с ответами тестируемого", command=tested_answer)
button.pack()

button = Button(root, text="Проверка теста", command=lambda: check_test(correct_data, tested_data))
button.pack()


root.mainloop()



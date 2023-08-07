import mysql.connector
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.textfield import MDTextField


class TodoListApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_connection = None
        self.db_cursor = None

    def build(self):
        self.title = "Todo List App"
        self.todo_list = []

        layout = BoxLayout(orientation='vertical')

        self.text_input = MDTextField(
            hint_text="Tambahkan tugas baru",
            on_text_validate=self.add_task
        )

        layout.add_widget(self.text_input)

        return layout

    def connect_to_database(self):
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_todo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               list"
        )
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255))"
        )

    def close_database_connection(self):
        if self.db_cursor:
            self.db_cursor.close()
        if self.db_connection:
            self.db_connection.close()

    def add_task(self, text_input):
        task = text_input.text

        self.save_task_to_database(task)

        item_id = self.db_cursor.lastrowid
        task_item = {"id": item_id, "task": task, "widget": None}
        self.todo_list.append(task_item)

        item = OneLineIconListItem(text=task)
        delete_button = MDIconButton(icon="delete", on_release=lambda x, item_id=item_id: self.delete_task(item_id))
        edit_button = MDIconButton(icon="pencil", on_release=lambda x, item_id=item_id: self.edit_task(item_id))
        item.add_widget(delete_button)
        item.add_widget(edit_button)

        task_item["widget"] = item  # Mengupdate referensi widget dalam dictionary task_item

        self.root.add_widget(item)

        text_input.text = ""

    def delete_task(self, item_id):
        task_item = next((item for item in self.todo_list if item["id"] == item_id), None)
        if task_item:
            self.delete_task_from_database(item_id)
            self.todo_list.remove(task_item)
            self.root.remove_widget(task_item["widget"])

    def edit_task(self, item_id):
        task_item = next((item for item in self.todo_list if item["id"] == item_id), None)
        if task_item:
            self.text_input.text = task_item["task"]
            self.delete_task(item_id)

            self.text_input.on_text_validate = lambda text_input: self.update_task(text_input, item_id)

    def update_task(self, text_input, item_id):
        new_task = text_input.text

        task_item = next((item for item in self.todo_list if item["id"] == item_id), None)
        if task_item:
            task_item["task"] = new_task
            self.update_task_in_database(item_id, new_task)

            item = OneLineIconListItem(text=new_task)
            delete_button = MDIconButton(icon="delete", on_release=lambda x, item_id=item_id: self.delete_task(item_id))
            edit_button = MDIconButton(icon="pencil", on_release=lambda x, item_id=item_id: self.edit_task(item_id))
            item.add_widget(delete_button)
            item.add_widget(edit_button)

            task_item["widget"] = item  # Mengupdate referensi widget dalam dictionary task_item

            self.root.add_widget(item)

            text_input.text = ""
            self.text_input.on_text_validate = self.add_task

    def save_task_to_database(self, task):
        self.db_cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        self.db_connection.commit()

    def delete_task_from_database(self, item_id):
        self.db_cursor.execute("DELETE FROM tasks WHERE id = %s", (item_id,))
        self.db_connection.commit()

    def update_task_in_database(self, item_id, new_task):
        self.db_cursor.execute("UPDATE tasks SET task = %s WHERE id = %s", (new_task, item_id))
        self.db_connection.commit()

    def load_tasks_from_database(self):
        self.db_cursor.execute("SELECT id, task FROM tasks")
        self.todo_list = [{"id": task[0], "task": task[1], "widget": None} for task in self.db_cursor.fetchall()]

    def on_start(self):
        self.connect_to_database()
        self.load_tasks_from_database()

        for task in self.todo_list:
            item = OneLineIconListItem(text=task["task"])
            delete_button = MDIconButton(icon="delete", on_release=lambda x, item_id=task["id"]: self.delete_task(item_id))
            edit_button = MDIconButton(icon="pencil", on_release=lambda x, item_id=task["id"]: self.edit_task(item_id))
            item.add_widget(delete_button)
            item.add_widget(edit_button)

            task["widget"] = item  # Menyimpan referensi widget dalam dictionary task

            self.root.add_widget(item)

    def on_stop(self):
        self.close_database_connection()


if __name__ == "__main__":
    TodoListApp().run()


'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    # & page setup
    page.title = "Simple ToDo app"

    # | Data storing
    tasks: list[dict] = []

    # & task input
    task_input = ft.TextField(
        label="Your task",
        hint_text="What needs to be done?",
        width=300
    )

    # * function to toggle complete
    def toggle_complete(e, i):
        tasks[i]['completed'] = not tasks[i]['completed']
        update_ui()

    # * function to delete task
    def delete_task(e, i):
        tasks.pop(i)
        update_ui()

    # * function to update ui
    def update_ui():
        task_input.value = ""
        tasks_column.controls.clear()
        for i, task in enumerate(tasks):
            tasks_column.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(task['task']), 
                        ft.Checkbox(value=task['completed'], on_change=lambda e,i=i: toggle_complete(e, i)), 
                        ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e,i=i: delete_task(e, i))
                    ]
                )
            )
        page.update()

    # * function to handle add_task
    def add_task(e):
        tasks.append({
            "task": task_input.value,
            "completed": False
        })
        update_ui()

    # & add task
    add_btn = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task)

    # & tasks column
    tasks_column = ft.Column(
        controls=[],
        spacing=10
    )

    update_ui()

    # & adding elements to page
    page.add(
        ft.Row(
            controls=[task_input, add_btn],
            spacing=20
        ),
        tasks_column
    )

# ! Run the app
ft.app(main)
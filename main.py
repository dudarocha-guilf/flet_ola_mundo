import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text(value="Maria Eduarda"),

        ft.ElevatedButton("Clique aqui!")
    )
ft.run(main)
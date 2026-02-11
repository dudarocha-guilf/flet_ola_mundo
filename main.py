import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro App Flet"
    page.bgcolor = "#f07ae2"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="Maria Eduarda"),
        ft.ElevatedButton("Clique aqui!")
    )
ft.run(main)
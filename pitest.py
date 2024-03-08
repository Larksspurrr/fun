from mpmath import mp
import flet as ft

def main(page: ft.Page):
    page.title = "Pi test"
    page.window_maximized = True
    page.window_resizable = False

    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    app_title = ft.Text("Pi Test", color="white", size = 50, text_align=ft.TextAlign.CENTER)
    digits = ft.Text("3.", color="white", size=30, text_align=ft.TextAlign.CENTER)
    page.add(app_title)

    def digit_entered(e):
        digits.value += e.control.value
        e.control.value = ""
        if digits.value != str(mp.pi)[:len(digits.value)]:
            digits.value = digits.value[:-1]
            page.dialog = mistake_msg
            mistake_msg.open = True
        if len(digits.value) == int(decimal_places.value) + 2:
            textbox.disabled = True
        page.update()

    def submitted(e):
        page.dialog = decimal_places_msg
        decimal_places_msg.open = True
        decimal_places.disabled = True
        textbox.disabled = False
        mp.dps = int(e.control.value) + 2
        page.update()

    def delete_digit(e):
        if digits.value != "3.":
            digits.value = digits.value[:-1]
        page.update()

    def reset(e):
        digits.value = "3."
        decimal_places.value = ""
        decimal_places.disabled = False
        textbox.disabled = True
        page.update()

    textbox = ft.TextField(label="Pi digits here", width=200, height=50, border_color="white", on_change=digit_entered, disabled=True)
    decimal_places = ft.TextField(label="To how many digits?", width=200, height=50, border_color="white", on_submit=submitted)
    del_digit = ft.TextButton(text="Delete last digit", style=ft.ButtonStyle(color=ft.colors.WHITE,
                                                                             shape=ft.RoundedRectangleBorder(radius=10)), width=200, on_click=delete_digit)
    reset = ft.TextButton(text="Restart", style=ft.ButtonStyle(color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)), width=200, on_click=reset)
    decimal_places_msg = ft.AlertDialog(title=ft.Text("Decimal places set", color="white", size=25, text_align=ft.TextAlign.CENTER))
    mistake_msg = ft.AlertDialog(title=ft.Text("Mistake!", color="white", size=25, text_align=ft.TextAlign.CENTER))

    page.add(
        ft.Column(
            [
                decimal_places,
                textbox,
                del_digit,
                reset,
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        digits
    )


if __name__ == "__main__":
    ft.app(target=main)
import flet as ft
from random import shuffle as randshuffle

def main(page: ft.Page):
    page.window_maximized = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text(value="Connections", color="white", size=50, text_align=ft.TextAlign.CENTER)
    words = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    sets={
        "set1": ["ARE", "QUEUE", "SEA", "WHY"], # LETTER HOMOPHONES
        "set2": ["FOOT", "LEAGUE", "MILE", "YARD"], # UNITS OF LENGTH
        "set3": ["BOOT", "LOAFER", "PUMP", "SNEAKERS"], # FOOTWEAR
        "set4": ["ESSENCE", "PEOPLE", "TIME", "US"] # MAGAZINES
    }

    text_words = [word for sublist in sets.values() for word in sublist]
    randshuffle(text_words)

    clicked = []
    done = []

    lives = 4
    outer_break = False

    def win():
        words.clean()
        i = 0
        for answer in clicked:
            done.append(answer)
            index = text_words.index(answer)
            word = text_words.pop(index)
            text_words.insert(i, word)
            i += 1
        
        for set_name, word_set in sets.items():
            if clicked[0] in word_set:
                del sets[set_name]
                break
        
        clicked.clear()
        grid_words()

        page.update()

    
    def loss():
        nonlocal lives
        print("You lost")
        lives -= 1

    def click(e):
        if e.control.style.bgcolor == ft.colors.PINK:
            clicked.remove(e.control.text)
            e.control.style.bgcolor = ft.colors.GREY_700
            page.update()
            return None
        if len(clicked) < 4:
            if e.control.style.bgcolor == ft.colors.GREY_700:
                clicked.append(e.control.text)
                e.control.style.bgcolor = ft.colors.PINK
        
        page.update()

    def submit_words(e):
        won = False
        last_key = list(sets.keys())[-1]
        for word_set in sets.values():
            if set(clicked) == set(word_set):
                won = True
                break
            elif word_set == sets[last_key] and set(clicked) == set(word_set):
                loss()
            else:
                continue
        if won: win()

    def grid_words():
        for word in text_words:
                if word in done:
                    Color = ft.colors.BLUE
                    status = True
                else:
                    Color = ft.colors.GREY_700
                    status = False
                words.controls.append(ft.TextButton(
                    text=word,
                    style=ft.ButtonStyle(
                        bgcolor=Color,
                        color="white",
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    disabled=status,
                    on_click=click
                    ))
    grid_words()

    submit = ft.TextButton(
        text="Submit",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.GREY_700,
            color="white"
        ),
        on_click=submit_words
    )

    page.add(
        ft.Column(
            [
                title,
                ft.Container(words, width=500),
                submit
            ], alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
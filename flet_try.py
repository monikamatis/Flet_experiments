import flet as ft
from flet import CrossAxisAlignment, RoundedRectangleBorder
from flet.border import BorderSide


def main(page: ft.Page):

    page.title = "Routes Example"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def store_url(_):
        return page.go('/store')

    def main_url(_):
        return page.go("/")

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=store_url),
                ],
            )
        )

        if page.route == "/store":

            page.views.append(
                ft.View(
                    "/store",
                    [
                        img,
                        images,
                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    img = ft.Image(
        src=f"/icons/icon-512.png",
        width=100,
        height=100,
        fit=ft.ImageFit.FILL,
    )
    images = ft.Row(expand=1, wrap=True, scroll="always")

    for i in range(0, 30):
        images.controls.append(
            ft.ElevatedButton(
                style=ft.ButtonStyle(

                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0, "": 0},
                ),
                content=ft.Image(
                    src=f"https://picsum.photos/400/?{i}",
                    # width=200,
                    # height=200,
                    fit=ft.ImageFit.FILL,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                ),
                on_click=main_url,
            )
        )

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)

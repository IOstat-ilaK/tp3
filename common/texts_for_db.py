from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Для дома','Для себя', 'Для друга']

description_for_info_pages = {
    "main": "Добро пожаловать!",
    "about": "Магазинчик всякого\nРежим работы - с начала времён.",
    "payment": as_marked_section(
        Bold("Варианты оплаты:"),
        "Картой в боте",
        "При получении",
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Курьер",
            "Самовывоз",
            marker="✅ ",
        ),
        as_marked_section(Bold("Нельзя:"), "Почта", "Голуби", marker="❌ "),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Категории:',
    'cart': 'В корзине ничего нет!'
}

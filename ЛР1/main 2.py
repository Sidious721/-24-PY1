# TODO Найдите количество книг, которое можно разместить на дискете
line_volume = 25 * 4
page_volume = line_volume * 50
book_volume = int(100 * page_volume)
HDD_volume = int(1024 * 1024 * 1.44)
book_quantity = HDD_volume//book_volume

print("Количество книг, помещающихся на дискету:", book_quantity)

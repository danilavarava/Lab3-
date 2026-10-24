from cart_service import CartModule


def run_tests():
    cart = CartModule()

    res1 = cart.calculate_total([100, 200, 50])
    print(f"Тест 1 (ожидается 350.0): {res1}")
    assert res1 == 350.0, f"Тест 1 упал: {res1}"

    res2 = cart.calculate_total([1000], "STUDENT2024")
    print(f"Тест 2 (ожидается 900.0): {res2}")
    assert res2 == 900.0, f"Тест 2 упал: {res2}"

    res3 = cart.calculate_total([])
    print(f"Тест 3 (ожидается 0.0): {res3}")
    assert res3 == 0.0, f"Тест 3 упал: {res3}"

    try:
        res4 = cart.calculate_total([-500, 100])
        print(f"Тест 4 негативный (ожидается ошибка валидации): {res4}")
    except Exception as ex:
        print(f"Тест 4 негативный: программа упала: {type(ex).__name__}: {ex}")

    try:
        res5 = cart.calculate_total(["борщ", 100])
        print(f"Тест 5 негативный (ожидается ошибка о неверном типе): {res5}")
    except Exception as ex:
        print(f"Тест 5 негативный: программа упала: {type(ex).__name__}: {ex}")

    res6 = cart.calculate_total([1000], "student2024")
    print(f"Тест 6 негативный (ожидается 900.0 с промокодом): {res6}")

    res7 = cart.calculate_total([1000], "A" * 100)
    print(f"Тест 7 негативный (ожидается 1000.0 без скидки): {res7}")


if __name__ == "__main__":
    run_tests()

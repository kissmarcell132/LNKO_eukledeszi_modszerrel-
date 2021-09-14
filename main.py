def main() -> None:
    input_a: int = int(input('a = '))
    input_b: int = int(input('b = '))
    maradek = int
    print(f'A két szám LNKOja({input_a}, {input_b}) = ', end='')
    while maradek != 0:
        maradek = input_a % input_b
        input_a = input_b
        input_b = maradek
    print(input_a)


if __name__ == "__main__":
    main()

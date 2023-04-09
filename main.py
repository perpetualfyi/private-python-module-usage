from type_conversion import cast_to_decimal

def cast_and_print_types():
    print(cast_to_decimal(0.1+0.2))
    print(cast_to_decimal('1.61803398875'))
    print(cast_to_decimal(42))

if __name__ == '__main__':
    cast_and_print_types()

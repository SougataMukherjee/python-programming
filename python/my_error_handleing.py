def divide_numbers(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "can not divide by zero"
    except TypeError:
        return "invalid input type"
    except (Exception, ValueError) as e:
        return f"an error occurred: {e}"
    finally:
        print("division operation attempted")


if __name__ == "__main__":
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))

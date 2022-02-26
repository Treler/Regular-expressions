from re import fullmatch


# delete excess symbols
def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


# Example: 89008007060
def unified_format():
    # symbols which will be replaced
    values4_replace = {"-": " ", "(": " ", ")": " ", "{": " ", "}": " ", "[": " ", "]": " ", "+": ""}
    new_number = "".join(multiple_replace(number, values4_replace).split())
    return f"8{new_number}\n"


with open("numbers.txt", "r", encoding="utf-8") as old:
    numbers = old.readlines()

count_before = len(numbers)

# this regular expression can be modified according to your preferences
pattern = r"\+?[78](([\s-]|[({[])*\d{3}([\s-]|[)\]}])*\d{3}[\s-]*\d{2}[\s-]*\d{2})\b"
new_numbers = set(num.strip().lower() for num in numbers if fullmatch(pattern, num.strip()))

count_after = len(new_numbers)

with open("clear_numbers.txt", "w", encoding="utf-8") as new:
    for number in new_numbers:
        new.write(number.strip() + "\n")
        # new.write(unified_format())

print(f"Total numbers: {count_before}")
print(f"Deleted duplicates or nonexistent: {count_before - count_after}")
print(f"Available for anything: {count_after}")
_ = input()

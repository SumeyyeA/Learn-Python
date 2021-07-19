is_female = True
is_tall = True
if is_female or is_tall:
    print("you are female or tall or both")
elif is_female and not(is_tall):
    print("You are short female")
else:
    print("You are neither female or tall")
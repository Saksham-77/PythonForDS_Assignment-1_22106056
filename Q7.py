str = input("Enter the string: ")
char, dgdts, symbls, uppr_char, lwr_char = 0, 0, 0, 0, 0
for _ in str:
    if "0" <= _ <= "9":
        dgdts += 1
    elif "a" <= _ <= "z":
        lwr_char += 1
        char += 1
    elif "A" <= _ <= "Z":
        uppr_char += 1
        char += 1
    else:
        symbls += 1
print(f"""Number of alphabets {char}
Number of digits {dgdts}
Number of symbols {symbls}
Number of uppercase alphabets {uppr_char}
Number of lowercase alphabets {lwr_char}""")
hr_to_sec=3600
min_to_sec=60

print("Input seconds:")
seconds=int(input())

hour=seconds // hr_to_sec
rem=seconds % hr_to_sec

min=rem // min_to_sec
sec=rem % min_to_sec

print(f"{hour} hour(s), {min} minute(s), {sec} second(s)")
seconds = int(input("Enter seconds "))

hours = seconds // 3600
mins = (seconds - (3600 * hours)) // 60
secs = seconds - (3600 * hours) - (mins * 60)

print(f'{hours}:{mins}:{secs}')
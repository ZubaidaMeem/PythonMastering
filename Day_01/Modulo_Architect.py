total_seconds = int(input("Enter number of seconds: "))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"hours: {hours}")
print(f"minutes: {minutes}")
print(f"seconds: {seconds}")

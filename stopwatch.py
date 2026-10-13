import time

seconds = 0

while True:
    minutes = seconds // 60
    remaining_seconds = seconds % 60

    print(f"{minutes:02d}:{remaining_seconds:02d}")

    time.sleep(1)
    seconds += 1

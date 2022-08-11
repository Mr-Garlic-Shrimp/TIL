import time

# 現在時刻を表示（エポックからの経過秒数。エポックは１９７０年１月１日）
print(time.time())

# 現在時刻に１０秒足す
till_end = 10
print(time.time() + till_end)


# time.sleepでPythonの処理を一時停止する
time.sleep(5)
print(time.time())
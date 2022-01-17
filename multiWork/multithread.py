import threading

def count():
    for i in range(1000000000):
        continue

# 定義線程
t_list = []

t1 = threading.Thread(target=count)
t_list.append(t1)
t2 = threading.Thread(target=count)
t_list.append(t2)
t3 = threading.Thread(target=count)
t_list.append(t3)

# 開始工作
for t in t_list:
    t.start()

# 調整多程順序
for t in t_list:
    t.join()
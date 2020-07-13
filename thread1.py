import threading

# 获取已激活的线程数
print(threading.active_count())

# 查看所有线程信息
print(threading.enumerate())

# 查看正在运行的线程
print(threading.current_thread())


# 添加线程
def thread_job():
    print('This is a thread of %s' % threading.current_thread())


def main():
    added_thread = threading.Thread(target=thread_job)    # 定义线程 不要加()
    added_thread.start()    # 让线程开始工作


if __name__ == '__main__':
    main()

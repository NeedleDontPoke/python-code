import multiprocessing


def worker(num):
    result = num * num
    print(f"进程 {num}: {result}")


if __name__ == "__main__":
    processes = []

    for i in range(4):  # 创建4个进程
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("所有进程执行完毕.")

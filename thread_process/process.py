import multiprocessing as mp
import time


def foo_pool(x):
    time.sleep(2)
    return x * x


result_list = []


def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)


def apply_async_with_callback():
    pool = mp.Pool(5)
    for i in range(10):
        pool.apply(foo_pool, args=(i,))
        # pool.apply_async(foo_pool, args=(i,), callback=log_result)
    pool.close()
    pool.join()
    print(result_list)


if __name__ == '__main__':
    start = time.time()
    apply_async_with_callback()
    end = time.time()
    print("Elapsed: {}".format(end - start))

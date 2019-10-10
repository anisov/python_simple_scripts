from multiprocessing import Pool


def cq(n):
    summ = 0
    for i in range(1000):
        summ += n**i
    return summ


def main():
    nums = [i for i in range(1000)]
    pool = Pool()
    result = pool.map(cq, nums)
    pool.close()
    pool.join()
    print(nums, result)

    pool = Pool()
    result = pool.apply_async(cq, (1, ))
    print(result.get(timeout=1))


if __name__ == '__main__':
    main()

from multiprocessing import Pool
import tqdm
import time

def child(num):

    time.sleep(0.5)
    return num*num

if __name__ == "__main__":
    with Pool(8) as p:
        l = list(range(2000))
        print(l)
        r = list(tqdm.tqdm(p.imap(child, l), total= len(l)))
        print(list(r))

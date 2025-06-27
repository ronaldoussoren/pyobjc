import threading

N_THREAD = 8

t_list = []

have_exception = False


def excepthook(args):
    global have_exception
    threading.__excepthook__(args)
    have_exception = True


threading.excepthook = excepthook


def run_in_threads(func, args):
    bar = threading.Barrier(N_THREAD)
    for _ in range(N_THREAD):
        t = threading.Thread(target=func, args=args + (bar,))
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()

    if have_exception:
        raise SystemExit(1)


def run_multiple_in_threads(*func_args):

    bar = threading.Barrier(len(func_args))
    for func, args in func_args:
        t = threading.Thread(target=func, args=args + (bar,))
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()

    if have_exception:
        raise SystemExit(1)

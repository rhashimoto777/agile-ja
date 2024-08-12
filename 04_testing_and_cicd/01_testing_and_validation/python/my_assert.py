# ----これらの関数を変更する必要はありません----
names = ["Nick", "Lewis", "Nikos"]

def contains(name, list_of_names):
    if name not in list_of_names:
        return False
    else:
        return True

def get_name(name, list_of_names):
    if name in list_of_names:
        return name
    else:
        return -1

def add_name(name, list_of_names):
    list_of_names.append(name)
    return name

def add_two(num):
    return num + 2

def divide_by_two(num):
    return num / 2

def greeting(name, num):
    message = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    print(message)
    return message

# ----ここにコードを書いてください----*/
# ----難易度: 富士----
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='########### LOG_%(levelname)s [%(asctime)s][%(name)s][%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[
                        logging.StreamHandler()  # コンソール出力
                    ])
logger = logging.getLogger(__name__)
str_start_test = "*********** start test ***********"

# `my_assert` をここに定義し、以降のテストに使用してください。
def my_assert(expr, msg=None, print_log: bool = True):
    if expr == False:
        if msg == None:
            msg = "assertion error"
        if print_log:
            print(f'test-FAILED : {msg}')
        return msg
    if print_log:
        print("test-OK")
    return None

# `contains` 用のテスト `test_contains` を作成してください
def test_contains():
    logger.info(str_start_test)
    tnames = ["Alice", "Bob", "Chris"]
    my_assert(contains("Alice", tnames) == True)    
    my_assert(contains("aaa", tnames) == False)
    return

test_contains()

# `add_name` 用のテスト `test_add_name` を作成してください
def test_add_name():
    logger.info(str_start_test)
    tnames = ["Alice", "Bob", "Chris"]
    tnames_len = len(tnames)
    my_assert(contains("Taro", tnames) == False)
    my_assert(add_name("Taro", tnames) == "Taro")
    my_assert(contains("Taro", tnames) == True)
    my_assert(len(tnames) == (tnames_len + 1))
    return

test_add_name()

# `add_two` 用のテスト `test_add_two` を作成してください
def test_add_two():
    logger.info(str_start_test)
    my_assert(add_two(5) == 7)
    my_assert(add_two(-1) == 1)
    my_assert(add_two(-9) == -7)
    return

test_add_two()

# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください
def test_divide_by_two():
    logger.info(str_start_test)
    my_assert(divide_by_two(1) == 0.5)
    my_assert(divide_by_two(4) == 2)
    my_assert(divide_by_two(0) == 0)
    my_assert(divide_by_two(-3) == -1.5)
    return

test_divide_by_two()

# `greeting` 用のテスト `test_greeting` を作成してください
def test_greeting():
    logger.info(str_start_test)
    name = "Taro"
    num = {10.0}
    msg_expect = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    my_assert(greeting(name, num) == msg_expect)
    return

test_greeting()

# ----難易度: キリマンジャロ----

# `my_assert` 用のテスト `test_my_assert_false` を作成し、式がFalseと評価されたときに指定したオプションの `msg` を適切に返すかどうかをチェックしてください。
def test_my_assert_false():
    logger.info(str_start_test)
    assert my_assert(False, "testestestest", False) == "testestestest"
    assert my_assert(False, "", False) == ""
    assert my_assert(expr=False, print_log=False) == "assertion error"
    assert my_assert(True, "testestestest", False) == None
    assert my_assert(True, "", False) == None
    assert my_assert(expr=True, print_log=False) == None
    print("test-OK")
    return

test_my_assert_false()
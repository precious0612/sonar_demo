# py-app/app.py

import math  # 1) 未使用 import（常见 Code Smell）
import json  # 2) 未使用 import（常见 Code Smell）

def will_always_return(x: int) -> int:
    unused = 123  # 3) 未使用变量（典型 Code Smell：Unused local variables should be removed）
    if x > 0:
        return 1
    else:
        return 1  # 4) 两个分支完全相同（冗余分支，典型 Code Smell）

def bad_exception_handling() -> None:
    try:
        int("not-a-number")
    except Exception:
        # 5) 捕获 Exception + 什么都不做（隐藏错误，典型 Code Smell）
        pass

def wrong_bool_logic(flag: bool) -> bool:
    # 6) 恒等逻辑（always true/false 或多余布尔判断，很多 profile 都会报“简化表达式”类问题）
    return True if flag else True

def lose_stacktrace() -> None:
    try:
        1 / 0
    except ZeroDivisionError as e:
        # 7) raise Exception(e) 会丢失原始堆栈语义（很多规则会建议 `raise` 或 `raise ... from e`
        raise Exception(e)

if __name__ == "__main__":
    print(will_always_return(-1))
    bad_exception_handling()
    print(wrong_bool_logic(False))
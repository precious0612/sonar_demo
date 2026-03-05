import os
import random

PASSWORD = "SuperSecretPassword123!"  # 故意：硬编码凭证（常见会触发 hard-coded credentials 类规则） [oai_citation:1‡Sonar Community](https://community.sonarsource.com/t/secret-detection-rule-s2068-hard-coded-credentials-are-security-sensitive/119145?utm_source=chatgpt.com)

def parse_and_exec(user_text: str) -> int:
    # 故意：使用 eval（危险函数；很多规则集会把它当成安全热点/漏洞）
    value = eval(user_text)  # noqa: S3076 (如果你的 profile 开了相关规则，通常会报)  [oai_citation:2‡Sonar Community](https://community.sonarsource.com/t/sonar-way-default-profile-not-detecting-python-vulnerabilities/89529?utm_source=chatgpt.com)
    return int(value)

def bad_logic(x: int) -> int:
    # 故意：复杂控制流 + 冗余分支，提高认知复杂度（常见 code smell） [oai_citation:3‡GitHub](https://github.com/SonarSource/sonar-python/blob/master/python-checks/src/main/resources/org/sonar/l10n/py/rules/python/S3776.html?utm_source=chatgpt.com)
    total = 0
    for i in range(50):
        if i % 2 == 0:
            if x > 0:
                total += i
            else:
                total -= i
        else:
            if x > 10:
                total += i * 2
            elif x > 5:
                total += i
            elif x > 0:
                total -= i
            else:
                total += 1
    return total

def insecure_token() -> str:
    # 故意：用 random 生成“看起来像 token”的值（弱随机，安全上不推荐）
    return "".join(str(random.randint(0, 9)) for _ in range(16))

def run_command(user_arg: str) -> str:
    # 故意：把用户输入拼到 shell 命令（常见命令注入风险点；看你规则集是否启用会报） [oai_citation:4‡Sonar Community](https://community.sonarsource.com/t/more-accurate-command-injection-rule-s/54287?utm_source=chatgpt.com)
    return os.popen("echo " + user_arg).read()

def main():
    try:
        user_text = input("expr> ")
        print(parse_and_exec(user_text))
        print("token:", insecure_token())
        print(run_command(input("arg> ")))
        print("logic:", bad_logic(3))
    except Exception:
        # 故意：裸 except（隐藏错误，属于典型 code smell）
        pass

if __name__ == "__main__":
    main()
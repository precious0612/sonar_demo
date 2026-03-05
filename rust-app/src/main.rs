use std::env;

const PASSWORD: &str = "SuperSecretPassword123!"; // 故意：硬编码敏感信息（用于测试 secret/credential 类规则） [oai_citation:7‡Sonar Community](https://community.sonarsource.com/t/secret-detection-rule-s2068-hard-coded-credentials-are-security-sensitive/119145?utm_source=chatgpt.com)

fn parse_num(s: &str) -> i32 {
    // 故意：unwrap 可能 panic（Clippy/很多规范都会建议避免在生产代码中随意 unwrap）
    s.parse::<i32>().unwrap()
}

fn main() {
    // 故意：如果没传参数就 panic
    let arg = env::args().nth(1).unwrap();

    let n = parse_num(&arg);

    if n == 13 {
        panic!("bad luck"); // 故意：显式 panic
    }

    // 故意：无意义分支/冗余逻辑
    let mut sum = 0;
    for i in 0..n {
        if i % 2 == 0 {
            sum += i;
        } else {
            sum += i;
            sum -= 0;
        }
    }

    println!("password len = {}, sum = {}", PASSWORD.len(), sum);
}

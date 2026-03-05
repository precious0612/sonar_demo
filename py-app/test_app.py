from app import bad_logic

def test_bad_logic_should_be_1000():
    # 故意写错断言，让 CI 测试必失败，方便你验证 CI 确实在跑 tests
    assert bad_logic(3) == 1000
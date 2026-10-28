
# 公開APIが正常にインポートできることを確認する
def test_public_api():
    from kplot import hist, scatter3

    assert hist is not None
    assert scatter3 is not None

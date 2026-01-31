# Version

めんどくさいので日本語で

## 今後

- fitterの実装
    - 最近開発されていた`kfittingbase.py`はscipy-base(tiny class)
    - 非対称性誤差も考慮できる`iminuit`を用いた最小化キットを利用したfitterを実装する予定
- 関数のモダン化
   - Pythonをすこし理解したのでそれに合わせて引数を始めとした関数関係をモダンにする  

## 1.0.1

1. デフォルト設定の変更
    - より`CERN ROOT`らしく: 軸のデフォルト設定を変更(x: right、y:top)  
    - 上記に対して、論文に投稿する図を作成することも考慮して最適化
        - fig_sizeは`A4`からデフォルト値の`8:6`へ変更
        - 前述のサイズ変更に伴いフォントサイズを18に最適化。凡例は14pt
        - セリフ体の場合: 数式フォントを`stix`を使用するように変更
        - 枠全体に内向きの線を追加(今後消せるフラグを追加する予定)
        - save_fig: tightレイアウト(0.05 inchの余白)を採用
2. setup.pyの標準化
   - 今後のメンテナンスのため、書き方を変更した。 

- Ref
  - [Pull requests](https://github.com/kyashaa/kplot/pull/1#issue-3876555452)
  - [Pull requests](https://github.com/kyashaa/kplot/pull/6#issue-3876782047)

## 1.0.0

- first release
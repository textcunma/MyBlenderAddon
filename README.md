# MyBlenderAddon
self-made Blender Addon


## Skip frame アドオン
アニメーション作業時、特定コマンドを押して数フレーム移動可能にするアドオン。2コマ作画や3コマ作画などリミテッドアニメーション作成に便利かと思われます。ドープシート、タイムライン画面においてボタンが表示されます。

ドープシート画面
<img src="./assets/skip_dopesheet.jpg" alt="アドオン適用時のドープシート画面">

タイムライン画面
<img src="./assets/skip_timeline.jpg" alt="アドオン適用時のタイムライン画面">

【ショートカットキー一覧】
- 1フレーム前進：テンキー1
- 2フレーム前進：テンキー2
- 3フレーム前進：テンキー3
- 4フレーム前進：テンキー4
- 1フレーム後進：Ctrl+テンキー1
- 2フレーム後進：Ctrl+テンキー2
- 3フレーム後進：Ctrl+テンキー3
- 4フレーム後進：Ctrl+テンキー4

ソースコード：skipframe.py

## Click Start End アドオン
アニメーション作業時、現時点のフレームを開始フレームまたは終了フレームにする機能をコンテキストメニューに追加するアドオン。
※コンテキストメニューは右クリックを押すと表示されます

<div align="center">
    <img src="./assets/set_startend.jpg" width="70%"　alt="アドオン適用時のコンテキストメニュー内">
</div>


ソースコード：click_startend.py
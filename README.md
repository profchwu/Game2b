# 小小夢魔：霧中種子園

給小學生玩的繁體中文生活理財互動遊戲。玩家在布偶定格風格的夢境房間裡完成兩個選擇題，學習「先照顧需要再儲蓄」與「分散能降低集中風險，但不保證獲利」，取得兩把 KEY，最後查看關卡分數與學習成果。

## 操作

- 點「進入花園」開始。
- 每關選一個答案；答錯可以再試，首次答對得 100 分，嘗試後答對得 80 分。
- 每關解題通過後取得 KEY，再前往下一關。
- 完成兩關查看分數、KEY 與學習回顧。
- 鍵盤 Tab/Enter 可操作介面；「動態」可關閉角色動畫。

## 本機開發

使用 Godot 4.7.2 開啟此資料夾中的 `project.godot`。Blender 場景原檔位於 `assets/blender/source/`，網站直接使用已匯出的 GLB。以 Blender 5.x 開啟 `tools/build_blender_assets.py` 重新建置資產。

匯出 Web：在 Godot 安裝相符版本的 Web export templates，選擇 Web preset 並匯出為 `build/web/index.html`。Web 版使用單執行緒設定，避免要求額外跨來源隔離標頭。

## GitHub Pages

`.github/workflows/pages.yml` 會在推送 `main` 時自動匯出 Godot Web 並部署到 GitHub Pages。第一次設定此 repo 時，到 **Settings → Pages → Build and deployment** 將來源設為 **GitHub Actions**。後續每次推送會自動更新網站。

## 專案紀錄

設計決策與製作提示詞見 `docs/`。角色、兩個場景、動畫與可編輯 Blender 原檔見 `assets/blender/`。

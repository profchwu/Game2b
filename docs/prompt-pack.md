# 小小夢魔 — 專案 Prompt Pack

Version: 1.0
Date: 2026-11-24
Status: art direction B approved; gameplay concept awaiting owner selection.

This file records the project prompts and reusable execution prompts. It includes user-facing project instructions only; it does not include system/developer instructions or private reasoning. Prompts marked **used** were used in this process. Prompts marked **next phase** are prepared for implementation and should be run after the remaining gameplay decision.

## 1. Original project request — used

> 角色：你是一位 AI 教育遊戲開發專家。
> 使用我的 `C:\Godot` 完成小小夢魔遊戲，使用我的 `C:\blender` 製作 3D 模型。
> 教學單元：生活理財投資；對象：小學生。
> 設計 2 關，每一關有一個互動單元，解題通過才能取得 KEY。每一關要顯示得分，並最後顯示進步成果。
> 參考《Little Nightmares》Steam 頁面與提供的圖片。製作成網頁形式，讓我可以部署在 GitHub 或 Netlify。

## 2. Project master prompt — normalized from the owner's request

> 你是 AI 教育遊戲設計、Blender 3D、美術技術與 Godot Web 開發團隊。請在目前 Game2b 專案中完成一款原創的繁體中文兒童理財遊戲。
>
> **已確認需求**：Godot 專案並匯出網頁版；用 Blender 製作 3D 環境、角色與動畫；兩個關卡各有一個主要互動、個別得分、解題通過後取得 KEY，最後顯示進步成果；部署至 `https://github.com/profchwu/Game2b` 的 GitHub Pages。
>
> **已核准美術方向**：B「布偶定格 3D」。嚴格依照 `docs/visual-style-guide.md` 與 `assets/concepts/approved-style-b-stop-motion.png`，統一所有環境、角色、道具、材質、燈光與動畫。布料、補丁、縫線、黏土感造型、手作木頭、黃銅燈籠、暖色微光；神秘但溫暖，適合國小學生。不要把文字畫進貼圖。
>
> **玩法待選**：先讀 `docs/design-tournament.md`，等待專案負責人選擇玩法概念；AI 排名只作參考，不要擅自把推薦選項記成核准。Balanced L/E/M/A 權重只是暫定假設，不能宣稱有玩家或學習成效證據。
>
> **安全與原創**：只用虛構夢幣和示意情境，不提供個人化投資建議、不使用真實金融商品或即時報價、不保證獲利、不收集可識別學生資料。Little Nightmares 僅作大尺度空間、光影氣氛的高層次參考；不可複製其角色、場景、道具、故事、音樂或標誌。避免血腥、追逐驚嚇與懲罰式失敗。
>
> **交付品質**：保持 GDScript、Godot Compatibility renderer 與單執行緒 Web 匯出預設；支援鍵盤、滑鼠及觸控；含重試、復原、重開、清楚回饋、繁體中文及減少動態效果。實作前先確認目標關卡玩法與規格；完成後實際匯出並以瀏覽器驗證，不得把未測試內容稱為完成。

## 3. Design Thinking / game-design tournament prompt — used as process brief

> 針對國小生活理財與投資概念，設計兩個短關卡；每關僅一個主要互動。先列 6–10 個在核心動詞、壓力模型、資訊呈現、失敗復原及重玩方式上真正不同的玩法。建立兒童安全、財務正確性、兩關/單互動、Godot Web 可行性、原創 IP 與無個資收集等硬門檻。用遊戲設計、新手玩家/無障礙、金融領域、評量有效性、製作可行性五個分開的評審角度檢視，標示 AI pre-score 與假設，不得冒稱玩家證據。分別呈現 Game Experience、Purpose Fit、Development Feasibility，不把教育診斷分數混入前三軸。使用預設 Balanced profile `L=.40, E=.20, M=.15, A=.25, pG=.15, pC=.10` 計算 `R_edu`，並標示為暫定假設。列出前三名、淘汰項目、風險與可推翻核心假設的最低成本測試；最後停下來讓負責人選玩法。

## 4. ImageGen prompts — used

All three concepts used the same scene, character, and composition. The attached Little Nightmares screenshot was supplied only as a high-level mood reference for old-house scale, dust, and light/shadow; exact composition, furniture, characters, and protected assets were excluded.

### Shared prompt body

> Use case: stylized-concept. Asset type: visual-style selection image for an original elementary-school financial-literacy adventure game. Input image: the user's attached Little Nightmares screenshot is a high-level mood reference only for tall old-house scale, dusty darkness, and a warm pool of light; do not recreate its composition, furniture, characters, or any protected game assets. Primary request: show the exact same representative gameplay moment in every style option: a tiny original dream-keeper in a teal patchwork rain cape, rust-red shorts, round satchel, and a small brass firefly lantern stands beside a wooden table, deciding how to divide a small pile of dream coins between three glass jars labeled only with simple icons (a heart for needs, a star for a wish, a sprout for savings); behind them is a tall old wooden door with a softly glowing keyhole. Scene/backdrop: an oversized, cozy old-house savings room with shelves, a ledger, a few oversized coins, worn patterned wallpaper, and gentle dust motes. Composition/framing: 16:9 landscape, medium-wide third-person side-view game camera, character and three jars clearly readable in the middle third, door visible in background, identical camera and layout across all three style options. Lighting/mood: mysterious and dreamlike but safe and welcoming for elementary students, warm lantern key light, soft shadow, no fear or peril. Palette: muted olive and teal with warm amber accents. Constraints: original character and original room; strong readability at small game-screen size; no text, letters, logos, watermark, violence, gore, chase, monsters, or copied Little Nightmares elements.

### Style suffix A — hand-painted storybook

> Style/medium: a hand-painted 2.5D storybook illustration, visible gouache brushwork and subtle paper grain, layered painted scenery, tender expressive shapes, warm sage-green and amber palette, polished yet handmade.

### Style suffix B — selected tactile stop-motion 3D

> Style/medium: a high-quality stop-motion miniature set rendered as tactile stylized 3D, rounded sculpted wood, felt and knitted fabrics, clay-like forms, soft miniature depth of field, warm amber lantern glow, gentle handcrafted charm.

### Style suffix C — geometric paper diorama

> Style/medium: a crisp low-poly paper-craft diorama, folded cardstock and faceted carved forms, clean silhouette design, layered depth, precise soft shadows, restrained forest-green, dusty blue and golden-orange palette, playful and calm.

## 5. Blender asset-production prompt — next phase

> Use Blender 5.3 to create original, editable 3D assets for Game2b in the approved tactile stop-motion style. Treat `assets/concepts/approved-style-b-stop-motion.png` and `docs/visual-style-guide.md` as the visual source of truth. Create a named, organized `.blend` scene for the shared dream-keeper character and the dream-coin savings room. Use felt/stitched cape and satchel, clay-like rounded face, hand-worked wood, glass jars, brass lantern, teal/rust/amber palette, warm lantern key light, soft cool fill, readable silhouettes. Add reusable animation clips for Idle (gentle breathing/lantern sway), Walk, Reach/Interact, and KEY unlock; motion should communicate cause and result, remain calm, and be reducible. Keep text out of textures and keep interaction space clear for Godot UI. Export a GLB with correct scale, materials, pivots, and animations into the project. Render a preview for visual review. Do not begin unique gameplay-only set dressing until the owner chooses the gameplay concept. Record asset IDs, source, version, and licensing; all modeled content must be original.

## 6. Godot Web implementation prompt — next phase

> After the owner selects a concept in `docs/design-tournament.md`, implement that concept in Godot 4.7.2 using GDScript and the approved Blender GLB assets. Build exactly two short levels with one primary scored interaction per level. A correct solution unlocks that level's KEY; each level shows its own score. The final screen shows each score, total progress, and a short explanation of demonstrated skills. Include accessible instructions, keyboard/pointer/touch input, feedback, retry/recovery, restart, and reduced-motion behavior. Keep scores deterministic and session-local; no student names, telemetry, account, or real-money/investment data. Do not present profit as guaranteed. Use the Compatibility renderer and a single-threaded Web export unless a tested hosting configuration requires otherwise. Keep source project separate from generated web export; add a GitHub Pages workflow only after the exported game passes verification.

## 7. Verification and release prompt — next phase

> Verify the Godot project imports and launches; play both full level flows; confirm score, KEY gating, feedback, retry, final recap, and restart. Export the Web build and serve it over HTTPS; verify a modern WebGL 2 browser, responsive desktop/mobile viewport, keyboard/pointer/touch controls, Traditional Chinese rendering, reduced motion, asset loading, and browser-console errors. Record exact Godot/Blender versions, commands, results, limitations, and screenshots. Only after checks pass, publish the build to the existing `profchwu/Game2b` repository and verify the GitHub Pages URL. Never report unrun checks as passed.

## 8. Current status

- Visual direction B is approved and saved as `assets/concepts/approved-style-b-stop-motion.png`.
- Gameplay selection is still open. Candidate A is recommended but not approved.
- The Blender and Godot prompts above are prepared, not yet executed.
- The current repository already contains an HTML prototype. It is not a Godot Web export and must not be described as one.

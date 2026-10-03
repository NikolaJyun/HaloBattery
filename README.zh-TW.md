# Halo Battery

[English](README.md)

在 Windows 系統匣顯示無線滑鼠、鍵盤、耳機與控制器的電量——每個裝置各有一個圖示，不需要原廠軟體。

![所有圖示狀態](docs/icons.png)

充電時，圓弧會緩慢地「呼吸」：

![充電動畫](docs/charging.gif)

每個裝置都有自己的系統匣圖示：中央顯示裝置圖案，外圍則是電量環。圓弧從頂端開始順時針填滿；電量接近警示值時會變成琥珀色，等於或低於警示值時則變成紅色；裝置充電時會以綠色呼吸。將滑鼠游標移到圖示上可查看確切百分比；按一下滑鼠右鍵即可重新命名、隱藏裝置、變更偏好設定或產生診斷報告。

程式會透過 USB/HID（接收器、轉接器或傳輸線）、Xbox 類控制器回報，以及 Windows 本身提供的藍牙裝置資訊讀取電量。

## 支援的裝置

**`是`** 表示確實曾在實體裝置上讀取到電量。**`否`** 表示支援程式碼取自其他工具，但尚未有人在實體硬體上測試。**`很可能`** 表示同系列其他型號共用相同程式碼，理論上應該也能運作，只是尚未逐一測試。每個裝置都連結至其[電量讀取方式說明](docs/protocols.md)。

| 裝置 | 連線方式 | 已在實體硬體驗證 |
|---|---|---|
| [8BitDo Pro 2、Pro 3、SN30 Pro、SF30 Pro（D-input 模式）](docs/protocols.md#8bitdo-pro-2-pro-3-sn30-pro-sf30-pro-in-d-input-mode) | 藍牙或 USB | 否 |
| [AM Infinity 8K（Angry Miao）](docs/protocols.md#am-infinity-8k-angry-miao) | 2.4 GHz 接收器 | 否 |
| [Astro A50 Gen 5（Logitech 046D:0B1C）](docs/protocols.md#astro-a50-gen-5-logitech-046d0b1c) | 基地台 | 否 |
| [ASUS ROG Gladius III Aimpoint 與其他 ROG／TUF 無線滑鼠（清單請見 `providers/asus.py`）](docs/protocols.md#asus-rog-gladius-iii-aimpoint-and-other-rog--tuf-wireless-mice) | 2.4 GHz 接收器或 USB 傳輸線 | 否 |
| [Audeze Maxwell](docs/protocols.md#audeze-maxwell) | 2.4 GHz 轉接器或 USB-C 傳輸線 | 是 |
| [藍牙裝置；以 1MORE SonoFlow 耳機測試（使用者亦回報 Audio-Technica 與 JBL Tune 760NC 可用）](docs/protocols.md#bluetooth-devices-tested-on-the-1more-sonoflow-headset) | 藍牙（預設開啟，可從選單關閉） | 是 |
| [Corsair Dark Core RGB Pro SE](docs/protocols.md#corsair-dark-core-rgb-pro-se) | 2.4 GHz 轉接器 | 否 |
| [Corsair Void v2 Wireless、Virtuoso Max Wireless、HS80 Max Wireless](docs/protocols.md#corsair-void-v2-wireless-virtuoso-max-wireless-hs80-max-wireless) | 無線接收器 | 否 |
| [GameSir G7 Pro；FlyDigi Vader Pro（經使用者測試）](docs/protocols.md#gamesir-g7-pro-flydigi-vader-pro) | 2.4 GHz 接收器（顯示為 Xbox 控制器） | 是 |
| [G-Wolves WARG、HTS Plus（Pro）、HTXU、Lycan、Fenrir Pro／Asym、HTX Mini](docs/protocols.md#g-wolves-warg-hts-plus-pro-htxu-lycan-fenrir-pro--asym-htx-mini) | 8K 接收器或 USB 傳輸線 | 否 |
| [Hitscan Hyperlight](docs/protocols.md#hitscan-hyperlight) | 2.4 GHz 接收器或 USB 傳輸線 | 否 |
| [HyperX Cloud Alpha 2](docs/protocols.md#hyperx-cloud-alpha-2) | 2.4 GHz 基地台 | 是 |
| [HyperX Cloud II Wireless](docs/protocols.md#hyperx-cloud-ii-wireless) | 2.4 GHz 轉接器 | 否 |
| [HyperX Cloud III Wireless](docs/protocols.md#hyperx-cloud-iii-wireless) | 2.4 GHz 轉接器 | 否 |
| [JBL Quantum 910 Wireless](docs/protocols.md#jbl-quantum-910-wireless) | 2.4 GHz 轉接器 | 是 |
| [Keychron Ultra-Link 8K、Keychron M5](docs/protocols.md#keychron-ultra-link-8k-keychron-m5) | 2.4 GHz 接收器與 USB 傳輸線 | 否 |
| [LAMZU Maya X](docs/protocols.md#lamzu-maya-x) | 8K 轉接器或 USB 傳輸線 | 是 |
| [Lofree Hyzen](docs/protocols.md#lofree-hyzen) | 2.4 GHz 轉接器 | 否 |
| [Logitech G502 LIGHTSPEED、G502 X PLUS](docs/protocols.md#logitech-g502-lightspeed-g502-x-plus) | Lightspeed 接收器 | 是 |
| [Logitech（更多 HID++ 2.0 裝置與 G 系列耳機）](docs/protocols.md#logitech-more-hid-20-devices-and-g-series-headsets) | Lightspeed、Unifying 或 Bolt 接收器 | 很可能 |
| [MCHOSE A7 V2 Ultra](docs/protocols.md#mchose-a7-v2-ultra) | 2.4 GHz 接收器 | 否 |
| [MCHOSE G7](docs/protocols.md#mchose-g7) | USB（晶片「YJX-CHIP」） | 是 |
| [MCHOSE M7 Ultra](docs/protocols.md#mchose-m7-ultra) | 2.4 GHz 接收器 | 是 |
| [Nintendo Switch Pro Controller、Joy-Con（L）／（R）](docs/protocols.md#nintendo-switch-pro-controller-joy-con-l--r) | 藍牙 | 否 |
| [Pulsar X2 V2 Mini／X2 V3 Mini、ATK VXE R1 SE+、VXE R1 Pro Max](docs/protocols.md#pulsar-x2-v2-mini-x2-v3-mini-atk-vxe-r1-se-vxe-r1-pro-max) | 2.4 GHz／8K 轉接器與 USB 傳輸線 | 是 |
| [Razer Barracuda Pro（2.4 GHz）](docs/protocols.md#razer-barracuda-pro-24-ghz) | 2.4 GHz 轉接器 | 是 |
| [Razer Basilisk V3 Pro、Razer Basilisk Ultimate（經使用者測試）](docs/protocols.md#razer-basilisk-v3-pro-razer-basilisk-ultimate) | 2.4 GHz 接收器 | 是 |
| [Razer BlackShark V2 Pro（2023）](docs/protocols.md#razer-blackshark-v2-pro-2023) | 2.4 GHz 接收器 | 是 |
| [Razer BlackWidow V3 Pro](docs/protocols.md#razer-blackwidow-v3-pro) | 2.4 GHz 接收器或 USB 傳輸線 | 否 |
| [Razer DeathAdder V4 Pro](docs/protocols.md#razer-deathadder-v4-pro) | 2.4 GHz 接收器 | 是 |
| [Razer 無線滑鼠（其他 OpenRazer 型號）](docs/protocols.md#razer-wireless-mice-other-openrazer-models) | 2.4 GHz 接收器或 USB 傳輸線 | 很可能 |
| [Sony DualSense（PS5）](docs/protocols.md#sony-dualsense-ps5) | USB 或藍牙 | 是 |
| [Sony DualShock 4（PS4）](docs/protocols.md#sony-dualshock-4-ps4) | USB 傳輸線與藍牙 | 是 |
| [SteelSeries Aerox 3 Wireless](docs/protocols.md#steelseries-aerox-3-wireless) | 2.4 GHz 轉接器 | 否 |
| [SteelSeries Arctis 與 GameBuds（其他型號）](docs/protocols.md#steelseries-arctis-and-gamebuds-other-models) | 無線基地台或轉接器 | 很可能 |
| [SteelSeries Arctis Nova 7](docs/protocols.md#steelseries-arctis-nova-7) | 2.4 GHz 轉接器 | 是 |
| [SteelSeries Arctis Nova Pro Wireless（`1038:12E0`、`1038:12E5` X）](docs/protocols.md#steelseries-arctis-nova-pro-wireless-103812e0-103812e5-x) | 無線基地台，介面 3 或 4 | 否 |
| [SteelSeries Rival 3 Wireless](docs/protocols.md#steelseries-rival-3-wireless) | 2.4 GHz 轉接器 | 否 |
| [WLmouse Beast X 與 Beast X Mini Pro](docs/protocols.md#wlmouse-beast-x-and-beast-x-mini-pro) | 8K 或 1K 接收器，或 USB 傳輸線 | 很可能 |
| [WLmouse Beast X Max](docs/protocols.md#wlmouse-beast-x-max) | 8K 接收器與 USB 傳輸線 | 是 |
| [Xbox 相容控制器（其他型號）](docs/protocols.md#xbox-compatible-controllers-other-models) | USB 或 Xbox 無線轉接器 | 很可能 |

**透過藍牙連線的 PlayStation 控制器：** DualShock 4 或 DualSense 只有在「完整回報」模式下才會透過藍牙傳送電量。此模式會讓使用 DirectInput 的遊戲無法偵測控制器，直到控制器關閉再重新開啟（#96），因此程式不會自行切換；只有 Steam 或遊戲已切換模式時才顯示電量。若不玩此類遊戲，可開啟**偏好設定 → PlayStation 完整模式（藍牙）**。USB 連線一律顯示電量。

**D-input 模式的 8BitDo 控制器：** 電量只存在於增強回報中。切換後 DirectInput 遊戲會無法偵測控制器，直到控制器關閉再重新開啟（經 #101 回報者測試），因此程式不會自行切換。Steam 或遊戲已切換模式時才顯示電量；XInput 模式則一律顯示。

標示為 `很可能` 的裝置與其他型號共用程式路徑，包括其餘 OpenRazer 型號、其他 WLmouse 型號、更多 Logitech HID++ 2.0 裝置與 G 系列耳機、其他 Arctis 型號及 Xbox 相容控制器。

不保證支援其他裝置。若裝置未被偵測或電量錯誤，請建立 Issue 並附上診斷報告——詳見下方的**疑難排解**。

## 安裝

### 選項一：使用已編譯的 .exe（建議）

1. 從 [Releases](../../releases/latest) 下載 `HaloBattery-<版本>.zip`。
2. 解壓縮至固定位置，例如 `C:\Tools`，得到 `C:\Tools\HaloBattery\HaloBattery.exe`，然後執行。請完整保留 `HaloBattery` 資料夾；.exe 需要旁邊的 `_internal` 資料夾。
3. 在系統匣圖示上按一下滑鼠右鍵 → **隨 Windows 啟動**。

程式每天檢查一次更新；有新版本時，選單會出現**下載 vX.Y.Z…**。更新時請在系統匣選單選擇**結束**，再取代原資料夾；**隨 Windows 啟動**會跟隨新副本。若曾使用舊版單檔 `HaloBattery.exe`，請將它刪除。

由於程式未經程式碼簽署，Windows SmartScreen 初次啟動時可能警告：請選擇**其他資訊 → 仍要執行**。部分防毒軟體可能誤判未簽署的 Python 應用程式（通常是 `!ml` 泛用偵測）。Release 由 GitHub Actions 直接從此儲存庫建置，並提供公開記錄；若不願信任成品，請使用選項二。

### 選項二：從原始碼執行

1. 安裝 [Python 3.10 以上版本](https://www.python.org/downloads/)，並勾選 **Add python.exe to PATH**。
2. 將此儲存庫下載或複製至固定位置，例如 `C:\Tools\HaloBattery`。
3. 執行 `install_and_run.bat`，再從系統匣開啟**隨 Windows 啟動**。

`build_exe.bat` 可自行建置至 `dist\HaloBattery`。推送如 `v1.8.0` 的標籤後，GitHub Actions 會自動建置並將 ZIP 附加至 Release（`.github/workflows/release.yml`）。

## 圖示

- **中央**：耳機、滑鼠、鍵盤（帶 K 的鍵帽）、Xbox／PlayStation 控制器或藍牙符號；可從選單關閉。
- **色彩**：跟隨工作列（深色使用白色，淺色使用黑色）。執行 [MyDockFinder](https://store.steampowered.com/app/1787090/MyDockFinder/) 時會跟隨其頂端選單列。透明工作列可選擇**圖示色彩 → 白色**或**黑色**。
- **琥珀色**：接近警示值。**紅色**：等於或低於警示值。
- **綠色呼吸效果**：充電中；可關閉動畫，留下靜態綠色圓弧。
- **半透明**：滑鼠休眠中，保留最後電量 5 分鐘。關閉的裝置會消失，重新開啟後再出現。

低電量通知只會發出一次，裝置充電後才會再次發出。

## 系統匣選單

在圖示上按右鍵即可開啟 Windows 11 風格選單。如果無法運作，請在 `%APPDATA%\HaloBattery\config.json` 設定 `"fluent_menu": false`，恢復傳統 Windows 選單。

- **重新命名…**：自訂裝置名稱；**重設名稱**可恢復原名。
- **圖示**：選擇自動、滑鼠、鍵盤、耳機、控制器或藍牙圖案。
- **低電量警示值**：此裝置專用的警示值（關閉或 10–30%），或選擇**預設**。
- **隱藏此裝置**：移除裝置圖示。
- **立即重新整理**
- **偏好設定**：
  - **更新間隔**（15 秒至 5 分鐘）與**低電量警示**（關閉或 10–30%）：以 −、+ 或滾輪調整
  - **充飽電時通知**（每次充電一次，預設開啟）
  - **顯示預估剩餘時間**：依上次充電後的耗電速度估算。只有裝置喚醒且使用電池時才計時；使用滿 30 分鐘且下降 3% 後才估算。歷史位於 `%APPDATA%\HaloBattery\history.json`。
  - **遊戲時勿擾**（預設開啟）：全螢幕時暫緩通知並改為每 5 分鐘輪詢；離開全螢幕後顯示仍有效的通知。接上裝置仍會立即更新。
  - **Windows 藍牙裝置**、**裝置圖案**、**在圖示中顯示百分比**、**充電動畫**
  - **PlayStation 完整模式（藍牙）**（預設關閉）：一律讀取 PS4／PS5 藍牙控制器電量；部分遊戲在此模式下會停止偵測控制器，直到重新開關控制器
  - **供其他應用程式使用的狀態檔**（預設關閉）：每次輪詢寫入 `%APPDATA%\HaloBattery\status.json`。裝置包含 `name`、`level`、`charging`、`online`、`kind`、`seconds_left` 與 `text`；程式結束時 `running` 變為 false，`updated_unix` 表示更新時間。關閉會刪除檔案。
  - **裝置類型**：停用特定品牌或裝置系列
  - **圖示色彩**：自動、白色或黑色
  - **隨 Windows 啟動**（使用者層級登錄機碼，無需系統管理員權限）
  - **檢查更新**：預設開啟，每天一次；有更新時顯示通知及**下載 vX.Y.Z…**
- **隱藏的裝置**：按一下即可重新顯示
- **診斷資訊…**：寫入並開啟詳細報告

## 疑難排解

1. 關閉 Synapse、WLmouse 網頁驅動程式與其他電量工具，它們可能占用接收器。
2. 移動滑鼠將其喚醒。
3. 執行 `probe.bat` 或選擇**診斷資訊…**。報告列出所有 HID 裝置與原始通訊回覆；請附加至 Issue。報告含藍牙 MAC 位址與序號，公開前可先遮蔽。[CONTRIBUTING.md](CONTRIBUTING.md) 說明需附哪些資料、如何擷取 USB 流量及建立 Pull Request。
4. 出現**「找不到 python312.dll」**，或**隨 Windows 啟動**提示程式位於暫存資料夾：請勿直接從 ZIP 執行或只複製 .exe。請完整解壓縮（`_internal` 必須留在 .exe 旁）後再執行。

設定、記錄檔與診斷報告位於 `%APPDATA%\HaloBattery`。

## 鳴謝

- WLmouse 通訊協定：@len0c（[incconutwo/mouse-battery-tray](https://github.com/incconutwo/mouse-battery-tray)，MIT）。
- MCHOSE 通訊協定：@alexfrih（[alexfrih/mchose-linux](https://github.com/alexfrih/mchose-linux)，從 MCHOSE 網頁驅動程式復原）；G7 來自 @kek353 的監控程式及 [#8](https://github.com/HeyOkay/HaloBattery/issues/8) 的傾印。
- Hitscan Hyperlight 通訊協定：@sopparus（[sopparus/hitscan-battery](https://github.com/sopparus/hitscan-battery)），從原廠程式 USB 流量解析並在 [libratbag 討論](https://github.com/libratbag/libratbag/issues/1893)確認。
- AM Infinity 8K 通訊協定：AJAZZ Control Center（[Aiacos/ajazz-control-center](https://github.com/Aiacos/ajazz-control-center)，GPL-3.0），從 AJ159 APEX 實機讀取相同 USB ID。
- BlackShark V2 Pro 2023：OpenRazer 驅動程式（[PR #2862](https://github.com/openrazer/openrazer/pull/2862)）。Razer PID 與交易 ID 來自 OpenRazer 及 [RazerBatteryTaskbar](https://github.com/Tekk-Know/RazerBatteryTaskbar)。
- 個別裝置的參考實作——HeadsetControl、rivalcfg、Solaar、G-Helper、HyperHeadset、mouse.xyz、[`@openmouse/protocol`](https://github.com/OpenMouse-Project/openmouse)、keychron-battery-dkms、JBL_Baterry_Monitor 等——均標示於 [docs/protocols.md](docs/protocols.md) 相應裝置旁。

## 授權

MIT，詳見 [LICENSE](LICENSE)。

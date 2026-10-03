# Halo Battery 繁體中文版

[English](README.md)

Halo Battery 會在 Windows 系統匣顯示無線滑鼠、鍵盤、耳機與控制器的電量；每個裝置各有一個圖示，不必安裝原廠軟體。

![所有圖示狀態](docs/icons.png)

充電時，外圈會以綠色呼吸動畫顯示。將滑鼠游標移到圖示上可查看精確電量；按一下滑鼠右鍵則可重新命名、隱藏裝置、調整偏好設定或產生診斷報告。

## 安裝

### 使用已編譯版本（建議）

1. 從 [Releases](../../releases/latest) 下載 `HaloBattery-<版本>.zip`。
2. 將 ZIP 完整解壓縮至獨立資料夾。
3. 執行 `HaloBattery.exe`。程式不會顯示主視窗；裝置圖示會出現在系統匣。
4. 若要開機自動執行，請在任一 Halo Battery 圖示上按一下滑鼠右鍵，開啟「偏好設定 → 隨 Windows 啟動」。

> 此 fork 的介面、通知、裝置狀態、剩餘時間與重新命名視窗均已繁體中文化（台灣用語）。

### 從原始碼執行

需要 Windows 10 或 11，以及 Python 3.9 以上版本：

```powershell
py -m pip install -r requirements.txt
pyw halo_battery.pyw
```

## 主要功能

- 支援 USB/HID 接收器、傳輸線、Xbox 類控制器回報，以及 Windows 藍牙裝置電量。
- 支援低電量與充飽電通知、預估剩餘使用時間、遊戲全螢幕勿擾模式。
- 可為個別裝置重新命名、隱藏裝置、選擇圖示及設定不同的低電量警示值。
- 可輸出 `status.json`，供 Rainmeter、Stream Deck 或其他程式使用。
- 支援 Razer、Logitech、SteelSeries、Audeze、HyperX、ASUS、Corsair、PlayStation、Nintendo、Xbox 相容控制器等多種裝置；完整清單請參閱 [英文 README](README.md#supported-devices)。

## 疑難排解

若裝置未被偵測或電量不正確，請從系統匣選單開啟「診斷資訊…」，再到此儲存庫建立 Issue 並附上產生的 `diagnostics.txt`。診斷內容保留英文技術字串，方便與上游專案共同除錯。

## 授權

本專案沿用原專案的 [MIT License](LICENSE)。

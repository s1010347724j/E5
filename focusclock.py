import time
import winsound  # 仅适用于 Windows 系统，用于播放提醒音频

def focus_timer(focus_minutes, break_minutes):
    while True:
        print(f"专注倒计时：{focus_minutes} 分钟")
        time.sleep(focus_minutes * 60)  # 将分钟转换为秒
        print("时间到！休息一下。")
        
        # 播放提醒音频（可选，仅适用于 Windows）
        winsound.Beep(1000, 1000)  # 参数分别是频率和持续时间
        
        print(f"休息倒计时：{break_minutes} 分钟")
        time.sleep(break_minutes * 60)  # 将分钟转换为秒

if __name__ == "__main__":
    focus_minutes = 25  # 专注时间，例如 25 分钟
    break_minutes = 5   # 休息时间，例如 5 分钟
    focus_timer(focus_minutes, break_minutes)

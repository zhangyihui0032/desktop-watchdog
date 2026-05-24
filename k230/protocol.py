"""指令协议定义 — 此文件为接口契约，三人协商一致后才能修改。

单字节十六进制指令，通过 UART 发送给 STM32。
"""

# 动作指令 (Action_Mode)
ACTION_RELAXED_GETDOWN = 0x29  # 放松趴下 (睡觉表情)
ACTION_SIT = 0x30              # 蹲下 (瞪眼表情)
ACTION_UPRIGHT = 0x31          # 直立 (眼睛表情)
ACTION_GETDOWN = 0x32          # 趴下 (瞪眼表情)
ACTION_ADVANCE = 0x33          # 前进 (快乐表情)
ACTION_BACK = 0x34             # 后退 (快乐表情)
ACTION_TURN_LEFT = 0x35        # 左转 (快乐表情)
ACTION_TURN_RIGHT = 0x36       # 右转 (快乐表情)
ACTION_SWING = 0x37            # 摇摆 (非常快乐表情)
ACTION_SPEED_UP = 0x38         # 步行加速
ACTION_SWING_UP = 0x39         # 摇摆加速
ACTION_WAG_TAIL = 0x40         # 摇尾巴 (切换开/关)
ACTION_JUMP_FORWARD = 0x41     # 向前跳
ACTION_JUMP_BACK = 0x42        # 向后跳
ACTION_HELLO = 0x43            # 打招呼
ACTION_LED_ON = 0x44           # 开启灯光
ACTION_LED_OFF = 0x45          # 关闭灯光
ACTION_BREATHE_ON = 0x46       # 开启呼吸灯
ACTION_BREATHE_OFF = 0x47      # 关闭呼吸灯
ACTION_STRETCH = 0x48          # 伸懒腰
ACTION_LEG_STRETCH = 0x49      # 拉伸腿
ACTION_BATTERY_TOGGLE = 0x50   # 显示电量 (切换开/关)

# 表情 (Face_Mode) — 仅供参考，表情由指令自动触发
FACE_SLEEP = 0       # 睡觉
FACE_STARE = 1       # 瞪眼
FACE_HAPPY = 2       # 快乐
FACE_MANIA = 3       # 狂热
FACE_VERY_HAPPY = 4  # 非常快乐
FACE_EYES = 5        # 眼睛
FACE_HELLO = 6       # 打招呼

# 指令 → 表情映射
CMD_FACE_MAP = {
    ACTION_RELAXED_GETDOWN: FACE_SLEEP,
    ACTION_SIT: FACE_STARE,
    ACTION_UPRIGHT: FACE_EYES,
    ACTION_GETDOWN: FACE_STARE,
    ACTION_ADVANCE: FACE_HAPPY,
    ACTION_BACK: FACE_HAPPY,
    ACTION_TURN_LEFT: FACE_HAPPY,
    ACTION_TURN_RIGHT: FACE_HAPPY,
    ACTION_SWING: FACE_VERY_HAPPY,
    ACTION_WAG_TAIL: FACE_STARE,
    ACTION_JUMP_FORWARD: FACE_HAPPY,
    ACTION_JUMP_BACK: FACE_HAPPY,
    ACTION_HELLO: FACE_HELLO,
    ACTION_STRETCH: FACE_HELLO,
    ACTION_LEG_STRETCH: FACE_HELLO,
}

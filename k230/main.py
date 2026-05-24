"""K230 智能桌面看护机器人 — 主入口。

线程调度:
  1. 视觉线程: 摄像头 → 人脸检测/识别 → 看门狗逻辑 → 发指令
  2. 对话线程: 语音唤醒 → LLM 对话 → TTS → 发指令
"""

import threading
import time
import uart_bridge
import protocol as CMD


def vision_loop():
    """视觉线程: 人脸检测 + 看门狗逻辑 (人B 实现)"""
    # TODO: 人B — 在此实现视觉主循环
    # 伪代码:
    #   detector = FaceDetector(config.FACE_DETECT_MODEL)
    #   recognizer = FaceRecognizer(config.FACE_RECOGNIZE_MODEL)
    #   watchdog = WatchdogStateMachine()
    #
    #   while True:
    #       frame = camera.read()
    #       faces = detector.detect(frame)
    #
    #       if not faces:
    #           action = watchdog.on_nobody()
    #       else:
    #           for face in faces:
    #               identity = recognizer.recognize(face)
    #               if identity == "stranger":
    #                   action = watchdog.on_stranger()
    #               else:
    #                   action = watchdog.on_known_person(identity)
    #
    #       uart_bridge.send_command(action)
    #       time.sleep(0.1)
    pass


def chat_loop():
    """对话线程: 语音唤醒 + LLM + TTS (人C 实现)"""
    # TODO: 人C — 在此实现对话主循环
    # 伪代码:
    #   while True:
    #       voice_wake.wait_for_wake_word()
    #
    #       # 录音 + STT
    #       text = stt.recognize()
    #
    #       # 调 LLM
    #       reply, emotion = llm.chat(text)
    #
    #       # 播放语音
    #       tts.speak(reply)
    #
    #       # 根据情绪映射动作
    #       cmd = emotion_map.to_command(emotion)
    #       uart_bridge.send_command(cmd)
    pass


def main():
    print("[watchdog] 智能桌面看护机器人启动...")

    # 开机动画：站立 + 打招呼
    uart_bridge.send_command(CMD.ACTION_UPRIGHT)
    time.sleep(0.5)
    uart_bridge.send_command(CMD.ACTION_HELLO)
    time.sleep(2)

    # 启动子线程
    t_vision = threading.Thread(target=vision_loop, daemon=True, name="vision")
    t_chat = threading.Thread(target=chat_loop, daemon=True, name="chat")

    t_vision.start()
    t_chat.start()

    print("[watchdog] 视觉线程与对话线程已启动")

    try:
        # 主线程保活
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[watchdog] 正在关闭...")
        uart_bridge.send_command(CMD.ACTION_LED_OFF)
        uart_bridge.close()


if __name__ == "__main__":
    main()

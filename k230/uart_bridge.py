"""串口通信模块 — 线程安全，全局单例。

所有模块发指令给 STM32 必须通过此模块的 send_command()。
严禁各模块直接操作 /dev/ttyS*。
"""

import serial
import threading
from config import UART_PORT, UART_BAUDRATE, UART_TIMEOUT

_lock = threading.Lock()
_ser = None


def _get_serial():
    """延迟初始化串口，确保只打开一次。"""
    global _ser
    if _ser is None:
        _ser = serial.Serial(UART_PORT, UART_BAUDRATE, timeout=UART_TIMEOUT)
    return _ser


def send_command(cmd: int):
    """发送单字节指令给 STM32。线程安全。

    Args:
        cmd: 单字节指令，例如 0x43 表示打招呼
    """
    if not (0x00 <= cmd <= 0xFF):
        raise ValueError(f"指令超出范围: {hex(cmd)}")

    with _lock:
        ser = _get_serial()
        ser.write(bytes([cmd]))


def close():
    """关闭串口（程序退出时调用）。"""
    global _ser
    if _ser is not None:
        _ser.close()
        _ser = None

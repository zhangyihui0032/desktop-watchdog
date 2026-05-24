# 团队分工与合作规范

## 人员分工

### 人 A (STM32 小狗执行层)

**职责范围**: `stm32/` 目录下的所有文件

| 任务 | 说明 |
|------|------|
| STM32 固件验证 | 确保 0x29-0x50 每条指令均正确响应 |
| 硬件维护 | 舵机、OLED、LED、电池检测等外设正常工作 |
| 串口联调 | 配合 K230 端测试 UART 通信 |
| 结构装配 | 3D 打印外壳、舵机安装、走线整理 |

**输出物**: 
- 烧录好的 STM32 固件 HEX 文件
- 硬件接线图（拍照标注引脚）

### 人 B (K230 视觉 + 安防)

**职责范围**: `k230/vision/` 目录下的所有文件

| 任务 | 说明 |
|------|------|
| 摄像头驱动 | MIPI CSI 摄像头初始化与图像采集 |
| 人脸检测 | 加载 SDK 自带 `face_detection.kmodel`，NPU 推理 |
| 人脸识别 | CPU 端特征提取 + 与注册人脸库比对 |
| 看门狗逻辑 | 无人休眠 / 熟人欢迎 / 陌生人告警状态机 |
| 人脸注册工具 | 对着摄像头拍几张照录入人脸库 |

**输出物**:
- `vision/face_detect.py`
- `vision/face_recognize.py`
- `vision/watchdog.py`

### 人 C (K230 语音 + 对话)

**职责范围**: `k230/chat/` 目录下的所有文件

| 任务 | 说明 |
|------|------|
| 语音唤醒 | 本地唤醒词检测（"你好小智"） |
| LLM 对接 | WiFi 连接，调用云端 LLM API |
| 情绪提取 | 从 LLM 回复文本中提取情绪标签 |
| TTS 合成 | LLM 回复转语音播放 |
| 情绪→动作映射 | `emotion_map.py` — 情绪标签映射为 0x29-0x50 指令 |

**输出物**:
- `chat/voice_wake.py`
- `chat/llm_client.py`
- `chat/tts.py`
- `chat/emotion_map.py`

---

## 接口契约

**三人以 `README.md` 中的接口协议为准，任何修改必须先更新文档、三人确认后再改代码。**

关键规则：

1. **指令协议不可随意变更**。0x29-0x50 的映射关系是对接口的绑定约束
2. **K230 端所有串口发送统一走 `uart_bridge.send(cmd)`**。人 B 和人 C 都调用这个接口，不允许自己开串口
3. **配置文件集中**。串口号、波特率、LLM API Key 等统一放在 `k230/config.py`
4. **目录不重叠**。人 B 只提交 `k230/vision/`，人 C 只提交 `k230/chat/`，冲突概率为零

---

## Git 工作流

### 仓库结构

```
main             ← 稳定版本，只有通过测试的代码才能合并到这里
├── stm32        ← 人A 工作分支
├── k230-vision  ← 人B 工作分支
├── k230-chat    ← 人C 工作分支
└── dev          ← 集成测试分支（可选）
```

### 日常工作流

```bash
# 1. 每天开始工作前，拉取最新代码
git checkout main
git pull origin main

# 2. 切换到自己的分支
git checkout stm32          # 人A
git checkout k230-vision    # 人B
git checkout k230-chat      # 人C

# 3. 把 main 的最新改动合并到自己分支
git merge main

# 4. 写代码...

# 5. 提交
git add .
git commit -m "feat: xxx功能描述"

# 6. 推送自己的分支
git push origin stm32       # 人A 推送
git push origin k230-vision # 人B 推送
git push origin k230-chat   # 人C 推送
```

### 合并到 main 的流程

1. 自己的功能开发完并自测通过
2. 在 GitHub 上发起 **Pull Request** 把自己的分支合并到 `main`
3. **至少一个队友 Review 代码**，确认：
   - 没有改到别人的目录
   - 接口调用方式符合 README 规范
   - `uart_bridge` 没有绕过直接操作串口
4. Review 通过后合并

---

## 联调顺序

```
第一步：人A 独立 → 用串口助手验证每条指令正确
第二步：人B + 人A → 联调人脸检测 → 动作响应
第三步：人C + 人A → 联调 LLM 对话 → 动作响应
第四步：三人合体 → 全功能联调
```

---

## 文件冲突规则

| 文件 | 谁可以改 | 改之前 |
|------|---------|--------|
| `k230/main.py` | 三人协商 | 群里说一声 |
| `k230/config.py` | 三人协商 | 群里说一声 |
| `k230/uart_bridge.py` | 三人协商 | 群里说一声 |
| `k230/protocol.py` | **锁定，只读** | 除非三人同意 |
| `k230/vision/*` | 仅人B | 随便改 |
| `k230/chat/*` | 仅人C | 随便改 |
| `stm32/*` | 仅人A | 随便改 |
| `README.md` | 三人协商 | 群里说一声 |

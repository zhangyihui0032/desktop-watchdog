"""全局配置 — 三人协商一致后才能修改。"""

# --- 串口配置 ---
UART_PORT = "/dev/ttyS0"       # K230 连接 STM32 的串口 (根据实际调整)
UART_BAUDRATE = 115200
UART_TIMEOUT = 0.1

# --- 摄像头 ---
CAMERA_ID = 0                  # /dev/video0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# --- 人脸识别 ---
FACE_DETECT_MODEL = "models/face_detection.kmodel"
FACE_RECOGNIZE_MODEL = "models/face_recognition.kmodel"
FACE_DB_DIR = "models/face_db/"        # 注册人脸特征库目录
FACE_CONFIDENCE_THRESHOLD = 0.7        # 人脸识别置信度阈值
STRANGER_ALERT_TIMEOUT = 30            # 陌生人持续多久触发告警 (秒)
NOBODY_SLEEP_TIMEOUT = 300             # 无人多久进入休眠 (秒)

# --- 语音 ---
WAKE_WORD = "你好小智"

# --- LLM ---
LLM_API_URL = "https://api.deepseek.com/v1/chat/completions"  # 或其他 LLM API
LLM_API_KEY = ""                     # 填入 API Key
LLM_MODEL = "deepseek-chat"
LLM_SYSTEM_PROMPT = "你是一只桌面机器狗，名叫小智。回答要简短，不超过两句话。语气活泼可爱。"

# --- TTS ---
TTS_ENABLED = True

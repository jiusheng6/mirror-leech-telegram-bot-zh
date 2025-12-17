# 国际化 (i18n) 使用说明

本项目已添加完整的国际化支持，目前支持中文和英文两种语言。

## 功能特性

- ✅ 完整的帮助消息翻译
- ✅ 用户设置界面翻译
- ✅ 所有命令说明翻译
- ✅ 统计信息翻译
- ✅ 支持语言切换

## 如何使用

### 1. 设置语言

在 `config.py` 文件中设置 `LANGUAGE` 参数：

```python
# 中文
LANGUAGE = "zh-CN"

# 英文
LANGUAGE = "en"
```

### 2. 支持的语言

| 语言代码 | 语言名称 | 文件位置 |
|---------|---------|---------|
| `en` | English (英文) | `locales/en/messages.json` |
| `zh-CN` | 简体中文 | `locales/zh-CN/messages.json` |

### 3. 配置示例

```python
# config.py

# 必需配置
BOT_TOKEN = "your_bot_token"
OWNER_ID = 123456789
TELEGRAM_API = 123456
TELEGRAM_HASH = "your_hash"

# 可选配置
LANGUAGE = "zh-CN"  # 设置为中文
# LANGUAGE = "en"   # 设置为英文
```

## 已翻译的内容

### 1. 帮助消息
- Mirror 命令帮助
- YT-DLP 命令帮助
- Clone 命令帮助
- RSS 订阅帮助
- 所有参数说明

### 2. 用户设置
- 所有用户设置选项的说明文本
- 配置项的详细说明

### 3. 系统消息
- 统计信息
- 错误提示
- 状态信息

## 目录结构

```
mirror-leech-telegram-bot/
├── locales/                    # 语言文件目录
│   ├── en/                     # 英文
│   │   └── messages.json       # 英文翻译
│   └── zh-CN/                  # 中文
│       └── messages.json       # 中文翻译
├── bot/
│   └── helper/
│       ├── i18n/               # i18n 模块
│       │   └── __init__.py     # i18n 核心代码
│       └── ext_utils/
│           └── help_messages.py # 帮助消息（已适配）
└── config_sample.py            # 配置样例（包含 LANGUAGE 选项）
```

## 自定义翻译

如果你想修改现有翻译或添加新语言：

### 修改现有翻译

1. 打开对应的语言文件：
   - 中文：`locales/zh-CN/messages.json`
   - 英文：`locales/en/messages.json`

2. 找到要修改的键值对，例如：
```json
{
  "help": {
    "mirror": {
      "main": "<b>发送链接和命令：</b>\n\n/cmd 链接"
    }
  }
}
```

3. 修改翻译文本后保存

4. 重启机器人即可生效

### 添加新语言

1. 在 `locales/` 目录下创建新的语言目录，例如 `locales/ja/`（日语）

2. 复制 `locales/en/messages.json` 到新目录

3. 翻译所有文本内容

4. 在 `config.py` 中设置：
```python
LANGUAGE = "ja"
```

## 技术实现

本项目使用自定义的 i18n 模块实现国际化：

- **翻译文件格式**：JSON
- **键值访问**：支持点号分隔的嵌套键（如 `help.mirror.main`）
- **变量插值**：支持在翻译中使用变量（如 `{is_premium}`）
- **后备机制**：如果当前语言缺少某个翻译，会自动使用英文

### 使用示例

```python
from bot.helper.i18n import t

# 简单翻译
message = t("help.mirror.main")

# 带变量的翻译
message = t("user_settings.leech_split_size", is_premium=True)
```

## 注意事项

1. **配置文件**：确保在 `config.py` 中设置了 `LANGUAGE` 参数
2. **重启生效**：修改语言设置后需要重启机器人
3. **编码格式**：翻译文件使用 UTF-8 编码，请确保编辑器设置正确
4. **JSON 格式**：修改翻译文件时注意保持 JSON 格式正确

## 常见问题

**Q: 如何恢复到英文？**
A: 在 `config.py` 中设置 `LANGUAGE = "en"` 并重启机器人。

**Q: 翻译不生效怎么办？**
A: 检查以下几点：
1. `config.py` 中是否正确设置了 `LANGUAGE`
2. 翻译文件格式是否正确（可以用 JSON 验证器检查）
3. 是否重启了机器人

**Q: 可以动态切换语言吗？**
A: 当前版本需要重启机器人才能切换语言。未来版本可能会支持动态切换。

**Q: 部分文本还是英文？**
A: 这是正常的，某些技术术语（如命令名称、参数名）保持英文以保证兼容性。

## 贡献翻译

欢迎为项目贡献更多语言的翻译！

1. Fork 本项目
2. 添加新语言的翻译文件
3. 测试翻译效果
4. 提交 Pull Request

## 更新日志

- **2024-12-17**:
  - 添加完整的中英文国际化支持
  - 翻译了所有帮助消息和用户设置
  - 实现了 i18n 框架

---

**Made with ❤️ for the MLTB community**

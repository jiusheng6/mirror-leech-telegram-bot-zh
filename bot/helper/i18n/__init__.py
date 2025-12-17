import json
from pathlib import Path
from typing import Dict, Any

class I18n:
    def __init__(self, default_lang: str = "zh-CN"):
        self.default_lang = default_lang
        self.current_lang = default_lang
        self.translations: Dict[str, Dict[str, Any]] = {}
        self.locales_dir = Path(__file__).parent.parent.parent.parent / "locales"
        self._load_translations()

    def _load_translations(self):
        """Load all available translation files"""
        if not self.locales_dir.exists():
            return

        for lang_dir in self.locales_dir.iterdir():
            if lang_dir.is_dir():
                lang_code = lang_dir.name
                messages_file = lang_dir / "messages.json"
                if messages_file.exists():
                    with open(messages_file, "r", encoding="utf-8") as f:
                        self.translations[lang_code] = json.load(f)

    def set_language(self, lang: str):
        """Set current language"""
        if lang in self.translations:
            self.current_lang = lang
        else:
            self.current_lang = self.default_lang

    def t(self, key: str, **kwargs) -> str:
        """
        Translate a message key
        Args:
            key: Translation key (e.g., "help.mirror.main")
            **kwargs: Variables for string formatting
        Returns:
            Translated string
        """
        # Get translation from current language or fallback to default
        translation = self._get_nested_value(
            self.translations.get(self.current_lang, {}), key
        ) or self._get_nested_value(
            self.translations.get(self.default_lang, {}), key
        ) or key

        # Format string with provided variables if any
        if kwargs:
            try:
                translation = translation.format(**kwargs)
            except (KeyError, ValueError):
                pass

        return translation

    def _get_nested_value(self, data: dict, key: str) -> Any:
        """Get value from nested dict using dot notation"""
        keys = key.split(".")
        value = data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return None
        return value

# Global i18n instance (default: Chinese)
_i18n = I18n("zh-CN")

def set_language(lang: str):
    """Set current language"""
    _i18n.set_language(lang)

def t(key: str, **kwargs) -> str:
    """Translate a message"""
    return _i18n.t(key, **kwargs)

def init_i18n(lang: str = "zh-CN"):
    """Initialize i18n with a specific language"""
    global _i18n
    _i18n = I18n(default_lang=lang)
    return _i18n

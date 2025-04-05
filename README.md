
# TelegramBot
## Установка и настройка

1. **Клонируйте репозиторий**:
   ```bash
   git clone git@github.com:SergioSboy/telco-monitor-miniapp-bot.git
   cd telegram-bot-nn-gid
   ```

2. **Создайте виртуальное окружение**:
   ```bash
   python3 -m venv venv
   ```

3. **Активируйте виртуальное окружение**:
   - На Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - На Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Настройте переменные окружения**:
   - Создайте файл `.env` в корневой директории проекта.
   - Добавьте в `.env` ваш токен Telegram бота:
     ```plaintext
     TELEGRAM_TOKEN=***
     ```

6. **Запустите бота**:
   ```bash
   python main.py
   ```

## Обновление зависимостей

Если в проект добавляются новые зависимости, сохраните их в `requirements.txt`:
```bash
pip freeze > requirements.txt
```
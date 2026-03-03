import re
import json
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
prices = re.findall(r"Стоимость\n([0-9 ]+,[0-9]{2})", text)
prices = [p.strip() for p in prices]
products = re.findall(r"\d+\.\n(.+?)\n\d+,\d+\s*x", text)
total_match = re.search(r"ИТОГО:\n([0-9 ]+,[0-9]{2})", text)
total = total_match.group(1).strip() if total_match else None
datetime_match = re.search(r"Время:\s*(.+)", text)
datetime = datetime_match.group(1).strip() if datetime_match else None
payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment = payment_match.group(1) if payment_match else None
result = {
    "products": products,
    "prices": prices,
    "total": total,
    "datetime": datetime,
    "payment_method": payment
}
print(json.dumps(result, ensure_ascii=False, indent=4))
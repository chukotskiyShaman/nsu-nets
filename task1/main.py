import csv

from pythonping import ping

domains = ["google.com", "yandex.ru", "wikipedia.org", "steamcommunity.org", "telegram.org",
           "notion.so", "dzen.ru", "github.com", "vk.com"]

with open('ping_results.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Domain', 'Response Time (ms)', 'Packet Loss'])

    for domain in domains:
        response = ping(domain, count=5, timeout=2)
        writer.writerow([domain, response.rtt_avg_ms, response.packet_loss])

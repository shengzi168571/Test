IPS = { '192.168.123.10': 34, '12 .34.56.78 ': 12, '90 .12.34.56':19}
sorted_IPS = sorted(IPS.items(), key=lambda IPS : IPS[1], reverse=True)
print(sorted_IPS)
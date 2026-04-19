dist = float(input('Distância (em metros): '))
km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000

print(f'A distância de {dist}m corresponde a: {km}Km\n{hm}Hm\n{dam}Dam\n{dm}dm\n{cm}cm\n{mm}mm.')

secret=7
while True:
 g=int(input())
 if g==secret:print('Correct');break
 print('Lower' if g>secret else 'Higher')
def toplama (sayi1: int, sayi2: int) -> int :
    return sayi1 + sayi2

print(toplama(3,"4"))



def buyut (isimler: list[str]) -> list[str]:
    upper = []
    for isim in isimler:
        upper.append(isim.upper())
        
    return upper
    
def ikinci_ad(ad: str | None) -> str:
    if ad is None:
        return "bilinmiyor"
    else:
        return "2. ad var"
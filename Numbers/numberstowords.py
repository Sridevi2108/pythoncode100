def count_words(n):
    if n==0:
        return "None"
    words=""
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    tens=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    teens=["ten","eleven","twelve","thirteen","fouteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    if n>=1000:
        words+=ones[n//1000]+" thousand "
        n=n%1000
    if n>=100:
        words+=ones[n//100]+" hundered "
        n=n%100
    if n >=10  and n<=19:
        words+=teens[n-10]+" "
        n = 0
    if n >=20:
        words+=tens[n//10]+" "
        n=n%10
    if n>=1 and n<=9:
        words+=ones[n]+" "

    return words


n=int(111)
num = count_words(n)
print(num)
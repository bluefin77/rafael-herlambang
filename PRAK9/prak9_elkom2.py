a = ('1021, 1022, 1023', '1025, 1026, 1027', '1029, 1030, 1030')
print(a)
def ratarata(angka):
    rata_rata = [int(x) for x in angka.split(', ')]
    return int(sum(rata_rata) / len(rata_rata))

averages = [ratarata(group) for group in a]
print("rata rata dari tuple adalah : ")
print(averages)
print(5*"=", "Rafael Gala Herlambang", 5*"=")
print(6*"=", "064002300036", 6*"=")
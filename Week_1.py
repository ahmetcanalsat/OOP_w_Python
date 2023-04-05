import numpy as np
'''dizi=np.array([1,2,3,4,5])
print(dizi)
dizi=np.array([1,2,3,4,5])
print(dizi)
print(type(dizi))
dizi2=np.array((1,2,3,4,5))
print(dizi2)
print(type(dizi2))'''

'''#0 boyutlu dizi
dizi0D=np.array(70)
print("0 boyutlu dizi--",dizi0D)'''

'''#1 boyutlu dizi
dizi1D=np.array([1,2,3,4,5])
print("1 boyutlu dizi--",dizi1D)'''

'''#2 boyutlu dizi
dizi2D=np.array([[1,2,3],[4,5,6]])
print("2 boyutlu dizi--",dizi2D)'''

'''#3 boyutlu dizi
dizi3D=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print("3 boyutlu dizi",dizi3D)'''

'''#Aşağıdaki komutlarımızda farklı boyutlarda dizileri tanımlayıp bu dizilerin kaç boyutlu olduğunu yazdırtıyoruz
a=np.array(34)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)'''

'''dizi5D=np.array([1,2,3,4],ndmin=5)
print(dizi5D)
print("Dizinin boyutu:",dizi5D.ndim)'''

'''#Bir dizinin elemanlarını yazdırma
dizi=np.array([0,2,4,6])#Index değeri daima 0 dan başlar.
print(dizi[1])#Yukarıda tanımladığımız dizinin 1. indexindeki değeri yazdırır.
print(dizi[3])'''


'''#Dizideki elemanları çağırma veya kullanma
dizi=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('1. Satırın 3. Elemanı:',dizi[0,2]) #Buradaki 0,2 komutu, dizide indexi 0 olan(yani 1,2,3'lü kısım) satırdan, indexi 2 olan elemanın yazılmasını istemektedir. 
print('2. Satırın 4. Elemanı:',dizi[1,3])'''


'''#3 Boyutlu Dizide Eleman Çağırma
dizi=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(dizi[0,1,2])#Yandaki komutumuz koordinat sistemine göre Y,X,Z değerleri üzerinde eleman aramaktadır. 0 değeri dikeyde, 1 değeri yataydan 1. indexteki diziyi alır ve 2 değeri, 1 numaralı dizinin 2 numaralı index değerini çağırır.'''



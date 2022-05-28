# [7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.
# Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.
"""
-[7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
    0. indexteki elemanı root alarak  bir arama ağacı (search tree) oluşturduğumuz zaman oluşum süreci şöyle olmalıdır.
    Root 7 ise 7 den büyükler sağ tarafa küçükler sol tarafa yazılır.
    5, 7 nin solundadır. Peki bu ilerleyişe göre bir sonraki rakamı yani 1'i nasıl ekleriz ?
    Öncelikle 1, 7 den büyük mü ? Hayır, o zaman sola yazılma sola baktığımızda da bizi 5 karşılıyor.
    Peki 1, 5 den büyük mü ? Hayır, o zaman 1'i 5 in soluna yazmalıyız.

                               7
                              / \
                             5   8
                            / \   \
                           1   6   9
                          / \
                         0   3
                            / \
                           2   4

**Big-O gösterimi: Eğer elimizde ki dengeli olursa yani sağ ve solda da hemen hemen eleman sayısı eşit olursa O(logn);
    Lakin dengesiz olursa yani sağda daha fazla ya da solda daha fazla olursa O(n) olur.
"""
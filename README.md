# facemaskdetector

Bu Proje, bir yüz maskesi tespit sistemi ile birlikte basit bir PyQt5 tabanlı arayüz içeren bir projeyi içerir. Projeyi iki ana bölüme ayırabiliriz: kamera akışını gösteren arayüz (arayüz.py) ve yüz maskesi tespiti gerçekleştiren algoritma (video.py).

arayüz.py:

Bu modül, PyQt5 kullanılarak oluşturulan bir pencere içinde kamera görüntüsünü gösterir. Ayrıca, mevcut kameraları listeleyip seçme olanağı sunar.

video.py:

Bu modül, TensorFlow ve OpenCV kullanarak yüz maskesi tespiti gerçekleştirir. Video akışından kareler alır, yüzleri tespit eder ve her yüz için maske tespiti yapar. Maskesiz yüzlerin tespiti durumunda ekran görüntüsü alır ve bu bilgileri SQLite veritabanına kaydeder.

Kullanım:

PyQt5 arayüzünü çalıştırmak için arayüz.py dosyasını çalıştırın.
video.py dosyasında TensorFlow modeli ile yüz maskesi tespiti gerçekleştirin.
"q" tuşuna basarak her iki modülü de kapatın.
Bu proje, yüz maskesi tespiti ile ilgili temel bir örnek sunar ve daha fazla özelleştirmeye açıktır.

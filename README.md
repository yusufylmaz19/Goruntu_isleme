# Goruntu_isleme

# Mermer Çeşitlerinin Sınıflandırılması

## Giriş

Mermer çeşitlerinin sınıflandırılması, inşaat ve dekorasyon sektörlerinde önemli bir uygulamadır. Mermer çeşitlerinin doğru bir şekilde sınıflandırılması, mermerin özelliklerinin ve kalitesinin anlaşılması için gereklidir. Bu bilgi, mermerin doğru şekilde işlenmesini ve kullanılmasını sağlar.

Bu projede, derin öğrenme tekniklerini kullanarak mermer çeşitlerini otomatik olarak sınıflandıran bir model geliştirilmiştir. Model, TensorFlow ve Keras kütüphaneleri ile Python dilinde oluşturulmuştur.

## Projenin Aşamaları

### Veri Setinin Hazırlanması

Proje için, 25 farklı mermer çeşidine ait 7547 adet görüntü toplanmıştır. Görüntüler, eğitim, doğrulama ve test olmak üzere üç gruba ayrılmıştır.

- Eğitim veri seti: Modelin öğrenmesi için kullanılır.
- Doğrulama veri seti: Modelin performansının değerlendirilmesi için kullanılır.
- Test veri seti: Modelin gerçek dünyadaki performansının değerlendirilmesi için kullanılır.

### Modelin Tasarımı

Model, ResNet152V2 model mimarisi temel alınarak tasarlanmıştır. ResNet152V2, ImageNet veri setinde eğitilmiş derin bir öğrenme modelidir. Modelin son katmanları, mermer çeşitlerini sınıflandırmak üzere özelleştirilmiştir.

### Modelin Eğitimi

Model, transfer learning tekniği ile eğitilmiştir. Transfer learning, önceden eğitilmiş bir modelin, yeni bir veri setinde iyi performans göstermesi için kullanılmasıdır. Eğitim sürecinde, Adam optimizasyon algoritması kullanılmıştır. Eğitim, 45 epoch boyunca gerçekleşmiştir.

### Modelin Değerlendirilmesi

Modelin performansı, doğruluk, kayıp, confusion matrix, sınıflandırma raporu ve ROC AUC skoru gibi metrikler ile değerlendirilmiştir.

- Doğruluk: Modelin doğru sınıflandırma yaptığı örnek sayısının toplam örnek sayısına oranıdır.
- Kayıp: Modelin tahminlerinin gerçek değerlerden sapma miktarıdır.
- Confusion matrix: Modelin sınıflandırma hataları hakkında bilgi verir.
- Sınıflandırma raporu: Modelin her bir sınıfta doğruluk, hassasiyet ve özgüllük gibi metrikleri verir.
- ROC AUC skoru: Modelin sınıflandırma doğruluğunun bir ölçüsüdür.

### Modelin Kullanımı

Model, yeni mermer görüntülerini sınıflandırmak için kullanılabilir. Model, mobil uygulamalar ve web servisleri gibi farklı platformlarda kullanım için TensorFlow Lite formatına dönüştürülmüştür.

## Modelin Performansı

Model, doğrulama veri setinde %88.25 doğruluk ve %0.26 kayıp elde etmiştir. Test veri setinde %87.45 doğruluk ve %0.30 kayıp elde edilmiştir. Bu sonuçlar, modelin mermer çeşitlerini yüksek doğrulukla sınıflandırabildiğini göstermektedir.

## Kodların Açıklaması

Proje kapsamında geliştirilen kodlar, aşağıdaki iki dosyada yer almaktadır:

- [prediction.py](link-to-prediction.py)
  Bu dosya, modeli kullanarak tek bir görüntüyü sınıflandırmak için gerekli kodları içerir.

- [resnet_model.py](link-to-resnet_model.py)
  Bu dosya, modelin oluşturulması, eğitimi ve değerlendirilmesi için gerekli kodları içerir.

## Sonuç

Geliştirilen model, mermer çeşitlerini yüksek doğrulukla sınıflandırabilmektedir. Bu model, inşaat ve dekorasyon sektörlerinde mermer çeşitlerinin otomatik olarak tespit edilmesi için kullanılabilir.


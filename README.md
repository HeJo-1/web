# Selenium ile Bir Web Sayfasındaki Tüm Linkleri ve Düğmeleri Alma

Aşağıdaki kod, Selenium kütüphanesini kullanarak bir web sayfasındaki tüm linkleri ve düğmeleri alır. Kod çalıştırılmadan önce geçerli bir URL girmeniz istenecektir.

## Gereksinimler

    Selenium kütüphanesi
    Chrome web tarayıcısı ve Chrome sürücüsü

## Kullanım

    Selenium kütüphanesini ve Chrome sürücüsünü yükleyin.
    pip install selenium
    git clone https://github.com/HeJo-1/web
    cd web
    python web.py

## Notlar

    Kod, //a[@href] ve //button XPath ifadelerini kullanarak tüm linkleri ve düğmeleri alır. Bu ifadeler, tüm <a> ve <button> etiketleri içerir.
    Kod, startswith() metodunu kullanarak geçerli bir URL girme zorunluluğunu sağlar.
    Kod, WebDriverWait sınıfını kullanarak link ve düğme görünürlüğünü bekler.

Bu kod, web crawler ve automation projelerinde yararlı olabilir

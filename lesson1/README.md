Bài mở đầu
==========

Chúng ta sẽ cùng nhau học `Tensorflow` từ cơ bản đi lên, mà không yêu cầu `PHẢI` biết hoặc học `Deep Learning` cùng lúc. Như chúng ta thấy có quá nhiều hướng dẫn nặng về phần học máy Machine Learning, mà bỏ qua phần làm thế nào để cài đặt các kỹ thuật này trong `Tensorflow`, làm cho chúng ta rất khó để bắt đầu viết ra một chương trình ứng dụng.

Thực hành
=========

Bài 1 này, hãy theo hướng dẫn sau đây để cài được `Tensorflow`, cá nhân mình sử dụng Linux on Windows để lập trình `Tensorflow` rất tiện.

Yêu cầu:

* Python 2.7 hoặc Python 3.3+
* Ubuntu hoặc Mac OS X, hoặc Bash Ubuntu on Windows.

Các bước, để cài đặt Tensorflow: Sử dụng `Anaconda` và công cụ quản lý các gói thư viện `conda`

### 1. Cài đặt Anaconda, xem hướng dẫn [tại đây](https://www.continuum.io/Downloads)

### 2. Tạo 1 môi trường conda, gọi là `tensorflow`

Ở đây, tôi sẽ tạo ra 1 môi trường conda tên là `tensorflow` sử dụng Python 3.5, bạn có thể sử dụng 1 phiên bản khác sử dụng 2.7 hoặc tùy sở thích của bạn

```bash
# Python 3.5
$ conda create -n tensorflow python=3.5
```

### 3. Kích hoạt môi trường conda và cài đặt Tensorflow ở trong nó

```bash
$ source activate tensorflow
(tensorflow)$  # Your prompt should change

# Linux/Mac OS X, Python 2.7/3.4/3.5, CPU only:
(tensorflow)$ conda install -c conda-forge tensorflow
```

Bạn chờ quá trình cài đặt hoàn tất là có thể bắt tay ngay vào lập trình Tensorflow.

### 4. (Tùy chọn) Cài đặt iPython

Có thể cài đặt thêm gói thư viện iPython bằng lệnh sau:

```bash
$ source activate tensorflow
(tensorflow)$ conda install ipython
```

Chúc các bạn hoàn thành bước cơ sở đầu tiên này để có thể làm việc được với Tensorflow đầy hấp dẫn ở phía sau nhé !
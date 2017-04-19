Viết một chương trình cơ bản sử dụng Tensorflow
===============================================

Xem xét 1 chương trình cơ bản sau đây:

```python
import tensorflow as tf                         # Khai báo sử dụng tensorflow

x = tf.constant(35, name='x')                   # Khai báo một hằng số
y = tf.Variable(x + 5, name='y')                # Khai báo một biến Tensor

print(y)                                        # In ra kiểu dữ liệu y, cụ thể: Tensor("y/read:0", shape=(), dtype=int32)

model = tf.global_variables_initializer()       # Khởi tạo một đồ thị phụ thuộc giữa các biến, y phụ thuộc vào x
                                                # Nếu không sẽ báo lỗi, biến phụ thuộc y chưa được khởi tạo
                                                # Chú ý, lúc này giá trị của y vẫn chưa được tính toán cho đến lúc gọi hàm run()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))
```
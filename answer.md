# Trả lời  

## Viết chương trình thực hiện theo 2 cách khác nhau

Ngôn ngữ em sử dụng là Python. $2$ cách em đã sử dựng bao gồm sử dụng **dictionary** và **OOP** của Python. Chi tiết về code em đã để lần lượt tại file *DictionarySolution.py* và *OOPSolution.py*

## Các testcase minh hoạ

Em đã test chương trình với việc nhập từ file **json**, các file test nằm ở thư mục *TestCases*, với 3 trường hợp đề cập ở trên gồm:

- Các đơn hàng có địa chỉ trùng nhau,  tại file *sameAddress.json*

- Các đơn hàng có địa chỉ hoàn toàn khác nhau,  tại file *diffrentAddress.json*

- Trường hợp hỗn hợp, tại file *randomCase.json*

Toàn bộ code test các trường hợp với 2 cách tiếp cận ở file *test.py*, để chạy, hãy sử dụng lệnh sau:

```bash
python test.py
```

## Ưu nhược điểm của 2 cách tiếp cận

| Cách tiếp cận              | `Dictionary`                 | OOP (`Order`, `OrderGroup`)  |
| --------------------- | ----------------------------- | ---------------------------- |
| Độ rõ ràng code       | Trung bình, người lập trình phải chú thích rõ ràng cho các key trong dictionary                    | Cao, có thể code được ngay từ bản thiết kế hoặc yêu cầu đề bài                        |
| Hiệu năng             | Tốt (ít lớp logic)            | Tốt, nhưng hơi chậm hơn chút (phải gọi nhiều hàm) |
| Khả năng mở rộng      | Thấp, phải thêm các hàm hỗ trợ global cho dictionary   | Cao, chỉ cần thêm thuộc tính và phương thức cho 2 lớp, chẳng hạn như thuộc tính tên người nhận, số điện thoại người nhận|

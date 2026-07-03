# image-processing
# Xử lý ảnh cơ bản với Python thuần (Pure Python Image Processing)

Dự án này chứa các thuật toán xử lý ảnh cơ bản được lập trình hoàn toàn bằng Python thuần, sử dụng cấu trúc dữ liệu mảng 2 chiều (List of Lists). Mã nguồn không yêu cầu cài đặt bất kỳ thư viện bên thứ ba nào (như OpenCV hay NumPy), rất phù hợp cho mục đích học tập và tìm hiểu bản chất của các phép toán trên pixel.

# Các tính năng chính

File code bao gồm 3 hàm xử lý ảnh cốt lõi:

1. **`convert_to_gray(image_rgb)` - Chuyển đổi ảnh màu sang ảnh xám:**
   - Chuyển đổi mảng 2 chiều chứa các pixel màu RGB thành ảnh grayscale.
   - Sử dụng công thức hệ số độ sáng chuẩn (Luminosity Method): `Gray = 0.299*R + 0.587*G + 0.114*B`.

2. **`apply_threshold(gray_image, t=100)` - Phân ngưỡng (Thresholding):**
   - Chuyển đổi ảnh xám thành ảnh nhị phân (đen/trắng).
   - Bất kỳ pixel nào có giá trị $\ge t$ (mặc định là `100`) sẽ chuyển thành màu Trắng (`255`), ngược lại chuyển thành Đen (`0`).

3. **`average_filter_3x3(image)` - Lọc trung bình (Average Filter):**
   - Làm mờ hoặc giảm nhiễu ảnh bằng cách duyệt qua ma trận ảnh với cửa sổ lọc (kernel) kích thước 3x3.
   - Cập nhật giá trị mỗi pixel bằng trung bình cộng của 9 pixel lân cận.
   - **Đặc biệt:** Có xử lý giữ nguyên giá trị viền ngoài cùng của ảnh để tránh làm đen viền.

# Yêu cầu hệ thống

- Python 3.x (Không yêu cầu cài đặt thêm thư viện).

# Cấu trúc dữ liệu đầu vào (Input Format)

Thuật toán hoạt động trên danh sách lồng nhau (Nested Lists). 
- **Đối với ảnh RGB:** Là một mảng 2 chiều, trong đó mỗi phần tử là một tuple hoặc list gồm 3 giá trị `(R, G, B)`.
- **Đối với ảnh Xám (Grayscale):** Là một mảng 2 chiều, trong đó mỗi phần tử là một số nguyên từ `0` đến `255`.

# Hướng dẫn sử dụng (Usage Example)

Dưới đây là một ví dụ minh họa cách gọi và sử dụng các hàm trên:

```python
1. Tạo một ma trận ảnh RGB giả định (ví dụ ảnh kích thước 3x3)
image_rgb = [
    [(255, 0, 0),   (0, 255, 0),     (0, 0, 255)],
    [(255, 255, 0), (0, 255, 255),   (255, 0, 255)],
    [(0, 0, 0),     (128, 128, 128), (255, 255, 255)]
]

2. Áp dụng chuyển sang ảnh xám
gray_image = convert_to_gray(image_rgb)
print("Ảnh xám:")
print(gray_image)

3. Phân ngưỡng nhị phân
thresholded_img = apply_threshold(gray_image, t=100)
print("\nẢnh sau khi phân ngưỡng:")
print(thresholded_img)

4. Lọc trung bình giảm nhiễu (áp dụng trên ảnh xám)
filtered_img = average_filter_3x3(gray_image)
print("\nẢnh sau khi lọc trung bình 3x3:")
print(filtered_img)

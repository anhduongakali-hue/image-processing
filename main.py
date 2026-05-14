def convert_to_gray(image_rgb):

    height = len(image_rgb)
    width = len(image_rgb[0])
    gray_image = []
    
    for i in range(height):
        row = []
        for j in range(width):
            r, g, b = image_rgb[i][j]
            gray_val = int(0.299 * r + 0.587 * g + 0.114 * b)
            row.append(gray_val)
        gray_image.append(row)
        
    return gray_image


def apply_threshold(gray_image, t=100):
    """2. Phân ngưỡng (Thresholding) t=100."""
    height = len(gray_image)
    width = len(gray_image[0])
    thresholded_image = []
    
    for i in range(height):
        row = []
        for j in range(width):
            if gray_image[i][j] >= t:
                row.append(255) # Trắng
            else:
                row.append(0)   # Đen
        thresholded_image.append(row)
        
    return thresholded_image

def average_filter_3x3(image):
    """3. Lọc trung bình (Average) 3x3."""
    height = len(image)
    width = len(image[0])
    
    # Tạo ma trận trống
    filtered_image = [[0 for _ in range(width)] for _ in range(height)]
    
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            sum_pixels = (
                image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] +
                image[i][j-1]   + image[i][j]   + image[i][j+1] +
                image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]
            )
            filtered_image[i][j] = sum_pixels // 9
            
    # Xử lý viền sơ bộ (để viền giữ nguyên giá trị ảnh gốc thay vì viền đen)
    for i in range(height):
        filtered_image[i][0] = image[i][0]
        filtered_image[i][width-1] = image[i][width-1]
    for j in range(width):
        filtered_image[0][j] = image[0][j]
        filtered_image[height-1][j] = image[height-1][j]
            
    return filtered_image
# K58KTP_CKS_BT02
## Họ Tên: Nguyễn Phương Nam
## MSV: K225480106092
## LỚP: K58KTP
## BÀI TẬP – MÔN: AN TOÀN VÀ BẢO MẬT THÔNG TIN
# Chủ đề: Chữ ký số trong File PDF
# Giảng viên: Đỗ Duy Cốp
Thời điểm giao: 2025-10-24 11:45
# I. MÔ TẢ CHUNG

Sinh viên thực hiện báo cáo và thực hành: phân tích và hiện thực việc nhúng, xác thực chữ ký số trong file PDF.
Phải nêu rõ chuẩn tham chiếu (PDF 1.7 / PDF 2.0, PAdES/ETSI) và sử dụng công cụ thực thi (ví dụ iText7, OpenSSL, PyPDF, pdf-lib).
# II. CÁC YÊU CẦU CỤ THỂ

Cấu trúc PDF liên quan chữ ký (Nghiên cứu).
Thời gian ký được lưu ở đâu?
Các bước tạo và lưu chữ ký trong PDF (đã có private RSA)
Các bước xác thực chữ ký trên PDF đã ký
# III. YÊU CẦU NỘP BÀI

Báo cáo PDF ≤ 6 trang: mô tả cấu trúc, thời gian ký, rủi ro bảo mật.
Code + README (Git repo hoặc zip).
Demo files: original.pdf, signed.pdf, tampered.pdf.
(Tuỳ chọn) Video 3–5 phút demo kết quả.
# IV. TIÊU CHÍ CHẤM

Lý thuyết & cấu trúc PDF/chữ ký: 25%
Quy trình tạo chữ ký đúng kỹ thuật: 30%
Xác thực đầy đủ (chain, OCSP, timestamp): 25%
Code & demo rõ ràng: 15%
Sáng tạo mở rộng (LTV, PAdES): 5%
# V. GHI CHÚ AN TOÀN

Vẫn lưu private key (sinh random) trong repo. Tránh dùng private key thương mại.
Dùng RSA ≥ 2048-bit và SHA-256 hoặc mạnh hơn.
Có thể dùng RSA-PSS thay cho PKCS#1 v1.5.
Khuyến khích giải thích rủi ro: padding oracle, replay, key leak.
# VI. GỢI Ý CÔNG CỤ

OpenSSL, iText7/BouncyCastle, pypdf/PyPDF2.
Tham khảo chuẩn PDF: ISO 32000-2 (PDF 2.0) và ETSI EN 319 142 (PAdES).
tạm thời bài của em chưa fix xong  ;(( 
![Uploading image.png…]()

import sys
import pprint
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign.validation import validate_pdf_signature 
from pyhanko.sign.validation.errors import SignatureValidationError
from pyhanko.sign.validation.policy import SignatureValidationPolicy, StandardValidationPolicy 

def verify_pdf(file_path):
    print(f"==================================================")
    print(f"🚀 BẮT ĐẦU XÁC THỰC CHỮ KÝ: {file_path}")
    print(f"==================================================")

    try:
        with open(file_path, 'rb') as doc_file:
            reader = PdfFileReader(doc_file)
            if not reader.security_handler or not reader.security_handler.sig_fields:
                print("⚠️ LỖI: Tài liệu không chứa trường chữ ký số.")
                return

            sig_field_name = reader.security_handler.sig_fields[0]
            
            validation_policy = StandardValidationPolicy() 

            validation_result = validate_pdf_signature(
                reader, 
                sig_field_name, 
                validation_policy=validation_policy
            )
            
            signer_info = validation_result.signer_info
            
            print("\n--------------------------------------------------")
            print("         LOG KIỂM THỬ XÁC THỰC (8 BƯỚC)")
            print("--------------------------------------------------")
            
            print(f"🎉 KẾT QUẢ CHUNG: {'THÀNH CÔNG' if validation_result.valid else 'THẤT BẠI'}")
            print(f"[3/8] Toàn vẹn dữ liệu (Hash/ByteRange): {'OK' if validation_result.intact else 'THẤT BẠI'}")
            print(f"[4/5/6] Chuỗi & Revocation (Trust): {signer_info.signing_cert_valid}")
            
            timestamp_info = signer_info.timestamp_info
            if timestamp_info and timestamp_info.timestamp_valid:
                print(f"[7/8] Timestamp (RFC 3161): OK ({timestamp_info.timestamp})")
            else:
                print("[7/8] Timestamp: KHÔNG CÓ (hoặc không hợp lệ)")

            print(f"[8/8] Sửa đổi sau ký (Incremental Update): {'KHÔNG' if validation_result.modification_ok else 'CÓ SỬA ĐỔI'}")
            
    except Exception as e:
        print(f"Lỗi: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Cú pháp: python verify.py <đường_dẫn_đến_signed.pdf>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    verify_pdf(pdf_file)
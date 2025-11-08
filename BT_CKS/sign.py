import sys
import os
from pyhanko.pdf_utils.writer import PdfFileWriter
from pyhanko.sign import signers, fields
from pyhanko.sign.fields import SigFieldSpec
from pyhanko.sign.timestamps import HTTPTimeStamper 
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.backends import default_backend as crypto_default_backend

# FIX: Cấu trúc Import đã ổn định
try:
    from pyhanko.keys import load_cert_from_pemder 
except ImportError:
    print("LỖI CẤU HÌNH: Không tìm thấy 'load_cert_from_pemder'.")
    sys.exit(1)

def manual_load_key_from_pemder(key_file_path):
    """ Hàm thay thế tải Private Key thủ công. """
    with open(key_file_path, "rb") as key_file:
        key_data = key_file.read()
    return crypto_serialization.load_pem_private_key(
        key_data, password=None, backend=crypto_default_backend()
    )

ORIGINAL_PDF = "original.pdf"
SIGNED_PDF = "signed.pdf"
PRIVATE_KEY_FILE = "private_key.pem" 
CERT_FILE = "certificate.pem"       
TSA_URL = "http://tsa.digicert.com" 

def create_signature(input_path, output_path):
    print(f"Bắt đầu ký file: {input_path}")
    
    signer_cert = load_cert_from_pemder(CERT_FILE)
    key = manual_load_key_from_pemder(PRIVATE_KEY_FILE) 

    # KHẮC PHỤC LỖI LOGIC: Loại bỏ các tham số gây lỗi
    signer = signers.SimpleSigner(
        signing_cert=signer_cert,
        signing_key=key,
        prefer_pss=True,
        cert_registry=None 
    )
    
    tsa = HTTPTimeStamper(TSA_URL)
    signer.timestamp_setter = tsa

    # Khắc phục lỗi SigObjectSpec
    # Tạo SigFieldSpec chỉ để lấy tên trường
    w = fields.SigFieldSpec(
        'MySignatureField', 
        box=(50, 700, 250, 750) 
    )

    with open(input_path, 'rb') as inf:
        with open(output_path, 'wb') as outf:
            signers.sign_pdf(
                inf, outf, 
                signer=signer, 
                # SỬ DỤNG field_name VÀ LOẠI BỎ field_specs
                field_name='MySignatureField', 
                subfilter='adbe.pkcs7.detached', 
                # field_specs=[w] <-- ĐÃ LOẠI BỎ
            )
    
    print(f"🎉 Đã ký thành công và tạo file: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            create_signature(ORIGINAL_PDF, SIGNED_PDF)
        except FileNotFoundError as e:
            print(f"LỖI: Không tìm thấy file (Kiểm tra {ORIGINAL_PDF} và key/cert). Chi tiết: {e}")
        except Exception as e:
            print(f"LỖI KÝ: Đã xảy ra lỗi. Chi tiết: {e}")
from PyPDF2 import PdfMerger
import os

# PdfFileMerger sınıfından bir nesne oluşturun
merger = PdfMerger()

# PDF dosyalarının bulunduğu klasörün yolunu tanımlayın
path_to_files = r"pdf_files//"

# Klasördeki dosya isimlerini alın
for root, dirs, file_names in os.walk(path_to_files):
    # Dosya isimleri üzerinde döngü kurun
    for file_name in file_names:
        # Her dosyayı birleştiriciye ekleyin
        merger.append(path_to_files + file_name)

# Birleştirilmiş PDF dosyasını yazın
merger.write("merged_all_pages.pdf")
merger.close()
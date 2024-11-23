from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_pdf_links', methods=['GET'])
def get_pdf_links():
    pdf_links = {
        "pdf_links": [
            "https://eprints.unmer.ac.id/id/eprint/282/1/JURNAL%20PENELITIAN%20PENDIDIKAN.pdf",
            "https://pustaka.ut.ac.id/lib/wp-content/uploads/2022/05/Panduan_Scopus.pdf",
            "https://drive.google.com/uc?export=download&id=1FhVv9nDSwha6kbOyqFb46-5bnTHkCKRK",
            "https://journal.uinjkt.ac.id/index.php/ti/article/view/27927/pdf",
            "https://journal.uinjkt.ac.id/index.php/ti/article/view/28585/pdf",
           
            # Tautan terpercaya open source
            "https://arxiv.org/pdf/2102.01830.pdf",   # Arxiv - Open access paper           
            "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0231234&type=printable",  # PLOS ONE
            
        
        
            # Repositori Universitas Airlangga
            "https://repository.unair.ac.id/14315/1/Literasi_Digital_Remaja_Di_Kota_Surabaya.pdf",  # Literasi Digital Remaja di Surabaya
            "https://repository.unair.ac.id/14235/1/Hubungan_Antara_Moral_Disengagement_Dan_Perilaku_Cyberaggression.pdf",  # Cyberaggression pada Remaja
            "https://repository.unair.ac.id/14345/1/Konstruksi_Sosial_Masyarakat_Tentang_Perpustakaan.pdf",  # Konstruksi Sosial Masyarakat Perpustakaan

            # Repositori Universitas Gadjah Mada
            "https://etd.repository.ugm.ac.id/25834/Perancangan_Sistem_Informasi_Monitoring_Skripsi.pdf",  # Perancangan Sistem Informasi Monitoring Skripsi
            "https://etd.repository.ugm.ac.id/22897/Implementasi_Smart_City.pdf"  # Implementasi Smart City di Kota Semarang
        ]
    }
    
    return jsonify(pdf_links)

if __name__ == '__main__':
    app.run(debug=True)

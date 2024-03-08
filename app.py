import numpy as np
from flask import Flask, render_template, request
import tensorflow as tf
#import tensorflow_recommenders as tfrs


app = Flask(_name_)
loaded = tf.saved_model.load('model/model_strng_060_realdata/') # Folder Dari Model TFRS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index_ta_2.html")
    elif request.method == "POST":
        Jenis_Kelamin = request.form.getlist('jenisKelamin') # Menyimpan value dari inputan user dengan 'request.form.getlist()'
        Nilai_MTK = request.form.getlist('Nilai-MTK') # memakai 'getlist' dikarenakan inputan dari TFRS menerima dalam bentuk 'list'
        Nilai_Bindo = request.form.getlist('Nilai-bhs-indo')
        Nilai_Bingg = request.form.getlist('Nilai-bhs-ingg')
        Mata_Pelajaran = request.form.getlist('mapel') # udah dalam bentuk list ["Matematika","Fisika","Kimia"]
        Mata_Pelajaran_result = [', '.join(Mata_Pelajaran)] # diubah supaya menjadi list ['Matematika, Fisika, Kimia']
        Preferensi_Pekerjaan = request.form.getlist('PreferensiPekerjaan')
        Kriteria_Diri = request.form.getlist('kritediri')
        Kriteria_Diri_result = [', '.join(Kriteria_Diri)]
        Topik_Bidang = request.form.getlist('topkbidng')
        Topik_Bidang_result = [', '.join(Topik_Bidang)]
        Kecerdasan = request.form.getlist('Kecerdasan')
        Bakat_Keahlian = request.form.getlist('bakatahli')
        Bakat_Keahlian_result = [', '.join(Bakat_Keahlian)]
        
        _, titles = loaded({
            "jenis_kelamin": np.array(Jenis_Kelamin),
            "nilai_mtk": np.array(Nilai_MTK),
            "nilai_bindo": np.array(Nilai_Bindo),
            "nilai_bingg": np.array(Nilai_Bingg),
            "mata_pelajaran": np.array(Mata_Pelajaran_result),
            "prefe_kerja": np.array(Preferensi_Pekerjaan),
            "kriteria_diri": np.array(Kriteria_Diri_result),
            "topik_bidang": np.array(Topik_Bidang_result),
            "kecerdasan": np.array(Kecerdasan),
            "bakat_keahlian": np.array(Bakat_Keahlian_result)})
        #recommendations = f"Recommendations: {titles[0][:7]}"
        recommendations_tensor = titles[0][:7]
        # Konversi tf.Tensor menjadi numpy array dan kemudian ke list Python
        recommendations_list = recommendations_tensor.numpy().tolist()
        # Konversi byte string menjadi string Python
        program_studies = [program.decode('utf-8') for program in recommendations_list]
        
        return render_template("index_ta_2.html", program_studies=program_studies)


if _name_ == "_main_":
    app.run(host="0.0.0.0", port="0000")
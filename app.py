# pip install flask

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Mengambil data dari form
    nama = request.form['nama']
    nim = request.form['nim']
    prodi = request.form['prodi']
    
    # Menampilkan data yang diterima
    return f'''
    Nama: {nama}
    NIM: {nim}
    Prodi: {prodi}
    '''

# Jalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
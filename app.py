from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    hasil = None
    status = None
    
    if request.method == 'POST':
        pendapatan = int(request.form['pendapatan'])
        pengeluaran = int(request.form['pengeluaran'])
        
        keuntungan = pendapatan - pengeluaran
        
        if keuntungan > 0:
            status = "Untung"
            hasil = keuntungan
        elif keuntungan < 0:
            status = "Rugi"
            hasil = keuntungan
        else:
            status = "Balik Modal"
            hasil = 0
        
    return render_template('index.html', hasil=hasil, status=status)

if __name__ == '__main__':
    app.run(debug=True)
    